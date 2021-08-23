# Python - Darwin API Automation

## Prerequisites:

```
Python3
Pytest
```

## Tests Execution:

To execute the tests on your machine or any CI/CD


1- Extract zip file:

2- Open terminal and `cd` to `pytest-api-automation`

3- Execute command in terminal:

For Linux, MAC OS:
```
.\run.sh
```

For Windows OS:
```
.\run.bat
```

*Optional command-line arguments:*

*--env*

`--env` takes `qa` and `dev` arguments and set the base URL to QA or Dev environments, default is `qa`.

*_e.g_*

```pytest -v --env=qa```

```pytest -v --env=dev```
