# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


app = dash.Dash()

# Bootstrap CSS.
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})

app.layout = html.Div([
    html.Div([
        html.Div([
            html.H2(children='T-cells',
                    className="nine columns",
                    ),
            html.Img(
                src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/SEM_Lymphocyte.jpg/1024px-SEM_Lymphocyte.jpg",
                className='three columns',
                style={
                    'height': '10%',
                    'width': '10%',
                    'float': 'right',
                    'position': 'relative',
                    'margin-top': 10,
                    'margin-right': 30
                },
            ),

            html.Div(children='''DBT: Design Build Test
                    ''',
                    className='nine columns',
            )
        ], className='row', style={'backgroundColor': '#E0E0E0', 'margin-top': 0}),
        html.Div(
            [
            html.Div([
                dcc.Graph(
                    id='example-graph',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                        ],
                        'layout': {
                            'title': 'Graph 1'
                        }
                    }
                ),
            ], className='six columns'
            ),
            html.Div([
                dcc.Graph(
                    id='example-graph-2',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': u'Montréal'},
                        ],
                        'layout': {
                            'title': 'Graph 2'
                        }
                    }
                ),
            ], className='six columns'
            )
        ], className='row'),
        html.Div([
            dcc.Input(id='my-id', value='initial value', type="text"),
            html.Div(id='my-div')
        ], className='row'),
    ], className='ten columns offset-by-one')

])

@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)