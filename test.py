from bs4 import BeautifulSoup
import requests
from page import Page  # assuming Page is the class that contains your analyze methods

# URL of the page you want to test
url = "https://gamingrevealed.com"

# Fetch the page content
response = requests.get(url)
html_content = response.text

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Convert the BeautifulSoup object to a string
soup_str = str(soup)

# Create a Page object and analyze the page
page = Page(url)
page.analyze(soup_str)

# Print the results
print(page.headings)
print(page.links)
# ... print any other data you're interested in
