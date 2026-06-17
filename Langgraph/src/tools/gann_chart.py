import pandas as pd
import plotly.express as px

df = pd.DataFrame([
    ["Pre-Kick Off", "2026-06-01", "2026-06-05", "Phase"],
    ["Data Access", "2026-06-01", "2026-06-03", "Task"],
    ["Workshop Scheduling", "2026-06-02", "2026-06-05", "Task"],

    ["Business Requirements", "2026-06-08", "2026-06-12", "Phase"],
    ["System Walkthrough", "2026-06-09", "2026-06-10", "Task"],
    ["KPI Review", "2026-06-10", "2026-06-12", "Task"],

    ["Architecture Design", "2026-06-15", "2026-06-26", "Phase"],
    ["Architecture Blueprint", "2026-06-16", "2026-06-20", "Task"],
    ["Data Model Design", "2026-06-18", "2026-06-25", "Task"],
],
columns=["Task","Start","Finish","Type"])

colors = {
    "Phase":"#001f6b",
    "Task":"#a8a8d8"
}

fig = px.timeline(
    df,
    x_start="Start",
    x_end="Finish",
    y="Task",
    color="Type",
    color_discrete_map=colors
)

fig.update_yaxes(autorange="reversed")

fig.update_layout(
    plot_bgcolor="#f2f2f2",
    paper_bgcolor="#f2f2f2",
    height=700,
    title="AI Proposal Generation Project Plan"
)

fig.show()