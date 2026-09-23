"""Optional AI explanations grounded in a simulated portfolio snapshot."""

import json
import os


def explain_portfolio(snapshot: dict, goal: str = "Learn investing basics") -> str:
    """Return educational next steps; never submit account or personal data."""
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("Set OPENAI_API_KEY to enable AI portfolio explanations.")

    # Import lazily so the simulator works without an API key or SDK.
    from openai import OpenAI

    client = OpenAI(timeout=20.0)
    response = client.responses.create(
        model=os.getenv("FINLEARNX_AI_MODEL", "gpt-4.1-mini"),
        store=False,
        instructions=(
            "You are a finance education coach for a virtual trading simulator. "
            "Use only the supplied snapshot. Explain observed allocation and risk in plain language. "
            "Give two specific learning exercises and one reflection question. "
            "Do not recommend buying, selling, or holding securities, predict returns, "
            "or claim to know a benchmark or sector exposure that was not supplied. "
            "Call out missing price data and avoid treating a heuristic score as a validated risk measure."
        ),
        input=json.dumps({"learning_goal": goal, "simulated_portfolio": snapshot}),
    )
    if not response.output_text.strip():
        raise RuntimeError("The AI service returned no explanation. Please try again.")
    return response.output_text.strip()
