"""Tests for this cookiecutter.

See Also: https://github.com/pydanny/cookiecutter-django
"""
import os
import re
import pytest
from binaryornot.check import is_binary

PATTERN = "{{(\s?cookiecutter)[.](.*?)}}"
RE_OBJ = re.compile(PATTERN)


@pytest.fixture
def context():
    return {
        "project_name": "My Test Project",
        "repo_name": "my-test-project",
        "package_name": "my_test_project",
        "author_name": "Test Author",
        "github_username": "jackdbd",
        "email": "you@example.com",
        "description": "A short description of the project.",
        "version": "0.1.0",
        "open_source_license": "MIT",
    }


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, subdirs, files in os.walk(root_dir)
        for file_path in files
    ]


def check_paths(paths):
    """Method to check all paths have correct substitutions,
    used by other tests cases
    """
    # Assert that no match is found in any of the files
    for path in paths:
        if is_binary(path):
            continue

        for line in open(path, "r"):
            match = RE_OBJ.search(line)
            msg = "cookiecutter variable not replaced in {}"
            assert match is None, msg.format(path)


def test_default_configuration(cookies, context):
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context["repo_name"]
    assert result.project.isdir()
    paths = build_files_list(str(result.project))
    assert paths
    check_paths(paths)


def test_heroku_procfile(cookies, context):
    result = cookies.bake(extra_context=context)
    procfile_path = os.path.join(result.project, 'Procfile')
    with open(procfile_path, mode='r') as f:
        heroku_config = f.readline()
        server_config = heroku_config.split()[2]
        assert server_config == 'my_test_project.app:server'
