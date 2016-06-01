import logging
import settings
from flask import Flask
from routes import routes

app = Flask(__name__)

# import the routes in routes.py
app.register_blueprint(routes)


# run the Flask app
if __name__ == '__main__':
    logging.basicConfig(filename=settings.LOGFILE,
                        level=settings.LOGLEVEL,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)s %(levelname)s %(message)s')

    app.run(host=settings.HOST,
            port=settings.PORT,
            debug=settings.DEBUG)