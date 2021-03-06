#!/bin/bash

# Add contact
curl -i -H "Content-Type: application/json" -X POST -d '{"sender_login":"log_OOO", "chat_name":"log123_log2", "text":"second message text"}' http://localhost:5000/send_message
