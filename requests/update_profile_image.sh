#!/bin/bash

# Update username
curl -i -H "Content-Type: application/json" -X POST -d '{"login":"log2", "new_value":"https://firebasestorage.googleapis.com/v0/b/justchat-85e5f.appspot.com/o/users%2Fprofile_images%2Fuser13.jpg?alt=media&token=1cbe8548-cbc1-422c-b7a9-21e210e00d76"}' http://localhost:5000/update_profile_image
