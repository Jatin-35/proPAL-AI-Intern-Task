import uuid
from metrics import MetricsLogger
from dotenv import load_dotenv
from livekit import agents
from livekit.agents import (
    AgentSession, 
    Agent, 
    RoomInputOptions, 
    metrics, 
    MetricsCollectedEvent
)
from livekit.plugins import (
    groq, 
    cartesia, 
    deepgram, 
    noise_cancellation, 
    silero
)
from livekit.plugins.turn_detector.multilingual import MultilingualModel

load_dotenv()

class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="You are a helpful voice AI assistant.")

async def entrypoint(ctx: agents.JobContext):
    session_id = str(uuid.uuid4())
    logger = MetricsLogger()
    usage_collector = metrics.UsageCollector()

    session = AgentSession(
        stt=deepgram.STT(model="nova-3", language="multi"),
        llm=groq.LLM(model="llama3-8b-8192"),
        tts=cartesia.TTS(model="sonic-2", voice="f786b574-daa5-4673-aa0c-cbe3e8534c02"),
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
    )

    temp_store = {}

    @session.on("metrics_collected")
    def _on_metrics(ev: MetricsCollectedEvent):
        usage_collector.collect(ev.metrics)
        m = ev.metrics
        speech_id = getattr(m, "speech_id", None)

        # Capture EOU delay
        if m.__class__.__name__ == "EOUMetrics":
            temp_store[speech_id] = {"eou_delay": m.end_of_utterance_delay}

        # Capture TTFT
        elif m.__class__.__name__ == "LLMMetrics":
            if speech_id not in temp_store:
                temp_store[speech_id] = {}
            temp_store[speech_id]["ttft"] = m.ttft

        # Capture TTFB and log final latency
        elif m.__class__.__name__ == "TTSMetrics":
            if speech_id not in temp_store:
                temp_store[speech_id] = {}
            temp_store[speech_id]["ttfb"] = m.ttfb

            # Log only when all values are present
            vals = temp_store[speech_id]
            logger.log_latency(
                session_id,
                speech_id,
                vals.get("eou_delay"),
                vals.get("ttft"),
                vals.get("ttfb"),
            )

    async def log_usage():
        summary = usage_collector.get_summary()
        logger.log_usage_summary(summary)

    ctx.add_shutdown_callback(log_usage)

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await ctx.connect()
    await session.generate_reply(instructions="Greet the user and offer your assistance.")

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
