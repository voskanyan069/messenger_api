#!/bin/bash

# Add contact
curl -i -H "Content-Type: application/json" -X POST -d '{"login":"log2", "chat_login":"log3", "message_text":"new message Yoo-hoo"}' http://localhost:5000/send_message
curl -i -H "Content-Type: application/json" -X POST -d '{"login":"log2", "chat_login":"log4", "message_text":"new message Yoo-hoo"}' http://localhost:5000/send_message
curl -i -H "Content-Type: application/json" -X POST -d '{"login":"log3", "chat_login":"log2", "message_text":"new message Yoo-hoo"}' http://localhost:5000/send_message
