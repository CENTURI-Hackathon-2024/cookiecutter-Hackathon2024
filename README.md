# A [Cookiecutter] template for members of the [Guignard Lab] and maybe others (?)

----------------------------------

This [Cookiecutter] template allows to "rapidly" create the folder structure for a "decent" python project.
It includes config files, tests structure and version control.

## Folder structure:

When creating a project, the folder structure is the following (assuming that you are creating a module named FooBar):
```
FooBar # Folder with the project
├── LICENSE                         # License file
├── MANIFEST.in                     # Manifest file (for including and excluding when building)
├── README.md                       # ReadMe file
├── bumpver.toml                    # Bumpver config file (for automativ version management, optional)
├── notebooks                       # Folder for notebooks (optional)
│    └── FooBar_notebook.ipynb          # A notebook (optional)
├── pyproject.toml                  # config file for building the project
├── setup.cfg                       # config file for dependencies etc.
├── src                             # source folder
│    └── foobar                         # module folder
│        ├── __init__.py                    # init python file
│        ├── _foobar.py                     # file which will contain your module
│        └── _tests                         # test folder for the module
│            ├── __init__.py                    # init file for the tests
│            └── test_module.py                 # test file
├── tox.ini                         # test config file
├── .github                         # github config file
│    └── workflows                      # workflow folder
│        └── test_and_deploy.yml            # workflow config file
└── .gitignore                      # ignored filed by git
```

This format can of course be modified if necessary but it is a decent basis to start with.

## Installation

1. It is necessary to first install [Cookiecutter]:

```
pip install cookiecutter
```
or
```
conda install cookiecutter
```

2. Then, one can run:
```
cookiecutter gh:guignardlab/cookiecutter-guignardlab
```
or
```
cookiecutter https://github.com/guignardlab/cookiecutter-guignardlab
```

## Usage

When starting a new project/module, one can setup the folder tree using [Cookiecutter].

It can be done the following way:
```
cookiecutter gh:guignardlab/cookiecutter-guignardlab
```

or by:
1. cloning this repository:
```
git clone https://github.com/guignardlab/cookiecutter-guignardlab
```

2. calling cookiecutter with the cloned repository:
```
cookiecutter cookiecutter-guignardlab
```

3. Once ran, the command will prompt the user with few questions (the bracket is the automatic answer when nothing is given):
    - `full_name [Your Name]:` -> Inform your name
    - `email [your.name@univ-amu.fr]:` -> Inform your email
    - `github_username_or_organization [GuignardLab]:` -> inform to which account the repository should be saved in (it could be your personal account too for example)
    - `library_name [test_Foo-Bar]:` -> Inform the name of your library
    - `module_name [test_foo_bar]:` -> name of the module itself (should be lower-case **no** `-`, `_` instead)
    - `class_name [testFooBar]:` -> name of the module itself (**no** `-` or `_`)
    - `display_name [test_Foo-Bar]:` -> Name to display in the README etc
    - 
            Select github_repository_url:
            1 - https://github.com/GuignardLab/test_Foo-Bar
            2 - provide later
            Choose from 1, 2 [1]:
      -> choose the address to the github repository
    - `test_notebook [y]:` -> `y` to create a folder for the test notebooks and a notebook in it
    - `version_numbering [y]:` -> `y` if you plan on using bumpver to maintain your versions
    - `dependency_prefil [y]:` -> `y` if you want to have `y` as a prefil for the dependencies, otherwise `n`
    - 
            numpy [y]:
            scipy [y]:
            scikit_image [y]:
            scikit_learn [y]:
            napari [y]:
      -> whether you want to add the following dependencies (`y`: yes, `n`: no)
    - `short_description [A repository to analyse data]:` -> Short description of your module
    - 
            Select license:
            1 - MIT
            2 - BSD-3
            3 - Mozilla Public License 2.0
            4 - Apache Software License 2.0
            5 - GNU LGPL v3.0
            6 - GNU GPL v3.0
            Choose from 1, 2, 3, 4, 5, 6 [1]:
      -> Type of license to use
    - `M1_processor [n]:` -> whether or not to include numpy in the build (because of the Apple Silicon M1 processor problem)


[Guignard Lab]: https://www.guignardlab.com
[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[file an issue]: https://github.com/leoguignard/napari-boids/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
