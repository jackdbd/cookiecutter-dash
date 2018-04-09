import os
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
import plotly.graph_objs as go
from flask import Flask
from dash import Dash
from dash.dependencies import Input, Output, State
from dotenv import load_dotenv
from {{cookiecutter.package_name}}.exceptions import ImproperlyConfigured

DOTENV_PATH = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(DOTENV_PATH)

external_js = []

external_css = [
    # dash stylesheet
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    # Google Fonts
    'https://fonts.googleapis.com/css?family=Lobster|Raleway',
]


if 'DYNO' in os.environ:
    # the app is on Heroku
    debug = False
    # google analytics with the tracking ID for this app
    # external_js.append('https://codepen.io/jackdbd/pen/rYmdLN.js')
else:
    debug = True
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)

py.sign_in(os.environ['PLOTLY_USERNAME'], os.environ['PLOTLY_API_KEY'])



app_name = 'Dash FDA'
server = Flask(app_name)
server.secret_key = os.environ.get('SECRET_KEY')
if server.secret_key is None:
    raise ImproperlyConfigured('Flask SECRET KEY not set in .env')
app = Dash(name=app_name, server=server, csrf_protect=False)

cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem', 'CACHE_DIR': 'cache',
    'CACHE_THRESHOLD': 10, 'CACHE_DEFAULT_TIMEOUT': 30})
# app.config.supress_callback_exceptions = True

theme = {
    'font-family': 'Lobster',
    # 'background-color': '#787878',
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

            # line charts
            html.Div(
                children=[
                    dcc.Graph(id='line-chart'),
                    dcc.Graph(id='line-chart-day'),
                ],
            ),

            html.Hr(),

            dcc.Graph(
                id='example-graph',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                    ],
                    'layout': {'title': 'Dash Data Visualization'},
                }
            )

            # pie charts
            html.Div(
                children=[
                    html.Div(
                        dcc.Graph(id='pie-event'),
                        className='six columns',
                    ),
                    html.Div(
                        dcc.Graph(id='pie-device'),
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
    div = html.Div([p0, p1])
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


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run_server(debug=debug, port=port, threaded=True)
