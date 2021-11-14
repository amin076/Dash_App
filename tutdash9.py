import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas_datareader.data as web
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div(children=[
    html.Div(
        html.H3('pair companies comparision : ',
                style={'margin':'10px','padding':'10px' })
                       ),
    html.Div([
              html.Span(' code 1 : '),
              dcc.Input(id="inputcode1", type="text",placeholder='appl'
                 , style = {'border': '0px', 'borderRadius': '5px','padding':'5px'}),
              html.Span(' code 2 : '),
              dcc.Input(id="inputcode2", type="text",placeholder='appl'
                 , style = {'border': '0px', 'borderRadius': '5px','padding':'5px'}),
              html.Span(' start date : '),
              dcc.Input(id="inputst", type="text",
                        style = {'border': '0px', 'borderRadius': '5px','padding':'5px'}),
              html.Span(' end date : '),
              dcc.Input(id="inputend", type="text",
                        style = {'border': '0px', 'borderRadius': '5px','padding':'5px'}),
              html.Hr(),
    html.Div(id='outpout1'),
    html.Div(id='outpout2')])
], style={
    'margin': '35px',
    'background' : '#F6EFEB',
    'borderRadius' : '7px',
'boxShadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)'
},
    className=' text-center')


@app.callback(
    [Output('outpout1', 'children'),Output('outpout2', 'children')],
    [Input("inputcode1", "value"),Input("inputcode2", "value"), Input("inputst", "value"), Input("inputend", "value")],
             )
def HistoryGraph(a,d, b, c):
    if [a,d, b, c] is None:
        raise PreventUpdate

    company1 = a
    starting = b
    ending = c
    company2 = d
    df1 = web.DataReader(company1, data_source='yahoo', start=starting, end=ending)
    df2 = web.DataReader(company2, data_source='yahoo', start=starting, end=ending)
    figure1=dcc.Graph(
        id='example-graph',
        figure={'data': [{'x': df1.index, 'y': df1.Close, 'type': 'line', 'name': company1}]
                })

    figure2 = dcc.Graph(
        id='example-graph2',
        figure={'data': [{'x': df2.index, 'y': df2.Close, 'type': 'line', 'name': company2}]
                })
    return figure1, figure2


if __name__ == '__main__':
    app.run_server()


