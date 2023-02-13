import plotly.express as px
from dash import html, dcc, Dash
from dash.dependencies import Input, Output
import pandas as pd


# Import datasets
df_visualization = pd.read_csv('data/gender_pay_gap_prepared.csv')
df_visualization['EmployerSizeMedian'] = df_visualization['EmployerSizeMedian'].astype(str)
df_3 = pd.read_csv('data/df_hourly_percent_on_region')
df_4 = pd.read_csv('data/df_bonus_percent_on_region')
df_5 = pd.read_csv('data/df_female_top_percent_on_region')
df_6 = pd.read_csv('data/df_bar_on_region.csv')
df_7 = pd.read_csv('data/df_bar_on_size.csv')
df_7['EmployerSizeMedian'] = df_7['EmployerSizeMedian'].astype(str)
df_8 = pd.read_csv('data/df_bar_on_industry.csv')

# Plot1: Histogram on DiffMeanHourlyPercent
fig1 = px.histogram(df_visualization, nbins=200, title="Distribution of DiffMeanHourlyPercent",
                    x="DiffMeanHourlyPercent")

# Plot2: Histogram on DiffMedianHourlyPercent
fig2 = px.histogram(df_visualization, nbins=200, title="Distribution of DiffMedianHourlyPercent",
                    x="DiffMedianHourlyPercent")

# Plot3: UK map on DiffMeanHourlyPercent
fig3 = px.scatter_mapbox(df_3, lat='Latitude', lon='Longitude', hover_name='UK region', color='UK region',
                         color_discrete_sequence=px.colors.sequential.Plasma,
                         zoom=4.5, height=500)
for i, trace in enumerate(fig3.data):
    customdata_3 = [df_3.iloc[i]['mean_diff_hourly_percent'].round(2),
                    df_3.iloc[i]['median_diff_hourly_percent'].round(2),
                    df_3.iloc[i]['lower_quartile_hourly_percent'].round(2),
                    df_3.iloc[i]['upper_quartile_hourly_percent'].round(2)]

    trace.update(hovertemplate='Average of Mean Hourly Payment % Difference:' + str(customdata_3[0]) +
                               '<br>Median of Mean Hourly Payment % Difference:' + str(customdata_3[1]) +
                               '<br>Lower Quartile of Mean Hourly Payment % Difference:' + str(customdata_3[2]) +
                               '<br>Upper Quartile of Mean Hourly Payment % Difference:' + str(customdata_3[3]),
                 customdata=customdata_3)

fig3.update_layout(mapbox_style='open-street-map')
fig3.update_layout(margin=dict(l=0, r=0, t=0, b=0))

# Plot4: UK map on DiffMeanBonusPercent
fig4 = px.scatter_mapbox(df_4, lat='Latitude', lon='Longitude', hover_name='UK region', color='UK region',
                         color_discrete_sequence=px.colors.sequential.Plasma,
                         zoom=4.5, height=500)
for i, trace in enumerate(fig4.data):
    customdata_4 = [df_4.iloc[i]['mean_diff_bonus_percent'].round(2),
                    df_4.iloc[i]['median_diff_bonus_percent'].round(2),
                    df_4.iloc[i]['lower_quartile_bonus_percent'].round(2),
                    df_4.iloc[i]['upper_quartile_bonus_percent'].round(2)]

    trace.update(hovertemplate='Average of Mean Bonus Payment % Difference:' + str(customdata_4[0]) +
                               '<br>Median of Mean Bonus Payment % Difference:' + str(customdata_4[1]) +
                               '<br>Lower Quartile of Mean Bonus Payment % Difference:' + str(customdata_4[2]) +
                               '<br>Upper Quartile of Mean Bonus Payment % Difference:' + str(customdata_4[3]),
                 customdata=customdata_4)

fig4.update_layout(mapbox_style='open-street-map')
fig4.update_layout(margin=dict(l=0, r=0, t=0, b=0))

# Plot5: UK map on FemaleTopQuartile
fig5 = px.scatter_mapbox(df_5, lat='Latitude', lon='Longitude', hover_name='UK region', color='UK region',
                         color_discrete_sequence=px.colors.sequential.Plasma,
                         zoom=4.5, height=500)
for i, trace in enumerate(fig5.data):
    customdata_5 = [df_5.iloc[i]['mean_female_top_percent'].round(2),
                    df_5.iloc[i]['median_female_top_percent'].round(2),
                    df_5.iloc[i]['lower_quartile_female_top_percent'].round(2),
                    df_5.iloc[i]['upper_quartile_female_top_percent'].round(2)]

    trace.update(hovertemplate='Average of Highly Paid Women %:' + str(customdata_5[0]) +
                               '<br>Median of Highly Paid Women %:' + str(customdata_5[1]) +
                               '<br>Lower Quartile of Highly Paid Women %:' + str(customdata_5[2]) +
                               '<br>Upper Quartile of Highly Paid Women %:' + str(customdata_5[3]),
                 customdata=customdata_5)

