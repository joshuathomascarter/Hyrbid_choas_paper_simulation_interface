import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import os

# Set output path
output_path = "/mnt/data/entropy_stream.json"

# Parameters
num_cycles = 1000
entropy_min = 1000
entropy_max = 65000
noise_spikes = [300, 600, 850]  # Random spike positions

# Generate entropy stream
np.random.seed(42)
entropy_stream = []

for cycle in range(num_cycles):
    base_entropy = np.random.randint(entropy_min, entropy_max)
    if cycle in noise_spikes:
        base_entropy += np.random.randint(5000, 15000)  # spike
    entropy_stream.append({
        "cycle": cycle,
        "entropy_value": int(base_entropy)
    })

# Save to JSON file
with open(output_path, 'w') as f:
    json.dump(entropy_stream, f, indent=2)

# Also create a quick plot for verification
df = pd.DataFrame(entropy_stream)
plt.figure(figsize=(12, 4))
plt.plot(df["cycle"], df["entropy_value"], label="Entropy")
plt.axhline(45000, color='red', linestyle='--', label='Flush Threshold')
plt.title("Simulated Entropy Stream")
plt.xlabel("Cycle")
plt.ylabel("Entropy Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt_path = "/mnt/data/entropy_plot_preview.png"
plt.savefig(plt_path)

output_path, plt_path
