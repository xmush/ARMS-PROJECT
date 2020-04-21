import requests

from math import cos, asin, sqrt, pi

def distance(lat1, lon1, lat2, lon2):
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a))

url = "https://ipinfo.io/	140.213.6.160?token=208c90f8a6a063"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

# print(response.text.encode('utf8'))

# print(response.json())

point = response.json()['loc']
mycity = response.json()['city']
# lon = response.json()['longitude']
listloc = list(point.split(','))

print(listloc)
# print(response.text.encode('utf8'))


# import requests

url = "https://developers.zomato.com/api/v2.1/search?entity_type=city&q=Jakarta&count=5"

payload = {}
headers = {
  'Accept': 'application/json',
  'user-key': '8e946f7a6fa107e641d881c817edc669'
}

response = requests.request("GET", url, headers=headers, data = payload)

restoran = response.json()['restaurants']

# print(ty)

for i in range(len(restoran)) :

  lat = restoran[i]['restaurant']['location']['latitude']
  lon = restoran[i]['restaurant']['location']['longitude']


  lat1 = float(listloc[0])
  lon1 = float(listloc[1])

  lat2 = float(lat)
  lon2 = float(lon)

  jarak = distance(lat1, lon1, lat2, lon2)

  print('%s lat : %s, lon : %s => jarak : %f kilometer' % (restoran[i]['restaurant']['name'], lat, lon, jarak))



# print(len(restoran))

# print(response.text.encode('utf8'))