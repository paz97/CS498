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

Install and run mongodb:
https://docs.mongodb.com/v3.2/administration/install-community/

# Running
Run the ```server.py``` script using:
```
$ export FLASK_APP=server.py
$ flask run
```

This will make the server accessible from only your computer.

To make an externally accessible server, run:
```
$ export FLASK_APP=server.py
$ flask run --host=0.0.0.0
```

# More detailed project planning:
https://docs.google.com/document/d/1tUmpBFls4SVh8OcdbXA0GqBk8xb7Fkw9oNzxno-9F2U/edit
