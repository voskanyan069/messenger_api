from flask import Flask, request
import time

app = Flask(__name__)
users = []
messages = {}
new_messages = {}
chats = {}
contacts = {}
calls = {}
stories = {}
contacts_stories = {}
user_id = 0
day_in_seconds = 86400


@app.route('/')
def get_server_status():
    return {
        'running': True,
        'date': time.time(),
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


@app.route('/get_messages/<login>/<chat_name>')
def get_messages(login, chat_name):
    after = request.args.get('after', '0')
    if login == chat_name:
        return {"error": "login and chat_name can not be same", "code": 10}
    if not messages.__contains__(login):
        messages[login] = {}
    if not messages[login].__contains__(chat_name):
        messages[login][chat_name] = []
    ret_messages = [message for message in messages[login][chat_name] if message['message_time'] > float(after)]
    return {'messages': ret_messages}


@app.route('/get_new_messages', methods=['POST'])
def get_new_messages():
    data = request.json
    login = data['login']
    chat_name = data['chat_name']
    if login == chat_name:
        return {"error": "login and chat_name can not be same", "code": 10}
    if not messages.__contains__(login):
        messages[login] = {}
    if not messages[login].__contains__(chat_name):
        messages[login][chat_name] = []
    if not new_messages.__contains__(login):
        return {"error": "not new messages for login", "code": 12}
    if not new_messages[login].__contains__(chat_name):
        return {"error": "not new messages for this chat", "code": 13}
    for i in range(len(new_messages[login][chat_name])):
        messages[login][chat_name].append(new_messages[login][chat_name][i])
        new_messages[login][chat_name].pop(i)
    return {'messages': 'updated'}


@app.route('/get_status/<login>')
def get_status(login):
    user = find_user_by_login(login)
    if user != 0:
        return {'status': user['status']}
    return {'error': 'user not find', 'code': 1}


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


@app.route('/get_stories/<login>')
def get_stories(login):
    user = find_user_by_login(login)
    if user != 0:
        return {'stories': stories[login]}
    return {'error': 'user not find', 'code': 1}


@app.route('/get_stories')
def get_all_stories():
    return {"stories": stories}


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
    stories[login] = {
        "login": login,
        "username": username,
        "profile_image": 'https://images.unsplash.com/photo-1614676367446-17828873a71c?ixid'
                         '=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=675&q'
                         '=80',
        "media_path": []
    }
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
    user_login = data['login']
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
        return {'contact_added': True}
    return {'error': 'user not find', 'code': 1}


@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    login = data['login']
    chat_login = data['chat_login']
    message_text = data['message_text']
    user = find_user_by_login(login)
    chat_user = find_user_by_login(chat_login)
    if user != 0 and chat_user != 0:
        new_login_chat = {
            'login': chat_user['login'],
            'username': chat_user['username'],
            'profile_image': chat_user['profile_image'],
            'last_msg': message_text,
            'status': chat_user['status']
        }
        new_chat_login_chat = {
            'login': user['login'],
            'username': user['username'],
            'profile_image': user['profile_image'],
            'last_msg': message_text,
            'status': user['status']
        }
        extend = False
        for chat in chats[login]:
            if chat_login == chat['login']:
                extend = True
                break
        if not extend:
            chats[login] += [new_login_chat]
        extend = False
        for chat in chats[chat_login]:
            if login == chat['login']:
                extend = True
                break
        if not extend:
            chats[chat_login] += [new_chat_login_chat]
        if not messages.__contains__(login):
            messages[login] = {}
        if not messages.__contains__(chat_login):
            messages[chat_login] = {}
        if not messages[login].__contains__(chat_login):
            messages[login][chat_login] = []
        if not messages[chat_login].__contains__(login):
            messages[chat_login][login] = []
        new_message = {
            'chat_login': chat_login,
            'login': login,
            'username': user['username'],
            'profile_image': user['profile_image'],
            'message_text': message_text,
            'message_time': time.time()
        }
        messages[login][chat_login].append(new_message)
        messages[chat_login][login].append(new_message)
        for chat in chats[login]:
            if chat['login'] == chat_login:
                chat['last_msg'] = 'You: ' + message_text
        for chat in chats[chat_login]:
            if chat['login'] == login:
                chat['last_msg'] = message_text
        return {'message_sent': True}
    return {'error': 'user not find', 'code': 1}


@app.route('/add_story', methods=['POST'])
def add_story():
    data = request.json
    login = data['login']
    path = data['path']
    user = find_user_by_login(login)
    if user != 0:
        stories[login]['media_path'].append({
            "path": path,
            "time": time.time()
        })
        return {'story_added': True}
    return {'story_added': False}


@app.route('/add_calls', methods=['POST'])
def add_calls():
    data = request.json
    user_login = data['login']
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
                'status': contact['status'],
                'call_status': call_status,
                'call_time': call_time
            }
        ]
        return {'call_added': True}
    return {'call_added': False}


@app.route('/delete_user', methods=['POST'])
def delete_user():
    data = request.json
    login = data['login']
    user = find_user_by_login(login)
    if user != 0:
        for contact in contacts:
            if contact['login'] == login:
                contact['login'] = 'Deleted account'
        for user in users:
            if user['login'] == login:
                users.pop(user)
        return {'deleted': True}
    return {'deleted': False}


@app.route('/delete_contact', methods=['POST'])
def delete_contact():
    data = request.json
    login = data['login']
    contact_login = data['contact_login']
    user = find_user_by_login(login)
    if user != 0:
        for contact in contacts:
            for c in range(len(contacts[contact])):
                if contacts[contact][c]['login'] == contact_login:
                    contacts[contact].pop(c)
                    break
        return {'deleted': True}
    return {'deleted': False}


@app.route('/update_username', methods=['POST'])
def update_username():
    data = request.json
    user_login = data['login']
    new_username = data['new_username']
    user = find_user_by_login(user_login)
    if user != 0:
        user['username'] = new_username
    for contact in contacts:
        for cont in contacts[contact]:
            if cont['login'] == user_login:
                cont['username'] = new_username
    for chat in chats:
        for c in chats[chat]:
            if c['login'] == user_login:
                c['username'] = new_username
    for call in calls:
        for c in calls[call]:
            if c['login'] == user_login:
                c['username'] = new_username
    return {
        'login': user_login,
        'username': new_username
    }


@app.route('/update_password', methods=['POST'])
def update_password():
    data = request.json
    user_login = data['login']
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
    login = data['login']
    new_status = data['new_status']
    user = find_user_by_login(login)
    if user != 0:
        user['status'] = new_status
        for contact in contacts:
            for cont in contacts[contact]:
                if cont['login'] == login:
                    cont['status'] = new_status
        for chat in chats:
            for c in chats[chat]:
                if c['login'] == login:
                    c['status'] = new_status
        for call in calls:
            for c in calls[call]:
                if c['login'] == login:
                    c['status'] = new_status
        return {'updated': True}
    return {'updated': False}


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


def delete_stories():
    while True:
        print('check')
        for user in users:
            login = user['login']
            for story in stories[login]['media_path']:
                print(story['time'])
        time.sleep(2)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
