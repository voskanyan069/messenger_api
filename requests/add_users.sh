#!/bin/bash

# Add users
curl -i -H "Content-Type: application/json" -X POST -d '{"login": "log", "username": "uname", "password": "password"}' http://localhost:5000/add_user
curl -i -H "Content-Type: application/json" -X POST -d '{"login": "log2", "username": "uname2", "password": "password2"}' http://localhost:5000/add_user
curl -i -H "Content-Type: application/json" -X POST -d '{"login": "log3", "username": "uname3", "password": "password3"}' http://localhost:5000/add_user
curl -i -H "Content-Type: application/json" -X POST -d '{"login": "log4", "username": "uname4", "password": "password4"}' http://localhost:5000/add_user
