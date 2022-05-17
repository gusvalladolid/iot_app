""" 
@author G. Valladolid
@since 2022-05-10
@descrip EJercicio de Flask
"""
# Inclusion de modulos
from flask import Flask, request

app = Flask('__main__')

user = {
    "code":"112233",
    "descrip":"Temp. Sensor",
    "value": 67
}


@app.route('/users', methods=['GET'])
def get_user():
    return user   

#Save an user
@app.route('/users', methods=['POST'])
def post_user():
    user = request.json
    print(user)
    return user

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
