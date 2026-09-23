# Running FinLearnX

## Local setup

Use Python 3.10 or 3.11. From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
streamlit run app/main.py
```

Open the simulator and portfolio review through the app navigation. These links expect `app/main.py` as the entrypoint.

```bash
python -m pytest -q
```

The AI learning coach is optional. Set `OPENAI_API_KEY` on the server if you want to enable it. Never put keys in source files, the README, screenshots, or a committed Streamlit config. `.streamlit/secrets.toml` and `.env` files are ignored, but environment variables work directly with the OpenAI client. No key is required to use the trading simulator and rule-based review.

## Hosting

For a Streamlit deployment, select this repository's `main` branch and `app/main.py` as the entrypoint, and choose Python 3.10 or 3.11. The host must install `requirements.txt` and allow access to the market-data provider. If you enable the AI button, add `OPENAI_API_KEY` using the host's private secrets or environment-variable settings. Verify the app loads, a first trade succeeds with available market data, and the review opens before sharing a live demo link.

The repository does not include a live deployment URL. Do not add a demo badge or URL until the deployment has been tested publicly. For a resume, the GitHub repository URL works independently of hosting.
