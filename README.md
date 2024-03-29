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


## Docker

You can build the two different environment containers with the appropriate command:
```bash
docker build --target production --tag todo-app:prod .
docker build --target development --tag todo-app:dev .
```
And run with:
```bash
docker run -d --env-file .env.docker -p 8000:8000 todo-app:prod
docker run -d --env-file .env -p 5000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:dev 
```

### Put Container Image on Docker Hub registry

Logging into DockerHub locally
```bash 
 docker login
 ```

Building the image, with
```bash 
 docker build --target <my_build_phase> --tag <image_tag> .
```

Tag an image referenced by Name and Tag, with
```bash 
 docker tag todo-app:prod leonmilcap/m8repo
```

Pushing the image, with
```bash 
 docker push leonmilcap/m8repo:latest
 ```

 ### Create a Web App

 First create an App Service Plan: 
 ```bash
 PS C:\temp\devops\projex\DevOps-Course-Starter2> az appservice plan create --resource-group Cohort28_LeoMil_ProjectExercise -n M8appservice_plan_name2 --sku B1 --is-linux
 ```
Then create the Web App: 
```bash 
az webapp create --resource-group Cohort28_LeoMil_ProjectExercise --plan M8appservice_plan_name2 --name M8webapp2 --deployment-container-image-name docker.io/leonmilcap/m8repo:latest
```
### Set up environment variables

Add environment variables through either Portal (Settings -> Configuration.  Add all the environment variables as “New application setting”) or through the CLI - individually:
```bash
az webapp config appsettings set -g Cohort28_LeoMil_ProjectExercise -n M8webapp2 --settings FLASK_APP=todo_app/app.
```
Or you can pass in a JSON file containing all variables by using --settings @foo.json


### Link to docker hub repo

https://hub.docker.com/repository/docker/leonmilcap/m8repo

### Link to Azure published web app

https://m8webapp2.azurewebsites.net/