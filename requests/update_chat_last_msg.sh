#!/bin/bash

# Update status
curl -i -H "Content-Type: application/json" -X POST -d '{"user_login":"log", "chat_name":"log2", "new_last_msg":"new_last_msg"}' http://localhost:5000/update_chat_last_message
