-- Populate the 'users' table

INSERT INTO `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`, `location`, `profile_image`, `profile_description`, `role`, `status`) 
VALUES 
('jdoe', '$2b$12$tVt26/NXHn0aVsBQYldNRuBylThGwpB5xxKKbkwF12XVgekYkGyv6', 'jdoe@hotpost.com', 'John', 'Doe', 'Lincoln, Canterbury', NULL, 'Here I can write about myself', 'admin', 'active'),
('sbrown', '$2b$12$dSZMiFCPTs.cJ/4Ei/mrvOZ1E9hZS1iQvMkdO4Vj/o1iu.9YA8Hde', 'sbrown@macrosoft.com', 'Sarah', 'Brown', 'Lincoln, Canterbury', NULL, 'Here I can write about myself', 'admin', 'active'),
('awilson', '$2b$12$/JisuYXPWf8KCm2Y/ZT1LeCGorX2QdyggYKCohrnmaEmG7KGaXCAy', 'awilson@moc.com', 'Amelia', 'Wilson', 'Lincoln, Canterbury', NULL, 'Here I can write about myself', 'editor', 'active'),
('lmckenzie', '$2b$12$FHJqu1wJNbXYgcNhCLMEhuWbbIviigcCBMwVlv/KdzzD0S8PLGq1a', 'lmckenzie@bluewave.co', 'Liam', 'McKenzie', 'Lincoln, Canterbury', NULL, 'Here I can write about myself', 'editor', 'active'),
('gparker', '$2b$12$390TIvS/A1fJ0qiFB/gXGu5bn.RO1/MulG7/enAnXF/6iCfsX8Phy', 'gparker@bigshift.io', 'Grace', 'Parker', 'Lincoln, Canterbury', NULL, 'Here I can write about myself', 'editor', 'active'),
('bsmith', '$2b$12$TNh8eGuCo42dMxXetW63pepj7me6S6sOuBGQqjcWUKez6qt5KPMBC', 'bsmith@pixzone.org', 'Bella', 'Smith', 'Lincoln, Canterbury', NULL, 'Here I can write about myself', 'editor', 'active'),
('mjones', '$2b$12$nlCKDNup.FqPt6xj.ag9Reb.hIhP/lrubceva.m/5Sclw7vND1IYi', 'mjones@trendpeak.com', 'Maya', 'Jones', 'Lincoln, Canterbury', NULL, 'Here I can write about myself', 'editor', 'active'),
('mking', '$2b$12$S536G.nSZkUMlqU2qUKwCefGSSexnA3ZMTyo3CN6xcqNvaztcJK8i', 'mking@neonstream.co.nz', 'Mia', 'King', 'New Zealand', NULL, 'Here I can write about myself', 'traveller', 'active'),
('hwhitaker', '$2b$12$88aNyPcrLUsU.wI/F0/1yOOIMLRFo.cLFBow8wmyQN0XLsIlyaQwW', 'hwhitaker@adventurelink.co.nz', 'Harrison', 'Whitaker', 'Christchurch', NULL, 'Here I can write about myself', 'traveller', 'active'),
('elam', '$2b$12$HNUcvKHsjjgtlFle7Hd8puG.X4ZPQsxc/quUnGgjpcE98TiY1OhSW', 'elam@rainforest.org', 'Ella', 'Lam', 'New Zealand', NULL, 'Here I can write about myself', 'traveller', 'active'),
('rawhiti', '$2b$12$ElDPb5JCRGNb2e9hdowKiO7hk0ZNbzvwesyL//YkuOHP28FxqRGUq', 'rawhiti@pinnaclezone.co.nz', 'Rangi', 'Awiti', 'New Zealand', NULL, 'Here I can write about myself', 'traveller', 'active'),
('tumu', '$2b$12$VESnZDFBuLlyyrwt4YhYFuB9Y9K8haDpM7sbn7XZpEduCFbwiQP4G', 'tumu@globalinnovate.co.nz', 'Tumu', 'Te Ao', 'Auckland', NULL, 'Here I can write about myself', 'traveller', 'active'),
('gwhite', '$2b$12$K9TrPyGc5bGWHbiOtLraPu9ghigEjMwAa3qnh3wtYxT/ZjKM4CVWy', 'gwhite@solarpowerhub.co.nz', 'Gemma', 'White', 'New Zealand', NULL, 'Here I can write about myself', 'traveller', 'active'),
('bgray', '$2b$12$E6LGLenQo2VAtYt2tUs0i.9JdVzRro2EwZVrTwFatCL7T4QKOnNXC', 'bgray@ecoenviro.com', 'Blake', 'Gray', 'Christchurch', NULL, 'Here I can write about myself', 'traveller', 'active'),
('csmith', '$2b$12$oEmleL3uK5f1BpbjmDIEa.W6zZM3V7/njCSpOltqu/OQ0l9u.34r2', 'csmith@nextgenventures.co.nz', 'Charlie', 'Smith', 'Dunedin', NULL, 'Here I can write about myself', 'traveller', 'active'),
('sdavis', '$2b$12$mirCtXOsCx6GzkGaY5ayP.tvpPeB1xOhMuMSGMP1j1VEwa2UsnShO', 'sdavis@cloudflare.co.nz', 'Sophia', 'Davis', 'Christchurch', NULL, 'Here I can write about myself', 'traveller', 'active'),
('pcrane', '$2b$12$1OYa6YYU6r8yQCecMLY9jeah8L7E.2kyLmMDbvsxayeD4.zSIGjPy', 'pcrane@futuretech.co.nz', 'Peter', 'Crane', 'Lincoln, New Zealand', NULL, 'Here I can write about myself', 'traveller', 'active'),
('nwilliams', '$2b$12$6dHG6KSJ1XErF5WqfSXkdOWLV9HEYBMGlf74vrGNaNU94xgLh7bM6', 'nwilliams@eurotravels.uk', 'Nina', 'Williams', 'UK', NULL, 'Here I can write about myself', 'traveller', 'active'),
('fwilson', '$2b$12$S0BVsK3jPnrgvFhfqpMpE.zm1rkPpGixIK2cC/lP9WL0a0dhBki1q', 'fwilson@greenpath.org', 'Finn', 'Wilson', 'New Zealand', NULL, 'Here I can write about myself', 'traveller', 'active'),
('djohnson', '$2b$12$gKOmFRmB67auj4qhO4O2le1FY/IwzayZebu1qhbAy2V16531aZQK2', 'djohnson@arcticventures.co.nz', 'Daniel', 'Johnson', 'New Zealand', NULL, 'Here I can write about myself', 'traveller', 'active'),
('mteo', '$2b$12$uoN4vDLkoK8oVm2bu2S8rus.DoGQRllz0rrDL3G4tiiO066Y6G83K', 'mteo@newhorizon.co.nz', 'Mako', 'Teo', 'New Zealand', NULL, 'Here I can write about myself', 'traveller', 'active'),
('awright', '$2b$12$.uph.7dS2ejwpftWU31.n.2oRhsEFlRZ/QASOBlsjSnrl837JNx7G', 'awright@crossworlds.uk', 'Aroha', 'Wright', 'UK', NULL, 'Here I can write about myself', 'traveller', 'active'),
('msmith', '$2b$12$a5pahdBBy8TBCMsjI6umretVxJX0FAXZxb/Mw5hl4OyRaEd7fSxX.', 'msmith@sunshineventures.uk', 'Mason', 'Smith', 'UK', NULL, 'Here I can write about myself', 'traveller', 'active'),
('ksanderson', '$2b$12$EgoMRkDQ6PC34K40wmkECuEgRffUyz22ypY8A27aw4ITLiEGNzxYm', 'ksanderson@earthsolutions.co.nz', 'Kylie', 'Anderson', 'New Zealand', NULL, 'Here I can write about myself', 'traveller', 'active'),
('hmckenzie', '$2b$12$xb3WXa0Xl5VGEGfRkJzLg.oI0R0E94iZJt3xwV4N6idqN2Ph8ALlW', 'hmckenzie@techconnect.sg', 'Hunter', 'McKenzie', 'Singapore', NULL, 'Here I can write about myself', 'traveller', 'active'),
('tjackson','$2b$12$8JaBt8Zy.U6SV7OtLfNqHujRvO0y8zHHTYCPIDlgEwyDv7PxsCzJC','tjackson@ecomind.co.nz','Thomas','Jackson','New Zealand',NULL, 'Here I can write about myself','traveller','active'),
('htawhiao','$2b$12$TwRGxQEWe64rTcA.vdhf4OElSU/xXUaFZWlDpKJ/3XEr7s875j3la','hemitawhiao@creativeemail.com','Hemi','Tāwhiao','Lincoln, New Zealand',NULL, 'Here I can write about myself','traveller','blocked');

