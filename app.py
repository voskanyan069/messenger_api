from flask import Flask, request
import time

app = Flask(__name__)
users = []
messages = []
chats = {}
contacts = {}
calls = {}
stories = {}
user_id = 0


@app.route('/')
def get_server_status():
    return {
        'running': True,
        'date': time.time(),
        'users_count': len(users),
        'messages_count': len(messages)
    }


@app.route('/get_users')
def get_users():
    return {'users': users}


@app.route('/get_user/<login>')
def get_user(login):
    user = find_user_by_login(login)
    if user != 0:
        return {'user': user}
    return {'error': 'user not find', 'code': 1}


@app.route('/get_messages/<chat_name>')
def get_messages(chat_name):
    last_message = float(request.args['last_message'])
    ret_data = [message for message in messages if chat_name == message['chat_name']]
    ret_data = [message for message in ret_data if last_message < message['time']]
    return {'messages': ret_data}


@app.route('/get_contacts/<login>')
def get_contacts(login):
    user = find_user_by_login(login)
    if user != 0:
        return {'contacts': contacts[login]}
    return {'error': 'user not find', 'code': 1}


@app.route('/get_status/<login>')
def get_online_status(login):
    user = find_user_by_login(login)
    if user != 0:
        return {'status': user['status']}
    return {'error': 'user not find', 'code': 1}


@app.route('/get_chats/<login>')
def get_chats(login):
    user = find_user_by_login(login)
    if user != 0:
        return {'chats': chats[login]}
    return {'error': 'user not find', 'code': 1}


@app.route('/get_stories')
def get_stories():
    return {'stories': stories}


@app.route('/get_stories/<login>')
def get_stories_login(login):
    story = find_stories_by_login(login)
    if story != 0:
        return {'stories': stories}
    return {'error': 'stories not find', 'code': 8}


@app.route('/get_calls/<login>')
def get_calls(login):
    user = find_user_by_login(login)
    if user != 0:
        return {'calls': calls[login]}
    return {'error': 'user not find', 'code': 1}


@app.route('/add_user', methods=['POST'])
def add_user():
    global user_id
    data = request.json
    login = data['login']
    username = data['username']
    password = data['password']

    user = find_user_by_login(login)
    if user != 0:
        return {'error': 'user with this login is contains', 'code': 2}
    users.append({
        'login': login,
        'username': username,
        'password': password,
        'user_id': id(user_id),
        'profile_image': 'https://images.unsplash.com/photo-1614676367446-17828873a71c?ixid'
                         '=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=675&q'
                         '=80',
        'status': 'online',
    })
    contacts[login] = []
    stories[login] = []
    calls[login] = []
    chats[login] = []

    user_id += 1
    return {
        'login': login,
        'username': username,
        'password': password,
        'created': True
    }


@app.route('/add_contact', methods=['POST'])
def add_contact():
    data = request.json
    user_login = data['user_login']
    contact_login = data['contact_login']
    if user_login == contact_login:
        return {'error': 'you can\'t add you to your contacts', 'code': 3}
    user = find_user_by_login(user_login)
    contact = find_user_by_login(contact_login)
    if user != 0 and contact != 0:
        for cont in contacts[user_login]:
            if cont['login'] == contact_login:
                return {'error': 'the contact was contains', 'code': 5}
        contacts[user_login] += [
            {
                'login': contact['login'],
                'username': contact['username'],
                'profile_image': contact['profile_image'],
                'user_id': contact['user_id'],
                'status': contact['status']
            }
        ]
        return {
            'login': contact['login'],
            'username': contact['username'],
            'profile_image': contact['profile_image'],
            'user_id': contact['user_id']
        }
    return {'error': 'user not find', 'code': 1}


# TODO
@app.route('/send_message', methods=['POST'])
def add_message():
    data = request.json
    sender_login = data['sender_login']
    chat_name = data['chat_name']
    text = data['text']
    new_message = {'chat_name': chat_name, 'sender_login': sender_login, 'text': text, 'time': time.time()}
    messages.append(new_message)
    return {'message_sent': True}


