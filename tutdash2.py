import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()
app.layout = html.Div(children=['first dash app and you can type something : ',
                     dcc.Input(id='input1', value='go to...', type='text')

                     ])

if __name__ == '__main__':
    app.run_server()