-- Populate the 'announcements' table
INSERT INTO `announcements` (`user_id`, `announcement_title`, `announcement_description`, `created_at`) VALUES
(1, 'Launch of the New App', 'Dear Travellers, we are happy to announce that we have launched the new Timbuktu app where you can keep your travelling memories and share them with the world.', CURRENT_TIMESTAMP),
(2, 'App down', 'Dear Travellers, please note that we are currently in the development phase of the app. Sorry for any disruption of service.', CURRENT_TIMESTAMP);

-- Populate the 'journeys' table
INSERT INTO `journeys` (`user_id`, `journey_title`, `journey_description`, `start_date`, `status`) VALUES
(8, 'COMP639 Workshop', 'Journey that documents the trip from Wellington to Lincoln and back for the Studio Project Workshop.',  current_date(), 'public'),
(9, 'Gold Coast 2024', 'Journey documenting a vacation to Australia.',  current_date(), 'public'),
(10, 'Seoul Summer 2025 Reunion', 'Documenting a trip home for a family reunion.',  current_date(), 'public'),
(11, 'Trip to Italy', 'Exploring Rome’s ancient ruins, tasting authentic pasta in Florence, and enjoying the Amalfi Coast views.',  current_date(), 'public'),
(12, 'Hiking the Inca Trail', 'A four-day trek through the Peruvian Andes, ending with a breathtaking sunrise at Machu Picchu.',  current_date(), 'public'),
(13, 'Sakura Season in Japan', 'Chasing cherry blossoms from Tokyo to Kyoto, experiencing hanami picnics in the parks.',  current_date(), 'public'),
(15, 'Road Trip Across New Zealand', 'A campervan adventure through the South Island, from Queenstown’s fjords to Christchurch’s gardens.',  current_date(), 'public'),
(17, 'Exploring the Greek Islands', 'Island hopping from Santorini to Mykonos, enjoying white-washed villages and crystal-clear waters.',  current_date(), 'public'),
(18, 'Backpacking Through Vietnam', 'From Hanoi’s bustling streets to the serene beauty of Ha Long Bay and Hoi An’s lantern-lit nights.',  current_date(), 'public'),
(19, 'Northern Lights in Norway', 'Chasing the aurora borealis in Tromsø while experiencing Arctic landscapes and Sami culture.',  current_date(), 'public'),
(21, 'Safari in Kenya', 'Tracking lions, elephants, and rhinos in the Maasai Mara, and learning about local conservation efforts.',  current_date(), 'public'),
(23, 'Solo Trip to Iceland', 'Driving the Ring Road, soaking in the Blue Lagoon, and hiking glaciers in a land of fire and ice.',  current_date(), 'public'),
(23, 'Cycling Across Europe', 'From Amsterdam’s canals to the vineyards of Bordeaux, covering thousands of kilometres on two wheels.',  current_date(), 'public'),
(23, 'Mystical Temples of Cambodia', 'Exploring the ancient wonders of Angkor Wat at sunrise and wandering through jungle-clad ruins.',  current_date(), 'private'),
(23, 'New York City Getaway', 'A weekend filled with Broadway shows, skyline views from the Empire State Building, and Central Park strolls.',  current_date(), 'private');

