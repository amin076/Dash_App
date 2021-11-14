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
    dcc.Input(id='input1', value='...', type='text'),
    html.H3(id='outpout1')])

])

@app.callback(
    Output('outpout1', 'children'),

    [Input('input1', 'value')],
             )

def rewrite(word):
    return 'you write : ', word

if __name__ == '__main__':
    app.run_server()
