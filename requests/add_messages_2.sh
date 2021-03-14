#!/bin/bash

# Add contact
curl -i -H "Content-Type: application/json" -X POST -d '{"login":"user13", "chat_login":"log2", "message_text":"Hi!"}' http://localhost:5000/send_message
curl -i -H "Content-Type: application/json" -X POST -d '{"login":"log2", "chat_login":"user13", "message_text":"Hello"}' http://localhost:5000/send_message