-- Populate the 'events' table
INSERT INTO `events` (`journey_id`, `event_title`, `event_description`, `start_date`, `end_date`, `event_location`,`event_image`) VALUES
(1, 'Flight NZ5373 Wellington to Christchurch', 'Add a description here', CURRENT_TIMESTAMP, NULL, 'Wellington', NULL),
(1, 'Stay at Lincoln Motel', 'Add a description here', CURRENT_TIMESTAMP, NULL, 'Lincoln', NULL),
(1, 'Panino at River Market', 'Add a description here', CURRENT_TIMESTAMP, NULL,'Christchurch', NULL),
(1, 'Coffee in town', 'Add a description here', CURRENT_TIMESTAMP, NULL, 'Christchurch', NULL),
(1, 'Dinner at the Univeristy recreation centre', 'Add a description here', CURRENT_TIMESTAMP, NULL, 'Lincoln', NULL),
(1, 'Workshop at Lincoln University', 'First day of the COMP639 workshop, hands-on coding and collaboration.', CURRENT_TIMESTAMP, NULL, 'Lincoln', NULL),
(1, 'Networking Dinner at Lincoln Motel', 'Dinner with fellow students and professors at Lincoln Motel to discuss the workshop project.', CURRENT_TIMESTAMP, NULL, 'Lincoln', NULL),
(1, 'Exploring Lincoln', 'An afternoon tour around Lincoln University and the nearby countryside.', CURRENT_TIMESTAMP, NULL, 'Lincoln', NULL),
(1, 'Return Flight to Wellington', 'Flying back to Wellington after the workshop concluded.', CURRENT_TIMESTAMP, NULL, 'Lincoln', NULL),

