#!/bin/bash

# Add contact
curl -i -H "Content-Type: application/json" -X POST -d '{"user_login":"log", "contact_login":"log2", "last_msg":"last message text"}' http://localhost:5000/add_chats
# curl -i -H "Content-Type: application/json" -X POST -d '{"user_login":"log2", "contact_login":"log3", "last_msg":"last message text"}' http://localhost:5000/add_chats
# curl -i -H "Content-Type: application/json" -X POST -d '{"user_login":"log3", "contact_login":"log2", "last_msg":"last message text"}' http://localhost:5000/add_chats
