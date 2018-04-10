# Cookiecutter Dash
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) [![Build Status](https://travis-ci.org/jackdbd/cookiecutter-dash.svg?branch=master)](https://travis-ci.org/jackdbd/cookiecutter-dash) [![Updates](https://pyup.io/repos/github/jackdbd/cookiecutter-dash/shield.svg)](https://pyup.io/repos/github/jackdbd/cookiecutter-dash/) [![Python 3](https://pyup.io/repos/github/jackdbd/cookiecutter-dash/python-3-shield.svg)](https://pyup.io/repos/github/jackdbd/cookiecutter-dash/) [![Coverage](https://codecov.io/github/jackdbd/cookiecutter-dash/coverage.svg?branch=master)](https://codecov.io/github/jackdbd/cookiecutter-dash?branch=master) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter), Cookiecutter Dash creates a minimal project skeleton for a Dash app.


## Usage
Create a new Dash is as easy as 1-2-3.

1. If you don't already have it, install `cookiecutter` globally:

```shell
pip install cookiecutter
```

2. Run the following command to create the skeleton of your Dash app:

```shell
cookiecutter https://github.com/jackdbd/cookiecutter-dash
```

3. Follow the instructions in the `README.md` of your generated project.


## Features
Your generated Dash app will have:

- Environment variables loaded from `.env` file, with [dotenv](https://github.com/theskumar/python-dotenv)
- `Procfile` to deploy on Heroku
- Continuous Integration with `.travis.yml`
- Code Quality with `.codeclimate.yml`
- Test coverage with `codecov.yml`
- Python dependencies management with `.pyup.yml`
- Python code formatting with [black](https://github.com/ambv/black)
- A utility shell script to create a Python virtual environment and create your `Initial commit`


## TODO
- ceate tests for the generated project
- create simple dash callbacks
- support different CSS frameworks (e.g. [bulma](https://bulma.io/), [milligram](https://milligram.io/), [iota](https://github.com/korywakefield/iota))
- automatic nightly builds for TravisCI with [nightli.es](http://nightli.es/)
