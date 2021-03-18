#!/bin/bash

# Add contact
curl -i -H "Content-Type: application/json" -X POST -d '{"login":"user13", "contact_login":"log2", "call_status":"missed", "call_time":"Missed call"}' http://localhost:5000/add_calls