(2, 'Arrival at Gold Coast', 'Checking in at the resort and exploring the beachside.', CURRENT_TIMESTAMP, NULL, 'Gold Coast', NULL),
(2, 'Dinner at Surfers Paradise', 'Enjoying a seafood feast at a beachfront restaurant in Surfers Paradise.', CURRENT_TIMESTAMP, NULL, 'Gold Coast', NULL),
(2, 'Morning Jog by the Beach', 'Starting the day with a refreshing jog along the Gold Coast beaches.', CURRENT_TIMESTAMP, NULL, 'Gold Coast', NULL),
(2, 'Visit to Currumbin Wildlife Sanctuary', 'Exploring the wildlife sanctuary and learning about native animals.', CURRENT_TIMESTAMP, NULL, 'Gold Coast', NULL),
(2, 'Surfing Lesson at Burleigh Heads', 'Taking a surfing lesson at Burleigh Heads, one of the Gold Coast’s iconic surf spots.', CURRENT_TIMESTAMP, NULL, 'Gold Coast', NULL),

(3, 'Reunion at Seoul Station', 'Arriving at Seoul Station to meet family for the 2025 reunion.', CURRENT_TIMESTAMP, NULL, 'Seoul', NULL),
(3, 'Lunch at Gwangjang Market', 'Sampling traditional Korean street food at the famous Gwangjang Market.', CURRENT_TIMESTAMP, NULL, 'Seoul', NULL),
(3, 'Visit to Gyeongbokgung Palace', 'Exploring the ancient Gyeongbokgung Palace, a symbol of Korean heritage.', CURRENT_TIMESTAMP, NULL, 'Seoul', NULL),
(3, 'Family BBQ in Namsan Park', 'A family gathering for a BBQ in the scenic Namsan Park.', CURRENT_TIMESTAMP, NULL, 'Seoul', NULL),
(3, 'Night Tour of Bukchon Hanok Village', 'Exploring the traditional Korean houses of Bukchon Hanok Village by night.', CURRENT_TIMESTAMP, NULL, 'Seoul', NULL),

(4, 'Arrival in Rome', 'Arriving in Rome and checking in to the hotel near the Colosseum.', CURRENT_TIMESTAMP, NULL, 'Rome', NULL),
(4, 'Visit to the Colosseum', 'A guided tour of the iconic Colosseum, learning about ancient Roman history.', CURRENT_TIMESTAMP, NULL, 'Rome', NULL),
(4, 'Pasta Cooking Class in Trastevere', 'Taking part in a local pasta cooking class in the Trastevere district.', CURRENT_TIMESTAMP, NULL, 'Rome', NULL),
(4, 'Exploring the Amalfi Coast', 'Driving along the Amalfi Coast, visiting Positano and Ravello.', CURRENT_TIMESTAMP, NULL, 'Amalfi Coast', NULL),
(4, 'Sunset at Sant’Angelo Castle', 'Watching the sunset from Sant’Angelo Castle with a view of the Tiber River.', CURRENT_TIMESTAMP, NULL, 'Rome', NULL),

