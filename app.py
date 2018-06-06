from flask import Flask, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'username'
app.config['MYSQL_DATABASE_PASSWORD'] = 'supersecret'
app.config['MYSQL_DATABASE_DB'] = 'dbname'
app.config['MYSQL_DATABASE_HOST'] = 'server'
mysql.init_app(app)

# To test the deployment use a url like this
# https://api_gateway_url/dev/auth?user=username&pass=password

@app.route("/auth")
def auth():
    username = request.args.get('user')
    password = request.args.get('pass')
    cursor = mysql.connect().cursor()
    cursor.execute(
        "SELECT * from User where Username='" +
        username +
        "' and Password='" +
        password +
        "'")
    data = cursor.fetchone()
    if data is None:
        return "Username or Password are wrong"
    else:
        return "Logged in successfully"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
