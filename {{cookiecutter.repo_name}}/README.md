# {{cookiecutter.project_name}}
{% if cookiecutter.open_source_license == "MIT" %} [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT){% elif cookiecutter.open_source_license == "BSD" %} [![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause){% elif cookiecutter.open_source_license == "GPLv3" %} [![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0){% elif cookiecutter.open_source_license == "Apache Software License 2.0" %} [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0){% endif %} [![Build Status](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}.svg?branch=master)](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}) [![Updates](https://pyup.io/repos/github/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/shield.svg)](https://pyup.io/repos/github/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/) [![Python 3](https://pyup.io/repos/github/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/python-3-shield.svg)](https://pyup.io/repos/github/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/) [![Coverage](https://codecov.io/github/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/coverage.svg?branch=master)](https://codecov.io/github/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}?branch=master) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


{{cookiecutter.description}}


## Usage
If you are on Linux and you have [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) installed you can run the script `utility/setup_virtualenv_and_repo.sh` to:

- create a python virtual environment and activate it
- install all project dependencies from `requirements.txt`
- create a git repository
- create your `Initial commit`

Here is how you run the script:

```shell
cd {{cookiecutter.repo_name}}
# mind the dot!
. utility/setup_virtualenv_and_repo.sh
```

Then you will need to create an `.env` file where to store your environment variables (SECRET key, plotly credentials, API keys, etc). Do NOT TRACK this `.env` file. See `.env.example`.

Run all tests with a simple:

```
python -m pytest -v
```


## Run your Dash app
Check that the virtual environment is activated, then run:

```shell
cd {{cookiecutter.package_name}}
python app.py
```

## Code formatting
To format all python files, run:

```shell
black .
```

## Pin your dependencies

```shell
pip freeze > requirements.txt
```

## Deploy on Heroku
[dash-heroku-template](https://github.com/plotly/dash-heroku-template)