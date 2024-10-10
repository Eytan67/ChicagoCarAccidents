from flask import Flask
from config import Config
from blue_prints.querys_bp import query_bp
from blue_prints.initial_database_bp import initdb_bp

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

app.register_blueprint(query_bp, url_prefix='/query')
app.register_blueprint(initdb_bp, url_prefix='/init')

if __name__ == '__main__':
    app.run()