fig5.update_layout(mapbox_style='open-street-map')
fig5.update_layout(margin=dict(l=0, r=0, t=0, b=0))

# Plot 6: Bar Chart of Average Percentage Difference on Hourly Pay against regions
fig6 = px.bar(df_6, x='mean_diff_hourly_percent', y='UK region', orientation='h')
fig6.update_layout(xaxis_title="Average Percentage Difference on Hourly Pay", yaxis_title="UK Region")

# Plot 7: Bar Chart of Average Percentage Difference on Hourly Pay against EmployerSize
fig7 = px.bar(df_7, x='mean_diff_hourly_percent', y='EmployerSizeMedian', orientation='h')
fig7.update_layout(xaxis_title="Average Percentage Difference on Hourly Pay", yaxis_title="Employer Size Median")

# Plot 8: Bar Chart of Average Percentage Difference on Hourly Pay against Industry
fig8 = px.bar(df_8, x='mean_diff_hourly_percent', y='Industry', orientation='h')
fig8.update_layout(xaxis_title="Average Percentage Difference on Hourly Pay", yaxis_title="Industry")

# Dash App
app = Dash(__name__)

app.css.append_css({
    "external_url": "/assets/style.css.css"
})

app.layout = html.Div([
    html.H1("Gender Pay Gap Situations Visualisation Dashboard"),
    html.H2('How Serious Is Gender Pay Gap?'),
    dcc.RadioItems(
        id='histogram-selector',
        options=[
            {'label': 'Percentage Difference on Mean Hourly Pay', 'value': 'DiffMeanHourlyPercent'},
            {'label': 'Percentage Difference on Median Hourly Pay', 'value': 'DiffMedianHourlyPercent'}
        ],
        value='DiffMeanHourlyPercent'
    ),
    dcc.Graph(id='histogram'),
    html.H2(
        'How Is Gender Pay Gap Distributed?'),
    html.Div([
        html.Label("Select X Axis Variable:"),
        dcc.Dropdown(
            id='xaxis_selector',
            options=[
                {'label': 'Employer Size Median', 'value': 'EmployerSizeMedian'},
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
                {'label': 'Percentage Difference on Hourly Pay', 'value': 'DiffMeanHourlyPercent'},
                {'label': 'Percentage Difference on Bonus', 'value': 'DiffMeanBonusPercent'},
                {'label': 'Percentage of Highly Paid Female', 'value': 'FemaleTopQuartile'}
            ],
            value='FemaleTopQuartile')
    ], ),
    dcc.Graph(id='boxplot'),
    html.H2('How is Gender Pay Gap Situation in Each Region?'),
    html.Div([
        html.Label("Select which data you wanna investigate"),
        dcc.Dropdown(
            id='map_selector',
            options=[
                {'label': 'Percentage Difference on Hourly Pay', 'value': 'DiffMeanHourlyPercent'},
                {'label': 'Percentage Difference on Bonus', 'value': 'DiffMeanBonusPercent'},
                {'label': 'Percentage of Highly Paid Female', 'value': 'FemaleTopQuartile'}
            ],
            value='DiffMeanHourlyPercent')
    ], ),
    dcc.Graph(id='scatter_mapbox'),
    html.H2('Where Is The Most Serious Gender Pay Gap? (The top the most)'),
    html.Div([
        html.Label("Select in which aspect you wanna compare"),
        dcc.Dropdown(
            id='bar_selector',
            options=[
                {'label': 'Region', 'value': 'UK region'},
                {'label': 'Employer Size', 'value': 'EmployerSizeMedian'},
                {'label': 'Industry', 'value': 'Industry'}
            ],
            value='UK region')
    ], ),
    dcc.Graph(id='bar')
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


@app.callback(
    Output('scatter_mapbox', 'figure'),
    [Input('map_selector', 'value')])
def update_map(map_selector):
    if map_selector == 'DiffMeanHourlyPercent':
        return fig3
    elif map_selector == 'DiffMeanBonusPercent':
        return fig4
    else:
        return fig5


@app.callback(
    Output('bar', 'figure'),
    [Input('bar_selector', 'value')])
def update_bar(bar_selector):
    if bar_selector == 'UK region':
        return fig6
    elif bar_selector == 'EmployerSizeMedian':
        return fig7
    else:
        return fig8


if __name__ == "__main__":
    app.run_server(debug=True)
