#!/bin/bash

# Add contact
curl -i -H "Content-Type: application/json" -X POST -d '{"user_login":"log2", "contact_login":"log"}' http://localhost:5000/add_contact
