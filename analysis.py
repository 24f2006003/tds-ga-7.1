{
  "cells": [
    {
      "cell_type": "code",
      "metadata": { "language": "python" },
      "source": [
  "# Data Analysis Notebook",
  "mo.md('**Contact:** 24f2006003@ds.study.iitm.ac.in')",
        "# This cell defines the dataset and initial variables.",
        "import marimo as mo",
        "import numpy as np",
        "import pandas as pd",
        "",
        "np.random.seed(42)",
        "x = np.linspace(0, 10, 100)",
        "y = 2 * x + np.random.normal(0, 2, 100)",
        "df = pd.DataFrame({'x': x, 'y': y})"
      ]
    },
    {
      "cell_type": "code",
      "metadata": { "language": "python" },
      "source": [
        "# Interactive slider to control slope",
        "# The value of 'slope' affects the plot and markdown below.",
        "slope = mo.ui.slider(1, 5, value=2, label='Slope')"
      ]
    },
    {
      "cell_type": "code",
      "metadata": { "language": "python" },
      "source": [
        "# Plot and dynamic markdown output based on slider value",
        "# This cell depends on 'slope' from the previous cell.",
        "import matplotlib.pyplot as plt",
        "",
        "y_pred = slope.value * x",
        "",
        "fig, ax = plt.subplots()",
        "ax.scatter(x, y, label='Data')",
        "ax.plot(x, y_pred, color='red', label=f'Fit: y={slope.value}x')",
        "ax.legend()",
        "mo.display(fig)",
        "",
        "mo.md(f\"### Current Slope: {slope.value}\")",
        "mo.md(f\"The red line shows the fit with slope = {slope.value}.\")"
      ]
    }
  ]
}