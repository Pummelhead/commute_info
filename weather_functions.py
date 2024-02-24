import requests
from private_info import home_zip, work_zip, weather_api_key

def make_weather_home_call():
    api_endpoint = f"https://api.openweathermap.org/data/2.5/forecast?zip={home_zip}&appid={weather_api_key}&units=imperial"
    home_weather_response = requests.get(api_endpoint)
    if home_weather_response.status_code == 200:
        print("Home Weather Pull Completed")
        home_weather_data = home_weather_response.json()
        current_temp_home = home_weather_data["list"][0]["main"]["temp"]
        max_temp_home = home_weather_data["list"][2]["main"]["temp"]
        home_location = home_weather_data["city"]["name"]
        return home_location, current_temp_home, max_temp_home
    else:
        print(f"Error: {home_weather_response.status_code}")
        return None  

def make_weather_work_call():
    api_endpoint = f"https://api.openweathermap.org/data/2.5/forecast?zip={work_zip}&appid={weather_api_key}&units=imperial"
    work_weather_response = requests.get(api_endpoint)
    if work_weather_response.status_code == 200:
        print("Work Weather Pull Completed")
        work_weather_data = work_weather_response.json()
        current_temp_work = work_weather_data["list"][0]["main"]["temp"]
        max_temp_work = work_weather_data["list"][2]["main"]["temp"]
        work_location = work_weather_data["city"]["name"]
        return work_location, current_temp_work, max_temp_work
    else:
        print(f"Error: {work_weather_response.status_code}")
        return None

if __name__ == "__main__":
    print(make_weather_home_call())
    print(make_weather_work_call())