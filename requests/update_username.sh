#!/bin/bash

# Update username
curl -i -H "Content-Type: application/json" -X POST -d '{"login":"log2", "new_value":"a_hngeryyyyy"}' http://localhost:5000/update_username
