import requests
from send_email import send_email

topic = "tesla"

api_key = "b5a7660624324cf4a08a09f097a11d2e"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-01-09&" \
      "sortBy=publishedAt&" \
      "apiKey=b5a7660624324cf4a08a09f097a11d2e&language=en"

# making request
request = requests.get(url)

# getting request as dictionary
content = request.json()

# Accessing article title and description
body = " "
for article in content["articles"][:10]:
    if article["title"] is not None:
        body = "Subject: Today's News"+ "\n" \
               + body + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)