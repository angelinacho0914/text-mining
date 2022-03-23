import urllib.request

url = 'https://www.gutenberg.org/ebooks/15489.txt.utf-8'
response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
text = data.decode('utf-8')
print(text) # for testing