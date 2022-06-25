# Chuck Norris API

# Installation process

To get started with this project, first you'll need to have [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/) installed. After that, you just need to enter the following command:
```
docker-compose -f docker-compose/development.yaml up --build
```
Now you'll have a PostgreSQL database running on your machine. Next, you'll need to create a virtual environment to install the system dependencies. (You can choose the venv's interpreter on vscode and have auto complete features :) )

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements/dev.txt
```

The python version this project employ is the ```3.8```, so to avoid compatibility issues with libraries or even language features, we strongly recommend you to stick with this version.


# API reference
Once you deployed the system locally, you can have access to the API Documentation, you can go to ```http://<host>/api/schema/redoc/``` or ```http://<host>/api/schema/swagger-ui/```.


# Test
For testing the application before deploying stage, you just need to run the next command:
```
python manage.py test
```
As soon as you enter this command the Django testing framework will look up for all files starting with the 'test' prefix and try to run these files.


# Generating fixtures

To generate a fixture, use the following command:
```
python manage.py dumpdata --all --indent 4 --output <file_name>.json <model or app>
```