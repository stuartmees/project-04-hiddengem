from app import app
from controllers import entries

app.register_blueprint(entries.router, url_prefix='/api')
