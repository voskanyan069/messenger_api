#!/bin/bash

# Add contact
curl -i -H "Content-Type: application/json" -X POST -d '{"login":"user13", "contact_login":"log4", "call_status":"incoming", "call_time":"1h 23m"}' http://localhost:5000/add_calls
