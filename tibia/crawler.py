from urllib.parse import urljoin
import json


class Crawler:
    def __init__(self, tibia_url, character, downloader):
        self.tibia_url = tibia_url
        self, downloader = downloader

    def get_tibia_information(self, character):
        character_url = urljoin(self.tibia_url, "community/?name=")
        params = self.config_params(character)

        response = self.downloader.post(character_url, data=params)

    def config_params(self, character):
        return {"name": character, "Submit.x": 0, "Submit.y": 0}