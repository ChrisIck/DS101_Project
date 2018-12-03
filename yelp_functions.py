import yelp_functions
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize
import ast

def Clean_Business_Data(df):
    df = df.loc[df['state'] == 'AZ']
    #df = df[~df['categories'].isnull()]
    df.categories.fillna('', inplace=True)
    
    excluded_categories = excluded_categories = ['& Probates', '3D Printing', 'Accessories', 'Accountants', 'Acne Treatment', 'Acupuncture', 'Addiction Medicine', 'Adoption Services', 'Adult', 'Adult Education', 'Adult Entertainment', 'Advertising', 'Aerial Fitness', 'Aerial Tours', 'Aestheticians', 'Air Duct Cleaning', 'Aircraft Dealers', 'Aircraft Repairs', 'Airlines', 
            'Airport Lounges', 'Airport Shuttles', 'Airport Terminals', 'Airports', 'Airsoft', 'Allergists', 'Alternative Medicine', 'Amateur Sports Teams', 'Amusement Parks', 'Anesthesiologists', 'Animal Assisted Therapy', 'Animal Physical Therapy', 'Animal Shelters', 'Antiques', 'Apartment Agents', 'Apartments', 'Appliances', 
            'Appliances & Repair', 'Appraisal Services', 'Aquarium Services', 'Aquariums', 'Arcades', 'Archery', 'Architects', 'Architectural Tours', 'Art Classes', 'Art Galleries', 'Art Museums', 'Art Restoration', 'Art Schools', 'Art Space Rentals', 'Art Supplies', 'Art Tours', 'Artificial Turf', 'Arts & Crafts', 'Asian Fusion', 
            'Assisted Living Facilities', 'Astrologers', 'Attraction Farms', 'ATV Rentals/Tours', 'Auction Houses', 'Audio/Visual Equipment Rental', 'Audiologist', 'Auto Customization', 'Auto Detailing', 'Auto Electric Services', 'Auto Glass Services', 'Auto Insurance', 'Auto Loan Providers', 'Auto Parts & Supplies', 'Auto Repair', 'Auto Security', 
            'Auto Upholstery', 'Automotive', 'Aviation Services', 'Awnings', 'Axe Throwing', 'Ayurveda', 'Baby Gear & Furniture', 'Backflow Services', 'Backshop', 'Badminton', 'Bail Bondsmen', 'Balloon Services', 'Bankruptcy Law', 'Banks & Credit Unions', 'Bar Crawl', 'Barre Classes', 'Bartending Schools', 'Baseball Fields', 'Basketball Courts', 'Battery Stores', 'Batting Cages', 'Beach Equipment Rentals', 'Beach Volleyball', 'Beaches', 'Beauty & Spas', 'Bed & Breakfast', 'Behavior Analysts', 'Bespoke Clothing', 'Beverage Store', 'Bicycles', 'Bike Parking', 'Bike Rentals', 'Bike Repair', 'Bike Repair/Maintenance', 'Bike Sharing', 'Bike Shop', 'Bike tours', 'Bikes', 'Billing Services', 'Bingo Halls', 'Bird Shops', 'Blood & Plasma Donation Centers', 'Blow Dry/Out Services', 'Boat Charters', 'Boat Dealers', 'Boat Parts & Supplies', 'Boat Repair', 'Boat Tours', 'Boating', 'Body Contouring', 'Body Shops', 'Bookbinding', 'Bookkeepers', 'Books', 'Bookstores', 'Boot Camps', 'Botanical Gardens', 'Boudoir Photography', 'Bounce House Rentals', 'Bowling', 'Boxing', 'Brazilian Jiu-jitsu', 'Brewing Supplies', 'Bridal', 'Bubble Soccer', 'Buddhist Temples', 'Buffets', 'Building Supplies', 'Bus Rental', 'Bus Tours', 'Buses', 'Business Consulting', 'Business Financing', 'Business Law', 'Cabaret', 'Cabinetry', 'Calligraphy', 'Campgrounds', 'Candle Stores', 'Cannabis Clinics', 'Cannabis Collective', 'Cannabis Dispensaries', 'Cannabis Tours', 'Car Auctions', 'Car Brokers', 'Car Buyers', 'Car Dealers', 'Car Inspectors', 'Car Rental', 'Car Share Services', 'Car Stereo Installation', 'Car Wash', 'Car Window Tinting', 'Cardio Classes', 'Cardiologists', 
            'Cards & Stationery', 'Career Counseling', 'Caribbean', 'Caricatures', 'Carousels', 'Carpenters', 'Carpet Cleaning', 'Carpet Dyeing', 'Carpet Installation', 'Carpeting', 'Casinos', 'Castles', 'Ceremonial Clothing', 'Challenge Courses', 'Check Cashing/Pay-day Loans', 'Cheerleading', 'Cheese Tasting Classes', 'Child Care & Day Care', 'Childbirth Education', 'Childproofing', 'Childrens Clothing', 'Childrens Clothing', 'Childrens Museums', 'Childrens Museums', 'Chimney Sweeps', 'Chinese', 'Chinese Martial Arts', 'Chiropractors', 'Christmas Markets', 'Christmas Trees', 'Churches', 'Cigar Bars', 'Cinema', 'Circuit Training Gyms', 'Civic Center', 'Climbing', 'Clock Repair', 'Clothing Rental', 'Clowns', 'Club Crawl', 'Coffee & Tea Supplies', 'College Counseling', 'Colleges & Universities', 'Colonics', 'Comedy Clubs', 'Comic Books', 'Commercial Real Estate', 'Commercial Truck Dealers', 'Commercial Truck Repair', 'Commissioned Artists', 'Community Centers', 'Community Gardens', 'Community Service/Non-Profit', 'Computers', 'Concept Shops', 'Concierge Medicine', 'Condominiums', 'Contract Law', 'Contractors', 'Convenience Stores', 'Conveyor Belt Sushi', 'Cooking Classes', 'Cooking Schools', 'Cosmetic Dentists', 'Cosmetic Surgeons', 'Cosmetics & Beauty Supply', 'Cosmetology Schools', 'Costumes', 'Counseling & Mental Health', 'Countertop Installation', 'Country Clubs', 'Country Dance Halls', 'Couriers & Delivery Services', 'Court Reporters', 'Courthouses', 'CPR Classes', 'Crane Services', 
            'Cremation Services', 'Criminal Defense Law', 'Cryotherapy', 'CSA', 'Cultural Center', 'Currency Exchange', 'Customized Merchandise', 'Customs Brokers', 'Cycling Classes', 'Damage Restoration', 'Dance Schools', 'Dance Studios', 'Dance Wear', 'Data Recovery', 'Day Camps', 'Day Spas', 'Debt Relief Services', 'Decks & Railing', 'Demolition Services', 'Dental Hygienists', 'Dentists', 'Department Stores', 'Departments of Motor Vehicles', 'Dermatologists', 'Diagnostic Imaging', 'Diagnostic Services', 'Dialysis Clinics', 'Dietitians', 'Digitizing Services', 'Dinner Theater', 'Disability Law', 'Disc Golf', 'Discount Store', 'Dive Shops', 'Diving', 'Divorce & Family Law', 'DIY Auto Shop', 'DJs', 'Doctors', 'Dog Parks', 'Dog Walkers', 'Donation Center', 'Door Sales/Installation', 'Doulas', 'Drive-In Theater', 'Driving Schools', 'Drones', 'Drugstores', 'Dry Cleaning', 'Dry Cleaning & Laundry', 'Drywall Installation & Repair', 'DUI Law', 'DUI Schools', 'Dumpster Rental', 'Duplication Services', 'Duty-Free Shops', 'Ear Nose & Throat', 'Eatertainment', 'Editorial Services', 'Education', 'Educational Services', 'Elder Care Planning', 'Electricians', 'Electricity Suppliers', 'Electronics', 'Electronics Repair', 'Elementary Schools', 'Embassy', 'Embroidery & Crochet', 'Emergency Medicine', 'Emergency Pet Hospital', 'Emergency Rooms', 'Employment Agencies', 'Employment Law', 'Endocrinologists', 'Endodontists', 'Engraving', 'Entertainment Law', 'Environmental Abatement', 'Environmental Testing', 'Erotic Massage', 
            'Escape Games', 'Estate Liquidation', 'Estate Planning Law', 'Estheticians', 'EV Charging Stations', 'Event Photography', 'Event Planning & Services', 'Excavation Services', 'Experiences', 'Eyebrow Services', 'Eyelash Service', 'Eyewear & Opticians', 'Fabric Stores', 'Face Painting', 'Family Practice', 'Farm Equipment Repair', 'Farmers Market', 'Farming Equipment', 'Farms', 'Fashion', 'Fences & Gates', 'Fencing Clubs', 'Feng Shui', 'Fertility', 'Festivals', 'Financial Advising', 'Financial Services', 'Fingerprinting', 'Fire Departments', 'Fire Protection Services', 'Firearm Training', 'Fireplace Services', 'Firewood', 'Fireworks', 'First Aid Classes', 'Fishing', 'Fitness & Instruction', 'Fitness/Exercise Equipment', 'Flea Markets', 'Flight Instruction', 'Float Spa', 'Flooring', 'Floral Designers', 'Florists', 'Flowers', 'Flowers & Gifts', 'Flyboarding', 'Food Banks', 'Food Delivery Services', 'Food Tours', 'Formal Wear', 'Foundation Repair', 'Framing', 'Free Diving', 'Fuel Docks', 'Funeral Services & Cemeteries', 'Fur Clothing', 'Furniture Assembly', 'Furniture Rental', 'Furniture Repair', 'Furniture Reupholstery', 'Furniture Stores', 'Game Meat', 'Game Truck Rental', 'Garage Door Services', 'Gardeners', 'Gas Stations', 'Gastroenterologist', 'Gay Bars', 'Gemstones & Minerals', 'General Dentistry', 'General Festivals', 'General Litigation', 'Generator Installation/Repair', 'Gerontologists', 'Gift Shops', 'Glass & Mirrors', 'Glass Blowing', 'Go Karts', 'Gold Buyers', 'Golf', 'Golf Cart Dealers', 'Golf Cart Rentals', 'Golf Equipment', 'Golf Equipment Shops', 'Golf Lessons', 'Graphic Design', 'Grilling Equipment', 'Grocery', 'Grout Services', 'Guamanian', 'Guest Houses', 'Guitar Stores', 'Gun/Rifle Ranges', 'Guns & Ammo', 'Gunsmith', 'Gutter Services', 
            'Gymnastics', 'Gyms', 'Habilitative Services', 'Hair Extensions', 'Hair Loss Centers', 'Hair Removal', 'Hair Salons', 'Hair Stylists', 'Halfway Houses', 'Halotherapy', 'Handyman', 'Hang Gliding', 'Hardware Stores', 'Hats', 'Haunted Houses', 'Hazardous Waste Disposal', 'Head Shops', 'Health & Medical', 'Health Coach', 'Health Insurance Offices', 'Health Markets', 'Health Retreats', 'Hearing Aid Providers', 'Hearing Aids', 'Heating & Air Conditioning/HVAC', 'Henna Artists', 'Hepatologists', 'Herbal Shops', 'Herbs & Spices', 'High Fidelity Audio Equipment', 'Hiking', 'Himalayan/Nepalese', 'Hindu Temples', 
            'Historical Tours', 'Hobby Shops', 'Hockey Equipment', 'Holiday Decorating Services', 'Holiday Decorations', 'Holistic Animal Care', 'Home & Garden', 'Home & Rental Insurance', 'Home Automation', 'Home Cleaning', 'Home Decor', 'Home Developers', 'Home Energy Auditors', 'Home Health Care', 'Home Inspectors', 'Home Network Installation', 'Home Organization', 'Home Services', 'Home Staging', 'Home Theatre Installation', 'Home Window Tinting', 'Homeless Shelters', 'Homeowner Association', 'Hookah Bars', 'Horse Boarding', 'Horse Equipment Shops', 'Horse Racing', 'Horseback Riding', 'Hospice', 'Hospitals', 'Hostels', 'Hot Air Balloons', 'Hot Tub & Pool', 'Hotels', 'Hotels & Travel', 'House Sitters', 'Hunting & Fishing Supplies', 'Hybrid Car Repair', 'Hydro-jetting', 'Hydroponics', 'Hydrotherapy', 'Hypnosis/Hypnotherapy', 'Ice Delivery', 'Immigration Law', 'Immunodermatologists', 'Indoor Landscaping', 'Indoor Playcentre', 'Infectious Disease Specialists', 'Installment Loans', 'Insulation Installation', 'Insurance', 'Interior Design', 'Interlock Systems', 'Internal Medicine', 'Internet Cafes', 'Internet Service Providers', 'Interval Training Gyms', 'Investing', 'IP & Internet Law', 'Irrigation', 'Island Pub', 'IT Services & Computer Repair', 'IV Hydration', 'Jails & Prisons', 'Jazz & Blues', 'Jet Skis', 'Jewelry', 'Jewelry Repair', 
            'Junk Removal & Hauling', 'Junkyards', 'Karate', 'Keys & Locksmiths', 'Kickboxing', 'Kids Activities', 'Kids Hair Salons', 'Kitchen & Bath', 'Kitchen Incubators', 'Kitchen Supplies', 'Knife Sharpening', 'Knitting Supplies', 'Laboratory Testing', 'Lactation Services', 'Lakes', 'LAN Centers',
            'Land Surveying', 'Landmarks & Historical Buildings', 'Landscape Architects', 'Landscaping', 'Language Schools', 'Laser Eye Surgery/Lasik', 'Laser Hair Removal', 'Laser Tag', 'Laundromat', 'Laundry Services', 'Lawn Services', 'Lawyers', 'Leather Goods', 'Legal Services', 'Leisure Centers', 
            'Libraries', 'Lice Services', 'Life Coach', 'Life Insurance', 'Lighting Fixtures & Equipment', 'Lighting Stores', 'Limos', 'Lingerie', 'Livestock Feed & Supply', 'Local Fish Stores', 'Local Services', 'Luggage', 'Luggage Storage', 'Machine & Tool Rental', 'Machine Shops', 'Magicians', 'Mags', 'Mailbox Centers', 'Makerspaces', 'Makeup Artists', 'Marinas', 'Market Stalls', 'Marketing', 'Martial Arts', 'Masonry/Concrete', 'Mass Media', 'Massage', 'Massage Schools', 'Massage Therapy', 'Matchmakers', 'Maternity Wear', 'Mattresses', 'Meat Shops', 'Mediators', 'Medical Cannabis Referrals', 'Medical Centers', 'Medical Foot Care', 'Medical Law', 'Medical Spas', 'Medical Supplies', 'Medical Transportation', 'Meditation Centers', 'Memory Care', 'Mens Clothing', 'Mens Clothing', 'Mens Hair Salons', 'Mens Hair Salons', 'Metal Fabricators', 'Metro Stations', 'Middle Schools & High Schools', 'Midwives', 'Military Surplus', 'Mini Golf', 'Misting System Services', 'Mobile Dent Repair', 'Mobile Home Dealers', 'Mobile Home Parks', 'Mobile Home Repair', 'Mobile Phone Accessories', 'Mobile Phone Repair', 'Mobile Phones', 'Mobility Equipment Sales & Services', 'Montessori Schools', 'Mortgage Brokers', 'Mortgage Lenders', 'Mortuary Services', 'Mosques', 'Motorcycle Dealers', 'Motorcycle Gear', 'Motorcycle Rental', 'Motorcycle Repair', 'Motorsport Vehicle Dealers', 'Motorsport Vehicle Repairs', 'Mountain Biking', 'Movers', 'Muay Thai', 'Municipality', 'Museums', 'Music & DVDs', 'Music & Video', 'Music Production Services', 'Music Venues', 'Musical Instrument Services', 'Musical Instruments & Teachers', 'Musicians', 'Nail Salons', 'Nail Technicians', 'Nanny Services', 'Natural Gas Suppliers', 'Naturopathic/Holistic', 'Nephrologists', 'Neurologist', 'Neuropathologists', 'Neurotologists', 'Newspapers & Magazines', 'Nicaraguan', 'Notaries', 'Nudist', 'Nurse Practitioner', 'Nurseries & Gardening', 'Nursing Schools', 'Nutritionists', 'Observatories', 'Obstetricians & Gynecologists', 'Occupational Therapy', 'Office Cleaning', 'Office Equipment', 'Officiants', 'Oil Change Stations', 'Oncologist', 'Opera & Ballet', 'Ophthalmologists', 'Optometrists', 'Oral Surgeons', 'Orthodontists', 'Orthopedists', 'Orthotics', 'Osteopathic Physicians', 'Osteopaths', 'Otologists', 'Outdoor Furniture Stores', 'Outdoor Gear', 'Outdoor Movies', 'Outlet Stores', 'Oxygen Bars', 'Packing Services', 'Packing Supplies', 'Paddleboarding', 'Pain Management', 'Paint & Sip', 'Paint Stores', 'Paint-Your-Own Pottery', 'Paintball', 'Painters', 'Parenting Classes', 'Parking', 'Parks', 'Party & Event Planning', 'Party Bike Rentals', 'Party Bus Rentals', 'Party Characters', 'Party Equipment Rentals', 'Party Supplies', 'Passport & Visa Services', 'Patent Law', 'Pathologists', 'Patio Coverings', 'Pawn Shops', 'Payroll Services', 'Pediatric Dentists', 'Pediatricians', 'Pedicabs', 'Pensions', 'Performing Arts', 'Perfume', 'Periodontists', 'Permanent Makeup', 'Personal Assistants', 'Personal Care Services', 'Personal Chefs', 'Personal Injury Law', 'Personal Shopping', 'Pest Control', 'Pet Adoption', 'Pet Boarding', 'Pet Breeders', 'Pet Cremation Services', 'Pet Groomers', 'Pet Hospice', 'Pet Insurance', 'Pet Photography', 'Pet Services', 'Pet Sitting', 'Pet Stores', 'Pet Training', 'Pet Transportation', 'Pet Waste Removal', 'Pets', 'Petting Zoos', 'Pharmacy', 'Phlebologists', 'Photo Booth Rentals', 'Photographers', 'Photography Classes', 'Photography Stores & Services', 'Physical Therapy', 'Piano Bars', 'Piano Services', 'Piano Stores', 'Pick Your Own Farms', 'Piercing', 'Pilates', 'Placenta Encapsulations', 'Planetarium', 'Plastic Surgeons', 'Playgrounds', 'Playsets', 'Plumbing', 'Plus Size Fashion', 'Podiatrists', 'Pole Dancing Classes', 'Police Departments', 'Pool & Billiards', 'Pool & Hot Tub Service', 'Pool Cleaners', 'Pool Halls', 'Pop-up Shops', 'Portuguese', 'Post Offices', 'Powder Coating', 'Prenatal/Perinatal Care', 'Preschools', 'Pressure Washers', 'Preventive Medicine', 'Print Media', 'Printing Services', 'Private Investigation', 'Private Jet Charter', 'Private Schools', 'Private Tutors', 'Process Servers', 'Proctologists', 'Product Design', 'Professional Services', 'Professional Sports Teams', 'Propane', 'Property Management', 'Props', 'Prosthetics', 'Prosthodontists', 'Psychiatrists', 'Psychic Mediums', 'Psychics', 'Psychologists', 'Public Adjusters', 'Public Art', 'Public Markets', 'Public Relations', 'Public Services & Government', 'Public Transportation', 'Pulmonologist', 'Pumpkin Patches', 'Qi Gong', 'Race Tracks', 'Races & Competitions', 'Racing Experience', 'Radio Stations', 'Radiologists', 'Rafting/Kayaking', 'Ranches', 'Real Estate', 'Real Estate Agents', 'Real Estate Law', 'Real Estate Photography', 'Real Estate Services', 'Recording & Rehearsal Studios', 'Recreation Centers', 'Recycling Center', 'Refinishing Services', 'Reflexology', 'Registration Services', 'Registry Office', 'Rehabilitation Center', 'Reiki', 'Religious Items', 'Religious Organizations', 'Religious Schools', 'Reptile Shops', 'Resorts', 'Rest Stops', 'Restaurant Supplies', 'Retina Specialists', 'Retirement Homes', 'Reunion', 'Rheumatologists', 'Roadside Assistance', 'Rock Climbing', 'Rodeo', 'Rolfing', 'Roof Inspectors', 'Roofing', 'Rugs', 'RV Dealers', 'RV Parks', 'RV Rental', 'RV Repair', 'Safe Stores', 'Safety Equipment', 'Sailing', 'Sandblasting', 'Sauna Installation & Repair', 'Saunas', 'Scavenger Hunts', 'Scooter Rentals', 'Scooter Tours', 'Screen Printing', 'Screen Printing/T-Shirt Printing', 'Scuba Diving', 'Seafood Markets', 'Security Services', 'Security Systems', 'Self Storage', 'Self-defense Classes', 'Senior Centers', 'Septic Services', 'Service Stations', 'Session Photography', 'Sewing & Alterations', 'Sex Therapists', 'Shades & Blinds', 'Shared Office Spaces', 'Shipping Centers', 'Shoe Repair', 'Shoe Shine', 'Shoe Stores', 'Shopping', 'Shopping Centers', 'Shredding Services', 'Shutters', 'Siding', 'Signature Cuisine', 'Signmaking', 'Skate Parks', 'Skate Shops', 'Skating Rinks', 'Ski & Snowboard Shops', 'Ski Resorts', 'Ski Schools', 'Skiing', 'Skilled Nursing', 'Skin Care', 'Skydiving', 'Sledding', 'Sleep Specialists', 'Smog Check Stations', 'Snorkeling', 'Snow Removal', 'Soccer', 'Social Clubs', 'Social Security Law', 'Software Development', 'Solar Installation', 'Solar Panel Cleaning', 'Souvenir Shops', 'Special Education', 'Specialty Schools', 'Speech Therapists', 'Spin Classes', 'Spine Surgeons', 'Spiritual Shop', 'Sport Equipment Hire', 'Sporting Goods', 'Sports Clubs', 'Sports Medicine', 'Sports Psychologists', 'Sports Wear', 'Spray Tanning', 'Squash', 'Stadiums & Arenas', 'Storefront Clinics', 'Street Art', 'Strip Clubs', 'Striptease Dancers', 'Structural Engineers', 'Stucco Services', 'Sugaring', 'Summer Camps', 'Sunglasses', 'Supernatural Readings', 'Surf Schools', 'Surf Shop', 'Surfing', 'Surgeons', 'Swimming Lessons/Schools', 'Swimming Pools', 'Swimwear', 'Synagogues', 'Tabletop Games', 'Tableware', 'Taekwondo', 'Tai Chi', 'Talent Agencies', 'Tanning', 'Tanning Beds', 'Tasting Classes', 'Tattoo', 'Tattoo Removal', 'Tax Law', 'Tax Services', 'Taxidermy', 'Taxis', 'Teacher Supplies', 'Team Building Activities', 'Teeth Whitening', 'Telecommunications', 'Television Service Providers', 'Television Stations', 'Tenant and Eviction Law', 'Tennis', 'Test Preparation', 'Tex-Mex', 'Threading Services', 'Thrift Stores', 'Ticket Sales', 'Tickets', 'Tiling', 'Tires', 'Title Loans', 'Tobacco Shops', 'Towing', 'Town Car Service', 'Town Hall', 'Toxicologists', 'Toy Stores', 'Traditional Chinese Medicine', 'Traditional Clothing', 'Traffic Schools', 'Traffic Ticketing Law', 'Trailer Dealers', 'Trailer Rental', 'Trailer Repair', 'Train Stations', 'Trainers', 'Trains', 'Trampoline Parks', 'Translation Services', 'Transmission Repair', 'Transportation', 'Travel Agents', 'Travel Services', 'Tree Services', 'Trinidadian', 'Trivia Hosts', 'Trophy Shops', 'Truck Rental', 'Trusts', 'Tubing', 'Tui Na', 'Tutoring Centers', 'TV Mounting', 'Ultrasound Imaging Centers', 'Undersea/Hyperbaric Medicine', 'Uniforms', 'University Housing', 'Unofficial Yelp Events', 'Urgent Care', 'Urologists', 'Used', 'Used Bookstore', 'Used Car Dealers', 'Utilities', 'Vacation Rental Agents', 'Vacation Rentals', 'Valet Services', 'Vape Shops', 'Vascular Medicine', 'Vegetarian', 'Vehicle Shipping', 'Vehicle Wraps', 'Venues & Event Spaces', 'Veterans Organizations', 'Veterinarians', 'Video Game Stores', 'Video/Film Production', 'Videographers', 'Videos & Video Game Rental', 'Vintage & Consignment', 'Vinyl Records', 'Virtual Reality Centers', 'Visitor Centers', 'Vocal Coach', 'Vocational & Technical School', 'Waldorf Schools', 'Walk-in Clinics', 'Walking Tours', 'Wallpapering', 'Watch Repair', 'Watches', 'Water Delivery', 'Water Heater Installation/Repair', 'Water Parks', 'Water Purification Services', 'Water Stores', 'Water Suppliers', 'Waterproofing', 'Waxing', 'Web Design', 'Wedding Chapels', 'Wedding Planning', 'Weight Loss Centers', 'Well Drilling', 'Wheel & Rim Repair', 'Wholesale Stores', 'Wholesalers', 'Wigs', 'Wildlife Control', 'Wildlife Hunting Ranges', 'Wills', 'Window Washing', 'Windows Installation', 'Windshield Installation & Repair', 'Wine Tasting Classes', 'Wine Tasting Room', 'Wine Tours', 'Wineries', 'Womens Clothing', 'Womens Clothing', 'Workers Compensation Law', 'Yelp Events', 'Yoga', 'Ziplining', 'Zoos', 'Tours', 'Vitamins & Supplements', 'Active Life', 'Arts & Entertainment', 'Barbers', 'Nightlife']

    delete_indexes = []
    
    for i in df.index.values:
        categories = df['categories'].loc[i].split(',')
        
        if any(x in excluded_categories for x in categories):
            delete_indexes.append(i)
    
    df = df.drop(delete_indexes)
    df = df[df.categories.str.contains('Restaurants')]
    df = df.loc[df['is_open']==1]
    
    return df

