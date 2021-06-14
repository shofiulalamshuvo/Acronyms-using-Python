#importing package
import city as city
import requests

#input the city name
city = input('Input the city name: ')
print(city)

#Display the output
print('Displaying Weather report for: '+ city)

#fetch waather details
url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)

#show the result
print(res.text)


