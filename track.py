import requests

url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/masks.php"

headers = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': "9380b1a8cbmsh045570843e6285dp164dcajsn55eb7dd0bd51"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
