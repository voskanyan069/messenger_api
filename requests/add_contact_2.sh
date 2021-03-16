#!/bin/bash

# Add contact
curl -i -H "Content-Type: application/json" -X POST -d '{"login":"user13", "contact_login":"log2"}' http://localhost:5000/add_contact
curl -i -H "Content-Type: application/json" -X POST -d '{"login":"user13", "contact_login":"log"}' http://localhost:5000/add_contact
