#!/bin/bash

# Add users
curl -i -H "Content-Type: application/json" -X POST -d '{"login": "log", "username": "uname", "password": "pwd"}' http://localhost:5000/add_user
curl -i -H "Content-Type: application/json" -X POST -d '{"login": "log2", "username": "uname2", "password": "pwd2"}' http://localhost:5000/add_user
curl -i -H "Content-Type: application/json" -X POST -d '{"login": "log3", "username": "uname3", "password": "pwd3"}' http://localhost:5000/add_user
