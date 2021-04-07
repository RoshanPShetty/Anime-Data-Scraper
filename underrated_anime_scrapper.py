# Imports
from bs4 import BeautifulSoup
import requests
import json

# Retreives the html text from the link as a content
html_text = requests.get(
    'https://www.animenewsnetwork.com/encyclopedia/ratings-anime.php?top50=most_underrated&n=500').content

# Makes it a soup
soup = BeautifulSoup(html_text, 'html.parser')

# Initializing the data variable
data = []

# Finds all the rows in the table from the underrated anime page
rows = soup.find_all("tr")

# Counter
count = 0

# Looping through all the rows
for i in rows:

    # Avoiding the first two and last rows of the table as they don't contain the information we require
    if count > 1 and count < len(rows) - 1:

        # Getting the title of the anime from the row with the class t
        title = i.find("td", class_="t")

        # Getting the source of the anime from the title as given in the href
        source = title.find("a")

        # Getting the rating of the anime from the row with the class r
        rating = i.find("td", class_="r")

        # Appending all of these data in a key-value pair passed as a dicitionary to the data array
        data.append({"title": title.text, "source": "https://www.animenewsnetwork.com" +
                     source['href'], "rating": rating.text})

    # Incrementing count for each iteration
    count += 1

# Converting arrary with the dictionary into JSON and "dumping" all the data into a newly created JSON file
with open("anime.json", "w") as f:
    json.dump(data, f, indent=4)
