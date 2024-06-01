import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    # Read the file into a DataFrame
    yield_df = pd.read_csv("../data/barley_yield.txt", sep="\s+")
    yield_df.columns = ["year", "yield_dt_ha"]
    preds_df = pd.read_csv("../data/climate_variables.txt", sep="\s+")
    # Merge
    data_df = pd.merge(yield_df, preds_df, on="year")
    return data_df


data_df = load_data()
data_df.drop("year", axis=1).corr()

# --------------------------------------------------------------
# Plot Correlation Matrix Heatmap
# --------------------------------------------------------------
# Basic Seaborn Heatmap
correlation_matrix = data_df.drop("year", axis=1).corr()
# plt.figure(figsize=(20, 12))
p = sns.heatmap(correlation_matrix, annot=True, cmap="BrBG", fmt=".2f")
p.set_title("Correlation Heatmap", fontdict={"fontsize": 12}, pad=12)
plt.savefig("../figures/heatmap.png", dpi=300, bbox_inches="tight")

# Triangle Correlation Heatmap
# plt.figure(figsize=(20, 12))
mask = np.triu(np.ones_like(correlation_matrix))
p = sns.heatmap(correlation_matrix, mask=mask, annot=True, cmap="BrBG", fmt=".2f")
p.set_title("Correlation Heatmap", fontdict={"fontsize": 12}, pad=12)
plt.savefig("../figures/heatmap.png", dpi=300, bbox_inches="tight")

# --------------------------------------------------------------
# Plot Scatterplots with Yield
# --------------------------------------------------------------
data_df.columns
cols1 = [
    "yield_dt_ha",
    "prec",
    "sun_hours",
    "temp_max",
    "temp_min",
]
sns.pairplot(data_df[cols1])
cols2 = ["yield_dt_ha", "temp_min_ground", "vap_pressure", "wind_vel"]
p = sns.pairplot(data_df[cols2])
p.set_title("Correlation Heatmap", fontdict={"fontsize": 12}, pad=12)
