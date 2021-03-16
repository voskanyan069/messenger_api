#!/bin/bash

# Update status
curl -i -H "Content-Type: application/json" -X POST -d '{"login":"log2", "new_status":"offline"}' http://localhost:5000/update_status
