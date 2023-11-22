import pyshorteners

# Getting the the URL from the user
url_to_shorten = input("Enter the URL to shorten: ")

# Shortening the URL using the TinyURL 
s = pyshorteners.Shortener()
short_url = s.tinyurl.short(url_to_shorten)

print("Original URL:", url_to_shorten)
print("Shortened URL:", short_url)