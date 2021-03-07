#!/bin/bash

# Add contact
curl -i -H "Content-Type: application/json" -X POST -d '{"sender_login":"log2", "chat_name":"log3", "text":"second message text"}' http://localhost:5000/send_message
