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
        title="Quaint, bustling village perched on ghats.",
        description='Pushkar has a magnetism all of its own – it’s quite unlike anywhere else in Rajasthan. It is world famous for its spectacular Camel Fair, which takes place in the Hindu month of Kartika (October/November). If you are anywhere nearby at the time you would be crazy to miss it. For the rest of the year Pushkar remains a prominent Hindu pilgrimage town, humming with puja (prayers), bells, drums and devotional songs. The town wraps itself around a holy lake featuring 52 bathing ghats and 400 milky-blue temples, including one of the world’s few Brahma temples. The main street is one long bazaar, selling anything to tickle a traveller’s fancy, from hippy-chic tie-dye to didgeridoos. The result is a muddle of religious and tourist scenes. Yet, despite the commercialism, the town remains enchantingly mystic and relaxed. Pushkar is only 11km from Ajmer, separated from it by rugged Nag Pahar (Snake Mountain)',
        location="Pushkar, Rajasthan, India",
        state=rajastan,
        category=going,
        lng=74.557300,
        lat=26.492000,
        created_by=stuseem,
        photo="https://www.travelogyindia.com/images/rajasthan/pushkar-tipl.jpg"
    )

    Entry(
        title="Unique and stunning cliff backed beach with bazaar.",
        description="Perched almost perilously along the edge of majestic 15m-high red laterite cliffs, 50km northwest of Trivandrum, Varkala has a naturally beautiful setting that has allowed it to steadily grow into Kerala's most popular backpacker hang-out. A small strand of golden beach nuzzles Varkala's North Cliff area, where restaurants play innocuous world music and shops sell elephant-stamped trousers, silver jewellery and cotton yoga-mat bags. While it's certainly on the beaten track and the sales pitch can be tiring, Varkala is still a great place to watch the days slowly turn into weeks, and it's easy to escape the crowds further north or south where the beaches are cleaner and quieter.",
        location="Varkala, Kerala, India",
        state=kerala,
        category=going,
        lng=76.725500,
        lat=8.734150,
        created_by=stacrus,
        photo="https://media-cdn.tripadvisor.com/media/photo-s/0e/15/20/f7/varkala-cliff.jpg"
    )

    Entry(
        description="Palolem is undoubtedly one of Goa’s most postcard-perfect beaches: a gentle curve of palm-fringed sand facing a calm bay. But in season the beachfront is transformed into a toy town of colourful and increasingly sophisticated timber and bamboo huts fronted by palm-thatch restaurants. It’s still a great place to be and is popular with backpackers, long-stayers and families. The protected bay is one of the safest swimming spots in Goa and you can comfortably kayak and paddleboard for hours here.",
        category=going,
        state=goa,
        lat=15.484280,
        title="Near perfect crescent moon shaped beach!!",
        lng=73.823010,
        location="Palolem Beach, Goa",
        created_by=stuseem,
        photo="https://media-cdn.tripadvisor.com/media/photo-s/0d/cf/5e/10/palolem.jpg"
    )

    db.commit()