(5, 'Arrival at the Inca Trail', 'Starting the journey to hike the Inca Trail to Machu Picchu.', CURRENT_TIMESTAMP, NULL, 'Cusco', NULL),
(5, 'Day 1: Inca Trail Hike', 'Trekking through the Sacred Valley and encountering Inca ruins along the way.', CURRENT_TIMESTAMP, NULL, 'Inca Trail', NULL),
(5, 'Camp at Wayllabamba', 'Camping in the valley of Wayllabamba after a day of hiking.', CURRENT_TIMESTAMP, NULL, 'Inca Trail', NULL),
(5, 'Day 2: Summit of Dead Woman’s Pass', 'Reaching the highest point on the trail at Dead Woman’s Pass.', CURRENT_TIMESTAMP, NULL, 'Inca Trail', NULL),
(5, 'Arrival at Machu Picchu', 'Witnessing the sunrise over Machu Picchu after completing the Inca Trail.', CURRENT_TIMESTAMP, NULL, 'Machu Picchu', NULL),

(6, 'Arrival in Tokyo', 'Landing in Tokyo and heading to the hotel for the Sakura season.', CURRENT_TIMESTAMP, NULL, 'Tokyo', NULL),
(6, 'Hanami Picnic at Ueno Park', 'Spending the afternoon in Ueno Park, enjoying the cherry blossoms during hanami season.', CURRENT_TIMESTAMP, NULL, 'Tokyo', NULL),
(6, 'Visit to Kyoto’s Fushimi Inari Shrine', 'Exploring the famous red torii gates of Fushimi Inari Shrine.', CURRENT_TIMESTAMP, NULL, 'Kyoto', NULL),
(6, 'Tea Ceremony in Kyoto', 'Participating in a traditional Japanese tea ceremony in Kyoto.', CURRENT_TIMESTAMP, NULL, 'Kyoto', NULL),
(6, 'Exploring Arashiyama Bamboo Grove', 'Strolling through the iconic bamboo grove in Arashiyama, Kyoto.', CURRENT_TIMESTAMP, NULL, 'Kyoto', NULL),

(7, 'Arrival in Queenstown', 'Arriving in Queenstown, ready for a campervan adventure across the South Island.', CURRENT_TIMESTAMP, NULL, 'Queenstown', NULL),
(7, 'Exploring Fiordland National Park', 'A scenic drive through Fiordland’s fjords, stopping for short hikes and spectacular views.', CURRENT_TIMESTAMP, NULL, 'Fiordland', NULL),
(7, 'Wine Tasting in Central Otago', 'Tasting some of New Zealand’s finest wines in the picturesque vineyards of Central Otago.', CURRENT_TIMESTAMP, NULL, 'Central Otago', NULL),
(7, 'Christchurch Botanical Gardens', 'Exploring the lush gardens of Christchurch, a relaxing stop before heading back to the city.', CURRENT_TIMESTAMP, NULL, 'Christchurch', NULL),
(7, 'Drive to Akaroa', 'A scenic drive through the hills and along the coast to the quaint town of Akaroa.', CURRENT_TIMESTAMP, NULL, 'Akaroa', NULL),

