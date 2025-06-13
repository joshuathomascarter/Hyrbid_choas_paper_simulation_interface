import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import json

# Load FSM trace data
fsm_trace_path = "/mnt/data/fsm_state_transitions.json"
with open(fsm_trace_path, 'r') as f:
    fsm_data = json.load(f)

df = pd.DataFrame(fsm_data)

# Simulate 4 input features for Pi score (normalized)
np.random.seed(42)
df["chaos_score"] = np.abs(np.gradient(df["ipc"])) * 10000
df["branch_miss_rate"] = np.random.uniform(0.05, 0.25, len(df))
df["execution_pressure"] = np.random.uniform(0.2, 0.9, len(df))

# Normalize
df["EV"] = df["entropy_value"] / 65535.0
df["CS"] = df["chaos_score"] / df["chaos_score"].max()
df["BMR"] = df["branch_miss_rate"]
df["EP"] = df["execution_pressure"]

# Calculate Pi score
alpha, beta, gamma, delta = 0.3, 0.25, 0.2, 0.25
df["Pi_score"] = (
    alpha * df["CS"] +
    beta * df["EV"] +
    gamma * df["BMR"] +
    delta * df["EP"]
)

# Select 50 random samples and pivot for heatmap
sample_df = df.sample(n=50, random_state=42).sort_values("cycle")
sample_df["Instruction Group"] = [f"G{i}" for i in range(1, 51)]
heatmap_data = pd.DataFrame({
    "Instruction Group": sample_df["Instruction Group"],
    "Pi Score": sample_df["Pi_score"]
}).set_index("Instruction Group").T

# Generate heatmap
plt.figure(figsize=(14, 2.5))
sns.heatmap(heatmap_data, cmap="viridis", annot=False, cbar=True)
plt.title("Instruction Priority Heatmap (Pi Score)")
plt.tight_layout()
heatmap_path = "/mnt/data/pi_score_heatmap.png"
plt.savefig(heatmap_path)

heatmap_path
