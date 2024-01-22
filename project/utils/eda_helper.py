import os
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
from scipy.stats.mstats import winsorize



def preliminary_analysis(df):
    # Display the first few rows
    print("top head")
    print(df.head())

    # Check for missing values
    print("missing values")
    print(df.isnull().sum())

    missing_values = df.isnull().sum()
    # Check if any column has missing values
    if (missing_values == 0).all():
        print("All values are correct.")
    else:
        print("Pending values:")
        for column, count in missing_values.items():
            if count > 0:
                print(f"{column}: {count} missing value/s")


def summary(df):
    pd.set_option('display.max_columns', None)
    # Descriptive statistics
    print("Statistic resume")
    print(df.describe(include='all'))
    print("\n")

    # Data types
    print("Data types")
    print(df.dtypes)
    print("\n")

    print("Unique values on each attribute")
    print(df.nunique())
    print("\n")


base_folder_string = os.path.join("generated_charts", datetime.now().strftime("%Y%m%d_%H%M"))


def create_directory_if_not_exists(directory):
    output_dir = os.path.join(base_folder_string, directory)
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


def univariate_analysis(df):
    # Create the directory if it doesn't exist
    output_dir = create_directory_if_not_exists("univariate_analysis")

    # Univariate analysis for numerical variables
    print("Univariate analysis for numerical variables")
    num_vars = ['carat', 'depth', 'table', 'price', 'x', 'y', 'z']
    df[num_vars].hist(bins=20, figsize=(15, 10))
    plt.savefig(os.path.join(output_dir, "numerical.png"))
    plt.close()

    # Univariate analysis for categorical variables
    print("Univariate analysis for categorical variables")
    cat_vars = ['cut', 'color', 'clarity']
    for var in cat_vars:
        sns.countplot(x=var, data=df, palette='viridis')
        plt.savefig(os.path.join(output_dir, f"categorical_{var}.png"))
        plt.close()


def bivariate_analysis(df):
    # Create the directory if it doesn't exist
    output_dir = create_directory_if_not_exists("bivariate_analysis")

    # Bivariate analysis for numerical variables - Pairplot
    print("Bivariate analysis for numerical variables - Pairplot")
    num_vars = ['carat', 'depth', 'table', 'price', 'x', 'y', 'z']
    pairplot = sns.pairplot(df[num_vars])
    pairplot.savefig(os.path.join(output_dir, "bivariate_pairplot.png"))
    plt.close()

    # Bivariate analysis for numerical variables - Correlation matrix
    print("Bivariate analysis for numerical variables - Correlation matrix")
    corr_matrix = df[num_vars].corr()
    heatmap = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    heatmap.figure.savefig(os.path.join(output_dir, "bivariate_corr_matrix.png"))
    plt.close()


# Multivariate analysis
def multivariable_analysis(df):
    output_dir = create_directory_if_not_exists("multivariable_analysis")
    scatterplot = sns.scatterplot(x='carat', y='price', hue='cut', size='depth', data=df, palette='Set2')
    scatterplot.figure.savefig(os.path.join(output_dir, "multivariate_scatterplot.png"))
    plt.close()

# Identify_outliers
def identify_outliers(df):
    print("z_scores")
    z_scores = zscore(df[['carat', 'depth', 'table', 'price', 'x', 'y', 'z']])
    outliers = (z_scores > 3) | (z_scores < -3)
    print(outliers)

    print("Interquartile Range")
    Q1 = df[['carat', 'depth', 'table', 'price', 'x', 'y', 'z']].quantile(0.25)
    Q3 = df[['carat', 'depth', 'table', 'price', 'x', 'y', 'z']].quantile(0.75)
    IQR = Q3 - Q1
    outliers = ((df[['carat', 'depth', 'table', 'price', 'x', 'y', 'z']] < (Q1 - 1.5 * IQR)) | (df[['carat', 'depth', 'table', 'price', 'x', 'y', 'z']] > (Q3 + 1.5 * IQR)))
    print(outliers)


    print("remove outliers")
    df_no_outliers = df[~outliers.any(axis=1)]
    print(df_no_outliers)


    print("Log transformation")
    df[['carat', 'depth', 'table', 'price', 'x', 'y', 'z']] = np.log1p(df[['carat', 'depth', 'table', 'price', 'x', 'y', 'z']])


