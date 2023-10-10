# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

On first use, you will need to populate data/config.py with the Trello configuration section items for TRELLO_BOARD_ID, TRELLO_APIKEY and TRELLO_TOKEN. Find succint instructions here https://project-exercises.devops.corndel.com/exercises/m2_exercise if a new token is required.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Testing the App

todo_app/tests contains a TDD test suite built along side the app.  To run the entire suite in a terminal or within your IDE: 

    PS C:\temp\devops\projex\DevOps-Course-Starter> pytest

You should see output similar to the following:

    ============================ test session starts ============================ 
    platform win32 -- Python 3.11.3, pytest-7.3.1, pluggy-1.0.0
    rootdir: C:\temp\devops\projex\DevOps-Course-Starter
    plugins: hypothesis-6.82.3
    collected 3 items

    todo_app\tests\test_view_model.py ...                                                                                                                                                                    [100%] 

    ============================ 3 passed in 0.05s ============================ 

To run a specific test of the suite in a terminal or within your IDE: 

    PS C:\temp\devops\projex\DevOps-Course-Starter> pytest -k test_view_model_todo_property 

You should see output similar to the following:

    ============================ test session starts ============================ 
    platform win32 -- Python 3.11.3, pytest-7.3.1, pluggy-1.0.0
    rootdir: C:\temp\devops\projex\DevOps-Course-Starter
    plugins: hypothesis-6.82.3
    collected 3 items / 2 deselected / 1 selected

    todo_app\tests\test_view_model.py .                                                                                                                                                                      [100%] 

    ============================ 1 passed, 2 deselected in 0.03s ============================ 

## Provision in cloud using Ansible 

Populate inventory list of IPs of managed nodes to provision:

    ec2-user@ControlNode:/home/ec2-user $ vim .ansible/inventory.ini

Command to provision a VM from an Ansible Control Node

    ec2-user@ControlNode:/home/ec2-user $ ansible-playbook .ansible/playbook2.yaml -i .ansible/inventory.ini
