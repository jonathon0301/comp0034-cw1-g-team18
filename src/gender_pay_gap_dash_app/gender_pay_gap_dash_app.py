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
    html.Div([
        html.Label("Select X Axis Variable:"),
        dcc.Dropdown(
            id='xaxis_selector',
            options=[
                {'label': 'EmployerSizeMedian', 'value': 'EmployerSizeMedian'},
                {'label': 'Industry', 'value': 'Industry'},
                {'label': 'Region', 'value': 'UK region'},
            ],
            value='UK region'
        ),
    ]),
    html.Div([
        html.Label("Select Y Axis Variable:"),
        dcc.Dropdown(
            id='yaxis_selector',
            options=[
                {'label': 'DiffMeanHourlyPercent', 'value': 'DiffMeanHourlyPercent'},
                {'label': 'DiffMedianBonusPercent', 'value': 'DiffMedianBonusPercent'},
                {'label': 'FemaleTopQuartile', 'value': 'FemaleTopQuartile'}
            ],
            value='FemaleTopQuartile')
        ],),
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
    [Input('xaxis_selector', 'value'), Input('yaxis_selector', 'value')]
)
def update_boxplot(xaxis_selector, yaxis_selector):
    fig = px.box(df_visualization, x=xaxis_selector, y=yaxis_selector)
    fig.update_layout(yaxis=dict(range=[-100, 100]))
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
