# {{cookiecutter.display_name}}

[![License {{cookiecutter.license}}](https://img.shields.io/pypi/l/{{cookiecutter.library_name}}.svg?color=green)](https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.library_name}}/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/{{cookiecutter.library_name}}.svg?color=green)](https://pypi.org/project/{{cookiecutter.library_name}})
[![Python Version](https://img.shields.io/pypi/pyversions/{{cookiecutter.library_name}}.svg?color=green)](https://python.org)
[![tests](https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.library_name}}/workflows/tests/badge.svg)](https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.library_name}}/actions)
[![codecov](https://codecov.io/gh/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.library_name}}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.library_name}})

{{cookiecutter.short_description}}

----------------------------------

## Installation

You can install `{{cookiecutter.library_name}}` via [pip]:

    pip install {{cookiecutter.library_name}}


{% if cookiecutter.github_repository_url != 'provide later' %}
To install latest development version :

    pip install git+https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.library_name}}.git
{% endif %}

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [{{cookiecutter.license}}] license,
"{{cookiecutter.library_name}}" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

----------------------------------

This library was generated using [Cookiecutter] and a custom made template based on [@napari]'s [cookiecutter-napari-plugin] template.


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
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
[tox]: https://tox.readthedocs.io/en/latest/
{% if cookiecutter.github_repository_url != 'provide later' %}
[file an issue]: https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.library_name}}/issues
{% endif %}
