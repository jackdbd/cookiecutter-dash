# {{cookiecutter.project_name}}
[![Build Status](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}.svg?branch=master)](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}){% if cookiecutter.open_source_license == "MIT" %} [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT){% elif cookiecutter.open_source_license == "BSD" %} [![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause){% elif cookiecutter.open_source_license == "GPLv3" %} [![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0){% elif cookiecutter.open_source_license == "Apache Software License 2.0" %} [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0){% endif %}


{{cookiecutter.description}}


## Usage

If you are on Linux and you have [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) installed you can run this shell script contained in `utility/`. This script will setup a virtual environment, install all project dependencies, create a git repository and create your first commit.

```shell
cd {{cookiecutter.repo_name}}
# mind the dot!
. utility/setup_virtualenv_and_repo.sh
```

Then you will need to create an `.env` file with your environment variable. See `.env.example`.
