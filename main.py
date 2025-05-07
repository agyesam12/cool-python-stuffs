import dash
from dash import dcc, html

# Creating a Dash application
app = dash.Dash(__name__)

# Defining the layout of the dashboard
app.layout = html.Div([
    html.H1("Sammykeys Dashboard"),
    dcc.Graph(
        id='Sammykeys Graph',
        figure={
            'data': [
                {
                    'x': [1, 2, 3],
                    'y': [4, 1, 2],
                    'type': 'bar',
                    'name': 'Bar Chart'
                },
                {
                    'x': [1, 2, 3],
                    'y': [2, 4, 5],
                    'type': 'line',
                    'name': 'Line Chart'
                }
            ],
            'layout': {
                'title': 'Graph Title',
                'xaxis': {'title': 'x-axis'},
                'yaxis': {'title': 'y-axis'}
            }
        }
    )
])

if __name__ == "__main__":
    app.run(debug=True)