(8, 'Arrival in Santorini', 'Landing in Santorini to explore its iconic blue domes and stunning caldera views.', CURRENT_TIMESTAMP, NULL, 'Santorini', NULL),
(8, 'Sunset at Oia', 'Watching the famous sunset from the town of Oia, known for its breathtaking views of the Aegean Sea.', CURRENT_TIMESTAMP, NULL, 'Oia', NULL),
(8, 'Beach Day at Red Beach', 'Relaxing at Santorini’s Red Beach, surrounded by dramatic red cliffs and crystal-clear waters.', CURRENT_TIMESTAMP, NULL, 'Santorini', NULL),
(8, 'Ferry to Mykonos', 'Taking a ferry to Mykonos for more island hopping and exploring the charming streets of Mykonos town.', CURRENT_TIMESTAMP, NULL, 'Mykonos', NULL),
(8, 'Nightlife in Mykonos', 'Exploring the vibrant nightlife of Mykonos, with beach clubs and bars by the sea.', CURRENT_TIMESTAMP, NULL, 'Mykonos', NULL),

(9, 'Arriving in Hanoi', 'Exploring the bustling streets of Hanoi, with its French colonial architecture and vibrant street food scene.', CURRENT_TIMESTAMP, NULL, 'Hanoi', NULL),
(9, 'Ha Long Bay Cruise', 'Sailing through the limestone karsts and emerald waters of Ha Long Bay on a traditional wooden boat.', CURRENT_TIMESTAMP, NULL, 'Ha Long Bay', NULL),
(9, 'Hoi An Lantern Festival', 'Wandering through the ancient town of Hoi An, lit by colourful lanterns during the monthly Lantern Festival.', CURRENT_TIMESTAMP, NULL, 'Hoi An', NULL),
(9, 'Visit to My Son Sanctuary', 'A day trip to the My Son Sanctuary, exploring the ancient Hindu temples hidden in the jungle.', CURRENT_TIMESTAMP, NULL, 'My Son', NULL),
(9, 'Cycling through the Mekong Delta', 'Cycling through the tranquil villages and rice paddies of the Mekong Delta.', CURRENT_TIMESTAMP, NULL, 'Mekong Delta', NULL),

(10, 'Arrival in Tromsø', 'Flying to Tromsø for a once-in-a-lifetime experience chasing the Northern Lights.', CURRENT_TIMESTAMP, NULL, 'Tromsø', NULL),
(10, 'Northern Lights Safari', 'Joining a guided tour to catch the aurora borealis in its full glory under the Arctic sky.', CURRENT_TIMESTAMP, NULL, 'Tromsø', NULL),
(10, 'Dog Sledding in the Arctic', 'Going on a thrilling dog sledding adventure across the snowy Arctic landscape.', CURRENT_TIMESTAMP, NULL, 'Tromsø', NULL),
(10, 'Visit to Sami Village', 'Spending a day learning about the Sami culture, including reindeer herding and traditional crafts.', CURRENT_TIMESTAMP, NULL, 'Tromsø', NULL),
(10, 'Midnight Sun at the Arctic Circle', 'Witnessing the stunning midnight sun from the Arctic Circle.', CURRENT_TIMESTAMP, NULL, 'Tromsø', NULL),

(11, 'Arrival at Maasai Mara', 'Landing at Maasai Mara and preparing for the safari adventure to see the “Big Five.”', CURRENT_TIMESTAMP, NULL, 'Maasai Mara', NULL),
(11, 'Morning Game Drive', 'An early morning game drive to catch the lions, elephants, and other animals during their most active time.', CURRENT_TIMESTAMP, NULL, 'Maasai Mara', NULL),
(11, 'Visit to a Maasai Village', 'Learning about the Maasai people, their traditions, and their role in local conservation efforts.', CURRENT_TIMESTAMP, NULL, 'Maasai Mara', NULL),
(11, 'Evening Sunset at the Mara', 'Watching the sunset over the savannah while enjoying a glass of wine.', CURRENT_TIMESTAMP, NULL, 'Maasai Mara', NULL),
(11, 'Safari Balloon Ride', 'Taking a hot air balloon ride over the Maasai Mara, offering an aerial view of wildlife and the landscape.', CURRENT_TIMESTAMP, NULL, 'Maasai Mara', NULL),

