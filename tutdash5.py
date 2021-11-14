import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.Div(
        html.H3('first dash app and you can type something : ')
                       ),
    html.Div(['type here : ',
              dcc.Input(id="inputa", type="number"),
              html.Span(' type here : '),
              dcc.Input(id="inputb", type="number"),
              html.Span(' type here : '),
              dcc.Input(id="inputc", type="number"),
              html.Hr(),
    html.H3(id='outpout1')])
])

@app.callback(
    Output('outpout1', 'children'),
    [Input("inputa", "value"), Input("inputb", "value"), Input("inputc", "value")],
             )

def rewrite (a, b, c):
    return a, b, c

if __name__ == '__main__':
    app.run_server()


