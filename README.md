# Anime-Data-Scraper
Anime Data Scrapers is repository with are two web scraping applications that scrap from [GogoAnime](http://gogoanime.io/) and [Anime News Network](https://www.animenewsnetwork.com/). 

## anime_scraper.py
This allow users to search the details and be provided the links to the anime they search. The data is scraped from [GogoAnime](http://gogoanime.io/) and then asks the user if they also want links to the anime. The demo for how it works is show below:

[![Anime Scraper](https://res.cloudinary.com/marcomontalbano/image/upload/v1617791426/video_to_markdown/images/google-drive--1Gbn4DCdHzodJc38BZDj719bg0wdVAQIy-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://drive.google.com/file/d/1Gbn4DCdHzodJc38BZDj719bg0wdVAQIy/view?usp=sharing "Anime Scraper")

## underrated_anime_scraper.py
This allows users to scrap underrated anime from  [Anime News Network](https://www.animenewsnetwork.com/) and convert it into JSON and save it as a separate JSON file. This scraper was used while building Anime Plug API that allows users to get underrated anime from a over a choice of 500.

### Sample JSON that was converted

```json
{
        "title": "Space Battleship Yamato 2199 Chapter 7: Soshite Kan wa Iku (movie)",
        "source": "https://www.animenewsnetwork.com/encyclopedia/anime.php?id=15552",
        "rating": "7.94"
}
