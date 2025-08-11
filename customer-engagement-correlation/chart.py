import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style and context
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic realistic data for customer engagement metrics
np.random.seed(42)  # reproducibility
data = pd.DataFrame({
    'Website Visits': np.random.normal(500, 50, 100),
    'Email Opens': np.random.normal(300, 40, 100),
    'Purchases': np.random.normal(50, 10, 100),
    'Social Media Interactions': np.random.normal(200, 30, 100),
    'Customer Support Calls': np.random.normal(20, 5, 100)
})

# Compute correlation matrix
corr_matrix = data.corr()

# Create heatmap
plt.figure(figsize=(8, 8))  # for 512x512 output with dpi=64
heatmap = sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    cbar=True,
    square=True,
    linewidths=.5,
    annot_kws={"size": 12}
)

# Titles and labels
plt.title("Customer Engagement Correlation Matrix", fontsize=16, pad=20)

# Save as exactly 512x512 pixels
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
plt.close()
