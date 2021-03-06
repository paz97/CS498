# CS498 Backend System
This will start a server that can accept POST/GET requests and send to a mongodb.


# Installation

This script is made using ```Python 3```.

Have the following dependencies:
```
flask
pymongo
requests
```

This time you have to install everything one by one.


We are using mongodb atlas testserver, so currently there is no reason you have to set up mongodb manually.

But if running db locally is required, you can install and run mongodb:
https://docs.mongodb.com/v3.2/administration/install-community/


# Sample Client

We now have provided the sameple python client for reference. See related directory for details.

# Running
Run the ```server.py``` script using:
```
$ export FLASK_APP=server.py
$ flask run
```

This will make the server accessible from only your computer.

To make it externally accessible, run flask with host params::
```
$ export FLASK_APP=server.py
$ flask run --host=0.0.0.0
```

# More detailed project planning:
https://docs.google.com/document/d/1tUmpBFls4SVh8OcdbXA0GqBk8xb7Fkw9oNzxno-9F2U/edit
