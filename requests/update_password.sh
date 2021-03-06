#!/bin/bash

# Update password
curl -i -H "Content-Type: application/json" -X POST -d '{"user_login":"log2", "new_password":"new_pwd2"}' http://localhost:5000/update_password
