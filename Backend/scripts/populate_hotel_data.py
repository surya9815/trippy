import csv, random 
from datetime import datetime
from Backend.pricecomp.models import Hotel, Pricing, City

"""
Load the Hotels_data.csv and Populate the DB with Data.
        {'': '1', 'CityName': 'Mumbai', 'Population': '12442373', 'CityRank': '0', 'IsMetroCity': '1', 'IsTouristDestination': '1', 
         'IsWeekend': '1', 'IsNewYearEve': '0', 'Date': 'Dec 18 2016', 'HotelName': 'Vivanta by Taj', 'RoomRent': '12375',
         'StarRating': '5', 'Airport': '21', 'HotelAddress': '90 Cuffe Parade, Colaba, Mumbai, Maharashtra', 
         'HotelPincode': '400005', 'HotelDescription': 'Luxury hotel with spa, near Gateway of India', 'FreeWifi': '1', 
         'FreeBreakfast': '0', 'HotelCapacity': '287', 'HasSwimmingPool': '1'}
"""

def populate_db_with_hotel_data():
    with open("/Users/suryanshthakur/Desktop/Personal Projects/TrippyFinal/hotels_data.csv",'r') as file:
        reader = csv.DictReader(file)
        # {'': '1', 'CityName': 'Mumbai', 'Population': '12442373', 'CityRank': '0', 'IsMetroCity': '1', 'IsTouristDestination': '1', 
        #  'IsWeekend': '1', 'IsNewYearEve': '0', 'Date': 'Dec 18 2016', 'HotelName': 'Vivanta by Taj', 'RoomRent': '12375',
        #  'StarRating': '5', 'Airport': '21', 'HotelAddress': '90 Cuffe Parade, Colaba, Mumbai, Maharashtra', 
        #  'HotelPincode': '400005', 'HotelDescription': 'Luxury hotel with spa, near Gateway of India', 'FreeWifi': '1', 
        #  'FreeBreakfast': '0', 'HotelCapacity': '287', 'HasSwimmingPool': '1'}
        for row in reader:
            # Check if the city already exists or create a new one
            city,city_created = City.objects.get_or_create(
                name = row.get('CityName'),
                defaults={
                    'country' : 'India',
                    'population' : int(row.get('Population',0)),
                    'rank' : int(row.get('CityRank',0)),
                    'airport_num' : int(row.get('Airport',0)),
                    'is_metro_city' : bool(int(row.get('IsMetroCity',0))),
                    'is_tourist_destination' : bool(int(row.get('IsTouristDestination',0)))
                }
            )
            # Check if a hotel with the same name and address already exists
            hotel, hotel_created = Hotel.objects.get_or_create(
                name = row.get('HotelName'),
                address = row.get('HotelAddress'),
                pincode = row.get('HotelPincode'),
                defaults={
                    'hotel_city' : city,
                    'description' : row.get('HotelDescription'),
                    'star_rating' : float(row.get('StarRating',0)),
                    'airport_dist' : float(row.get('Airport',0)),
                    'free_wifi' : bool(int(row.get('FreeWifi',0))),
                    'free_breakfast' : bool(int(row.get('FreeBreakfast',0))),
                    'hotel_capacity' : bool(int(row.get('HotelCapacity',0))),
                    'has_swimming_pool' : bool(int(row.get('HasSwimmingPool',0))),
                }
            )
            price_date = datetime.strptime(row.get('Date'),'%b %d %Y').date()
            room_type = random.choice(["Super Deluxe", "Presidential Suite", "Deluxe Room","Executive Room"])
            pricing, pricing_created = Pricing.objects.create(
                        hotel = hotel,
                        room_type = room_type,
                        date = price_date,
                        price = float(row.get('RoomRent')),
                        is_weekend = bool(int(row.get('IsWeekend',0))),
                        is_new_year_eve = bool(int(row.get('IsNewYearEve',0)))
            )

                
if __name__ == "__main__":
    # This code will only be executed 
    # if the script is run as the main program
    populate_db_with_hotel_data()
