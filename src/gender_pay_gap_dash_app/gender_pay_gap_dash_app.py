import plotly.express as px
from dash import html, dcc, Dash
from dash.dependencies import Input, Output
import pandas as pd

df_visualization = pd.read_csv('data/gender_pay_gap_prepared.csv')

# Plot1: Histogram on DiffMeanHourlyPercent
fig1 = px.histogram(df_visualization, nbins=200, title="Distribution of DiffMeanHourlyPercent",
                    x="DiffMeanHourlyPercent")

# Plot2: Histogram on DiffMedianHourlyPercent
fig2 = px.histogram(df_visualization, nbins=200, title="Distribution of DiffMedianHourlyPercent",
                    x="DiffMedianHourlyPercent")

app = Dash(__name__)

app.css.append_css({
    "external_url": "/assets/style.css.css"
})

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
    dcc.Graph(id='histogram'),
    html.H2(
        'Box plots of DiffMeanHourlyPercent, DiffMedianBonusPercent and FemaleTopQuartile against Industry'),
    dcc.Dropdown(
        id='yaxis_selector',
        options=[
            {'label': 'DiffMeanHourlyPercent', 'value': 'DiffMeanHourlyPercent'},
            {'label': 'DiffMedianBonusPercent', 'value': 'DiffMedianBonusPercent'},
            {'label': 'FemaleTopQuartile', 'value': 'FemaleTopQuartile'}
        ],
        value='FemaleTopQuartile'
    ),
    dcc.Graph(id='boxplot')
])


@app.callback(
    Output('histogram', 'figure'),
    [Input('histogram-selector', 'value')])
def update_histogram(selected_variable):
    if selected_variable == 'DiffMeanHourlyPercent':
        return fig1
    else:
        return fig2


@app.callback(
    Output('boxplot', 'figure'),
    [Input('yaxis_selector', 'value')])
def update_boxplot(yaxis_selector):
    fig = px.box(df_visualization, x="Industry", y=yaxis_selector)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
