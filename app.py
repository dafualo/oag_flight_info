import requests 
import os

my_api_key = os.environ.get("RAPIDKEY")
url = "https://flight-info-api.p.rapidapi.com/status"

querystring = {"version":"v2","DepartureDateTime":"2024-06-14","ArrivalDateTime":"2024-06-14","CarrierCode":"AC","FlightNumber":"799","CodeType":"IATA"}

headers = {
	"x-rapidapi-key": f"{my_api_key}",
	"x-rapidapi-host": "flight-info-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
print("HTTP Status Code: ", response.status_code)

data = response.json()
#print(response.json())

airline = data['data'][0]['carrier']['iata']
flight_num = data['data'][0]['flightNumber']
depart_airport = data['data'][0]['departure']['airport']['iata']
depart_time = data['data'][0]['departure']['time']['local']
depart_date = data['data'][0]['departure']['date']['local']
arrive_airport = data['data'][0]['arrival']['airport']['iata']
arrive_time = data['data'][0]['arrival']['time']['local']
arrive_date = data['data'][0]['arrival']['date']['local']

print(f"Flight {airline}{flight_num} is estimated to depart {depart_airport} on {depart_date} at {depart_time} (local) and arrive at {arrive_airport} on {arrive_date} at {arrive_time} (local).")
