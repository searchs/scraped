import requests

source_url = 'https://quotes.toscrape.com/'
req = requests.get(source_url)
print("Status Code: ",req.status_code)
print("Encoding: ", req.encoding)
print("\n\tResponse Content: ", req.text)

