# Hangman Game

It is a Python console app word guessing game.  
The player guesses one letter at a time. 
If the guessed letter is in the word, the game reveals where that letter appears in the word. For instance, if the player guesses "p" and the word is "python", the display would change to "p _ _ _ _ _".  
If the guessed letter is not in the word, a part of the 'hangman' is drawn.

Python console app hangman game based on the [code](https://github.com/markpatterson27/hangman-game) by [Mark Patterson](https://github.com/markpatterson27)

# Assignment

> :warning: **Note**: **Lab is counted as done, if you have your app is running on server, and pipelines are passing.**

### Installing poetry:  
   #### Why Poetry ?  
Poetry is a tool for dependency management and packaging in Python. It allows to declare the libraries project depends on and it will manage (install/update) them. Poetry offers a lockfile to ensure repeatable installs, and can build your project for distribution.  
One of the core features of Poetry is that making project environment isolation. By default, Poetry will try to use the Python version used during Poetry’s installation to create the virtual environment for the current project.
  > :warning: **Note**: Poetry requires Python 3.8+.

#### To install Poetry:  
(Linux, macOS, Windows (WSL))
     <pre>curl -sSL https://install.python-poetry.org | python3 -
 </pre>  
 Windows (Powershell)  
 <pre>(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py - 
 </pre>
Once Poetry is installed you can execute the following:
      <pre> poetry --version
</pre>
   
### Initialize poetry:  
To initialize poetry in your project:
<pre>cd path/to/your/project </pre>
<pre> poetry init</pre>  
It will ask you to insert some information, or you can use:  
<pre>poetry init -n</pre>  
for default intiliazation.  
Once intilization poetry a ``pyproject.toml`` will be added to the project folder. The toml file is a configuration file contains build system requirements and information, which are used by pip to build the package.  
### Poetry commands: 
1. <pre>poetry install</pre>  
The install command reads the ``pyproject.toml`` file from the current project, resolves the dependencies, and installs them.
When you run this command, one of two things may happen:

* Installing without poetry.lock:  
If you have never run the command before and there is also no poetry.lock file present, Poetry simply resolves all dependencies listed in your ``pyproject.toml`` file and downloads the latest version of their files.  
When Poetry has finished installing, it writes all the packages and their exact versions that it downloaded to the ``poetry.lock`` file, locking the project to those specific versions. You should commit the ``poetry.lock`` file to your project repo so all people working on the project are locked to the same versions of dependencies.  

* Installing with poetry.lock:  
If there is already a ``poetry.lock`` file and a ``pyproject.toml`` file when you run poetry install, it means either you ran the install command before, and committed the ``poetry.lock`` file to the project. This will use the exact versions from there instead of resolving them. This ensures that everyone using the library will get the same versions of the dependencies.

2. <pre>poetry update</pre>  
In order to get the latest versions of the dependencies and to update the ``poetry.lock`` file, you should use the update command.This will resolve all dependencies of the project and write the exact versions into ``poetry.lock``.  

3. <pre>poetry run python -V</pre>  
The run command executes the given command inside the project’s virtualenv. It can also execute one of the scripts defined in ``pyproject.toml``.  


### Organizing project folder:    

Create new folder with the same of your project name and another folder with name 'tests'.
 Inside each folder, create an \_\_init\_\_.py file  

In Ubuntu:

<pre>cd /path/to/your/project</pre>
<pre>mkdir app tests</pre>
<pre>touch app/__init__.py tests/__init__.py</pre>


<pre>
app/
├── pyproject.toml
├── app
│   └── __init__.py
└── tests
    └── __init__.py
</pre>

### Install pytest
<pre>poetry add pytest</pre>  

### Add a simple test for the hangman   
In the tests folder, add `test_hangman.py` to check with pytest. This test case should pass as it will be verified with CI later.

The project tree after adding the test file should look like:
<pre>
app/
├── pyproject.toml
|── poetry.lock
├── app
│   └── __init__.py
    └── hangman.py
└── tests
    └── __init__.py
    └── test_hangman.py
</pre>


### Add simple workflow 
In `.github/workflows` folder add `main.yaml` file, which automates testing every time code is commited to the repository.   
The workflow should contain the basic components.   
Specify when the workflow should run (on push or pull request), outline the steps to set up the environment, and a command to run `pytest`.  
This GitHub Actions workflow ensures automated testing for code quality and reliability.
```YAML
name: code quality test

on: push

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.12'
      - name: Run image
        uses: abatilo/actions-poetry@v2
        with:
          poetry-version: '1.7.1'
      - name: Install dependencies
        run: poetry install; poetry add pytest
      - name: Run pytest
        run: poetry run pytest .
```

  > :warning: **Note**: check the python version and poetry version so that they are in sync with your `pyproject.toml` file

# Slides

  > :warning: **Note**: [ Link to the presentation](https://docs.google.com/presentation/d/1R_D5KL-crTSb_vvWP39-Quqz0h2KMuGHxAtizo7ThqE/edit?usp=sharing)  


 
# Hint

Look in the [tutorial](https://testdriven.io/blog/python-environments/)
