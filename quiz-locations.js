/**
 * Franchise 101 - Smart Cascading Location Dropdowns (State -> District -> City)
 * Supports all Indian States & Union Territories with top business micro-markets
 * and seamless fallback to custom locality typing.
 */

window.quizLocationData = {
  "Maharashtra": {
    "Pune": [
      "Pune City (Central / Shivajinagar / FC Road)",
      "Kothrud & Karve Nagar",
      "Baner & Balewadi (High Street)",
      "Hinjawadi IT Park (Phases 1, 2, 3)",
      "Viman Nagar & Kalyani Nagar",
      "Wakad & Pimple Saudagar",
      "Hadapsar & Magarpatta City",
      "Kharadi & Chandan Nagar (EON Free Zone)",
      "Aundh & Pashan",
      "Pimpri & Chinchwad MIDC",
      "Camp & MG Road / East Street",
      "Bavdhan & Chandani Chowk",
      "Sinhagad Road & Dhayari",
      "Nigdi, Ravet & Akurdi",
      "Kondhwa, Undri & NIBM Road",
      "Dhanori & Vishrantwadi",
      "Baramati",
      "Shirur & Ranjangaon MIDC",
      "Lonavala & Talegaon Dabhade",
      "Chakan MIDC & Alandi"
    ],
    "Mumbai City (South Mumbai)": [
      "Colaba & Cuffe Parade",
      "Fort, Fountain & Kala Ghoda",
      "Marine Lines & Churchgate",
      "Nariman Point",
      "Lower Parel & Phoenix Mills",
      "Worli & Prabhadevi",
      "Dadar & Shivaji Park",
      "Byculla & Mazgaon",
      "Tardeo & Mumbai Central"
    ],
    "Mumbai Suburban": [
      "Bandra West (Linking Rd / Hill Rd / Pali Hill)",
      "Bandra Kurla Complex (BKC)",
      "Andheri West (Lokhandwala / Versova)",
      "Andheri East (MIDC / Chakala / Marol)",
      "Juhu & Vile Parle West",
      "Powai (Hiranandani Gardens)",
      "Goregaon West & East",
      "Malad (Link Road / Mindspace / Inorbit)",
      "Borivali & Kandivali",
      "Ghatkopar (R-City Mall / Station Area)",
      "Chembur & Tilak Nagar",
      "Kurla & Phoenix Marketcity",
      "Mulund & Bhandup",
      "Santacruz & Khar West"
    ],
    "Thane": [
      "Thane West (Ghodbunder Road / Majiwada)",
      "Thane East & Naupada",
      "Navi Mumbai - Vashi & Palm Beach Road",
      "Navi Mumbai - Nerul, Belapur & Seawoods",
      "Navi Mumbai - Airoli, Mahape & Kopar Khairane",
      "Navi Mumbai - Kharghar & Panvel Zone",
      "Kalyan & Dombivli",
      "Mira-Bhayandar",
      "Ulhasnagar & Ambernath",
      "Bhiwandi",
      "Badlapur"
    ],
    "Nagpur": [
      "Nagpur City (Central / Sitabuldi)",
      "Dharampeth, Ramdaspeth & Gokulpeth",
      "Sadar & Civil Lines",
      "Wardhaman Nagar & Lakadganj",
      "Pratap Nagar, Trimurti Nagar & Khamla",
      "Manish Nagar & Besa",
      "Hingna MIDC & MIHAN IT SEZ"
    ],
    "Nashik": [
      "College Road & Gangapur Road",
      "Panchavati & Old Nashik",
      "Indira Nagar & Mumbai Naka",
      "Deolali Camp & Nashik Road",
      "Satpur MIDC & Ambad MIDC",
      "Pathardi Phata & Govind Nagar"
    ],
    "Chhatrapati Sambhajinagar (Aurangabad)": [
      "Aurangabad City Centre & Nirala Bazar",
      "CIDCO & Cannaught Place",
      "Waluj MIDC & Shendra DMIC",
      "Railway Station & Jalna Road",
      "Beed Bypass & Garkheda"
    ],
    "Kolhapur": [
      "Kolhapur City (Mahalaxmi Area)",
      "Rajarampuri & Shahupuri",
      "Tarabai Park & Nagala Park",
      "Shiroli & Gokul Shirgaon MIDC"
    ],
    "Solapur": [
      "Solapur City Centre",
      "Hotgi Road & Saat Rasta",
      "Old Pune Naka",
      "Barshi",
      "Pandharpur"
    ],
    "Satara": [
      "Satara City & Powai Naka",
      "Karad",
      "Wai",
      "Mahabaleshwar & Panchgani",
      "Phaltan"
    ],
    "Sangli": [
      "Sangli City & Vishrambag",
      "Miraj & Mission Hospital Area",
      "Kupwad MIDC",
      "Islampur"
    ],
    "Ahilyanagar (Ahmednagar)": [
      "Ahmednagar City & Savedi",
      "Shirdi (Temple Zone & Commercial)",
      "Kopargaon & Rahata",
      "Sangamner"
    ],
    "Raigad": [
      "Panvel City & New Panvel",
      "Kharghar (Raigad jurisdiction)",
      "Alibag",
      "Khopoli & Pen",
      "Karjat",
      "Roha & Mahad MIDC"
    ],
    "Palghar": [
      "Vasai West & East",
      "Virar West & East",
      "Palghar City",
      "Boisar MIDC & Tarapur",
      "Dahanu"
    ],
    "Amravati": [
      "Amravati City",
      "Badnera",
      "Achalpur"
    ],
    "Jalgaon": [
      "Jalgaon City",
      "Bhusawal",
      "Chalisgaon",
      "Amalner"
    ],
    "Nanded": [
      "Nanded City",
      "CIDCO Nanded",
      "Degloor"
    ],
    "Latur": [
      "Latur City",
      "Ausa",
      "Udgir"
    ],
    "Dhule": [
      "Dhule City",
      "Shirpur",
      "Dondaicha"
    ],
    "Akola": [
      "Akola City",
      "Murtizapur",
      "Akot"
    ],
    "Chandrapur": [
      "Chandrapur City",
      "Ballarpur",
      "Warora"
    ],
    "Ratnagiri": [
      "Ratnagiri City",
      "Chiplun",
      "Khed"
    ],
    "Sindhudurg": [
      "Kudal",
      "Kankavli",
      "Sawantwadi",
      "Malvan"
    ],
    "Beed": [
      "Beed City",
      "Parli Vaijnath",
      "Ambejogai"
    ],
    "Jalna": [
      "Jalna City",
      "Partur",
      "Ambad MIDC"
    ],
    "Parbhani": [
      "Parbhani City",
      "Gangakhed",
      "Jintur"
    ],
    "Dharashiv (Osmanabad)": [
      "Dharashiv City",
      "Tuljapur",
      "Omerga"
    ],
    "Yavatmal": [
      "Yavatmal City",
      "Pusad",
      "Umarkhed"
    ],
    "Wardha": [
      "Wardha City",
      "Hinganghat",
      "Arvi"
    ],
    "Bhandara": [
      "Bhandara City",
      "Tumsar",
      "Sakoli"
    ],
    "Gondia": [
      "Gondia City",
      "Tirora"
    ],
    "Buldhana": [
      "Buldhana City",
      "Khamgaon",
      "Shegaon"
    ],
    "Washim": [
      "Washim City",
      "Karanja Lad",
      "Risod"
    ],
    "Hingoli": [
      "Hingoli City",
      "Basmath"
    ],
    "Nandurbar": [
      "Nandurbar City",
      "Navapur",
      "Shahada"
    ],
    "Gadchiroli": [
      "Gadchiroli City",
      "Aheri"
    ]
  },
  "Delhi NCR": {
    "New Delhi": [
      "Connaught Place (CP) & Barakhamba",
      "Chanakyapuri & Khan Market",
      "Gol Market & Bengali Market",
      "Lutyens Delhi & Mandi House"
    ],
    "South Delhi": [
      "Saket & Select Citywalk Mall",
      "Hauz Khas, Green Park & Safdarjung",
      "Greater Kailash 1 & Greater Kailash 2 (M-Block)",
      "South Extension 1 & 2",
      "Defence Colony & Lajpat Nagar (Central Market)",
      "Vasant Kunj (Promenade / Ambience Mall) & Vasant Vihar",
      "Malviya Nagar & Shivalik",
      "Nehru Place & Kalkaji",
      "CR Park & Alaknanda"
    ],
    "North Delhi": [
      "Civil Lines & Delhi University North Campus",
      "Rohini (Sectors 7, 8, 9, 10, 11, 24)",
      "Pitampura & Netaji Subhash Place (NSP)",
      "Model Town & Gujranwala Town",
      "Kamla Nagar & Roop Nagar",
      "Ashok Vihar & Shalimar Bagh"
    ],
    "West Delhi": [
      "Rajouri Garden & Subhash Nagar",
      "Janakpuri (District Centre) & Tilak Nagar",
      "Punjabi Bagh (Club Road) & Paschim Vihar",
      "Patel Nagar & Kirti Nagar",
      "Dwarka (Sectors 6, 7, 10, 11, 12, 21)",
      "Uttam Nagar & Vikaspuri"
    ],
    "East Delhi": [
      "Mayur Vihar (Phases 1, 2, 3)",
      "Laxmi Nagar & Shakarpur",
      "Preet Vihar & Nirman Vihar",
      "Anand Vihar & IP Extension",
      "Shahdara & Dilshad Garden"
    ],
    "Central Delhi": [
      "Karol Bagh & Gaffar Market",
      "Rajendra Nagar & Pusa Road",
      "Paharganj & Daryaganj",
      "Chandni Chowk & Old Delhi"
    ],
    "Gurugram (Gurgaon)": [
      "Cyber City & DLF Cyber Hub",
      "Golf Course Road & One Horizon Area",
      "Golf Course Extension Road (Sectors 56 to 65)",
      "Sohna Road & Sector 48/49",
      "Sector 29 & Leisure Valley (F&B Hub)",
      "MG Road & IFFCO Chowk",
      "Sushant Lok & South City",
      "New Gurgaon (Sectors 82 to 95)",
      "Manesar & IMT Industrial Hub"
    ],
    "Noida": [
      "Sector 18 (Atta Market / Mall of India)",
      "Sector 62 & 63 (Commercial / IT Hub)",
      "Noida Expressway (Sectors 128 to 144)",
      "Sector 74 to 78 (High-density Residential Hub)",
      "Sector 50 & 51",
      "Sector 104 & Hazipur (Boutique High Street)",
      "Sector 137 & Advant Navis Park Area"
    ],
    "Greater Noida": [
      "Greater Noida (Pari Chowk & Alpha/Beta/Gamma)",
      "Greater Noida West (Noida Extension)",
      "Knowledge Park (Colleges / Corporate Hub)",
      "Yamuna Expressway & Jewar Airport Corridor"
    ],
    "Ghaziabad": [
      "Indirapuram (Vaibhav Khand / Shipra Mall Area)",
      "Vaishali & Kaushambi",
      "Raj Nagar & Raj Nagar Extension",
      "Vasundhara",
      "Crossings Republik",
      "Ghaziabad Old City & GT Road"
    ],
    "Faridabad": [
      "Faridabad NIT (1, 2, 3, 5)",
      "Sector 15 & Sector 16 Market",
      "Mathura Road & Metro Corridor",
      "Greenfield Colony & Surajkund",
      "Greater Faridabad (Neharpar Sectors 79 to 88)"
    ]
  },
  "Karnataka": {
    "Bengaluru Urban": [
      "Koramangala (All Blocks)",
      "Indiranagar & 100ft Road / 12th Main",
      "HSR Layout (Sectors 1 to 7)",
      "Whitefield & ITPL Main Road",
      "Jayanagar (3rd, 4th, 9th Block)",
      "JP Nagar (Phases 1 to 7)",
      "MG Road, Brigade Road & Church Street",
      "Electronic City (Phases 1 & 2)",
      "Hebbal & Manyata Tech Park Area",
      "Malleshwaram & Rajajinagar (Orion Mall Area)",
      "Marathahalli & Bellandur Outer Ring Road",
      "Banashankari & Basavanagudi (Gandhi Bazaar)",
      "Sarjapur Road & Carmelaram",
      "Kalyan Nagar & Kammanahalli (HRBR Layout)",
      "Yelahanka & Sahakara Nagar",
      "BTM Layout & Bannerghatta Road",
      "Kengeri & Mysore Road",
      "Nagavara, Hennur & Thanisandra"
    ],
    "Bengaluru Rural": [
      "Devanahalli & Airport Road Corridor",
      "Doddaballapur",
      "Hosakote Industrial Area",
      "Nelamangala"
    ],
    "Mysuru (Mysore)": [
      "Mysuru City Centre (Devaraja / Sayyaji Rao Rd)",
      "Jayalakshmipuram & Gokulam",
      "Vijayanagar Mysuru",
      "Saraswathipuram & Kuvempunagar",
      "Hebbal Industrial Area Mysuru"
    ],
    "Mangaluru (Mangalore)": [
      "Mangaluru City Centre (Hampankatta)",
      "Kadri, Bejai & Lalbagh",
      "Balmatta & Bendoorwell",
      "Surathkal & NITK Area"
    ],
    "Belagavi (Belgaum)": [
      "Belagavi City Centre & Khade Bazar",
      "Tilakwadi & Congress Road",
      "Udyambag & Khanapur Road"
    ],
    "Hubballi-Dharwad": [
      "Hubballi Vidyanagar & Shirur Park",
      "Hubballi Gokul Road & Koppikar Road",
      "Dharwad City Centre & Jubilee Circle"
    ],
    "Kalaburagi (Gulbarga)": [
      "Kalaburagi City",
      "Sedam Road",
      "Super Market"
    ],
    "Davanagere": [
      "Davanagere City",
      "MCC B Block",
      "Vidyanagar"
    ],
    "Ballari (Bellary)": [
      "Ballari City",
      "Cantonment",
      "Infantry Road"
    ],
    "Shivamogga (Shimoga)": [
      "Shivamogga City",
      "Durgigudi",
      "Vinobhanagar"
    ],
    "Tumakuru (Tumkur)": [
      "Tumakuru City",
      "Kyatsandra",
      "SIT Main Road"
    ],
    "Udupi": [
      "Udupi City Centre",
      "Manipal University Campus Zone",
      "Malpe",
      "Kundapura"
    ],
    "Other Karnataka Districts": [
      "Chikkamagaluru",
      "Hassan",
      "Mandya",
      "Kodagu (Coorg / Madikeri)",
      "Chitradurga",
      "Kolar & KGF",
      "Chikkaballapur",
      "Bidar",
      "Raichur",
      "Koppal",
      "Gadag",
      "Haveri",
      "Uttara Kannada (Karwar / Sirsi)",
      "Bagalkot",
      "Vijayapura (Bijapur)",
      "Chamarajanagar",
      "Yadgir",
      "Ramanagara",
      "Vijayanagara (Hosapete)"
    ]
  },
  "Gujarat": {
    "Ahmedabad": [
      "SG Highway & Prahlad Nagar",
      "Bodakdev, Vastrapur & Judges Bungalow Rd",
      "Satellite, Jodhpur & Shivranjani",
      "CG Road & Navrangpura",
      "Sindhu Bhavan Road (SBR) - Prime High Street",
      "Bopal & South Bopal (SP Ring Road)",
      "Maninagar, Kankaria & Isanpur",
      "Gota, Chandkheda & Motera",
      "Naroda, Nikol & Odhav",
      "Ashram Road & Usmanpura",
      "Science City Road & Sola"
    ],
    "Surat": [
      "Athwa, Athwagate & Ghod Dod Road",
      "Vesu, VIP Road & University Area",
      "Adajan & Pal-Hazira Road",
      "Varachha & Mini Bazaar (Diamond Zone)",
      "Piplod & Dumas Road (Mall Corridor)",
      "Citylight & Althan",
      "Katargam & Ved Road"
    ],
    "Vadodara (Baroda)": [
      "Alkapuri & RC Dutt Road",
      "Sayajigunj & Fatehgunj",
      "Gotri, Sevasi & Vasna Road",
      "Manjalpur & Makarpura",
      "Karelibaug & VIP Road Vadodara",
      "Akota & Old Padra Road",
      "Waghodia Road & Harni"
    ],
    "Rajkot": [
      "Kalawad Road & Amin Marg",
      "Yagnik Road & Dr. Yagnik Road",
      "University Road Rajkot",
      "150 Feet Ring Road & Nana Mava",
      "Kotecha Chowk & Tagor Road"
    ],
    "Gandhinagar": [
      "Infocity & GIFT City (Fintech Hub)",
      "Kudasan, Raysan & PDPU Road",
      "Sargasan & Urjanagar",
      "Sector 11, 16 & 21 (Civic Heart)"
    ],
    "Bhavnagar": [
      "Bhavnagar City",
      "Waghawadi Road",
      "Kalanala & Crescent"
    ],
    "Jamnagar": [
      "Jamnagar City",
      "Digvijay Plot",
      "Patel Colony & Indira Marg"
    ],
    "Anand": [
      "Anand City",
      "Vallabh Vidyanagar (V.V. Nagar)",
      "Amul Dairy Road"
    ],
    "Bharuch": [
      "Bharuch City",
      "Ankleshwar GIDC",
      "Zadeshwar Road"
    ],
    "Valsad / Vapi": [
      "Vapi GIDC & Daman Road",
      "Valsad City & Tithal Road",
      "Silvassa Corridor"
    ],
    "Other Gujarat Districts": [
      "Navsari",
      "Mehsana",
      "Patan",
      "Banaskantha (Palanpur)",
      "Sabarkantha (Himmatnagar)",
      "Kutch (Bhuj / Gandhidham / Kandla)",
      "Junagadh",
      "Amreli",
      "Porbandar",
      "Surendranagar",
      "Morbi (Ceramic Hub)",
      "Panchmahal (Godhra)",
      "Dahod",
      "Kheda (Nadiad)",
      "Narmada",
      "Tapi",
      "Aravalli",
      "Botad",
      "Chhota Udaipur",
      "Devbhoomi Dwarka",
      "Gir Somnath (Veraval)",
      "Mahisagar"
    ]
  },
  "Telangana": {
    "Hyderabad": [
      "Banjara Hills (Roads 1 to 14)",
      "Jubilee Hills (Roads 36 & 45)",
      "Gachibowli & Financial District (Nanakramguda)",
      "HITEC City & Madhapur (Cyber Towers / Inorbit)",
      "Kondapur, Hafeezpet & Miyapur",
      "Kukatpally & KPHB Colony",
      "Begumpet & Somajiguda",
      "Secunderabad & West Marredpally",
      "Ameerpet & SR Nagar",
      "Dilsukhnagar & LB Nagar",
      "Himayatnagar, Narayanaguda & Basheerbagh",
      "Mehdipatnam & Tolichowki",
      "Attapur & Rajendranagar",
      "Uppal & Nagole",
      "Kompally & Suchitra"
    ],
    "Rangareddy": [
      "Manikonda & Puppalguda",
      "Narsingi, Kokapet & Gandipet",
      "Shamshabad (Airport Zone)",
      "Shadnagar"
    ],
    "Medchal-Malkajgiri": [
      "Kompally",
      "Malkajgiri & Alwal",
      "ECIL & Kapra",
      "Medchal Town"
    ],
    "Warangal / Hanamkonda": [
      "Hanamkonda Subedari & Chowrasta",
      "Warangal City & Station Road",
      "Kazipet"
    ],
    "Nizamabad": [
      "Nizamabad City",
      "Khaleelwadi",
      "Bodhan"
    ],
    "Karimnagar": [
      "Karimnagar City",
      "Mukarampura",
      "Collectorate Road"
    ],
    "Khammam": [
      "Khammam City",
      "Wyra Road",
      "Mamillagudem"
    ],
    "Other Telangana Districts": [
      "Siddipet",
      "Mahabubnagar",
      "Nalgonda",
      "Suryapet",
      "Adilabad",
      "Mancherial",
      "Jagtial",
      "Kamareddy",
      "Sangareddy",
      "Wanaparthy",
      "Bhadradri Kothagudem",
      "Peddapalli (Ramagundam)",
      "Vikrabad",
      "Medak"
    ]
  },
  "Tamil Nadu": {
    "Chennai": [
      "Anna Nagar (2nd Avenue / Shanthi Colony)",
      "T. Nagar & Pondy Bazaar (Shopping Capital)",
      "Adyar, Besant Nagar & Thiruvanmiyur",
      "Velachery (Phoenix Marketcity Area)",
      "Alwarpet, Mylapore & Mandaveli",
      "Nungambakkam & Khader Nawaz Khan Road",
      "OMR IT Expressway (Kandanchavadi to Sholinganallur)",
      "Porur, Ramapuram & DLF IT Park",
      "Guindy, Saidapet & Little Mount",
      "Tambaram, Chromepet & Pallavaram",
      "Kilpauk & Kellys",
      "Perambur & Kolathur",
      "Egmore & Central Area"
    ],
    "Coimbatore": [
      "RS Puram & DB Road",
      "Peelamedu & Avinashi Road",
      "Gandhipuram & Cross Cut Road",
      "Saibaba Colony & NSR Road",
      "Saravanampatti (IT Corridor)",
      "Race Course & Trichy Road"
    ],
    "Madurai": [
      "Madurai City",
      "Anna Nagar Madurai",
      "KK Nagar Madurai",
      "SS Colony & Bypass Road"
    ],
    "Tiruchirappalli (Trichy)": [
      "Thillai Nagar",
      "Cantonment Trichy",
      "Srirangam",
      "Main Guard Gate"
    ],
    "Salem": [
      "Salem City",
      "Fairlands",
      "Four Roads",
      "Suramangalam"
    ],
    "Tiruppur": [
      "Tiruppur City",
      "Kumaran Road",
      "Avinashi Road Tiruppur"
    ],
    "Erode": [
      "Erode City",
      "Perundurai Road",
      "Brough Road"
    ],
    "Vellore": [
      "Vellore City",
      "Katpadi & VIT Area",
      "Gandhinagar Vellore"
    ],
    "Other Tamil Nadu Districts": [
      "Kanchipuram",
      "Chengalpattu",
      "Tiruvallur",
      "Cuddalore",
      "Thanjavur",
      "Dindigul",
      "Tirunelveli",
      "Thoothukudi (Tuticorin)",
      "Kanyakumari (Nagercoil)",
      "Karur",
      "Namakkal",
      "Dharmapuri",
      "Krishnagiri (Hosur Industrial Hub)",
      "Nilgiris (Ooty / Coonoor)",
      "Pudukkottai",
      "Ramanathapuram",
      "Sivaganga (Karaikudi)",
      "Tenkasi",
      "Theni",
      "Tirupathur",
      "Tiruvarur",
      "Ranipet",
      "Kallakurichi",
      "Mayiladuthurai",
      "Nagapattinam"
    ]
  },
  "Uttar Pradesh": {
    "Lucknow": [
      "Hazratganj & Janpath Market",
      "Gomti Nagar (Patrakar Puram / Vivek Khand)",
      "Gomti Nagar Extension & Shaheed Path",
      "Alambagh & Phoenix United Mall Area",
      "Indira Nagar & Munshi Pulia",
      "Mahanagar & Kapoorthala",
      "Aliganj & Engineering College Chauraha",
      "Ashiyana & Bangla Bazar",
      "Vibhuti Khand (Corporate Hub)"
    ],
    "Kanpur": [
      "Swaroop Nagar & Arya Nagar",
      "Civil Lines Kanpur & Mall Road",
      "Kakadeo (Coaching Hub) & Sharda Nagar",
      "Kidwai Nagar & Govind Nagar",
      "Lajpat Nagar & Gumti No. 5"
    ],
    "Gautam Buddha Nagar (Noida / Gr Noida)": [
      "Noida Sector 18 & Atta",
      "Noida Sector 62 & 63",
      "Noida Expressway Corridor",
      "Greater Noida Pari Chowk & Alpha/Beta",
      "Greater Noida West (Noida Extension)"
    ],
    "Ghaziabad": [
      "Indirapuram",
      "Vaishali & Kaushambi",
      "Raj Nagar & Raj Nagar Extension",
      "Vasundhara",
      "Crossings Republik"
    ],
    "Agra": [
      "Sanjay Place (Commercial Centre)",
      "Fatehabad Road & Tajganj",
      "Kamla Nagar & Dayal Bagh",
      "Civil Lines Agra"
    ],
    "Varanasi": [
      "Sigra & Mahmoorganj",
      "Bhelupur, Lanka & BHU Area",
      "Cantonment Varanasi",
      "Godowlia & Dashashwamedh"
    ],
    "Prayagraj (Allahabad)": [
      "Civil Lines Prayagraj",
      "Katra & University Area",
      "Georgetown & Ashok Nagar"
    ],
    "Meerut": [
      "Meerut Cantt & Abu Lane",
      "Shastri Nagar Meerut & Mangal Pandey Nagar",
      "Modipuram & Delhi Road"
    ],
    "Bareilly": [
      "Civil Lines Bareilly",
      "Rajendra Nagar",
      "DD Puram & Stadium Road"
    ],
    "Aligarh": [
      "Civil Lines Aligarh",
      "Centre Point",
      "Ramghat Road"
    ],
    "Gorakhpur": [
      "Golghar & Park Road",
      "Civil Lines Gorakhpur",
      "Medical College Road"
    ],
    "Mathura": [
      "Mathura City",
      "Vrindavan (Chatikara / Bhaktivedanta Swami Marg)",
      "Highway Plaza Area"
    ],
    "Ayodhya": [
      "Ayodhya Dham / Ram Mandir Corridor",
      "Faizabad City",
      "Civil Lines Ayodhya"
    ],
    "Jhansi": [
      "Jhansi City",
      "Sadar Bazar",
      "Elite Crossing"
    ],
    "Other Uttar Pradesh Districts": [
      "Moradabad",
      "Saharanpur",
      "Firozabad",
      "Muzaffarnagar",
      "Budaun",
      "Rampur",
      "Shahjahanpur",
      "Farrukhabad",
      "Hapur",
      "Bulandshahr",
      "Sambhal",
      "Amroha",
      "Hardoi",
      "Fatehpur",
      "Raebareli",
      "Orai (Jalaun)",
      "Sitapur",
      "Bahraich",
      "Unnao",
      "Jaunpur",
      "Lakhimpur Kheri",
      "Hathras",
      "Banda",
      "Pilibhit",
      "Barabanki",
      "Basti",
      "Gonda",
      "Mirzapur",
      "Azamgarh",
      "Deoria",
      "Mau",
      "Ballia",
      "Bhadohi",
      "Chandauli",
      "Ghazipur",
      "Sonbhadra",
      "Kasganj",
      "Amethi",
      "Sultanpur",
      "Lalitpur",
      "Mainpuri",
      "Kannauj",
      "Etawah",
      "Auraiya"
    ]
  },
  "Rajasthan": {
    "Jaipur": [
      "C-Scheme & MI Road",
      "Malviya Nagar, Gaurav Tower & WTP Area",
      "Vaishali Nagar & Queens Road",
      "Raja Park & Tilak Nagar",
      "Mansarovar (VT Road / Madhyam Marg)",
      "Tonk Road, Durgapura & Gopalpura Bypass",
      "Jagatpura & Pratap Nagar",
      "Ajmer Road, Sodala & Shyam Nagar",
      "Bani Park & Station Road"
    ],
    "Jodhpur": [
      "Sardarpura (B/C Road)",
      "Ratanada & Circuit House Road",
      "Shastri Nagar Jodhpur",
      "Paota & Mandore Road"
    ],
    "Udaipur": [
      "Panchwati, Sukhadia Circle & Saheli Nagar",
      "Fatehpura & Old Fatehpura",
      "Hiran Magri (Sectors 3, 4, 11, 14)",
      "Bapu Bazaar & Delhi Gate",
      "Celebration Mall Area (Bhuwana)"
    ],
    "Kota": [
      "Talwandi & Vigyan Nagar",
      "Indra Vihar & Rajiv Gandhi Nagar (Coaching Hub)",
      "Gumanpura & Shopping Centre",
      "Dadabari & Chawani"
    ],
    "Ajmer": [
      "Civil Lines Ajmer",
      "Kutchery Road",
      "Vaishali Nagar Ajmer",
      "Pushkar"
    ],
    "Bikaner": [
      "Bikaner City",
      "Kote Gate",
      "Rani Bazar",
      "JNV Colony"
    ],
    "Bhilwara": [
      "Bhilwara City",
      "Bhopalganj",
      "Subhash Nagar",
      "Pur Road"
    ],
    "Alwar": [
      "Alwar City",
      "Neemrana (RIICO Japanese Zone)",
      "Bhiwadi Industrial Hub"
    ],
    "Other Rajasthan Districts": [
      "Sikar (Coaching Hub)",
      "Pali",
      "Sri Ganganagar",
      "Barmer",
      "Bharatpur",
      "Chittorgarh",
      "Jhunjhunu",
      "Nagaur",
      "Banswara",
      "Dausa",
      "Churu",
      "Dungarpur",
      "Jhalawar",
      "Baran",
      "Bundi",
      "Sawai Madhopur",
      "Karauli",
      "Dholpur",
      "Rajsamand",
      "Hanumangarh",
      "Jalore",
      "Sirohi (Abu Road)",
      "Jaisalmer",
      "Pratapgarh",
      "Beawar",
      "Balotra",
      "Didwana-Kuchaman",
      "Kotputli-Behror",
      "Phalodi",
      "Salumbar",
      "Shahpura"
    ]
  },
  "Madhya Pradesh": {
    "Indore": [
      "Vijay Nagar (Scheme 54, Malhar Mega Mall Area)",
      "Palasia (Old & New)",
      "AB Road, Bhawar Kuan & Sapna Sangeeta",
      "Saket, Anand Bazar & Kanadia Road",
      "Chappan Dukan, MG Road & Treasure Island Area",
      "Rau, Silicon City & CAT Road",
      "Super Corridor (TCS / Infosys SEZ Zone)",
      "Annapurna Road & Sudama Nagar"
    ],
    "Bhopal": [
      "MP Nagar (Zones 1 & 2 - Commercial Heart)",
      "Arera Colony & 10 No. Market",
      "Kolar Road & Danish Kunj",
      "Shahpura, Chunabhatti & Rohit Nagar",
      "New Market, TT Nagar & Malviya Nagar",
      "Hoshangabad Road & Aashima Mall Corridor",
      "Ayodhya Bypass & Indrapuri"
    ],
    "Gwalior": [
      "City Centre Gwalior & Patel Nagar",
      "Lashkar & Maharaj Bada",
      "Morar & Thatipur",
      "Pinto Park"
    ],
    "Jabalpur": [
      "Civil Lines Jabalpur",
      "Wright Town & Napier Town",
      "Gorakhpur Jabalpur",
      "Vijay Nagar Jabalpur"
    ],
    "Ujjain": [
      "Freeganj (Main Commercial Hub)",
      "Mahakal Mandir Corridor",
      "Nanakheda"
    ],
    "Other Madhya Pradesh Districts": [
      "Sagar",
      "Dewas (Industrial Hub)",
      "Satna",
      "Ratlam",
      "Rewa",
      "Katni",
      "Singrauli",
      "Burhanpur",
      "Khandwa",
      "Bhind",
      "Chhindwara",
      "Guna",
      "Shivpuri",
      "Vidisha",
      "Damoh",
      "Mandsaur",
      "Khargone",
      "Neemuch",
      "Pithampur (Dhar Industrial Zone)",
      "Narmadapuram (Hoshangabad)",
      "Itarsi",
      "Sehore",
      "Betul",
      "Seoni",
      "Datia"
    ]
  },
  "West Bengal": {
    "Kolkata": [
      "Park Street, Camac Street & Shakespeare Sarani",
      "Salt Lake (Sector 1, Sector 5 IT Hub)",
      "New Town & Rajarhat (City Centre 2)",
      "Ballygunge, Gariahat & Southern Avenue",
      "Alipore & New Alipore",
      "South City Mall & Prince Anwar Shah Road",
      "Behala, Taratala & Diamond Harbour Road",
      "North Kolkata (Shyambazar / Hatibagan / Girish Park)",
      "Ruby Hospital & EM Bypass Corridor",
      "Ultadanga & Kankurgachi"
    ],
    "Howrah": [
      "Howrah Station & Shibpur",
      "Salkia & Liluah",
      "Bally & Belur"
    ],
    "North 24 Parganas": [
      "Dum Dum & Nagerbazar",
      "Barasat",
      "Barrackpore",
      "Madhyamgram",
      "Bongaon"
    ],
    "South 24 Parganas": [
      "Garia & Jadavpur Extension",
      "Sonarpur",
      "Diamond Harbour"
    ],
    "Paschim Bardhaman": [
      "Asansol City",
      "Durgapur (City Centre / Benachity)",
      "Raniganj"
    ],
    "Darjeeling / Jalpaiguri": [
      "Siliguri (Sevoke Road / Hill Cart Road)",
      "Darjeeling Town",
      "Jalpaiguri Town"
    ],
    "Other West Bengal Districts": [
      "Hooghly (Serampore / Chinsurah / Chandannagar)",
      "Purba Bardhaman",
      "Nadia (Kalyani / Krishnanagar)",
      "Murshidabad (Baharampur)",
      "Malda",
      "Purba Medinipur (Haldia Industrial Hub / Digha)",
      "Paschim Medinipur (Kharagpur IIT Zone)",
      "Bankura",
      "Purulia",
      "Birbhum (Bolpur / Santiniketan)",
      "Cooch Behar",
      "Alipurduar",
      "Uttar Dinajpur",
      "Dakshin Dinajpur",
      "Kalimpong",
      "Jhargram"
    ]
  },
  "Kerala": {
    "Ernakulam (Kochi / Cochin)": [
      "MG Road & Marine Drive",
      "Panampilly Nagar & Kadavanthra",
      "Kakkanad & Infopark / SmartCity Zone",
      "Edappally & Lulu Mall Corridor",
      "Palarivattom & Kaloor",
      "Fort Kochi & Mattancherry",
      "Aluva & Angamaly (Airport Corridor)",
      "Vyttila & Mobility Hub Area",
      "Thrippunithura"
    ],
    "Thiruvananthapuram": [
      "MG Road Trivandrum",
      "Technopark & Kazhakoottam (IT Hub)",
      "Vellayambalam & Kowdiar",
      "Pattom, Kesavadasapuram & Medical College",
      "Lulu Mall Akkulam Area"
    ],
    "Kozhikode (Calicut)": [
      "Mavoor Road & SM Street",
      "Palayam & Focus Mall Area",
      "PT Usha Road & Beach Road",
      "Cyberpark & HiLITE City Corridor"
    ],
    "Thrissur": [
      "Swaraj Round",
      "East Fort Thrissur",
      "MG Road Thrissur"
    ],
    "Other Kerala Districts": [
      "Kollam",
      "Kannur",
      "Kottayam",
      "Palakkad",
      "Malappuram",
      "Alappuzha (Alleppey)",
      "Pathanamthitta",
      "Idukki",
      "Wayanad",
      "Kasaragod"
    ]
  },
  "Punjab": {
    "Ludhiana": [
      "Ferozepur Road & Gurdev Nagar",
      "Model Town Ludhiana & Tuition Market",
      "Sarabha Nagar (Kipps Market / South City)",
      "Civil Lines Ludhiana & Mall Road",
      "BRS Nagar & Dugri"
    ],
    "Amritsar": [
      "Mall Road & Lawrence Road",
      "Ranjit Avenue (Distt Shopping Centre)",
      "Golden Temple & Heritage Street Area",
      "Green Avenue & Albert Road",
      "Circular Road Amritsar"
    ],
    "Jalandhar": [
      "Model Town Jalandhar & PPR Mall Area",
      "Civil Lines Jalandhar",
      "BMC Chowk & GT Road",
      "Cantonment Road & Rama Mandi"
    ],
    "SAS Nagar (Mohali)": [
      "Phase 3B2 & Phase 7 Mohali (F&B Hubs)",
      "Phase 5 & Phase 8/9",
      "Aerocity & IT City Mohali (Infosys Zone)",
      "Kharar & Landran Road"
    ],
    "Patiala": [
      "Leela Bhawan & Mall Road",
      "Model Town Patiala",
      "Baradari",
      "Chhoti Baradari"
    ],
    "Bathinda": [
      "Mall Road Bathinda",
      "Civil Lines Bathinda",
      "Model Town Bathinda"
    ],
    "Other Punjab Districts": [
      "Hoshiarpur",
      "Pathankot",
      "Moga",
      "Batala",
      "Abohar",
      "Malerkotla",
      "Khanna",
      "Phagwara",
      "Kapurthala",
      "Sangrur",
      "Barnala",
      "Faridkot",
      "Firozpur",
      "Fazilka",
      "Gurdaspur",
      "Mansa",
      "Muktsar",
      "Nawanshahr (SBS Nagar)",
      "Rupnagar (Ropar)",
      "Tarn Taran",
      "Fatehgarh Sahib"
    ]
  },
  "Haryana": {
    "Gurugram (Gurgaon)": [
      "Cyber City & DLF Cyber Hub",
      "Golf Course Road",
      "Golf Course Extn Road",
      "Sohna Road",
      "Sector 29",
      "MG Road",
      "New Gurgaon (82-95)",
      "Manesar"
    ],
    "Faridabad": [
      "Faridabad NIT",
      "Sector 15 & 16",
      "Mathura Road Metro Corridor",
      "Greater Faridabad (Neharpar)"
    ],
    "Panchkula": [
      "Sector 5 & Sector 8 Market",
      "Sector 9 & 11 Panchkula",
      "Sector 20 Panchkula",
      "MDC Sector 4 & 5"
    ],
    "Panipat": [
      "Model Town Panipat",
      "GT Road Panipat",
      "Sanjay Chowk & Assandh Road"
    ],
    "Ambala": [
      "Ambala Cantt (Sadart Bazar)",
      "Ambala City (Cloth Market)",
      "Prem Nagar"
    ],
    "Karnal": [
      "Model Town Karnal",
      "Sector 12 & 13 Urban Estate",
      "Kunjpura Road"
    ],
    "Sonipat": [
      "Model Town Sonipat",
      "Kundli (TDI / Omaxe / Ashoka Univ)",
      "Murthal Food Hub Corridor"
    ],
    "Rohtak": [
      "Model Town Rohtak",
      "Delhi Road Rohtak",
      "D-Park Commercial Area"
    ],
    "Hisar": [
      "Model Town Hisar",
      "Urban Estate 2",
      "Red Square Market"
    ],
    "Other Haryana Districts": [
      "Yamunanagar & Jagadhri",
      "Kurukshetra",
      "Bhiwani",
      "Sirsa",
      "Bahadurgarh (Jhajjar)",
      "Jind",
      "Rewari & Bawal",
      "Palwal",
      "Kaithal",
      "Fatehabad",
      "Mahendragarh (Narnaul)",
      "Charkhi Dadri",
      "Nuh"
    ]
  },
  "Andhra Pradesh": {
    "Visakhapatnam (Vizag)": [
      "Siripuram, VIP Road & Waltair Uplands",
      "Dwaraka Nagar & Asilmetta",
      "MVP Colony & Beach Road",
      "Gajuwaka & Kurmannapalem",
      "Madhurawada IT SEZ & Rushikonda"
    ],
    "NTR / Krishna (Vijayawada)": [
      "MG Road (Bandar Road) & PB Siddhartha",
      "Benz Circle & Patamata",
      "Governorpet & Eluru Road",
      "Bhavanipuram & Gollapudi"
    ],
    "Guntur": [
      "Brodipet & Arundelpet",
      "Lakshmipuram Guntur",
      "Koretipadu & Gujanagundla"
    ],
    "Tirupati": [
      "AIR Bypass Road",
      "KT Road",
      "Bhavani Nagar",
      "Alipiri Road"
    ],
    "Other Andhra Pradesh Districts": [
      "Nellore",
      "Kurnool",
      "Kakinada",
      "Rajahmundry",
      "YSR Kadapa",
      "Anantapur",
      "Eluru",
      "Prakasam (Ongole)",
      "Srikakulam",
      "Vizianagaram",
      "Chittoor",
      "Machilipatnam",
      "Bhimavaram",
      "Proddatur",
      "Nandyal",
      "Tenali",
      "Hindupur",
      "Anakapalli",
      "Bapatla",
      "Palnadu (Narasaraopet)",
      "Konaseema (Amalapuram)",
      "Sri Sathya Sai (Puttaparthi)"
    ]
  },
  "Goa": {
    "North Goa": [
      "Panaji (Panjim) & Campal",
      "Porvorim & Mall De Goa Area",
      "Candolim, Calangute & Baga (Tourist Belt)",
      "Mapusa Commercial Centre",
      "Anjuna, Vagator & Chapora",
      "Assagao & Siolim (Lifestyle/Boutique Hub)",
      "Morjim & Mandrem"
    ],
    "South Goa": [
      "Margao (Madgaon) & Pajifond",
      "Vasco da Gama & Airport Area",
      "Colva & Benaulim",
      "Ponda City Centre",
      "Cansaulim & Majorda"
    ]
  },
  "Chandigarh (UT)": {
    "Chandigarh": [
      "Sector 17 (City Centre)",
      "Sector 35 & Sector 22 (Shopping & F&B Belt)",
      "Sector 8 & 9 (Inner Market / Madhya Marg)",
      "Sector 26 (Restaurant & Lounge Hub)",
      "Industrial Area Phase 1 (Elante Mall Zone)",
      "Industrial Area Phase 2",
      "Sector 43 & 44",
      "Sector 7 & 10",
      "Manimajra & IT Park"
    ]
  },
  "Bihar": {
    "Patna": [
      "Frazer Road & Dak Bungalow Crossing",
      "Boring Road & Boring Canal Road",
      "Kankarbagh & Rajendra Nagar",
      "Bailey Road & Raja Bazar",
      "Ashiana-Digha Road & Patliputra Colony",
      "Exhibition Road & Gandhi Maidan"
    ],
    "Gaya": [
      "Gaya City Centre",
      "Civil Lines Gaya",
      "Bodh Gaya (Tourist Belt)"
    ],
    "Muzaffarpur": [
      "Muzaffarpur City",
      "Motijheel Market",
      "Mithanpura & Club Road"
    ],
    "Bhagalpur": [
      "Bhagalpur City",
      "Tilka Manjhi",
      "Khalifabag Market"
    ],
    "Darbhanga": [
      "Darbhanga City",
      "Laheriasarai",
      "Tower Chowk"
    ],
    "Other Bihar Districts": [
      "Purnia",
      "Begusarai",
      "Ara (Bhojpur)",
      "Katihar",
      "Munger",
      "Chhapra (Saran)",
      "Saharsa",
      "Sasaram (Rohtas)",
      "Hajipur (Vaishali)",
      "Dehri-on-Sone",
      "Bettiah (West Champaran)",
      "Motihari (East Champaran)",
      "Siwan",
      "Kishanganj",
      "Samastipur",
      "Buxar",
      "Jehanabad",
      "Aurangabad (Bihar)",
      "Nawada",
      "Madhubani",
      "Sitamarhi",
      "Gopalganj"
    ]
  },
  "Odisha": {
    "Khordha (Bhubaneswar)": [
      "Janpath & Saheed Nagar",
      "Jayadev Vihar, Nayapalli & Esplanade One Mall",
      "Patia & KIIT University Area",
      "Chandrasekharpur & Infocity (IT Hub)",
      "Khandagiri, Baramunda & Cuttack-Puri Bypass"
    ],
    "Cuttack": [
      "Cuttack City",
      "Badambadi",
      "College Square Cuttack",
      "Link Road Cuttack"
    ],
    "Sundargarh (Rourkela)": [
      "Rourkela City",
      "Civil Township",
      "Sector 19 & Sector 5",
      "Panposh Road"
    ],
    "Other Odisha Districts": [
      "Puri (Grand Road & VIP Road)",
      "Sambalpur",
      "Berhampur (Ganjam)",
      "Balasore",
      "Bhadrak",
      "Baripada (Mayurbhanj)",
      "Jharsuguda",
      "Jeypore (Koraput)",
      "Angul",
      "Bargarh",
      "Kendujhar"
    ]
  },
  "Jharkhand": {
    "Ranchi": [
      "Main Road Ranchi & Albert Ekka Chowk",
      "Lalpur & Circular Road",
      "Harmu Housing Colony & Ashok Nagar",
      "Kanke Road & Morabadi",
      "Doranda & Hinoo (Airport Road)"
    ],
    "East Singhbhum (Jamshedpur)": [
      "Bistupur (Main Commercial Hub)",
      "Sakchi Market",
      "Kadma & Sonari",
      "Telco & Golmuri"
    ],
    "Dhanbad": [
      "Dhanbad City",
      "Bank More",
      "Saraidhela",
      "Hirapur"
    ],
    "Bokaro": [
      "Bokaro Steel City",
      "Sector 4 Bokaro",
      "Chas"
    ],
    "Other Jharkhand Districts": [
      "Deoghar (Temple Zone)",
      "Hazaribagh",
      "Giridih",
      "Ramgarh",
      "Medininagar (Daltonganj)",
      "Dumka",
      "Chaibasa"
    ]
  },
  "Chhattisgarh": {
    "Raipur": [
      "Pandri & Devendra Nagar (Cloth & Commercial)",
      "Telibandha & VIP Road / Magneto Mall Area",
      "Shankar Nagar & Civil Lines",
      "Jaistambh Chowk & Malviya Road",
      "Samta Colony & Choubey Colony",
      "Naya Raipur (Atal Nagar Corporate Area)"
    ],
    "Durg-Bhilai": [
      "Bhilai Civic Centre & Sector 6",
      "Nehru Nagar Bhilai",
      "Durg City & Station Road",
      "Supela Market"
    ],
    "Bilaspur": [
      "Bilaspur City",
      "Vyapar Vihar",
      "Link Road Bilaspur",
      "Magarpara"
    ],
    "Other Chhattisgarh Districts": [
      "Korba (Power City)",
      "Rajnandgaon",
      "Raigarh",
      "Jagdalpur (Bastar)",
      "Ambikapur (Surguja)",
      "Dhamtari"
    ]
  },
  "Uttarakhand": {
    "Dehradun": [
      "Rajpur Road (Ashley Hall to Jakhan)",
      "Paltan Bazaar & Clock Tower",
      "Jakhan & Malsi (Pacific Mall Area)",
      "Ballupur, Kaulagarh & Chakrata Road",
      "GMS Road & Saharanpur Chowk",
      "Rishikesh (Triveni Ghat / Tapovan / AIIMS Area)",
      "Mussoorie (Mall Road)"
    ],
    "Haridwar": [
      "Haridwar City & Ranipur More",
      "BHEL Township Area",
      "Jwalapur",
      "Roorkee & IIT Campus Area"
    ],
    "Nainital": [
      "Haldwani (Nainital Road / Kaladhungi Road)",
      "Nainital Town & Mall Road",
      "Ramnagar (Corbett Corridor)"
    ],
    "Other Uttarakhand Districts": [
      "Udham Singh Nagar (Rudrapur Industrial / Kashipur)",
      "Pauri Garhwal (Kotdwar)",
      "Almora",
      "Tehri Garhwal",
      "Pithoragarh",
      "Chamoli",
      "Uttarkashi",
      "Bageshwar",
      "Champawat",
      "Rudraprayag"
    ]
  },
  "Assam & North East": {
    "Kamrup Metropolitan (Guwahati)": [
      "GS Road (Christian Basti, Bhangagarh, Khanapara)",
      "Zoo Road (RG Baruah Road)",
      "Paltan Bazaar & Pan Bazaar",
      "Ulubari & Ganeshguri",
      "Beltola & Six Mile",
      "Jalukbari & Maligaon"
    ],
    "Dibrugarh": [
      "Dibrugarh City",
      "RKB Path",
      "Amolapatty"
    ],
    "Cachar (Silchar)": [
      "Silchar City",
      "Central Road",
      "Goldighi Mall Area"
    ],
    "Jorhat": [
      "Jorhat City",
      "Gar Ali",
      "AT Road Jorhat"
    ],
    "Other North East Cities": [
      "Shillong (Police Bazar / Laitumkhrah - Meghalaya)",
      "Agartala (Tripura)",
      "Imphal (Manipur)",
      "Aizawl (Mizoram)",
      "Dimapur & Kohima (Nagaland)",
      "Gangtok (MG Marg - Sikkim)",
      "Itanagar (Arunachal Pradesh)"
    ]
  },
  "Jammu & Kashmir / Ladakh": {
    "Jammu": [
      "Gandhi Nagar Jammu",
      "Resham Ghar & Residency Road",
      "Bahu Plaza & Channi Himmat",
      "Talab Tillo & Janipur"
    ],
    "Srinagar": [
      "Lal Chowk & Residency Road",
      "Rajbagh & Jawahar Nagar",
      "Karan Nagar",
      "Hyderpora & Airport Road"
    ],
    "Ladakh": [
      "Leh Main Market",
      "Kargil"
    ]
  },
  "Other Indian States & Union Territories": {
    "Puducherry (UT)": [
      "White Town (French Quarter)",
      "Heritage Town",
      "MG Road Puducherry"
    ],
    "Andaman and Nicobar Islands (UT)": [
      "Port Blair (Aberdeen Bazaar / Marine Hill)"
    ],
    "Dadra and Nagar Haveli and Daman and Diu (UT)": [
      "Daman (Nani Daman / Devka)",
      "Diu",
      "Silvassa (Dadra)"
    ],
    "Himachal Pradesh": [
      "Shimla (Mall Road / Sanjauli / New Shimla)",
      "Dharamshala & McLeodGanj",
      "Manali (Mall Road)",
      "Solan (Mall Road)",
      "Mandi",
      "Baddi (Industrial Pharma Hub)",
      "Kullu",
      "Hamirpur",
      "Bilaspur (HP)",
      "Una"
    ]
  }
};

