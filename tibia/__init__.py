from downloader import Downloader

class Character(Crawler):
    def __init__(self, Character):
        super()._init__("https://www.tibia.com/", Character, Downloader())