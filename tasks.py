from crewai import Task
from agents import risk_assessor_agent, report_writer_agent

identify_risks_task = Task(
    description="Examine the dataset and identify any suspicious or unusual financial activity.",
    expected_output="List of anomalies with brief reasons.",
    agent=risk_assessor_agent
)

generate_summary_task = Task(
    description="Using the anomalies found, generate a professional audit report summary.",
    expected_output="Written report including sections on risks, patterns, and next steps.",
    agent=report_writer_agent
)
