#!/bin/bash

# Update username
curl -i -H "Content-Type: application/json" -X POST -d '{"user_login":"log2", "new_username":"new_uname2"}' http://localhost:5000/update_username
