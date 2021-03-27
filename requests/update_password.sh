#!/bin/bash

# Update password
curl -i -H "Content-Type: application/json" -X POST -d '{"login":"log2", "new_value":"new_password2"}' http://localhost:5000/update_password
