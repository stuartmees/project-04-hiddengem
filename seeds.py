# seeds.py
from pony.orm import db_session
from app import db
from models.Entry import Entry

db.drop_all_tables(with_all_data=True)
db.create_tables()

with db_session():

    Entry(title="Pushkar", description="Quaint little trading village", town="pushkar", state="Rajestan", category="Thing to do...", lng=74.557300, lat=26.492000)

    Entry(title="Varkhala", description="Unique and stunning cliff backed beach. Shops and restaurants dotted along the top of the cliff", town="Varkhala", state="Kerala", category="Place", lng=76.725500, lat=8.734150)

    db.commit()
