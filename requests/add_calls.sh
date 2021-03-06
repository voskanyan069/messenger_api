#!/bin/bash

# Add contact
curl -i -H "Content-Type: application/json" -X POST -d '{"user_login":"log", "contact_login":"log2", "call_status":"incoming", "call_time":"1 hour 21 minute"}' http://localhost:5000/add_calls
