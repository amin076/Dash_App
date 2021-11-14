import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas_datareader.data as web
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div(children=[
    html.Div(
        html.H3('first dash app and you can type something : ',
                style={'margin':'10px','padding':'10px' })
                       ),
    html.Div(['company code : ',
              dcc.Input(id="inputcode", type="text",placeholder='appl'
                 , style = {'border': '0px', 'borderRadius': '5px','padding':'5px'}),
              html.Span(' start date : '),
              dcc.Input(id="inputst", type="text",
                        style = {'border': '0px', 'borderRadius': '5px','padding':'5px'}),
              html.Span(' end date : '),
              dcc.Input(id="inputend", type="text",
                        style = {'border': '0px', 'borderRadius': '5px','padding':'5px'}),
              html.Hr(),
    html.Div(id='outpout1')])
], style={
    'margin': '35px',
    'background' : '#F6EFEB',
    'borderRadius' : '7px',
'boxShadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)'
},
    className=' text-center')


@app.callback(
    Output('outpout1', 'children'),
    [Input("inputcode", "value"), Input("inputst", "value"), Input("inputend", "value")],
             )
def HistoryGraph(a, b, c):

    company = a
    starting = b
    ending = c
    df = web.DataReader(company, data_source='yahoo', start=starting, end=ending)
    return dcc.Graph(
        id='example-graph',
        figure={'data': [{'x': df.index, 'y': df.Close, 'type': 'bar', 'name': company}]
                })


if __name__ == '__main__':
    app.run_server()


