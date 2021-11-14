import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas_datareader.data as web
import datetime as dt
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([
    html.Div(
    html.Div( html.H1("Companies Correlation and History")
              )),
    html.Div(["Company : ",
              dcc.Input(id='company1', value='', type='text')]),
    html.Br(),
    html.Div(id='com1'),
html.Div('stock market',className='text-center' ),
], className='container fluid text-center')


@app.callback(
    Output(component_id='com1', component_property='children'),

    [Input(component_id='company1', component_property='value')],
)
def create_graph(company):
    starting = dt.datetime(2010, 1, 1)
    ending = dt.datetime.now()
    df = web.DataReader(company, data_source='yahoo', start=starting, end=ending)
    return dcc.Graph(
        id='example-graph',
        figure={'data': [{'x': df.index, 'y': df.Close, 'type': 'line', 'name': company}]
                })


if __name__ == '__main__':
    app.run_server()

