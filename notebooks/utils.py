# Import libraries
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt



# Remove outliers 
def remove_outliers(df, column_name, q1=0.1, q2=0.9):
    v1, v2 = df[column_name].quantile([q1, q2])
    mask = df[column_name].between(v1, v2)
    df = df[mask]

    return df


# plot boxplot
def plot_boxplot(data, x, title="title", x_axis="x", y_axis="y"):
    fig = px.box(
        x = x,
        data_frame=data,
        title = title
    )

    fig.update_layout(xaxis_title=x_axis)
    
    return fig

def sns_lineplot(x, y, title="title", xlabel="x-axis", ylabel="y-axis"):
    fig = sns.lineplot(
        x=x,
        y=y
    )
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # return fig
