#!/bin/bash

# Add contact
curl -i -H "Content-Type: application/json" -X POST -d '{"user_login":"user1", "contact_login":"log", "call_status":"missed", "call_time":"Missed call"}' http://localhost:5000/add_calls
