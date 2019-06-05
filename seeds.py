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
    madhya_pradesh = State(name="Madhya Pradesh")
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
        title="Majestic shopping town on  majestic lake!",
        description='Udaipur has a romance of setting unmatched in Rajasthan and arguably in all India – snuggling beside tranquil Lake Pichola, with the purple ridges of the Aravalli Range stretching away in every direction. Fantastical palaces, temples, havelis (traditional, ornately decorated residences) and countless narrow, crooked, timeless streets add the human counterpoint to the city’s natural charms. For the visitor theres the serenity of boat rides on the lakes, the bustle and colour of bazaars, a lively arts scene, the quaint old world feel of its heritage hotels, tempting shops and some lovely countryside to explore on wheels, feet or horseback.',
        location="Udaipur, Rajasthan, India",
        state=rajastan,
        category=going,
        lng=73.712479,
        lat=24.585445,
        created_by=stuseem,
        photo="https://img.traveltriangle.com/blog/wp-content/uploads/2018/07/udaipur-city-palace-blue-boat-cover-image.jpg"
    )

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
        title="Tiger Safari! Shere Khans Jungle!",
        description='I have been to many jungles across the country but Kanha, Rajastan is the best I have seen. Not just in tiger sighting but in overall experience. Visited the park in May 2019. Had 4 drives, 2 in Kanha zone and 2 in Mukki. zone Saw a total of 5 tigers including the dominant male of the region. One of the sightings was of a tigress walking towards us. She was about 6 feet away when she decided to move away. We also saw a tigress chasing another out of her territory. Also saw a pack of 11 dholes (Indian wild dogs). Other notable sightings were Barasingha which are endemic to this park, Gaurs, Sambar deers, jackals and numerous birds (including a Night Jar camouflaged a few feet away from the jeep tracks). Not just the fauna, the flora in Kanha is mesmerizing as well. The tall Sal trees provide a nice vista and keep the temperature down. We were shivering to the bone in the first hour of the morning safari (in the month of May). Lastly, a shout out for the park management. They are doing an amazing job. The restrooms at the Center Point can give any of our airports a run for their money in terms of cleanliness.',
        location="Kanha Tiger Reserve, Madhya Pradesh, India",
        state=rajastan,
        category=doing,
        lng=80.611513,
        lat=22.3345132,
        created_by=stuseem,
        photo="https://media-cdn.tripadvisor.com/media/photo-s/0f/64/43/78/kanha-national-park-one.jpg"
    )

    Entry(
        title="A must see in Varanassi.",
        description="The Ganges river and its ghats are a must see in Varanasi. When researching i thought it would be very dirty but this is not the case. I still won't be swimming in the Ganges but it isn't so bad that you can't walk around and enjoy your time. Their are numerous people bathing and washing their clothes in the river right next to areal graves. It is quite the sight and should not be missed. You can also take a boat which should cost you about 80 rupees per person per hour",
        location="Varanasi Cantt, Varanasi, Uttar Pradesh, India",
        state=uttar_pradesh,
        category=doing,
        lng=82.9689738,
        lat=25.3323527,
        created_by=stuseem,
        photo="https://media-cdn.tripadvisor.com/media/photo-s/01/64/b8/c9/varanassi-at-dawn.jpg"
    )

    Entry(
        title="Desert Camel trekking under the stars!",
        description="While exploring the Golden City its likely you will be offered a camel safari in Jaisalmer. Its the most popular tourist attraction in the western region of Rajasthan. The Sam Sand Dunes are on the outskirts of Jaisalmer in the Desert National Park provide the perfect landscape for slow-paced trekking and escaping the city. I spent three days and two nights sleeping in the sand dunes under the stars on my camel safari. It was one of the highlights from my three months in India. It was incredibly hot, isolated and barren. However, this is what made it so epic. Our guide Sambu started a fire with sticks he would find before each meal. Making chai, chapati, and curry from scratch in the heat of the desert was an amazing feat to watch. This would be my number one recommendation of things to do in Jaisalmer! There are a few ways to experience a camel safari in Jaisalmer. You can go for a half-day camel trek, overnight trek or a three-day trek. It really depends on your preference. I would advise only adventurous people to do several day journeys as it can be a bit uncomfortable and hot at times but very fun. I have put down below several of the best available tour options to book your very own camel safari depending on how long you want to spend in the desert. The half-day tour can be less than $30 while the overnight treks depend on the quality of the camping and sleeping arrangements",
        location="Jaisalmer, Rajasthan, India",
        state=rajastan,
        category=doing,
        lng=70.9083443,
        lat=26.492000,
        created_by=stuseem,
        photo="https://www.tripsavvy.com/thmb/tabuB30n8mKb54xfGl_sku-ugts=/960x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-807217976-5982bf97054ad90011a5d484.jpg"
    )

    Entry(
        title="Great little restaurant on the beach in Varkala!!! ",
        description="The shack is pretty scruffy, especially upstairs where the wood floor planks  areall croocked and squeaky, but the fried calamari were perfectly cooked and crispy. Came back a second time for lunch and and had a lovely grilled fish and a prawns noodle dish. We also tried a desert we never heard of before called Hello to the queen and it was heavenly. A little bomb of flavours and different textures: bananas and warm chocolate mixed with crumbles of Marie cookies, topped with soft ice cream and grated coconut entoured by tangerines slices. After 10 days in Varkala, we declared their version of this dessert to be the best!",
        location="Theeram Beach Restaurant, Varkala, Kerala, India",
        state=kerala,
        category=eating,
        lng=76.7054895,
        lat=8.733518499999999,
        created_by=stuseem,
        photo="https://content3.jdmagicbox.com/comp/thiruvananthapuram/r6/0471px471.x471.170930045308.d6r6/catalogue/theeram-beach-restaurant-varkala-thiruvananthapuram-restaurants-ne82dvzkdt.jpg"
    )

    Entry(
        title="Unique and stunning cliff backed beach with bazaar.",
        description="Perched almost perilously along the edge of majestic 15m-high red laterite cliffs, 50km northwest of Trivandrum, Kerala, Varkala has a naturally beautiful setting that has allowed it to steadily grow into Kerala's most popular backpacker hang-out. A small strand of golden beach nuzzles Varkala's North Cliff area, where restaurants play innocuous world music and shops sell elephant-stamped trousers, silver jewellery and cotton yoga-mat bags. While it's certainly on the beaten track and the sales pitch can be tiring, Varkala is still a great place to watch the days slowly turn into weeks, and it's easy to escape the crowds further north or south where the beaches are cleaner and quieter.",
        location="Varkala, Kerala, India",
        state=kerala,
        category=going,
        lng=75.725500,
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

    Entry(
        description="If youre after a classic Goa psychedelic trance party, Hill Top is where youll find it. This iconic open-air venue has been in business since the hippie heydays of the 1970s. It has evolved from a small restaurant into a mecca for psychedelic trance that's hosted artists from around the world. A grove of neon palm trees and groovy art installations give it an appropriately trippy vibe. Parties happen every Sunday from 5-10 p.m., as well as on other special occasions such as New Years Eve and Christmas Eve. Hill Top has also started hosting a funky new “Goa Collective” all-day market on Fridays. Plan to be there for the annual Hill Top Festival, happening from February 8 to 10, 2019. Boom!",
        category=doing,
        state=goa,
        lat=15.5735995,
        title="Party on the beach in Goa!!!!!",
        lng=73.7407065,
        location="Anjuna Beach, Goa",
        created_by=stuseem,
        photo="https://www.tripsavvy.com/thmb/nX7NHn_GSJuXFq1tAJkbq9fRlMg=/950x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/GettyImages-56957837-59ba853c845b340010300873.jpg"
    )

    Entry(
        description="Explore the backwaters of Kerala at here Alleppey or Alappuzha nearly 60 k.m from south kochi. A town with picturesque canals, backwaters and beaches.These is one of the most popular backwater destinations in Kerala. Also known as 'Venice of the East' Book a houseboat for backwater cruise journey. You can also stay overnight in the houseboat for delightful experience. I recommend to book a houseboat with balcony where you can enjoy the beauty of the lake in relaxed mood.",
        category=doing,
        state=kerala,
        lat=9.523814,
        title="Backwater boat cruises in Kerala!",
        lng=76.35675599999999,
        location="Alleppey Backwater, Punnamada, Kottankulangara, Alappuzha, Kerala, India",
        created_by=stuseem,
        photo="https://scontent.flhr4-1.fna.fbcdn.net/v/t1.0-9/30741858_10156236206979929_7381770109930438656_o.jpg?_nc_cat=105&_nc_ht=scontent.flhr4-1.fna&oh=5b28fc2fec68543889459c6221734ca3&oe=5D5B1DE1"
    )

    db.commit()