def enrich_biz_categories(biz_df,min_percent):
    
    cat_list=('Afghan','African','Arabian','Argentine','Armenian','Australian','Austrian','Bangladeshi','Basque','Bavarian','Brasseries','British','Bulgarian','Burmese','Cambodian','Cantonese','Chilean','Colombian','Cuban','Czech','Czech/Slovakian','Dominican','Donairs','Eastern European','Egyptian','Ethiopian','Falafel','Filipino','Greek','Hainan','Haitian','Hakka','Halal','Hawaiian','Honduran','Hot Pot','Iberian','Indonesian','International','Irish','Irish Pub','Izakaya','Japanese Curry','Kebab','Kosher','Laotian','Lebanese','Malaysian','Mauritius','Mediterranean','Modern European','Mongolian','Moroccan','New Mexican Cuisine','Noodles','Northern German','Pan Asian','Peruvian','Polish','Puerto Rican','Ramen','Russian','Salvadoran','Scandinavian','Scottish','Senegalese','Shanghainese','Sicilian','Singaporean','Slovakian','Soul Food','South African','Spanish','Sri Lankan','Swiss Food','Syrian','Szechuan','Teppanyaki','Traditional Norwegian','Turkish','Tuscan','Ukrainian','Uzbek','Venezuelan','Acai Bowls','American (New)','American (Traditional)','Bagels','Baguettes','Bakeries','Barbeque','Bars','Bartenders','Beach Bars','Beer','Beer Hall','Beer Tours','Beer Gardens','Beer Garden','Beer Bar','Belgian','Bistros','Brazilian','Breakfast & Brunch','Breweries','Brewpubs','Bubble Tea','Burgers','Butcher','Cafes','Cafeteria','Cajun/Creole','Canadian (New)','Candy Stores','Caterers','Champagne Bars','Cheese Shops','Cheesesteaks','Chicken Shop','Chicken Wings','Chocolatiers & Shops','Churros','Cideries','Cocktail Bars','Coffee & Tea','Coffee Roasteries','Coffeeshops','Comfort Food','Creperies','Cupcakes','Custom Cakes','Delicatessen','Delis','Desserts','Dim Sum','Diners','Distilleries','Dive Bars','Do-It-Yourself Food','Donuts','Drive-Thru Bars','Empanadas','Ethical Grocery','Ethnic Food','Ethnic Grocery','Fast Food','Fish & Chips','Fishmonger','Fondue','Food Court','Food Stands','Food Trucks','French','Fruits & Veggies','Gastropubs','Gelato','German','Gluten-Free','Honey','Hong Kong Style Cafe','Hot Dogs','Hotel bar','Hungarian','Ice Cream & Frozen Yogurt','Imported Food','Indian','International Grocery','Italian','Japanese','Japanese Sweets','Juice Bars & Smoothies','Karaoke','Kombucha','Korean','Latin American','Live/Raw Food','Local Flavor','Lounges','Macarons','Mexican','Middle Eastern','Milkshake Bars','Minho','Olive Oil','Organic Stores','Pakistani','Palatine','Pasta Shops','Patisserie/Cake Shop','Persian/Iranian','Pita','Pizza','Poke','Pop-Up Restaurants','Popcorn Shops','Poutineries','Pretzels','Pub Food','Pubs','Rotisserie Chicken','Salad','Sandwiches','Seafood','Serbo Croatian','Shaved Ice','Shaved Snow','Smokehouse','Soba','Soup','Southern','Speakeasies','Specialty Food','Sports Bars','Steakhouses','Street Vendors','Sugar Shacks','Supper Clubs','Sushi Bars','Tacos','Taiwanese','Tapas Bars','Tapas/Small Plates','Tea Rooms','Tempura','Thai','Themed Cafes','Tiki Bars','Tonkatsu','Udon','Vegan','Vietnamese','Waffles','Whiskey Bars','Wine & Spirits','Wine Bars','Wraps','None')
    cat_df=pd.DataFrame(index=range(0,len(cat_list)),columns=('category','count'))
    for i in range(0,len(cat_list)):
        cat_df['category'][i]=cat_list[i]
        cat_df['count'][i]=biz_df.categories.str.contains(cat_list[i]).sum()

    min_count=len(biz_df)*min_percent 
    cat_df = cat_df[cat_df['count'] > min_count] 

    for x in cat_df['category']:
        biz_df[x]=biz_df.categories.str.contains(x)*1
    
    return biz_df
    
    
