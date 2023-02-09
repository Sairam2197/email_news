import requests

api_key = "b5a7660624324cf4a08a09f097a11d2e"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-01-09&" \
      "sortBy=publishedAt&api" \
      "Key=b5a7660624324cf4a08a09f097a11d2e"

# making request
request = requests.get(url)

# getting request as dictionary
content = request.json()

# Accessing article title and description
for article in content['articles']:
    print(article["title"])
    print(article['description'])
    print(article["author"])
