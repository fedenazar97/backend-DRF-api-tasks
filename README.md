# TO-DO API with Django rest framework

The api has token authentication, and CRUD operations for tasks. 

### Installation to run locally:
- In the terminal create and active your favorite virtual enviroment.
- Clone the repository.
- Then, install the project's dependencies:
    ~~~
    pip install -r requirements.txt
    ~~~
- After that, migrate the app's models:
    ~~~
    python manage.py migrate
    ~~~
- You can now run the server and enjoy:
    ~~~
    python manage.py runserver
    ~~~
- You can check the documentation of the API in the route localhost:8000/schema/swagger/