@app.route('/add_chats', methods=['POST'])
def add_chats():
    data = request.json
    user_login = data['user_login']
    contact_login = data['contact_login']
    last_msg = data['last_msg']
    user = find_user_by_login(user_login)
    contact = find_user_by_login(contact_login)
    if user != 0 and contact != 0:
        for chat in chats[user_login]:
            if chat['login'] == contact_login:
                return {'error': 'the chat was contains', 'code': 9}
        chats[user_login] += [
            {
                'login': contact['login'],
                'username': contact['username'],
                'profile_image': contact['profile_image'],
                'last_msg': last_msg,
                'messages': []
            }
        ]
        return {
            'login': contact['login'],
            'username': contact['username'],
            'profile_image': contact['profile_image'],
            'last_msg': last_msg
        }
    return {'error': 'user not find', 'code': 1}


@app.route('/add_story', methods=['POST'])
def add_story():
    data = request.json
    login = data['login']
    path = data['path']

    user = find_user_by_login(login)
    profile_image = user['profile_image']

    stories[login].append({
        'login': login,
        'profile_image': profile_image,
        'path': path
    })

    return {'story_added': True}


@app.route('/add_calls', methods=['POST'])
def add_calls():
    data = request.json
    user_login = data['user_login']
    contact_login = data['contact_login']
    call_status = data['call_status']
    call_time = data['call_time']
    user = find_user_by_login(user_login)
    contact = find_user_by_login(contact_login)
    if user != 0 and contact != 0:
        calls[user_login] += [
            {
                'login': contact['login'],
                'username': contact['username'],
                'profile_image': contact['profile_image'],
                'call_status': call_status,
                'call_time': call_time
            }
        ]
        return {
            'login': contact['login'],
            'username': contact['username'],
            'profile_image': contact['profile_image'],
            'call_status': call_status,
            'call_time': call_time
        }
    return {'error': 'user not find', 'code': 1}


@app.route('/delete_user', methods=['POST'])
def delete_user():
    data = request.json
    user_login = data['user_login']
    for contact in contacts:
        if contact['login'] == user_login:
            contact['login'] = 'Deleted account'
    for user in users:
        if user['login'] == user_login:
            users.pop(user)
    return {'login': user_login}


@app.route('/delete_contact', methods=['POST'])
def delete_contact():
    data = request.json
    user_login = data['user_login']
    contact_login = data['contact_login']
    user = find_user_by_login(user_login)
    if user != 0:
        for contact in contacts:
            if contact['login'] == contact_login:
                contacts.pop(contact)
                break
    return {
        'login': user_login,
        'contact': contact_login
    }


@app.route('/update_username', methods=['POST'])
def update_username():
    data = request.json
    user_login = data['user_login']
    new_username = data['new_username']
    user = find_user_by_login(user_login)
    if user != 0:
        user['username'] = new_username
    print(contacts)
    for contact in contacts:
        for cont in contacts[contact]:
            if cont['login'] == user_login:
                cont['username'] = new_username
    return {
        'login': user_login,
        'username': new_username
    }


@app.route('/update_password', methods=['POST'])
def update_password():
    data = request.json
    user_login = data['user_login']
    new_password = data['new_password']
    user = find_user_by_login(user_login)
    if user != 0:
        user['password'] = new_password

    return {
        'login': user_login,
        'password': new_password
    }


@app.route('/update_status', methods=['POST'])
def update_status():
    data = request.json
    login = data['user_login']
    new_status = data['new_status']
    user = find_user_by_login(login)
    if user != 0:
        user['status'] = new_status
    for contact in contacts:
        for cont in contacts[contact]:
            if cont['login'] == login:
                cont['status'] = new_status
    return {
        'login': login,
        'status': new_status
    }


@app.route('/update_chat_last_message', methods=['POST'])
def update_chat_last_message():
    data = request.json
    login = data['user_login']
    chat_name = data['chat_name']
    new_last_msg = data['new_last_msg']
    user = find_user_by_login(login)
    if user != 0:
        for chat in chats[login]:
            if chat['login'] == chat_name:
                chat['last_msg'] = new_last_msg
    return {
        'login': login,
        'chat_name': chat_name,
        'new_last_msg': new_last_msg
    }


def find_user_by_login(user_login):
    for user in users:
        if user['login'] == user_login:
            return user
    return 0


def find_stories_by_login(user_login):
    for story in stories:
        if story['login'] == user_login:
            return story
    return 0


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
