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
    1.5, 2.5, 2.5, 3.5, 3.5, 5, 5, 7, 7, 7.5, 6, 10, 12, 11, 10, 9, 8 # Next 17 sessions + 1 added to make 24: climbing towards higher baseline
]

# Ensure all phases have the same number of data points for direct session-by-session comparison
num_sessions = len(baseline1_data)

# X-axis labels (Session numbers)
session_labels = np.arange(1, num_sessions + 1)

# Define bar width and positions for grouped bars
bar_width = 0.25
index = np.arange(num_sessions)

# Define colors for each phase
color_baseline1 = '#D3D3D3' # Lightest gray
color_intervention = '#000000' # Blackest
color_baseline2 = '#808080' # Medium gray

# Create the plot
fig, ax = plt.subplots(figsize=(16, 8)) # Wider figure to accommodate grouped bars

# Plot each set of bars for each phase, with an offset for grouping
bar1 = ax.bar(index - bar_width, baseline1_data, bar_width, 
              label='Baseline 1', color=color_baseline1)
bar2 = ax.bar(index, intervention_data, bar_width, 
              label='Intervention', color=color_intervention)
bar3 = ax.bar(index + bar_width, baseline2_data, bar_width, 
              label='Baseline 2 (Withdrawal)', color=color_baseline2)

# JABA style: No top/right spines, no grid lines
ax.spines[['right', 'top']].set_visible(False)
ax.grid(False)

# Set axis labels and title
ax.set_xlabel("Observation Sessions")
ax.set_ylabel("Frequency of Escape-Maintained Off-Task Behavior")
ax.set_title("Impact of Negative Reinforcement on Off-Task Behavior Across Phases", fontsize=16, pad=20)

# Set x-axis ticks to be at the center of each group of bars
ax.set_xticks(index)
ax.set_xticklabels(session_labels)
ax.tick_params(axis='x', length=5) # Add small tick marks

# Adjust y-axis to start from 0 and have appropriate range
ax.set_ylim(bottom=0)
ax.set_yticks(np.arange(0, ax.get_ylim()[1] + 5, 5)) # Adjust y-ticks to be clear

# Add a legend to differentiate the phases by color
ax.legend(loc='upper right', frameon=False, fontsize=10)

# Save the figure to a file instead of showing it interactively
plt.savefig('negative_reinforcement_grouped_graph.png', dpi=300, bbox_inches='tight')

# Close the plot to free up memory (important in non-interactive environments)
plt.close(fig)
