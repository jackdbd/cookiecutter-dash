# Cookiecutter Dash
[![Build Status](https://travis-ci.org/jackdbd/cookiecutter-dash.svg?branch=master)](https://travis-ci.org/jackdbd/cookiecutter-dash)

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
