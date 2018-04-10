# Cookiecutter Dash
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) [![Build Status](https://travis-ci.org/jackdbd/cookiecutter-dash.svg?branch=master)](https://travis-ci.org/jackdbd/cookiecutter-dash) [![Updates](https://pyup.io/repos/github/jackdbd/cookiecutter-dash/shield.svg)](https://pyup.io/repos/github/jackdbd/cookiecutter-dash/) [![Python 3](https://pyup.io/repos/github/jackdbd/cookiecutter-dash/python-3-shield.svg)](https://pyup.io/repos/github/jackdbd/cookiecutter-dash/) [![Coverage](https://codecov.io/github/jackdbd/cookiecutter-dash/coverage.svg?branch=master)](https://codecov.io/github/jackdbd/cookiecutter-dash?branch=master) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter), Cookiecutter Dash creates a minimal project skeleton for a Dash app.


## Usage
If you don't already have it, install `cookiecutter` globally:

```shell
pip install cookiecutter
```

Then, run the following command to create the skeleton of your Dash app:

```shell
cookiecutter https://github.com/jackdbd/cookiecutter-dash
```

Finally, read the `README.md` of your generated project.


## Features
- Environment variables loaded from `.env` file, with [dotenv](https://github.com/theskumar/python-dotenv)
- `Procfile` to deploy on Heroku
- Continuous Integration with `.travis.yml`
- Code Quality with `.codeclimate.yml`


## TODO
- ceate tests for the generated project
- create simple dash callbacks
- support different CSS frameworks (e.g. [bulma](https://bulma.io/), [milligram](https://milligram.io/), [iota](https://github.com/korywakefield/iota))
- automatic nightly builds for TravisCI with [nightli.es](http://nightli.es/)
