import os

from flask import Flask

from flaskbook_api.api import api
from flaskbook_api.api.config import config

config_name = os.environ.get("CONFIG", "local")

app = Flask(__name__)
app.config.from_object(config[config_name])
# blueprintをアプリケーションに登録
app.register_blueprint(api)


#from apps.app import create_app
#app = create_app("local")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5002)), debug=True)
