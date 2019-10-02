# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go

app = dash.Dash()
server = app.server

# Gets the data from Leo repo, using tool pd from panda
df = pd.read_csv('https://raw.githubusercontent.com/LeoMonrroy/legendary-palm-tree/master/fakegraph.csv', sep=";")

app.layout = html.Div(children=[

    # Header
    html.H1(children='Försök till visualiseing'),

    # New section, Body
    html.Div(children='''
        Grupp 6
    '''),

    # Plotting the graph with the id; try_at_data_vis
    dcc.Graph(
        id='try_at_data_vis',
        figure={
            'data': [
                go.Scatter(
                    x=df.Tidpunkter,
                    y=df.testset,
                    mode='lines'
                )
            ],
            'layout': go.Layout(
                title='TH0 Genexpression över tid',
                xaxis={'title': 'Tid(h)'},
                yaxis={'title': 'Expression .../...'},
            )

        })])
    # End of graph.

