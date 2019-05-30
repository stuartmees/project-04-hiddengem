from app import app
from controllers import entries, auth, categories, states, locations

app.register_blueprint(entries.router, url_prefix='/api')
app.register_blueprint(categories.router, url_prefix='/api')
app.register_blueprint(states.router, url_prefix='/api')
app.register_blueprint(auth.router, url_prefix='/api')
app.register_blueprint(locations.router, url_prefix='/api')
