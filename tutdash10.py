import dash_core_components as dcc
import dash_table as dt
import dash_html_components as html
import dash
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

sample_data = {
    'series': {
        'data': [
            {'title': 'Game of Thrones', 'score': 9.5},
            {'title': 'Stranger Things', 'score': 8.9},
            {'title': 'Vikings', 'score': 8.6}
        ],
        'style': {
            'backgroundColor': '#ff998a'
        }
    },
    'movies': {
        'data': [
            {'title': 'Rambo', 'score': 7.7},
            {'title': 'The Terminator', 'score': 8.0},
            {'title': 'Alien', 'score': 8.5}
        ],
        'style': {
            'backgroundColor': '#fff289'
        }
    }
}

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.H1('Multi output example'),
    dcc.Dropdown(id='data-dropdown', options=[
        {'label': 'Movies', 'value': 'movies'},
        {'label': 'Series', 'value': 'series'}
    ], value='movies'),
    html.Div([
        dcc.Graph(id='graph'),
        dt.DataTable(id='data-table', columns=[
            {'name': 'Title', 'id': 'title'},
            {'name': 'Score', 'id': 'score'}
        ])
    ])
], id='container', style={
    'margin': '35px',
    'background' : '#F6EFEB',
    'borderRadius' : '7px',
'boxShadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)'
},
    className='container text-center')


@app.callback([
    Output('graph', 'figure'),
    Output('data-table', 'data'),
    Output('data-table', 'columns'),
    Output('container', 'style')
], [Input('data-dropdown', 'value')])
def multi_output(value):
    if value is None:
        raise PreventUpdate

    selected = sample_data[value]
    data = selected['data']
    columns = [
        {'name': k.capitalize(), 'id': k}
        for k in data[0].keys()
    ]
    figure = go.Figure(
        data=[
            go.Bar(x=[x['score']], text=x['title'], name=x['title'])
            for x in data
        ]
    )

    return figure, data, columns, selected['style']


if __name__ == '__main__':
    app.run_server()