import googlemaps
import os
from dotenv import load_dotenv

load_dotenv()



def fetch_hospitals(location_query):

        try:
# Use google maps API to get the hospitals in Nairobi 
          
            API_KEY = os.environ['GOOGLE_MAPS_API_KEY']
           
        except KeyError:
            print("ERROR: Set the API_KEY environment variable")
            return[]
        
        gmaps = googlemaps.Client(key=API_KEY)

# Geocode the location to get coordinates biased to Knya
        try:
            geocode_result = gmaps.geocode(f'{location_query}, Nairobi', components={"country":"KE"})
            if not geocode_result:
                print(f"Could not find location coordinated for '{location_query}'")
                return[]
            
            loc_coords = geocode_result[0]['geometry']['location']
             
            # API  to find nearby hospitals
            places_result = gmaps.places_nearby(location=loc_coords, radius=5000, keyword='hospital') # 5 kilometers
            
            hospital_list = []
            for place in places_result.get('results',[]):
                details = gmaps.place(place_id=place['place_id'], fields= ['name', 'vicinity','formatted_phone_number','rating','user_ratings_total', 'reviews'])
                place_details = details.get('result',{})

                hospital_list.append({
                    'name':place_details.get('name','N/A'),
                    'address': place_details.get('vicinity', 'N/A'),
                    'contact': place_details.get('formatted_phone_number', 'N/A'),
                    'rating': place_details.get('rating'),
                    'reviews': place_details.get('reviews')
                })
                return hospital_list

        except Exception as e:
            print(f" An error occurred:{e}")
            return[]

class Hospital:
    def __init__(self,name,address,contact,rating = None,reviews = None,accepts_insurance = None):
        self.name = name
        self.address = address
        self.contact = contact
        self.rating = rating
        self.reviews = reviews or []
        self.accepts_insurance = accepts_insurance

    def __repr__(self):
        return f"Hospital(Name:{self.name}, Contact:{self.contact},Rating:{self.rating})"
    
    def display_reviews(self):
        if not self.reviews:
            print(" No reviews found!")
            return
        print(" Recent reviews:")
        for review in self.reviews[:4]:
            print(f" -Rating:{review.get('rating')} stars")
            print(f" Review:{review.get('text', 'N/A')}")
            print(f" Author:{review.get('author_name', 'Anonymous')}")
            print("-"  * 20)


    

 #Fetches real data and converts it into a list of Hospital objects.
    @staticmethod
    def get_hospitals_as_objects(location):
        hospital_data = fetch_hospitals(location)
        hospitals_to_display = []
        
        for data in hospital_data:
            hospital_object = Hospital(
                name=data['name'], 
                address=data['address'], 
                contact=data['contact'],
                rating=data['rating'],  # Pass the new data
                reviews=data['reviews'] # Pass the new data
            )
            hospitals_to_display.append(hospital_object)
        
        return hospitals_to_display



if __name__ == '__main__':
        

        print("--- Real Hospital Search (using Google Maps API) ---")
        location = input("Enter a location in Nairobi (e.g., Westlands, CBD): ")
    
        if not location:
            print("No location entered. Exiting.")
        else:
            found_hospitals = Hospital.get_hospitals_as_objects(location)
        
        if found_hospitals:
            print(f"\nFound {len(found_hospitals)} hospital(s) near {location}:")
            for hospital in found_hospitals:
                print(f"  - Name: {hospital.name}")
                print(f"    Address: {hospital.address}")
                print(f"    Contact: {hospital.contact}")
                print(f"    Rating: {hospital.rating} out of 5 stars")
                hospital.display_reviews()
                print("=" * 40)
        else:
            print(f"\nSorry, no hospitals found for '{location}'.")




        

            
            
            

       
            
        
    
    
    
    
    
        