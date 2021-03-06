#!/bin/bash

# Add users
curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/get_user/log
