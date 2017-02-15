from flask import Flask
from flask import request
from flask.ext.mysql import MySQL
import json
import redis


mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'Delivery'
app.config['MYSQL_DATABASE_HOST'] = '10.213.96.211'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)


@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/mysql')
def con_mysql():
    _date = request.args.get('date')
    conn = mysql.connect()
    cursor = conn.cursor()
    select_stmt = "SELECT DATE,TYPE,CODE,ENGLISH_NAME,CAR_TYPE,SIZE FROM Delivery.truck where date = (%s);"
    cursor.execute(select_stmt, (_date))
    data = cursor.fetchall()
    return json.dumps(data)


@app.route('/redis')
def con_redis():
    _locpair = request.args.get('loc')
    pool = redis.ConnectionPool(host='localhost', port=6379, db=2)
    rClient = redis.Redis(connection_pool=pool)
    dis_dur=rClient.get(_locpair)
    return dis_dur


if __name__ == '__main__':
    app.run()
