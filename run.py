# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go


app = dash.Dash()
server = app.server
df = pd.read_csv('https://raw.githubusercontent.com/RasmusBurge/DBT-T-Cell/master/rawdata.csv', sep=";")


app.layout = html.Div(children=[
    html.H1(children='Försök till visualisering'),
    html.Div(children='''
        Grupp nr 6
    '''),

    dcc.Graph(
        id='Försök till datavisualisering',
        figure={
            'data': [
                go.Scatter(x=df.Tidpunkter, y=df.ENSG00000283297, name='ENSG00000283297', mode='lines+markers'),
                go.Scatter(x=df.Tidpunkter, y=df.ENSG00000283573, name='ENSG00000283573 ', mode='lines+markers'),
                go.Scatter(x=df.Tidpunkter, y=df.ENSG00000282961, name='ENSG00000282961 ', mode='lines+markers')

            ],
            'layout': go.Layout(
                title='TH0 Genexpression över tid',
                xaxis={'title' : 'Tid(h)'},
                yaxis={'title': 'Expression .../...'},
            )
        })])


