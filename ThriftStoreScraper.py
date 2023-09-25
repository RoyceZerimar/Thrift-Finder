# Scraper for the Thrift Store App
import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = "https://www.thethriftshopper.com/Thrift-Stores/Spokane/WA"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    print("request was successful")

    # Find all the containers that hold thrift store information
    store_info_containers = soup.find_all('div', class_='col-md-9')

    for container in store_info_containers:
        # Extract store name
        store_name = container.find('a', title='View Profile')
        if store_name:  # Check if the name is not empty
            if store_name != "View Profile":
                st_name = store_name.text.strip()
                print(st_name)

            else:
                continue  # Skip if the store name is not found

            # Extract rating
        rating_element = container.find('div', class_='rating')
        if rating_element:
            numeric_rating = rating_element.text.strip()
            numeric_rating = numeric_rating.split('(')[0].strip()
            print(numeric_rating)
        else:
            numeric_rating = "N/A"


else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
