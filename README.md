# 🔁 Hybrid Chaos–Entropy Execution Core — Simulation Interface

This repository contains a modular simulation stack for a next-gen post-classical CPU architecture.  
It combines entropy-aware scheduling, FSM-driven control logic, and machine learning hazard overrides into a real-time executable interface.

📄 **Research Paper:** [Hybrid Chaos–Entropy Execution Cores (v2.0.0)](paper/Hybrid_Chaos_v2.0.0.pdf)  
📊 **Live Visualizations:** IPC/entropy plots, FSM states, ML logs, instruction priority heatmaps

---

## 📂 Interface Modules

### `generate_entropy_bus.py`
Simulates quantum-style entropy spikes using von Neumann-like randomness.  
🔧 Output: `entropy_stream.json`

---

### `ipc_vs_entropy_plot.py`
Plots IPC vs. entropy across 1000 simulation cycles.  
Shows entropy-triggered IPC collapse and ML override stabilization.  
📈 Output: `ipc_vs_entropy_plot.png`  
📄 Data: `ipc_entropy_combined.json`

---

### `fsm_visualizer.py`
Analyzes FSM state transitions using entropy thresholds.  
Includes `OK`, `STALL`, `FLUSH`, and `ML_OVERRIDE` states.  
🥧 Output: `fsm_state_pie_chart.png`  
📄 Trace: `fsm_state_transitions.json`

---

### `override_log_window.py`
Logs override events where ML confidence exceeded 85%.  
Includes entropy, IPC, and justification for each override.  
📄 Output: `ml_override_log.json`

---

### `heatmap_scheduler_view.py`
Displays Pi scores for instruction groups as a real-time heatmap.  
Score reflects entropy + chaos + thermal + branch pressure inputs.  
🌡️ Output: `pi_score_heatmap.png`

---

## 🛠️ Requirements

```bash
pip install numpy pandas matplotlib seaborn
