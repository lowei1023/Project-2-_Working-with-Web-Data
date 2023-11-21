import pandas as pd
import requests
from io import StringIO
from urllib.parse import urljoin

class SitemapParser:
    """
    A class to parse sitemaps from robots.txt and create a DataFrame.

    Args:
    base_url (str): The base URL of the website.

    Methods:
    parse_sitemap(): Parses sitemaps from robots.txt into a DataFrame.
    """

    def __init__(self, base_url):
        self.base_url = base_url

    def parse_sitemap(self):
        """
        Parses sitemaps from robots.txt and creates a DataFrame.

        Returns:
        pandas.DataFrame: Combined DataFrame of parsed sitemaps.
        """
        robots_url = urljoin(self.base_url, '/robots.txt')
        response = requests.get(robots_url)

        if response.status_code == 200:
            sitemap_urls = [line.split(': ')[1].strip() for line in response.text.split('\n') if line.startswith('Sitemap')]
            dfs = []

            for sitemap_url in sitemap_urls:
                sitemap_response = requests.get(sitemap_url)

                if sitemap_response.status_code == 200:
                    data = StringIO(sitemap_response.text)
                    df = pd.read_xml(data)
                    dfs.append(df)

            if dfs:
                combined_df = pd.concat(dfs, ignore_index=True)
                return combined_df
            else:
                return pd.DataFrame()
        else:
            print(f"Failed to fetch robots.txt from {self.base_url}")
            return pd.DataFrame()

# Usage
parser = SitemapParser('https://www.eia.gov/')
sitemap_df = parser.parse_sitemap()
print(sitemap_df)  # Displaying the  rows of the combined DataFrame