
CONTENTS OF THIS FILE
---------------------

 * Shorty
 * Prerequisites
 * Configuration
 * Examples
 * Run the application
 * API Swagger Documentation
 * Running tests
 * Read the SDD
 * Maintainers

SHORTY
------

Shorty is a URL shortener API prepared for the interview with Plum.
The shortener API is accepting a url to shorten and the client can optionally decide on which URL shortener provider to use.

PREREQUISITES
-------------

For the convenience of the interviewers, i created accounts in both Bitly and Tinyurl providers
and generated the access tokens for accessing their shortener API's.

If for some reason you API response is 401 Unathorized, please make sure to have your tokens ready.


CONFIGURATION
-------------
There is an .env file which i have added in order to pass the access tokens as environment variables 
at the runtime of the container. The application is reading these tokens from the config file which i will explain
in more detail in the design document that i will forward to Vasilis.

You can add the providers access tokens to the .env file before running the container, or just use the tokens that i have
already provided for you.

EXAMPLES
--------

There is an examples package, which contains some modules with examples on how to use
some of the resources that i've created for this application. I think that the examples are 
very convenient for the engineers who would like to use the software and see some code examples.

RUNNING THE APP
---------------

The application is running within a docker container, which is spinning a Green Unicorn WSGI with 2 workers and binding the 8080 port.

Please build the image:

```bash
docker build -t shorty .
```
Rename the .env.sample to .env
```bash
cp .env.sample .env
```

Run the container:

```bash
docker run -itd -p 8080:8080 --env-file .env shorty
```


API SWAGGER DOCUMENTATION
-------------------------

I used Flask-restX, the flask extension for building better RESTFUL API's.
Flask-RESTplus (deprecated) and Flask-restX (his successor) are providing API documentation
out of the box (Swagger).

You can read the API documentation and use the API by navigating to the:
http://localhost:8080/v1


RUN THE TESTS
-------------

I used poetry for package and dependency management. 
Poetry also provides python virtualenv which makes running test easier for me.
Please Make sure that you have **poetry** installed in your machine,

Then you can run:
```bash
poetry install
source $(poetry env info --path)/bin/activate 
```

Then build and install the generated shorty package:
```bash
poetry build
pip install dist/shorty-0.1.0.tar.gz
```

Run the unit tests:
```bash
cd tests/unit/
pytest
```

Run the integration tests:
```bash
cd tests/integration/
pytest
```


READ THE SOFTWARE DESIGN DOCUMENT
---------------------------------

I will send a simple SSD that i have written along with the github repo link to this project, to Vasilis
and i will ask him to forward it to you. I would appreciate if you could have a look on it.

MAINTAINERS
-----------

Anastasios Kentominas <akentominas@gmail.com>


