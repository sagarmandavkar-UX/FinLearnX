# Research and activation measurement

## Historical claims and evidence

The creator reports 500+ simulated trades and feedback gathered from 90+ users. The repository does not contain raw participant feedback, trade logs, study dates, sampling method, or analysis outputs for those figures. Treat them as creator-reported context, not independently reproducible metrics. The 502-trade automated test demonstrates transaction handling under repeated operations, not user activity.

To substantiate the project story, add a de-identified research summary with participant count, recruitment period, question guide, coding approach, recurring friction themes, changes shipped, and before/after measurements. Do not upload names, contact details, or personal financial information.

## Current onboarding changes

The Home page asks for experience, learning goal, and risk preference, then points to the $100K challenge. The simulator now gives a specific first trade prompt, blocks unavailable prices, and links directly to portfolio review after a trade. The review offers contextual portfolio feedback, reflection prompts, and an optional AI explanation. These choices address plausible first-session friction; no causal improvement is claimed without measured comparison.

## Session funnel

The app records these milestones once per Streamlit session:

| Event | Trigger |
| --- | --- |
| `onboarding_started` | Profile card shown |
| `onboarding_completed` | Profile saved |
| `simulator_opened` | Simulator page opened |
| `first_trade_completed` | First successful virtual order |
| `portfolio_review_opened` | Review page opened, including empty portfolios |
| `learning_review_completed` | All reflection prompts submitted |
| `ai_explanation_requested` | Generate clicked, regardless of API outcome |

Users can download their own session CSV from Home. These events are ephemeral, lack a stable anonymous identifier, and are insufficient for cross-session unique users, aggregate conversion, or retention. A production measurement implementation would require consent, privacy review, stable anonymous IDs, persistent event storage, and separate `ai_explanation_succeeded` measurement.

## Evaluation plan

1. Recruit new learners and observe the first-session journey; record where they pause or abandon it.
2. Compare first learning-loop completion, time to first successful trade, and review completion before and after the guided path with consistent cohorts and a defined observation window.
3. Segment by stated experience level. Inspect failed price loads separately from user friction.
4. Collect a short usefulness rating after portfolio review and examine whether explanations lead to a second learning decision.

Primary activation metric: eligible new sessions completing onboarding, a first successful trade, and a reflection, divided by eligible new sessions. Engagement metric: learning decisions per active learner. Do not substitute trade count for learning or claim measured uplift without the underlying data.