def enrich_biz_attributes(biz_df):
    
    biz_df = biz_df.reset_index(drop=True)
    
    exclude_list=('HairSpecializesIn','AcceptsInsurance','ByAppointmentOnly','AgesAllowed','DietaryRestrictions','Open24Hours','RestaurantsCounterService','BusinessAcceptsBitcoin','Corkage','BestNights')

    #these attributes are a dict within a dict rather than a single value like the other attributes
    second_list=('Music','GoodForMeal','Ambience','BusinessParking')

    for i in range(0,len(biz_df)):
        if biz_df['attributes'][i] is not None:
            attribute_data=pd.DataFrame(json_normalize(data=biz_df['attributes'][i])) #normalize the attribute field and put in a DF
        
            for j in attribute_data:
                if j not in exclude_list and j not in second_list:
                    biz_df.loc[i,j]=attribute_data[j].values
            
            #THIS IS WHERE I AM HAVING A PROBLEM
                if j in second_list: #extract 2nd list of attributes
                    for key,value in ast.literal_eval(attribute_data[j].values[0]).items():
                        biz_df.loc[i,j+'.'+key] = value
                    
    return biz_df
    
def join_datasets(reviews,biz,tips):
    reviews['date'] =  pd.to_datetime(reviews['date'])
    join1 = pd.merge(reviews,biz, left_on='business_id', right_on = 'business_id',how='inner')
    join2 = pd.merge(join1,tips, how='inner', left_on=['business_id','date','user_id'], right_on = ['business_id','date','user_id'])
    join2 = join2.rename(index=str, columns={"text_x": "review_text", "text_y": "tips_text","stars_x":"stars"})
    join2 = join2.drop(['stars_y','Unnamed: 0'], axis=1)
    return join2


