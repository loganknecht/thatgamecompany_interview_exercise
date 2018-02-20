# Environment Configuration
- Install Python
    - `brew install python`
- Install libev
    - `brew install libev`
    - Dependency of gevent for Locustio testing library
    - https://docs.locust.io/en/latest/installation.html
- Install Postman
    - https://www.getpostman.com/

# Repository Configuration
- Configure `virtualenv` for Python 3
- Activate virtualenv
- Install dependencies
    - You'll want everything, so use the dev dependencies
    - `pip install -r requirements-dev.txt`
- Open up postman
- Import Postman project
    - Import -> Import File -> Select `./postman/Clickhole.postman_collection_v1.json`
- Import Postman environment variables
    - Click the cog -> Click `Manage Environments` -> Click `Import` -> Select `./postman/clickhole.dev_environment_variables.json`

# Running the Server
- Start up the server
    - From the root of the repository
        - type `make cleanboot`
        - OR if there is a database already
        - type `make nukeboot`
- Open Postman
    - Expand the `Clickhole` project
    - Execute the `/ping` endpoint to confirm the server is working

# Running the tests
## Unit Tests
- Make sure the database is setup
- From the root directory enter the command `make do_migrate`
- Enter the command `pytest django_source_code/api/tests.py`

## Load Tests
- Start up the server
    - From the root of the repository
        - type `make cleanboot`
        - OR if there is a database already
        - type `make nukeboot`
- In your terminal go to the `django_source_code/test/api/` directory
- Enter the command `sh run_load_tests.sh`
- In your browser, go to `http://localhost:8089`
- Configure the load and press start
