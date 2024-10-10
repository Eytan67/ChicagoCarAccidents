from flask import Flask
from config import Config
from repository.database import Database

app = Flask(__name__)


app.config.from_object(Config)

db = Database(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.teardown_appcontext
def close_db_connection(exception):
    db.close_connection()

if __name__ == '__main__':
    app.run()
