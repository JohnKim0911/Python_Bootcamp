import pandas
import requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4
from datetime import date

# Web to scrape
URL = "https://www.billboard.com/charts/hot-100/"

# Get html from the web
response = requests.get(URL)
website_html = response.text

# Convert html to BeautifulSoup
soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())

# Get titles
titles_temp = soup.css.select("div.o-chart-results-list-row-container h3.c-title.a-no-trucate")
titles = [title.getText().strip() for title in titles_temp]
# print(titles)

# Get singers
singers_temp = soup.css.select("div.o-chart-results-list-row-container span.c-label.a-no-trucate")
singers = [singer.getText().strip() for singer in singers_temp]
# print(singers)

# Rank
rank = [index + 1 for index in range(100)]

# Make a Chart dictionary
data_dict = {
    "Rank": rank,
    "Title": titles,
    "Singer": singers
}

# Create a dataframe using Pandas
df = pandas.DataFrame(data_dict)
# print(df)

# Get today's date
today = str(date.today())

# Save data to csv format
result_csv = f"Billboard Hot 100_{today}.csv"
df.to_csv(result_csv)