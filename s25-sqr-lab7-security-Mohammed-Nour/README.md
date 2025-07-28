# Lab Security  

## Storyline

- An electronics shop without an online presence rushed to create a website to reach a broader customer base. As a result, they spent all their budget on development without investing in security. Thus, their software has some vulnerabilities and your mission is to spot and fix them. Good luck!

## What is in the repo?

- `app` directory contains the `code.py` file  which includes the vulnerable code to be reviewed.
- `test` directory contains the `hack.py` file which has five tests designed exploit vulnerabilities found within `code.py`. These five tests are failling in the current state of the `code.py`.
- `.github/workflows` folder contains `main.yaml` file and `classroom.yaml` which automates testing every time code is committed to the repository.

## Lab Assignment

1. Install Bandit checking tool.  
2. Utilize Bandit to identify and fix vulnerabilities of `code.py`.
3. Analyze and review the `code.py` to ensure that all the tests in the `hack.py` are passing. All default security checks **must pass.**
4. In `main.yaml` file add your workflow to run a Bandit check, and make it run on push, and outline the steps to set up the environment.

> **Note**: Check the python and poetry versions if they are in sync with your `pyproject.toml` file.

> **Note**: Do not edit autograding, classroom files or `hack.py`.

> **Note:** if you add new tests, all tests should pass for final submission.

## Lab points distrubution (4 points)
- 0.5 point for each test in total 2.5 points for all tests.
- 1.5 points for Bandit checking. 



## Hints

- Check the [code quality tutorial](https://testdriven.io/blog/python-code-quality/#security-vulnerability-scanners).