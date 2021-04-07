# Imports
import os
import requests
from bs4 import BeautifulSoup

# Title and url array initialized to being empty
title = []
url = []


# Function to print the anime and it's details by parsing through the html tags to get the title and body information and prints them of each line
def details(custome_url):
    source_code = requests.get("https://www10.gogoanime.io"+custome_url)
    content = source_code.content
    soup = BeautifulSoup(content, 'html.parser')
    container_soup = soup.find('div', {'class': 'anime_info_body_bg'})
    print("\nName of the Anime : ", container_soup.find('h1').getText(), "\n")
    titles_detail = container_soup.find_all('p', {'class': 'type'})
    for elem in titles_detail:
        print(elem.getText())
        print("\n")


# Function that finas all the matching values for the div and image tag and then appends the information to the title and url arrays
def get_details(soup):
    raw_soup = soup.find_all('div', {"class": 'img'})
    for item in raw_soup:
        temp_soup = item.find('a')
        title.append(temp_soup['title'])
        url.append(temp_soup['href'])


# Function that would print all the possible links by using the title array
def get_url(title, custom_url):
    print("Links: \n")
    for i in range(len(title)):
        print("%d. %s : https://www10.gogoanime.io%s\n" %
              (i+1, title[i], custom_url[i]))


# Function to take user input for the name of the anime and whether they want the details pr
def entry():
    anime_name = input("[+] Enter the name of the Anime : ")
    search_url = (
        "https://www10.gogoanime.io//search.html?keyword=" + anime_name)
    html_text = requests.get(search_url)
    content = html_text.content
    global soup
    soup = BeautifulSoup(content, features="html.parser")
    choice = input(
        "[+] Do you want also want the links? (y/n): ")
    if choice.lower() == "n":
        get_details(soup)
        details(url[0])
    elif choice.lower() == "y":
        get_details(soup)
        details(url[0])
        get_url(title, url)
    else:
        print("[-] Enter a valid choice.")


# Calling the entry fucntion for user input
if __name__ == "__main__":
    entry()
