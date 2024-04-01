import pandas as pd

def explore_most_rated_products(df):
    return df['PRODUCTID'].value_counts().head(10)

def explore_most_active_users(df):
    return df['USERID'].value_counts().head(10)

def explore_most_correlated_variables(df):
    # Identify correlations between variables
    correlation_matrix = df.corr()

    # Print the top correlated variables
    top_correlations = correlation_matrix.unstack().sort_values(ascending=False)
    print("Top Correlated Variables:")
    print(top_correlations.head(10))
