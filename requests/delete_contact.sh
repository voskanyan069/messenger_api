#!/bin/bash

# Delete contact
curl -i -H "Content-Type: application/json" -X POST -d '{"login":"log2", "contact_login": "log"}' http://localhost:5000/delete_contact
