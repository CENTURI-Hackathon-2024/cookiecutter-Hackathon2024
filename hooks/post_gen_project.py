#!/usr/bin/env python

import logging
import os
import shutil
import subprocess
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("post_gen_project")

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
ALL_TEMP_FOLDERS = ["licenses"]



def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_temp_folders(temp_folders):
    for folder in temp_folders:
        logger.debug("Remove temporary folder: %s", folder)
        shutil.rmtree(folder, ignore_errors=True)

def remove_notebook():
    a = 1
    {% if cookiecutter.test_notebook == 'No' %}
    shutil.rmtree("notebooks")
    {% endif %}


if __name__ == "__main__":
    remove_temp_folders(ALL_TEMP_FOLDERS)
    remove_notebook()
    msg = ''
    # try to run git init
    try:
        subprocess.run(["git", "init", "-q"])
        subprocess.run(["git", "checkout", "-b", "main"])
    except Exception:
        pass
    try:
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-q", "-m", "initial commit"])
    except Exception:
        msg += """
Your library template is ready!  Next steps:

1. `cd` into your new directory and initialize a git repo
   (this is also important for version control!)

     cd {{ cookiecutter.library_name }}
     git init -b main
     git add .
     git commit -m 'initial commit'

     # you probably want to install your new package into your environment
     pip install -e ."""
    else:
        msg +="""
Your plugin template is ready!  Next steps:

1. `cd` into your new directory

     cd {{ cookiecutter.library_name }}
     # you probably want to install your new package into your env
     pip install -e ."""

{% if cookiecutter.github_repository_url != 'provide later' %}
    msg += """
2. Create a github repository with the name '{{ cookiecutter.library_name }}':
   https://github.com/{{ cookiecutter.github_username_or_organization }}/{{ cookiecutter.library_name }}.git

3. Add your newly created github repo as a remote and push:

     git remote add origin https://github.com/{{ cookiecutter.github_username_or_organization }}/{{ cookiecutter.library_name }}.git
     git push -u origin main

4. The following default URLs have been added to `setup.cfg`:

    Bug Tracker = https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.library_name}}/issues
    Documentation = https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.library_name}}#README.md
    Source Code = https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.library_name}}
    User Support = https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.library_name}}/issues

    You may wish to change these before publishing your library!"""

{% else %}
    msg += """
2. Create a github repository for your library:
   https://github.com/new

3. Add your newly created github repo as a remote and push:

     git remote add origin https://github.com/your-repo-username/your-repo-name.git
     git push -u origin main

   Don't forget to add this url to setup.cfg!

     [metadata]
     url = https://github.com/your-repo-username/your-repo-name.git

4. Consider adding additional links for documentation and user support to setup.cfg
   using the project_urls key e.g.

    [metadata]
    project_urls =
        Bug Tracker = https://github.com/your-repo-username/your-repo-name/issues
        Documentation = https://github.com/your-repo-username/your-repo-name#README.md
        Source Code = https://github.com/your-repo-username/your-repo-name
        User Support = https://github.com/your-repo-username/your-repo-name/issues"""
{% endif %}

    print(msg)
