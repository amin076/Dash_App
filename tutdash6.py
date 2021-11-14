import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div(['first dash app',
                      html.Div([
                     html.Img(src='/assets/iran.jpeg'),
                          html.P('''Mary Sheil is the first European, female travel writer who travelled and lived in
                        Persia and left behind a valuable travel journal which later was published in a book. 
                        There were many more female travellers to Persia, Ella Sykes, Gertrud Bell, Susan Townley,
                        Elizabeth Ross and others. I selected those that fitted better into the genre of travel
                        writing and also were larger than life characters. However, the inclusion of Mary Sheil is
                        solely for her being the first female who travelled to Persia and wrote a book of some historical importance.

''')]

                    )],className='container text-center')

if __name__ == '__main__':
    app.run_server()