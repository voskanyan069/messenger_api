#!/bin/bash

# Add contact
curl -i -H "Content-Type: application/json" -X POST -d '{"login":"log2", "chat_login":"log3", "message_text":"new 2 message Yoo-hoo"}' http://localhost:5000/send_message