(12, 'Arrival in Reykjavik', 'Landing in Reykjavik and preparing for a road trip along Iceland’s famous Ring Road.', CURRENT_TIMESTAMP, NULL, 'Reykjavik', NULL),
(12, 'Visit to the Blue Lagoon', 'Soaking in the hot, mineral-rich waters of the Blue Lagoon, one of Iceland’s most famous spas.', CURRENT_TIMESTAMP, NULL, 'Reykjavik', NULL),
(12, 'Golden Circle Tour', 'Exploring the Golden Circle, including Þingvellir National Park, Gullfoss Waterfall, and Geysir Hot Springs.', CURRENT_TIMESTAMP, NULL, 'Golden Circle', NULL),
(12, 'Hike on Sólheimajökull Glacier', 'Trekking across the Sólheimajökull Glacier, one of Iceland’s many beautiful glaciers.', CURRENT_TIMESTAMP, NULL, 'Sólheimajökull', NULL),
(12, 'Exploring Vatnajökull National Park', 'Discovering the immense Vatnajökull National Park, home to waterfalls, glaciers, and rugged landscapes.', CURRENT_TIMESTAMP, NULL, 'Vatnajökull', NULL),

(13, 'Cycling in Amsterdam', 'Exploring the canals and parks of Amsterdam by bike, the best way to see the city.', CURRENT_TIMESTAMP, NULL, 'Amsterdam', NULL),
(13, 'Vineyard Tour in Bordeaux', 'Cycling through the vineyards of Bordeaux, tasting local wines along the way.', CURRENT_TIMESTAMP, NULL, 'Bordeaux', NULL),
(13, 'Historic Sites in Paris', 'Cycling through the heart of Paris, stopping at landmarks like the Eiffel Tower and the Louvre.', CURRENT_TIMESTAMP, NULL, 'Paris', NULL),
(13, 'Cycling in the Swiss Alps', 'Riding through the picturesque landscapes of the Swiss Alps, enjoying the mountain views.', CURRENT_TIMESTAMP, NULL, 'Swiss Alps', NULL),
(13, 'Arrival in Venice', 'Arriving in Venice to finish the cycling journey with a scenic ride through this iconic city.', CURRENT_TIMESTAMP, NULL, 'Venice', NULL),

(14, 'Exploring Angkor Wat at Sunrise', 'Arriving early to witness the stunning sunrise over the ancient Angkor Wat temple.', CURRENT_TIMESTAMP, NULL, 'Angkor Wat', NULL),
(14, 'Temple Exploration in Angkor Thom', 'Wandering through the temples of Angkor Thom, including the famous Bayon Temple with its massive stone faces.', CURRENT_TIMESTAMP, NULL, 'Angkor Thom', NULL),
(14, 'Visit to Ta Prohm', 'Exploring the roots of giant trees growing over the ruins of Ta Prohm, one of Cambodia’s most iconic temples.', CURRENT_TIMESTAMP, NULL, 'Ta Prohm', NULL),
(14, 'Mysterious Banteay Srei Temple', 'Exploring the intricate carvings at Banteay Srei, known as the "Pink Temple."', CURRENT_TIMESTAMP, NULL, 'Banteay Srei', NULL),
(14, 'Boat Ride on Tonle Sap Lake', 'Taking a boat ride on Tonle Sap Lake to see the floating villages and observe local life.', CURRENT_TIMESTAMP, NULL, 'Tonle Sap Lake', NULL),

(15, 'Arrival in New York', 'Landing in New York City and preparing for an exciting weekend getaway.', CURRENT_TIMESTAMP, NULL, 'New York', NULL),
(15, 'Broadway Show', 'Enjoying a world-famous Broadway show in the heart of the Theatre District.', CURRENT_TIMESTAMP, NULL, 'New York', NULL),
(15, 'Central Park Stroll', 'Taking a leisurely walk through Central Park, relaxing amidst the bustling city.', CURRENT_TIMESTAMP, NULL, 'New York', NULL),
(15, 'Empire State Building Observation', 'Visiting the Empire State Building to enjoy breathtaking views of the city skyline.', CURRENT_TIMESTAMP, NULL, 'New York', NULL),
(15, 'Shopping on 5th Avenue', 'Spending the afternoon shopping along New York’s iconic 5th Avenue.', CURRENT_TIMESTAMP, NULL, 'New York', NULL);