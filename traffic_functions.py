import requests
from private_info import maps_api_key, home_address, work_address

def make_traffic_call():
    api_endpoint = f"https://maps.googleapis.com/maps/api/directions/json?departure_time=now&destination={work_address}&origin={home_address}&key={maps_api_key}"
    traffic_response = requests.get(api_endpoint)
    if traffic_response.status_code == 200:
        print("Traffic Pull Completed")
        traffic_data = traffic_response.json()
        trip_duration = traffic_data["routes"][0]["legs"][0]["duration"]["text"]
        return trip_duration
    else:
        print(f"Error: {traffic_response.status_code}")
        return None
    

if __name__ == "__main__":
    print(make_traffic_call())