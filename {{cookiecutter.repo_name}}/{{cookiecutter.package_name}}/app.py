import os
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
import plotly.graph_objs as go
from flask import Flask
from dash import Dash
from dash.dependencies import Input, Output, State
from dotenv import load_dotenv
from exceptions import ImproperlyConfigured

DOTENV_PATH = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(DOTENV_PATH)

if 'DYNO' in os.environ:
    # the app is on Heroku
    debug = False
    # google analytics with the tracking ID for this app
    # external_js.append('https://codepen.io/jackdbd/pen/rYmdLN.js')
else:
    debug = True
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)

try:
    py.sign_in(os.environ['PLOTLY_USERNAME'], os.environ['PLOTLY_API_KEY'])
except KeyError:
    raise ImproperlyConfigured('Plotly credentials not set in .env')

app_name = '{{cookiecutter.project_name}}'
server = Flask(app_name)

try:
    server.secret_key = os.environ['SECRET_KEY']
except KeyError:
    raise ImproperlyConfigured('SECRET KEY not set in .env:')

app = Dash(name=app_name, server=server, csrf_protect=False)

external_js = []

external_css = [
    # dash stylesheet
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    'https://fonts.googleapis.com/css?family=Lobster|Raleway',
    '//maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css',
]

theme = {
    'font-family': 'Lobster',
    'background-color': '#e0e0e0',
}
def create_header():
    header_style = {
        'background-color': theme['background-color'],
        'padding': '1.5rem',
    }
    header = html.Header(html.H1(children=app_name, style=header_style))
    return header


def create_content():
    content = html.Div(

        children=[

            # range slider with start date and end date
            html.Div(
                children=[
                    dcc.RangeSlider(
                        id='year-slider',
                        min=1990,
                        max=2018,
                        value=[2010, 2015],
                        marks={(i): f'{i}' for i in range(1990, 2018, 2)},
                    ),
                ],
                style={'margin-bottom': 20},
            ),

            html.Hr(),

            html.Div(
                children=[
                    dcc.Graph(
                        id='graph-0',
                        figure={
                            'data': [
                                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                            ],
                            'layout': {'title': 'Dash Data Visualization'},
                        },
                    ),
                ],
                className='row',
                style={'margin-bottom': 20},
            ),

            html.Div(
                children=[
                    html.Div(
                        dcc.Graph(id='graph-1'),
                        className='six columns',
                    ),
                    html.Div(
                        dcc.Markdown('''
                        This is a markdown description created with a Dash Core Component.
                        
                        > A {number} days of training to develop.
                        > Ten {number} days of training to polish.
                        >
                        > — Miyamoto Musashi

                        ***
                        '''.format(number='thousand').replace('  ', '')),
                        className='six columns',
                    ),
                ],
                className='row',
                style={'margin-bottom': 20},
            ),

            html.Hr(),

        ],
        id='content',
        style={'width': '100%', 'height': '100%'},
    )
    return content


def create_footer():
    footer_style = {
        'background-color': theme['background-color'],
        'padding': '0.5rem',
    }
    p0 = html.P(
        children=[
            html.Span('Built with '),
            html.A('Plotly Dash',
                   href='https://github.com/plotly/dash', target='_blank')
        ],
    )
    p1 = html.P(
        children=[
            html.Span('Data from '),
            html.A('some website', href='https://some-website.com/', target='_blank')
        ],
    )
    a_fa = html.A(
        children=[
            html.I([], className='fa fa-font-awesome fa-2x'),
            html.Span('Font Awesome')
        ],
        style={'text-decoration': 'none'},
        href='http://fontawesome.io/', target='_blank',
    )

    div = html.Div([p0, p1, a_fa])
    footer = html.Footer(children=div, style=footer_style)
    return footer


def serve_layout():
    layout = html.Div(
        children=[
            create_header(),
            create_content(),
            create_footer(),
        ],
        className='container',
        style={'font-family': theme['font-family']},
    )
    return layout


app.layout = serve_layout
for js in external_js:
    app.scripts.append_script({'external_url': js})
for css in external_css:
    app.css.append_css({'external_url': css})


# TODO: callbacks

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run_server(debug=debug, port=port, threaded=True)
