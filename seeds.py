from pony.orm import db_session
from app import db
from models.Entry import Entry
from models.State import State
from models.Category import Category
from models.User import User, UserSchema

db.drop_all_tables(with_all_data=True)
db.create_tables()

with db_session():
    user_schema = UserSchema()

    stuseem = User(
        username='stuseem',
        email='stu@seem',
        password_hash=user_schema.generate_hash('pass')
    )

    stacrus = User(
        username='stacrus',
        email='stac@rus',
        password_hash=user_schema.generate_hash('pass')
    )

    sleeping = Category(name="Sleeping")
    eating = Category(name="Eating")
    going = Category(name="Going")
    doing = Category(name="Doing")

    andra_pradesh = State(name="Andra Pradesh")
    arunachal_pradesh = State(name="Arunachal Pradesh")
    assam = State(name="Assam")
    bihar = State(name="Bihar")
    chhattisgarh = State(name="Chhattisgarh")
    goa = State(name="Goa")
    gujarat = State(name="Gujarat")
    haryana = State(name="Haryana")
    himachal_pradesh = State(name="Himachal Pradesh")
    jammu_and_kasmir = State(name="Jammu and Kashmir")
    jharkhand = State(name="Jharkhand")
    karnataka = State(name="Karnataka")
    kerala = State(name="Kerala")
    madya_pradesh = State(name="Madya Pradesh")
    maharashtra = State(name="Maharashtra")
    manipur = State(name="Manipur")
    meghalaya = State(name="Meghalaya")
    mizoram = State(name="Mizoram")
    nagaland = State(name="Nagaland")
    orissa = State(name="Orissa")
    punjab = State(name="Punjab")
    rajastan = State(name="Rajasthan")
    sikkim = State(name="Sikkim")
    tamil_nadu = State(name="Tamil Nadu")
    telagana = State(name="Telagana")
    tripura = State(name="Tripura")
    uttaranchal = State(name="Uttaranchal")
    uttar_pradesh = State(name="Uttar Pradesh")
    west_bengal = State(name="West Bengal")
    andaman_and_nicobar_islands = State(name="Andaman and Nicobar Islands")
    chandigarh = State(name="Chandigarh")
    dadar_and_nagar_haveli = State(name="Dadar and Nagar Haveli")
    daman_and_diu = State(name="Daman and Diu")
    daman = State(name="Daman")
    dehli = State(name="Delhi")
    lakshadeep = State(name="Lakshadeep")
    pondicherry = State(name="Pondicherry")

    Entry(
        title="Pushkar",
        description="Quaint little trading village",
        town="pushkar",
        state=rajastan,
        category=going,
        lng=74.557300,
        lat=26.492000,
        created_by=stuseem
    )

    Entry(
        title="Varkhala",
        description="Unique and stunning cliff backed beach. Shops and restaurants dotted along the top of the cliff",
        town="Varkhala",
        state=kerala,
        category=going,
        lng=76.725500,
        lat=8.734150,
        created_by=stacrus
    )

    Entry(
        description="Near perfect crescent moon shaped beach!!",
        category=going,
        state=goa,
        lat=15.484280,
        title="Palolem",
        lng=73.823010,
        town="Palolem",
        created_by=stuseem
    )

    db.commit()
