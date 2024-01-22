from project.utils.csv import get_csv
from project.utils.eda_helper import (preliminary_analysis, summary, univariate_analysis, bivariate_analysis
, multivariable_analysis, identify_outliers)

df = get_csv()

# Preliminary analisis
preliminary_analysis(df)

# Data Summary
summary(df)

# Univariate analisys
univariate_analysis(df)

# Bivariate analisys
bivariate_analysis(df)

# multivariable_analisys
multivariable_analysis(df)

# Identify Outliers
identify_outliers(df)
