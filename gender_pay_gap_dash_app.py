import plotly.express as px
from dash import html, dcc, Dash
from dash.dependencies import Input, Output
import pandas as pd

df_visualization = pd.read_csv('gender_pay_gap_prepared.csv')

# Plot1: Histogram on DiffMeanHourlyPercent
fig1 = px.histogram(df_visualization, nbins=50, title="Distribution of DiffMeanHourlyPercent",
                    x="DiffMeanHourlyPercent")

# Plot2: Histogram on DiffMedianHourlyPercent
fig2 = px.histogram(df_visualization, nbins=50, title="Distribution of DiffMedianHourlyPercent",
                    x="DiffMedianHourlyPercent")

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Gender Pay Gap Situations Visualisation Dashboard"),
    html.H2('Distributions of DiffMeanHourlyPercent and DiffMedianHourlyPercent in Histograms'),
    dcc.RadioItems(
        id='histogram-selector',
        options=[
            {'label': 'DiffMeanHourlyPercent', 'value': 'DiffMeanHourlyPercent'},
            {'label': 'DiffMedianHourlyPercent', 'value': 'DiffMedianHourlyPercent'}
        ],
        value='DiffMeanHourlyPercent'
    ),
    dcc.Graph(id='histogram')
])


@app.callback(
    Output('histogram', 'figure'),
    [Input('histogram-selector', 'value')])
def update_histogram(selected_variable):
    if selected_variable == 'DiffMeanHourlyPercent':
        return fig1
    else:
        return fig2


if __name__ == "__main__":
    app.run_server(debug=True)
