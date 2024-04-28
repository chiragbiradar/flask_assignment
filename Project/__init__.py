from flask import Flask

import extensions
import models
import routes

def create_app(database_uri="sqlite:///db.sqlite3"):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SECRET_KEY"] = "FesC9cBSuxakv9yN0vBY"

    extensions.db.init_app(app)
    extensions.login_manager.init_app(app)

    @extensions.login_manager.user_loader
    def load_user(user_id):
        return models.User.query.get(user_id)

    app.register_blueprint(routes.main)
    return app