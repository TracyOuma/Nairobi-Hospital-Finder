​  🚑 Nairobi Hospital Finder
- ​This is a Python console application designed to help users quickly find hospitals within Nairobi County, Kenya, using the Google Maps Platform API.
- ​The application allows users to input a specific location within Nairobi (e.g., "Westlands," "CBD") and returns a list of nearby hospitals, including their addresses, contact information, and public reviews.
​
✨ Features
- ​Location-Specific Search: Finds hospitals near any user-defined location within Nairobi.
- ​Secure API Handling: Uses a .env file and the python-dotenv library to securely manage the Google Maps API Key.
- ​Geographical Validation: Checks that the input location is within Nairobi County before running the search.
- ​Detailed Results: Returns hospital name, address, contact, and recent reviews/ratings.

​ ⚙🔧 Setup and Installation
​Prerequisites
- ​You must have Python 3.6+ installed and an active Google Maps API Key with the Places API enabled.
 ​Local Setup:
- Clone your repository
- Install the needed dependencies: pip install googlemaps python-dotenv
- Then you configure environment variables: you create a .env file with the your actual API key

✏ How to run:
  - You now execute the script directly from your terminal: python [your_script_name].py
  - The application will prompt you to enter a location in Nairobi
▶ Code Structure
- Hospital Class: An OOP class that defines the structure of a hospital object, including properties like name, rating and a method to display reviews.
-  fetch_hospitals() function" this one handles the API interaction from geocoding the user's location to retrieving nearby places and fetching and detailed information.
