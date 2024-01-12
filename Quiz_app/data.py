import requests
import html

parameters = {
    "amount": 10,
    "type": "boolean"
}

question_data = []

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

for item in response.json()['results']:
    item['question'] = html.unescape(item['question'])
    question_data.append(item)