def add_unique_users_per_bid(df): 
    bids = df['business_id'].unique()
    unique_users = {}
    for  i in bids: 
        bid_records = df.loc[df['business_id'] == i]
        unique_user_cnt = len(bid_records['user_id'].unique())
        unique_users[i] = unique_user_cnt 
    
    data = {'business_id': list(unique_users.keys()), 'unique user count': list(unique_users.values())}
    unique_cnt = pd.DataFrame.from_dict(data)
    df = pd.merge(df,unique_cnt,left_on=['business_id'],right_on =['business_id'])
    return df


def add_useful_funny_cool_cnt(df):
    #perhaps this needs to be weighted by a certain amount of records? 
    
    bids = df['business_id'].unique()
    engagement = {}
    
    for i in bids: 
        bid_records = df.loc[df['business_id'] == i]
        funny = bid_records['funny'].values
        useful = bid_records['useful'].values
        cool = bid_records['cool'].values
        avg_review_engagement = (sum(funny)+sum(useful)+sum(cool))/len(bid_records)
        engagement[i] = avg_review_engagement
        
    data = {'business_id': list(engagement.keys()), 'review engagement (useful,funny,cool)': list(engagement.values())}
    avg_reaction = pd.DataFrame.from_dict(data)
        
    df = pd.merge(df,avg_reaction,left_on=['business_id'],right_on =['business_id'])
    
    return df


