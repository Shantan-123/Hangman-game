# URL Shortner 

import random
import string

class URLShortener:
    def __init__(self):
        self.url_dict = {}

    def shorten_url(self, long_url):
        short_url = self.generate_short_url()
        self.url_dict[short_url] = long_url
        return short_url

    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(6))

    def redirect_url(self, short_url):
        if short_url in self.url_dict:
            return self.url_dict[short_url]
        else:
            return "URL not found."


# Example usage:
url_shortener = URLShortener()
long_url = "https://www.example.com"
short_url = url_shortener.shorten_url(long_url)
print("Shortened URL:", short_url)
original_url = url_shortener.redirect_url(short_url)
print("Original URL:", original_url)
