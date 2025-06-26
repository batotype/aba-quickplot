import matplotlib.pyplot as plt
import numpy as np

# Data for Escape-Maintained Off-Task Behavior (Frequency per 10-minute interval)
# Lower frequency is the desired outcome here.
# Note: Logarithmic scale cannot handle zero values. If any data point were 0,
# it would need to be adjusted (e.g., to a small epsilon like 0.01) or excluded.
# Current data already contains no zeros, so it's suitable for log scale.

# Phase 1: Baseline 1 (24 data points) - High and variable off-task behavior
baseline1_data = [
    18, 16, 20, 17, 19, 15, 21, 18, 16, 22, 17, 19, 
    15, 20, 18, 17, 21, 19, 16, 18, 20, 17, 19, 15
]

# Phase 2: Intervention (24 data points) - Negative Reinforcement
# Off-task behavior drops significantly and becomes stable/low with potential subtle improvements (generalization)
intervention_data = [
    5, 4, 3, 2, 2, 1, 1.5, 2, 2.5, 3, 2, 1, 
    1, 0.5, 1, 2, 1.5, 1, 0.5, 1, 1.5, 2, 1, 0.5
]

# Phase 3: Baseline 2 (24 data points) - Withdrawal of Intervention
# Behavior stabilizes low for 7 sessions, then climbs
baseline2_data = [
    1.5, 2, 1, 2.5, 1.5, 2, 1, # First 7 sessions: low and stable after withdrawal
    1.5, 2.5, 2.5, 3.5, 3.5, 5, 5, 7, 7, 7.5, 6, 10, 12, 11, 10, 9, 8 # Next 17 sessions + 1 added to make 24: climbing towards higher baseline
]

# Combine all data for plotting
all_data = baseline1_data + intervention_data + baseline2_data
x_indices = np.arange(1, len(all_data) + 1) # Session numbers for x-axis

# Define phase boundaries (indices after which a new phase starts)
phase_boundaries = [len(baseline1_data), len(baseline1_data) + len(intervention_data)]

# Labels for each phase
phase_labels = [
    "Baseline 1",
    "Intervention (Negative Reinforcement)",
    "Baseline 2 (Withdrawal)"
]

# Define colors for each phase and markers
color_baseline1 = '#D3D3D3' # Lightest gray
color_intervention = '#000000' # Blackest
color_baseline2 = '#808080' # Medium gray

marker_baseline1 = 'o'
marker_intervention = 's'
marker_baseline2 = '^'

# Create the plot
fig, ax = plt.subplots(figsize=(14, 7))

# Plot each phase as a separate line segment without connecting across phase lines
ax.plot(x_indices[:len(baseline1_data)], baseline1_data, 
        color=color_baseline1, marker=marker_baseline1, linestyle='-', linewidth=2)

ax.plot(x_indices[len(baseline1_data) : len(baseline1_data) + len(intervention_data)], 
        intervention_data, 
        color=color_intervention, marker=marker_intervention, linestyle='-', linewidth=2)

ax.plot(x_indices[len(baseline1_data) + len(intervention_data) :], 
        baseline2_data, 
        color=color_baseline2, marker=marker_baseline2, linestyle='-', linewidth=2)

# Set Y-axis to logarithmic scale for celeration format
ax.set_yscale('log')

# JABA style: No top/right spines, no grid lines
ax.spines[['right', 'top']].set_visible(False)
ax.grid(False)

# Set axis labels and title
ax.set_xlabel("Observation Sessions")
ax.set_ylabel("Frequency of Escape-Maintained Off-Task Behavior (Log Scale)")
ax.set_title("Impact of Negative Reinforcement on Off-Task Behavior Across Phases (Log-Linear)", fontsize=14, pad=20)

# Add vertical dotted lines for phase changes
for boundary in phase_boundaries:
    ax.axvline(x=boundary + 0.5, color='black', linestyle=':', linewidth=1.5)

# Add phase labels above the graph
current_x_pos_start = 1 # Starting x for label calculation based on 1-indexed sessions
y_text_pos = ax.get_ylim()[1] * 0.9 # Position labels slightly below max Y for log scale

for i, label in enumerate(phase_labels):
    if i == 0: # Baseline 1
        phase_length = len(baseline1_data)
        label_x_position = current_x_pos_start + (phase_length / 2) - 1 # Center the label within the phase
    elif i == 1: # Intervention
        phase_length = len(intervention_data)
        label_x_position = current_x_pos_start + len(baseline1_data) + (phase_length / 2) - 1
    else: # Baseline 2
        phase_length = len(baseline2_data)
        label_x_position = current_x_pos_start + len(baseline1_data) + len(intervention_data) + (phase_length / 2) - 1

    ax.text(label_x_position + 0.5, y_text_pos, label, 
            ha='center', va='bottom', fontsize=10, weight='bold')

# Set x-axis ticks to show every other trial to prevent overlap, and reduce font size
ax.set_xticks(x_indices[::2]) # Select every other tick
ax.set_xticklabels(x_indices[::2], fontsize=8) # Label with session numbers, smaller font
ax.tick_params(axis='x', length=5) # Add small tick marks

# Adjust y-axis to start from 0 and have appropriate range
ax.set_ylim(bottom=np.min(all_data) * 0.8 if np.min(all_data) > 0 else 0.1) # Ensure positive for log scale
min_y, max_y = ax.get_ylim()
log_min_y = np.floor(np.log10(min_y))
log_max_y = np.ceil(np.log10(max_y))
log_ticks = [10**i for i in range(int(log_min_y), int(log_max_y) + 1)]

ax.set_yticks(log_ticks)
ax.set_yticklabels([str(int(t)) if t >= 1 else str(t) for t in log_ticks]) # Format labels nicely

# Save the figure to a file instead of showing it interactively
plt.savefig('negative_reinforcement_log_linear_graph.png', dpi=300, bbox_inches='tight')

# Close the plot to free up memory (important in non-interactive environments)
plt.close(fig)
