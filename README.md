# README

[ ~ Dependencies scanned by PyUp.io ~ ]

## Overview

I had some difficulty in getting the default Azure Functions working beyond the most trivial case, as at April 2020.

You will find the tutorials on the Microsoft [website](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-azure-function-azure-cli?tabs=bash%2Cbrowser&pivots=programming-language-python).

```
Create a function PROJECT.
A function project is a container for one or more individual functions that each responds to a specific trigger. All functions in a project share the same local and hosting configurations.

func init LocalFunctionProj --python

cd LocalFunctionProj

func new --name HttpTrigger1 --template "HTTP trigger"
func new --name HttpTrigger2 --template "HTTP trigger"
```

This repo is my best attempt at creating an example with two Azure Functions, based on HTTP Triggers that depend on some *common shared code*, with some *automated pytests*. I am using Insiders build of Windows 10 and VSCode and WSL2. I am not paid to write code professionally, but I thought that it would be useful for me to better understand what "Serverless Functions" are about by getting some personal experience.

The layout is based on the Azure func templates and [feedback](https://github.com/microsoft/vscode-azurefunctions/issues/1970) by a [Brett Cannon](https://github.com/brettcannon) and [Anthony Chu](https://github.com/anthonychu).

I wanted to ensure that everything works via the terminal command line and/or via the VS-Code GUI.

You should be able use the repo as a template, copy and rename it, create a Python virtualenv in the root directory, update pip & install pip-tools, activate virtualenv .venv and then be ready to proceed on developing your own functions.

Initialise the pre-commit githook with ```pre-commit install```.  The pre-commit will use black to auto-format python files, remove trailing whitespace and check that you use case insensitive file names.

There is a github workflow that will run some quality checks,

- 100% test coverage,
- black formatting,
- packages checked for security safety
- mypy type checking

and then deploy to Azure.

To check your test coverage with ```python -m pytest --cov --cov-config=.coveragerc tests/```. Or ```coverage run -m pytest --cov __app__/```

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

## Tree view of the essential directories and files

```
(.venv) rnwolf@DESKTOP-2OQG1UG:/mnt/c/Users/rnwol/workspace/multi3$ tree -L 3 -a
.
├── .coverage
├── .coveragerc
├── .flake8
├── .git
├── .github
│   └── workflows
│       └── main.yml
├── .gitignore
├── .hypothesis
├── .pre-commit-config.yaml
├── .pylintrc
├── .python-version
├── .venv
│   ├── COPYING
│   ├── COPYING.GPL
│   ├── bin
│   │   ├── Activate.ps1
│   │   ├── activate
│   │   ├── activate.csh
│   │   ├── activate.fish
│   │   ├── autopep8-wrapper
│   │   ├── bandit
│   │   ├── bandit-baseline
│   │   ├── bandit-config-generator
│   │   ├── black
│   │   ├── blackd
│   │   ├── chardetect
│   │   ├── check-added-large-files
│   │   ├── check-ast
│   │   ├── check-builtin-literals
│   │   ├── check-byte-order-marker
│   │   ├── check-case-conflict
│   │   ├── check-docstring-first
│   │   ├── check-executables-have-shebangs
│   │   ├── check-json
│   │   ├── check-merge-conflict
│   │   ├── check-symlinks
│   │   ├── check-toml
│   │   ├── check-vcs-permalinks
│   │   ├── check-xml
│   │   ├── check-yaml
│   │   ├── coverage
│   │   ├── coverage-3.8
│   │   ├── coverage3
│   │   ├── debug-statement-hook
│   │   ├── detect-aws-credentials
│   │   ├── detect-private-key
│   │   ├── dmypy
│   │   ├── double-quote-string-fixer
│   │   ├── easy_install
│   │   ├── easy_install-3.8
│   │   ├── end-of-file-fixer
│   │   ├── epylint
│   │   ├── file-contents-sorter
│   │   ├── fix-encoding-pragma
│   │   ├── flake8
│   │   ├── forbid-new-submodules
│   │   ├── http
│   │   ├── https
│   │   ├── identify-cli
│   │   ├── isort
│   │   ├── mixed-line-ending
│   │   ├── mypy
│   │   ├── mypyc
│   │   ├── name-tests-test
│   │   ├── no-commit-to-branch
│   │   ├── nodeenv
│   │   ├── pbr
│   │   ├── pip
│   │   ├── pip-compile
│   │   ├── pip-sync
│   │   ├── pip3
│   │   ├── pip3.8
│   │   ├── pipenv
│   │   ├── pipenv-resolver
│   │   ├── pre-commit
│   │   ├── pre-commit-validate-config
│   │   ├── pre-commit-validate-manifest
│   │   ├── pretty-format-json
│   │   ├── py.test
│   │   ├── pycodestyle
│   │   ├── pydocstyle
│   │   ├── pyflakes
│   │   ├── pygmentize
│   │   ├── pylint
│   │   ├── pyreverse
│   │   ├── pytest
│   │   ├── python -> /home/rnwolf/.pyenv/versions/3.8.2/bin/python
│   │   ├── python3 -> python
│   │   ├── requirements-txt-fixer
│   │   ├── safety
│   │   ├── sort-simple-yaml
│   │   ├── stubgen
│   │   ├── stubtest
│   │   ├── symilar
│   │   ├── trailing-whitespace-fixer
│   │   ├── virtualenv
│   │   └── virtualenv-clone
│   ├── include
│   ├── lib
│   │   └── python3.8
│   ├── lib64 -> lib
│   └── pyvenv.cfg
├── .vscode
│   ├── .ropeproject
│   │   └── config.py
│   ├── extensions.json
│   ├── launch.json
│   ├── settings.json
│   └── tasks.json
├── .vstest
│   ├── extensions.json
│   ├── launch.json
│   ├── settings.json
│   └── tasks.json
├── Create .venv pythonvirtual env here.txt
├── LICENSE.md
├── README.md
├── __app__
│   ├── .funcignore
│   ├── .python_packages
│   ├── __init__.py
│   ├── conftest.py
│   ├── host.json
│   ├── http_trigger_1
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   └── function.json
│   ├── http_trigger_2
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   └── function.json
│   ├── local.settings.SAMPLE.json
│   ├── requirements.txt
│   └── sharedcode
│       ├── __init__.py
│       ├── __pycache__
│       └── my_helper_functions.py
├── dev-requirements.in
├── dev-requirements.txt
├── mypy.ini
├── pytest.ini
└── tests
    ├── .pylintrc
    ├── __init__.py
    ├── testHttpTrigger1.http
    ├── testHttpTrigger2.http
    ├── test_http_trigger_1.py
    └── test_http_trigger_2.py

```

## How to use the repo as a template for your own/next functions.

The following steps are a bit of a mix of MS-Windows(Powershell) and WSL2(Ubuntu 18.04 bash) commands. I tested the process out under both environments to make sure it was working for me.

### Make sure the Azure CLI is installed.

To install in Windows : Open powershell terminal.

```Invoke-WebRequest -Uri https://aka.ms/installazurecliwindows -OutFile .\AzureCLI.msi; Start-Process msiexec.exe -Wait -ArgumentList '/I AzureCLI.msi /quiet'; rm .\AzureCLI.msi```

#### Install the azure func tools

In WLS linux use APT to install Core Tools on your Ubuntu/Debian Linux distribution.
https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=linux%2Ccsharp%2Cbash#v2

```
sudo apt update
sudo apt-get install azure-cli
or sudo apt-get upgrade azure-cli
```

### Copy the template layout to a new repo in your private github account.

Login to your github account in the browser.
Open https://github.com/rnwolf/azure-func-python-layout
Press the green "Use this template" button.

Make a private repo. Lets say "multi3".

Click on the green "Clone or Download" button in github to get url of repo.
Open terminal window and clone the repo.

```git clone git@github.com:rnwolf/multi3.git```

Change working directory.

```cd multi3```

### Create a Virtualenv in .venv directory

Check the default version of python you have installed.

```python --version```

Install a version of python that you want/need. I use pyenv, to manage versions of Python installed in 18.04 WSL2 environment.

```pyenv install 3.8.2```

Specify version to be us in the directory with
``` pyenv local 3.8.2```

```python --version```

In Windows: Create a python vitual environment with, after having installed the required version of python, for all users, from https://Python.org.

```py -3.8 -m venv .venv```

### Activate the virtualenv

```
Windows:  .\.venv\Scripts\activate
Linux:  source .venv/bin/activate
```

Check that the version of python we are using in in the virtualenv.

```which python```

### Update to the latest version of pip

```python -m pip install --upgrade pip```

### Install pip-tools

```python -m pip install pip-tools```

### Create requirements file for the development packages that we want to use.

```
win: pip-compile -r .\dev-requirements.in
linux: pip-compile -r dev-requirements.in
```

### Install all the development packages.

```pip install -r dev-requirements.txt```

### Open up VS-Code and make sure extensions are installed.

```code .```

VSCode will suggest that some extensions are to be installed.
"Python" and "Azure Functions" ,by Microsoft, extensions.
Also consider installing sonarlint, Trailing Spaces, Git Lens, Code Spell Checker, Azure Account, REST Client

### Select the python interpreter for VScode.

```Ctrl+Shit+P  python interpreter```

Select the Virtualenv you created earlier.
```
Linux: ./venv/bin/python
Win: ./venv/Scripts/python
```

At the Terminal you can activate with

```
Win: .\.venv\scripts\activate
Linux: ./venv/bin/python
```

## Update the App Name in the Github workflow file.

open /.github/workflows/main.yml

Check python version.
Check/update app name.

## DEVELOP CODE and TESTS - Run tests to make sure we are in business

You should be able to do this via the terminal or via the VSCode GUI.

```
flake8
black .
safety check
python -m pytest --cov --cov-config=.coveragerc tests/
```

Run the function(s) locally from the root folder of the project.

```func start --python```

You can use tools such as https://insomnia.rest/, Postman, httpie or VSCode "REST Client"

For example with [httpie](https://github.com/jkbr/httpie/) you can run commands, similar to the following, at your terminal:

```
http POST http://localhost:7071/api/HttpRNWOLF name='John Smith'

http --form POST http://localhost:7071/post name='John Smith'
```

Setup a pre-commit hook to run some checks prior to commit.

```pre-commit install```.

## Setup your Azure Account with location to store and run the functions

```az login```

Create a resource group with the az group create command. For example:

```
az group create --name AzureFunctionsQuickstart-rg --location westeurope
```

Create a general-purpose storage account in your resource group and region by using the az storage account create command.
Use a globally unique name appropriate to you. Names must contain three to 24 characters numbers and lowercase letters only.

```
az storage account create --name rnwolfquickstart --location westeurope --resource-group AzureFunctionsQuickstart-rg --sku Standard_LRS
```

### Create the function app using the az functionapp create command.

Creates a function app running in your specified language runtime under the Azure Functions Consumption Plan.

The command also provisions an associated Azure Application Insights instance in the same resource group, with which you can monitor your function app and view logs.

<APP_NAME> with a globally unique name appropriate to you.

```
az functionapp create --resource-group AzureFunctionsQuickstart-rg --os-type Linux --consumption-plan-location westeurope --runtime python --runtime-version 3.8 --functions-version 3 --name <APP_NAME> --storage-account <STORAGE_NAME>

az functionapp create --resource-group AzureFunctionsQuickstart-rg --os-type Linux --consumption-plan-location westeurope --runtime python --runtime-version 3.8 --functions-version 3 --name rnwolfmulti3 --storage-account rnwolfquickstart

```

## Publish app to Azure

Open terminal and publish the functions to the app project.

```cd .\__app__
func azure functionapp publish rnwolfmulti3 --python
```

See the "Deployment successful." message with Invoke url's.


## Create github repo secret so that workflow can automatically publish

Open up the portal
https://portal.azure.com

Open up the "Function App" resources

Open up the function app "rnwolfmulti3" or what ever you called it.

Click on the "Get publish profile" link. Download the profile.

Open up the secrets setting for the repo on github
https://github.com/rnwolf/multi3/settings/secrets

Create a secret called
```
azureWebAppPublishProfile
```

and paste the contents of downloaded profile into the secret.

You can now push changes to your repo, tests will run and then function package will be deployed to your Azure account.

# TODO

Previously I found that I needed to remove pylint from app when using more than one azure resource.  When saving messages to the queue.
Check if this new layout still works with pylint in VSCode.