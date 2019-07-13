import json
import time
import urllib.request

API = 'OVuvfLGQQKBLiU4dbZ4IUZRPMMaUEe9u'
countryCode = 'VN'
city        = 'Hanoi'

key = ""

def getLocation(countryCode, city):
    search_address="http://dataservice.accuweather.com/locations/v1/cities/"+ countryCode +"/search?apikey=OVuvfLGQQKBLiU4dbZ4IUZRPMMaUEe9u&q="+ city +"&details=true"

    with urllib.request.urlopen(search_address) as search_address:
        data = json.loads(search_address.read().decode())
    
    location_key = data[0]['Key']
    return location_key

key = getLocation(countryCode,city)

def getForecast(location_key):
    day_count = 0
    five_days_forecast_url = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/"+ location_key +"?apikey=OVuvfLGQQKBLiU4dbZ4IUZRPMMaUEe9u&details=true"
    
    with urllib.request.urlopen(five_days_forecast_url) as five_days_forecast_url:
        data = json.loads(five_days_forecast_url.read().decode())
        # !!!!!!! Để xem data có những dữ liệu gì
        # print(data)     

    for _ in data['DailyForecasts']:
        day_count += 1
        print(str(_['Date']) + '\nDay', day_count)
        print(_['Temperature']['Minimum']['Value'], end=" - ")
        print(_['Temperature']['Maximum']['Value'])
        print('Rain Prob:' + str(_['Day']['RainProbability']), end=", ")
        print('Snow Prob:' + str(_['Day']['SnowProbability']))

        print(_['Day']['IconPhrase'], end = ' - ')
        print(_['Day']['LongPhrase'])
        print(_['Day']['Wind']['Speed']['Value'])
        print(_['Day']['Wind']['Direction']['English'])
        print(_['Night']['IconPhrase'], end = ' - ')
        print(_['Night']['LongPhrase'])
        print(_['Night']['Wind']['Speed']['Value'])
        print(_['Night']['Wind']['Direction']['English'])
        

getForecast(key)    
