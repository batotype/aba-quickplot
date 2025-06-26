import matplotlib.pyplot as plt
import numpy as np

# Data for Escape-Maintained Off-Task Behavior (Frequency per 10-minute interval)
# Lower frequency is the desired outcome here.

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
    1.5, 2.5, 2.5, 3.5, 3.5, 5, 5, 7, 7, 7.5, 6, 10, 12, 11, 10, 9, 8 # Adjusted to 24 data points for consistent length
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

# Define colors for each phase
color_baseline1 = '#D3D3D3' # Lightest gray
color_intervention = '#000000' # Blackest
color_baseline2 = '#808080' # Medium gray

# Create a list of colors corresponding to each data point's phase
colors = []
for i in range(len(all_data)):
    if i < len(baseline1_data):
        colors.append(color_baseline1)
    elif i < len(baseline1_data) + len(intervention_data):
        colors.append(color_intervention)
    else:
        colors.append(color_baseline2)

# Create the plot
fig, ax = plt.subplots(figsize=(14, 7))

# Create bar chart with differentiated colors
bars = ax.bar(x_indices, all_data, color=colors, width=0.8)

# JABA style: No top/right spines, no grid lines
ax.spines[['right', 'top']].set_visible(False)
ax.grid(False)

# Set axis labels and title
ax.set_xlabel("Observation Sessions")
ax.set_ylabel("Frequency of Escape-Maintained Off-Task Behavior")
ax.set_title("Impact of Negative Reinforcement on Off-Task Behavior", fontsize=14, pad=20)

# Add vertical dotted lines for phase changes
for boundary in phase_boundaries:
    ax.axvline(x=boundary + 0.5, color='black', linestyle=':', linewidth=1.5)

# Add phase labels above the graph
current_x_pos = 0.5 # Start position for the first label (center of first bar)
y_text_pos = ax.get_ylim()[1] * 1.05 # Position labels slightly above the max y-value

for i, label in enumerate(phase_labels):
    if i == 0: # Baseline 1
        phase_length = len(baseline1_data)
    elif i == 1: # Intervention
        phase_length = len(intervention_data)
    else: # Baseline 2
        phase_length = len(baseline2_data)

    label_x_position = current_x_pos + (phase_length / 2) - 0.5 # Center the label above the phase
    ax.text(label_x_position + 0.5, y_text_pos, label, ha='center', va='bottom', fontsize=10, weight='bold')
    current_x_pos += phase_length

# Set x-axis ticks to show every other trial to prevent overlap, and reduce font size
ax.set_xticks(x_indices[::2]) # Select every other tick
ax.set_xticklabels(x_indices[::2], fontsize=8) # Label with session numbers, smaller font
ax.tick_params(axis='x', length=5) # Add small tick marks

# Adjust y-axis to start from 0 and have appropriate range
ax.set_ylim(bottom=0)
# Generate ticks from 0 up to max Y value, with a step of 2
y_tick_values = np.arange(0, ax.get_ylim()[1] + 1, 2)
ax.set_yticks(y_tick_values)
ax.set_yticklabels(y_tick_values, fontsize=8) # Label with values, smaller font


# Save the figure to a file instead of showing it interactively
plt.savefig('negative_reinforcement_graph.png', dpi=300, bbox_inches='tight')

# Close the plot to free up memory (important in non-interactive environments)
plt.close(fig)