def add_avg_star_rating(df):
    bids = df['business_id'].unique()
    avg_stars = {}
    
    for i in bids:
        bid_records = df.loc[df['business_id'] == i]
        
        stars = bid_records['stars'].values
        stars_average = sum(stars)/len(stars)
        avg_stars[i] = stars_average
        
    data = {'business_id': list(avg_stars.keys()), 'avg star rating per business review': list(avg_stars.values())}
    avg_stars_per_bid = pd.DataFrame.from_dict(data)
        
    df = pd.merge(df,avg_stars_per_bid,left_on=['business_id'],right_on =['business_id'])
    
    return df 

def add_num_tips_per_bid(df):
    bids = df['business_id'].unique()
    tips_dict = {}
    
    for i in bids:
        bid_records = df.loc[df['business_id'] == i]
        
        tips = bid_records['tips_text'].values
        num_of_tips = len(tips)
        tips_dict[i] = num_of_tips
        
    data = {'business_id': list(tips_dict.keys()), 'number of tips per bid': list(tips_dict.values())}
    num_tips_per_bid = pd.DataFrame.from_dict(data)
        
    df = pd.merge(df,num_tips_per_bid,left_on=['business_id'],right_on =['business_id'])
    
    return df  


def add_num_likes_for_tips_per_bid(df):
    bids = df['business_id'].unique()
    likes_dict = {}
    
    for i in bids:
        bid_records = df.loc[df['business_id'] == i]
        
        likes = bid_records['likes'].values
        num_of_likes = sum(likes)
        likes_dict[i] = num_of_likes
        
    data = {'business_id': list(likes_dict.keys()), 'total number of likes for tips per bid': list(likes_dict.values())}
    num_likes_per_bid = pd.DataFrame.from_dict(data)
        
    df = pd.merge(df,num_likes_per_bid,left_on=['business_id'],right_on =['business_id'])
    
    return df  
    

