#!/bin/bash

# Add users
curl -i -H "Content-Type: application/json" -X POST -d '{"login": "log", "path": "story image path"}' http://localhost:5000/add_story
