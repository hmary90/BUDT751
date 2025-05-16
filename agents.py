from crewai import Agent

risk_assessor_agent = Agent(
    role="Risk Assessor",
    goal="Analyze transaction data to detect financial anomalies",
    backstory="A deep learning model trained on historical fraud patterns.",
    verbose=True
)

report_writer_agent = Agent(
    role="Report Writer",
    goal="Summarize audit findings clearly",
    backstory="A language model trained to write professional audit reports.",
    verbose=True
)
