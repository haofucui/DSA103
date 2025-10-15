"""
wine_eda.py
-----------
Homework: Exploratory Data Analysis on the Wine dataset.

Goals:
1. Load and inspect the data
2. Perform exploratory analysis and visualizations
3. Apply PCA
"""

# Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA



# Main analysis function
def main():
    # --- 1. Load data ---
    print("Loading dataset...")
    wine = load_wine()
    df = pd.DataFrame(wine.data, columns=wine.feature_names)

    # add a 'target' column
    y = pd.Series(wine.target, name='target')
    df = pd.concat([df, y], axis=1)

    # print basic info (shape, first rows, summary statistics)
    #print(df.shape)
    #print(df.columns)
    #print(df.head(5))
    #print(df.describe())

    # --- 2. Basic exploration ---
    # print class distribution and check for missing values
    #print(df['target'].value_counts())
    #print(df.isna().sum())

    # --- 3. Correlation analysis ---
    # compute correlation matrix (corr = df.corr(numeric_only=True))
    # plot and save a heatmap (e.g. 'heatmap.png')
    #corr = df.corr(numeric_only=True)
    #print(corr)
    #sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', square=True)
    #plt.show()

    # --- 4. Visualisations ---
    # create and save a pairplot using a few selected features
    # create and save a boxplot comparing one feature across classes
    #sns.pairplot(df[['alcohol', 'malic_acid', 'color_intensity', 'proline', 'target']], hue='target', diag_kind='kde', palette='husl')
    #plt.show()
    sns.boxplot(x='target', y='alcohol', data=df, palette='Set2')
    plt.show() 

    # --- 5. Scaling and PCA ---
    # separate features (X) and target (y)
    # scale the features using StandardScaler
    # apply PCA (2 components)
    # create a DataFrame with PCA results and target
    # plot and save a scatterplot of the first two components (color by target)
    

# Entry point
if __name__ == "__main__":
    main()