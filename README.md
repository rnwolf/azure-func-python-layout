# README

[ ~ Dependencies scanned by PyUp.io ~ ]

## Overview

I had some difficulty in getting the default Azure Functions working beyond the most trival case, as at April 2020.

This repo is my best attempt at creating an example of two Azure Functions, based on HTTP Triggers that depend on some common shared code, with some automated pytests. I am using Insiders build of Windows 10 and VSCode.

The layout is based on the Azure func templates and [feedback](https://github.com/microsoft/vscode-azurefunctions/issues/1970) by a [Brett Cannon](https://github.com/brettcannon) and [Anthony Chu](https://github.com/anthonychu).

I wanted to ensure that everything works via the terminal command line and/or via the VS-Code GUI.

You should be able copy the repo, rename it, create a Python virtualenv in the root directory, update pip & install pip-tools, activate venv and then be ready to proceed on your own.

Initialise the pre-commit githook with ```pre-commit install```.  The pre-commit will use black to auto-format python files, remove trailing whitespace and check that you use case insensitive file names.

There is a github workflow that will run some quality checks,

- 100% test coverage,
- black formatting,
- packages checked for security safety
- mypy type checking

and then deploy to Azure.

To check your test coverage with ```python -m pytest --cov --cov-config=.coveragerc __app__```. Or ```coverage run -m pytest --cov __app__/```

For the github workflow to work you will need you to create/download a "publish profile" which must be added as Github repo secret in order for the workflow to deploy to Azure.

## Helper utilities

I've included a number of utilities such as:

- Safety : [Safety checks your dependencies for known security vulnerabilities.](https://pyup.io/safety/)
- Black : [The uncompromising code formatter](https://black.readthedocs.io/en/stable/)
- Bandit : [Bandit is a tool designed to find common security issues in Python code.](https://pypi.org/project/bandit/)
- pylint : [Pylint is a tool that checks for errors in Python code, tries to enforce a coding standard and looks for code smells.](https://www.pylint.org/)
- flake8 : [Flake8 is a wrapper around source code checkers](https://pypi.org/project/flake8/)
- pytest : [pytest framework makes it easy to write tests](https://docs.pytest.org/en/latest/)
- pip-tools : [pip-tools keeps your pinned dependencies fresh.](https://github.com/jazzband/pip-tools)
- mypy : [Mypy is a static type checker for Python. Type checks your code and find common bugs.](https://mypy-lang.org/)
- rope : [A python refactoring library](https://github.com/python-rope/rope)
- hypothesis : [Python library for property-based testing](https://hypothesis.readthedocs.io/en/latest/)
- importlib_resources : [A backport of Python 3.9’s standard library importlib.resources](https://importlib-resources.readthedocs.io/en/latest/)


Update the dev-requirements.in and requirements.txt file with the python packages that you need/want in dev and production.
Activate virtualenv and then generate ```pip-compile -r dev-requirements.in```
Install packages with ```pip install -r dev-requirements.txt```

## Tree view of the essental directories and files

```
C:\Users\rnwol\workspace\application
├── .coverage
├── .coveragerc
├── .flake8
├── .git
├── .github
|  └── workflows
|     └── main.yml
├── .gitignore
├── .hypothesis
├── .pylintrc
├── .venv
|  ├── COPYING
|  ├── COPYING.GPL
|  ├── Include
|  ├── Lib
|  |  └── site-packages
|  ├── pyvenv.cfg
|  └── Scripts
|     ├── activate
|     ├── activate.bat
|     ├── Activate.ps1
|     ├── bandit-baseline.exe
|     ├── bandit-config-generator.exe
|     ├── bandit.exe
|     ├── black.exe
|     ├── blackd.exe
|     ├── chardetect.exe
|     ├── coverage-3.8.exe
|     ├── coverage.exe
|     ├── coverage3.exe
|     ├── deactivate.bat
|     ├── dmypy.exe
|     ├── easy_install-3.8.exe
|     ├── easy_install.exe
|     ├── epylint.exe
|     ├── flake8.exe
|     ├── isort.exe
|     ├── mypy.exe
|     ├── mypyc
|     ├── pbr.exe
|     ├── pip-compile.exe
|     ├── pip-sync.exe
|     ├── pip.exe
|     ├── pip3.8.exe
|     ├── pip3.exe
|     ├── pipenv-resolver.exe
|     ├── pipenv.exe
|     ├── py.test.exe
|     ├── pycodestyle.exe
|     ├── pydocstyle.exe
|     ├── pyflakes.exe
|     ├── pylint.exe
|     ├── pyreverse.exe
|     ├── pytest.exe
|     ├── python.exe
|     ├── pythonw.exe
|     ├── safety.exe
|     ├── stubgen.exe
|     ├── stubtest.exe
|     ├── symilar.exe
|     ├── virtualenv-clone.exe
|     └── virtualenv.exe
├── .vscode
|  ├── .ropeproject
|  |  └── config.py
|  ├── extensions.json
|  ├── launch.json
|  ├── settings.json
|  └── tasks.json
├── .vstest
|  ├── extensions.json
|  ├── launch.json
|  ├── settings.json
|  └── tasks.json
├── Create .venv pythonvirtual env here.txt
├── dev-requirements.in
├── dev-requirements.txt
├── LICENSE.md
├── mypy.ini
├── pytest.ini
├── README.md
├── tests
|  ├── .pylintrc
|  ├── testHttpTrigger1.http
|  ├── testHttpTrigger2.http
|  ├── test_http_trigger_1.py
|  ├── test_http_trigger_2.py
|  └── __init__.py
└── __app__
   ├── .funcignore
   ├── .python_packages
   ├── conftest.py
   ├── host.json
   ├── http_trigger_1
   |  ├── function.json
   |  └── __init__.py
   ├── http_trigger_2
   |  ├── function.json
   |  └── __init__.py
   ├── local.settings.json
   ├── local.settings.SAMPLE.json
   ├── not-needed.vscode
   |  ├── extensions.json
   |  ├── launch.json
   |  ├── settings.json
   |  └── tasks.json
   ├── requirements.txt
   ├── sharedcode
   |  ├── my_helper_functions.py
   |  └── __init__.py
   └── __init__.py
```

## How to use the repo as a template for your own/next functions.

Open powershell terminal.
Make sure the Azure CLI is installed.

```Invoke-WebRequest -Uri https://aka.ms/installazurecliwindows -OutFile .\AzureCLI.msi; Start-Process msiexec.exe -Wait -ArgumentList '/I AzureCLI.msi /quiet'; rm .\AzureCLI.msi```


# TODO

Previously I found that I needed to remove pylint from app when using more than one azure resource. Need to check if this new layout makes an difference.