import requests
import pandas as pd
from bs4 import BeautifulSoup

class WeatherScraper:
    def __init__(self, url):
        self.url = url
    
    def scrape_weather_data(self):
        website_url = requests.get(self.url).text
        soup = BeautifulSoup(website_url, 'html.parser')
        
        # Assuming the table with weather data has a specific class or ID
        weather_table = soup.find('table', {'id': 'wt-his'})
        
        if weather_table:
            # Extracting weather data from the table
            rows = weather_table.find_all('tr')
            data = []
            for row in rows[1:]:  # Skip the header row
                cols = row.find_all(['th', 'td'])  # Including both th and td tags
                cols = [col.text.strip() for col in cols]
                data.append(cols)
            
            # Creating a DataFrame with the weather data
            df = pd.DataFrame(data[1:], columns=data[0])  # Assigning the first row as column headers
            
            return df
        else:
            print("Weather table not found.")
            return None

# Example usage:
weather_url = "https://www.timeanddate.com/weather/usa/new-york/historic"
weather_scraper = WeatherScraper(weather_url)
weather_data = weather_scraper.scrape_weather_data()

if weather_data is not None:
    print(weather_data)