function initQuizLocations(prefix) {
  var p = prefix || 'q_';
  var stateSelect = document.getElementById(p + 'state');
  var districtSelect = document.getElementById(p + 'district');
  var citySelect = document.getElementById(p + 'city');
  var cityCustomInput = document.getElementById(p + 'city_custom');

  if (!stateSelect || !districtSelect || !citySelect) return;

  // Populate States
  var stateKeys = Object.keys(window.quizLocationData);
  stateSelect.innerHTML = '<option value="">Select Target State *</option>';
  
  // Maharashtra first as priority market, then others
  stateKeys.forEach(function(state) {
    var opt = document.createElement('option');
    opt.value = state;
    opt.textContent = state;
    stateSelect.appendChild(opt);
  });

  var otherStateOpt = document.createElement('option');
  otherStateOpt.value = 'Other State / Union Territory';
  otherStateOpt.textContent = 'Other State / Union Territory';
  stateSelect.appendChild(otherStateOpt);

  // When State Changes
  stateSelect.onchange = function() {
    var selectedState = stateSelect.value;
    districtSelect.innerHTML = '';
    citySelect.innerHTML = '<option value="">Select District first</option>';
    citySelect.disabled = true;
    if (cityCustomInput) {
      cityCustomInput.style.display = 'none';
      cityCustomInput.value = '';
    }

    if (!selectedState) {
      districtSelect.innerHTML = '<option value="">Select State first</option>';
      districtSelect.disabled = true;
      return;
    }

    var districtsObj = window.quizLocationData[selectedState];
    if (districtsObj) {
      var districtKeys = Object.keys(districtsObj);
      districtSelect.innerHTML = '<option value="">Select District / Zone *</option>';
      districtKeys.forEach(function(dist) {
        var opt = document.createElement('option');
        opt.value = dist;
        opt.textContent = dist;
        districtSelect.appendChild(opt);
      });
      var otherDistOpt = document.createElement('option');
      otherDistOpt.value = 'Other District';
      otherDistOpt.textContent = 'Other / Unlisted District';
      districtSelect.appendChild(otherDistOpt);
      districtSelect.disabled = false;
    } else {
      districtSelect.innerHTML = '<option value="Other">Other / Open</option>';
      districtSelect.disabled = false;
      citySelect.innerHTML = '<option value="Other">Specify Custom City below</option>';
      citySelect.disabled = false;
      if (cityCustomInput) {
        cityCustomInput.style.display = 'block';
        cityCustomInput.focus();
      }
    }
  };

  // When District Changes
  districtSelect.onchange = function() {
    var selectedState = stateSelect.value;
    var selectedDist = districtSelect.value;
    citySelect.innerHTML = '';
    if (cityCustomInput) {
      cityCustomInput.style.display = 'none';
      cityCustomInput.value = '';
    }

    if (!selectedDist) {
      citySelect.innerHTML = '<option value="">Select District first</option>';
      citySelect.disabled = true;
      return;
    }

    if (selectedDist === 'Other District' || selectedDist === 'Other') {
      citySelect.innerHTML = '<option value="Other" selected>Specify Custom City / Locality</option>';
      citySelect.disabled = false;
      if (cityCustomInput) {
        cityCustomInput.style.display = 'block';
        cityCustomInput.placeholder = 'Type your City / Locality';
        cityCustomInput.focus();
      }
      return;
    }

    var districtsObj = window.quizLocationData[selectedState];
    if (districtsObj && districtsObj[selectedDist]) {
      var cities = districtsObj[selectedDist];
      citySelect.innerHTML = '<option value="">Select City / Commercial Area *</option>';
      cities.forEach(function(c) {
        var opt = document.createElement('option');
        opt.value = c;
        opt.textContent = c;
        citySelect.appendChild(opt);
      });
      var customCityOpt = document.createElement('option');
      customCityOpt.value = 'Other';
      customCityOpt.textContent = 'Other / Type Custom City or Locality...';
      citySelect.appendChild(customCityOpt);
      citySelect.disabled = false;
    } else {
      citySelect.innerHTML = '<option value="Other" selected>Specify Custom City</option>';
      citySelect.disabled = false;
      if (cityCustomInput) {
        cityCustomInput.style.display = 'block';
        cityCustomInput.focus();
      }
    }
  };

  // When City Changes
  citySelect.onchange = function() {
    if (citySelect.value === 'Other') {
      if (cityCustomInput) {
        cityCustomInput.style.display = 'block';
        cityCustomInput.placeholder = 'Type your specific City / Locality';
        cityCustomInput.focus();
      }
    } else {
      if (cityCustomInput) {
        cityCustomInput.style.display = 'none';
        cityCustomInput.value = '';
      }
    }
  };
}

