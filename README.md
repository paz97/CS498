# CS498
This will start a server that can accept POST/GET requests and send to a mongodb.


# Installation

This script is made using ```Python 3```.

Have the following dependencies:
```
flask
pymongo
```

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

