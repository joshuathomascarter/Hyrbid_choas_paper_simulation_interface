import json
import pandas as pd
import matplotlib.pyplot as plt

# Load combined entropy + IPC data
combined_path = "/mnt/data/ipc_entropy_combined.json"
with open(combined_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Define FSM states based on entropy + ML confidence simulation
def determine_state(entropy):
    if entropy > 60000:
        return "FLUSH"
    elif entropy > 45000:
        return "STALL"
    elif entropy > 30000:
        return "ML_OVERRIDE"
    else:
        return "OK"

df["fsm_state"] = df["entropy_value"].apply(determine_state)

# Count each state
state_counts = df["fsm_state"].value_counts()
colors = {
    "OK": "#4CAF50",
    "STALL": "#FF9800",
    "FLUSH": "#F44336",
    "ML_OVERRIDE": "#2196F3"
}
state_colors = [colors[state] for state in state_counts.index]

# Pie chart for FSM state distribution
plt.figure(figsize=(6, 6))
plt.pie(state_counts, labels=state_counts.index, autopct='%1.1f%%', startangle=140, colors=state_colors)
plt.title("FSM State Distribution (Simulated)")
fsm_path = "/mnt/data/fsm_state_pie_chart.png"
plt.savefig(fsm_path)

# Save FSM state transitions for future logging
fsm_trace_path = "/mnt/data/fsm_state_transitions.json"
df[["cycle", "entropy_value", "ipc", "fsm_state"]].to_json(fsm_trace_path, orient='records', indent=2)

fsm_path, fsm_trace_path