// Helper function to get clean location value
function getQuizLocationData(prefix) {
  var p = prefix || 'q_';
  var state = document.getElementById(p + 'state') ? document.getElementById(p + 'state').value.trim() : '';
  var district = document.getElementById(p + 'district') ? document.getElementById(p + 'district').value.trim() : '';
  var citySelect = document.getElementById(p + 'city');
  var city = citySelect ? citySelect.value.trim() : '';
  var custom = document.getElementById(p + 'city_custom') ? document.getElementById(p + 'city_custom').value.trim() : '';
  
  if (city === 'Other' && custom) {
    city = custom;
  }
  return {
    state: state,
    district: district,
    city: city,
    isComplete: Boolean(state && district && city && (city !== 'Other' || custom))
  };
}

// Helper function to reset locations
function resetQuizLocationFields(prefix) {
  var p = prefix || 'q_';
  var stateSelect = document.getElementById(p + 'state');
  var districtSelect = document.getElementById(p + 'district');
  var citySelect = document.getElementById(p + 'city');
  var cityCustomInput = document.getElementById(p + 'city_custom');

  if (stateSelect) stateSelect.value = '';
  if (districtSelect) {
    districtSelect.innerHTML = '<option value="">Select State first</option>';
    districtSelect.disabled = true;
  }
  if (citySelect) {
    citySelect.innerHTML = '<option value="">Select District first</option>';
    citySelect.disabled = true;
  }
  if (cityCustomInput) {
    cityCustomInput.style.display = 'none';
    cityCustomInput.value = '';
  }
}

// Auto-run on DOMContentLoaded or immediately if DOM is loaded
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', function() {
    initQuizLocations('q_');
  });
} else {
  initQuizLocations('q_');
}
