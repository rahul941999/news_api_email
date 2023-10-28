import requests
import Send_email


topic = input("Enter the topic that you want news on : ")
api_key = "b7c2eeefffd7454faee79aca01023787"
url = (f"https://newsapi.org/v2/everything?q={topic}"
       f"&from=2023-09-28"
       f"&sortBy=publishedAt"
       f"&apiKey={api_key}"
       f"&language=en")

req = requests.get(url)
content = req.json()
message = ""
for item in content["articles"][:20]:
    message = message + item["title"] + "\n" + item["url"] + '\n\n'

Send_email.send(subject=topic + " news", txt=message)
