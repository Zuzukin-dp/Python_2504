from flask import Flask, request, url_for

from utils import generate_password, read_txt, generate_fake_user, get_astros, read_csv


app = Flask('MyFirstApp')

# my_lst = ['requirements', 'generate-users', 'mean', 'space']


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/test/')
def test():
    return f"{url_for('test').strip(' / ')} - {url_for('test', _external=True, page=2)}"


# validators.py
# def validate_integer(value, min_length=10, max_length=100) -> bool:
#     return True or False


@app.route('/gen-pass/')
def gen_pass():  # length = 20
    query_params = request.args

    # length: str = query_params.get('length', '') or '10'
    length = query_params.get('length') or ''
    default_password_length = 10
    minimum_password_length = 10
    maximum_password_length = 200

    if length.isdigit():
        length = int(length)
        if length > maximum_password_length or length < minimum_password_length:
            length = default_password_length

    else:
        length = default_password_length

    return generate_password(length)


@app.route('/requirements/')
def requirements():
    return read_txt('requirements.txt')


@app.route('/generate-users/')
def generate_users():
    q_params = request.args

    usr_num = q_params.get('usr_num') or ''
    default_usr_num = 100
    min_usr_num = 1
    max_usr_num = 782

    if usr_num.isdigit():
        usr_num = int(usr_num)
        if max_usr_num >= usr_num < min_usr_num:
            usr_num = default_usr_num
    else:
        usr_num = default_usr_num

    return generate_fake_user(usr_num)


@app.route('/mean/')
def mean():
    data = read_csv()

    cm = 2.54
    kg = 0.45359237

    col_num = max([int(i['Index']) for i in data])
    inches = sum([float(i['"Height(Inches)"']) for i in data])
    pounds = sum([float(i['"Weight(Pounds)"']) for i in data])

    mean_height = (inches * cm)/col_num
    mean_weight = (pounds * kg)/col_num

    return f"Mean height - {round(mean_height, 2)}(cm), mean weight {round(mean_weight, 2)}(kg)."


@app.route('/space/')
def space():
    astro = get_astros()
    return str(astro.json()['number'])


if __name__ == '__main__':
    app.run(port='5000', debug=True)

"""
http://127.0.0.1:5000/gen-pass/?length=20&name=Dima
http://  127.0.0.1  :5000  /  ?key=value
1           2          3   4  5
1 - protocol (http, https, ftp, smtp)
2 - server identify, IPv4 (23.48.3.1), IPv6 (), socket file
    IPv4
    0-255.0-255.0-255.0-255
    correct
    3.5.127.48
    254.254.0.0

    wrong
    256.0.0.3
    1.4.127
    1.4.127.0.1

    special ipv4 address
    127.0.0.1 - localhost

3 - port
    0 - 65353  - 2 ** 16
    0 - root

    #
    80 - http
    443 - https
    5432 - postgres
    #

4 - path
    / - hello_world()
    /test/ - test()

5 - query parameters
   start with ?
   key - value pair

stop app in terminal - Ctrl + C
"""