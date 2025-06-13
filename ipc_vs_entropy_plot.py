import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

# Load the simulated entropy stream
entropy_path = "/mnt/data/entropy_stream.json"
with open(entropy_path, 'r') as f:
    entropy_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(entropy_data)

# Simulate IPC: inversely correlated with entropy + ML override protection bump
def simulate_ipc(entropy):
    if entropy > 60000:
        return np.random.uniform(0.9, 1.1)
    elif entropy > 45000:
        return np.random.uniform(1.1, 1.3)
    elif entropy > 30000:
        return np.random.uniform(1.3, 1.5)
    else:
        return np.random.uniform(1.5, 1.7)

df["ipc"] = df["entropy_value"].apply(simulate_ipc)

# Plot IPC vs Entropy
plt.figure(figsize=(12, 6))
plt.plot(df["cycle"], df["entropy_value"], color='red', label="Entropy")
plt.plot(df["cycle"], df["ipc"], color='blue', label="IPC")
plt.axhline(45000, color='gray', linestyle='--', label='Flush Threshold')
plt.title("Cycle-wise IPC vs Entropy (Simulated)")
plt.xlabel("Cycle")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.tight_layout()

plot_path = "/mnt/data/ipc_vs_entropy_plot.png"
plt.savefig(plot_path)

# Save combined IPC + entropy stream for use in later scripts
combined_path = "/mnt/data/ipc_entropy_combined.json"
df[["cycle", "entropy_value", "ipc"]].to_json(combined_path, orient='records', indent=2)

plot_path, combined_path
