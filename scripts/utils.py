

def remove_outliers(df, column_name, v1=0.1, v2=0.9):
    q1, q2 = df[column_name].quantile([v1, v2])
    mask = df[column_name].between(q1, q2)
    df = df[mask]

    return df