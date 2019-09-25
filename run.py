# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go


app = dash.Dash()
server = app.server
df = pd.read_csv('https://raw.githubusercontent.com/LeoMonrroy/legendary-palm-tree/master/fakegraph.csv', sep=";")

app.layout = html.Div(children=[
    html.H1(children='Försök till visualiseing'),
    html.Div(children='''
        Grupp 6
    '''),
    dcc.Graph(
        id='Försök till datavisualisering',
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
                xaxis={'title' : 'Tid(h)'},
                yaxis={'title': 'Expression .../...'},
            )
        })])
