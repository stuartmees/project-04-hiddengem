import os
from app import app
from flask import abort
from controllers import entries, auth, categories, states, locations

app.register_blueprint(entries.router, url_prefix='/api')
app.register_blueprint(categories.router, url_prefix='/api')
app.register_blueprint(states.router, url_prefix='/api')
app.register_blueprint(auth.router, url_prefix='/api')
app.register_blueprint(locations.router, url_prefix='/api')

@app.route('/')
@app.route('/<path:path>')
def catch_all(path='index.html'):
    if os.path.isfile('dist/' + path):
        return app.send_static_file(path)

    return abort(404)
