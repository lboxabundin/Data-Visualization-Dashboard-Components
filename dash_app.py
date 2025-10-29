from dash import Dash, html, dcc
from dashboard_components.components import chart_card, data_table, summary_kpis
from dashboard_components.data import sample_timeseries

df = sample_timeseries(80)
chart = chart_card('Value over time', df, x='date', y='value', kind='line')
kpis = summary_kpis(df, numeric_cols=['value'])

app = Dash(__name__)
app.layout = html.Div([
    html.H1('Dashboard Components — Dash Demo'),
    html.Div([html.Div([html.H4(k['title']), html.P(f"{k['value']:.2f}"), html.P(k.get('subtitle') or '')]) for k in kpis], style={'display':'flex', 'gap':'1rem'}),
    dcc.Graph(figure=chart['figure']),
    html.H3('Sample data'),
    dcc.Markdown('Use this area to show a data table or controls.'),
])

if __name__ == '__main__':
    app.run_server(debug=True)
