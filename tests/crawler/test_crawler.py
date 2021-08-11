from tibia.crawler import Crawler
from tibia.crawler import Downloader


def teste_tibia_search_character():
    crawler = Crawler("https://www.tibia.com/", "Bobo", Downloader())
