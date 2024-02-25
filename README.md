# commute_info
Weather and traffic info about commute

I'm pulling info from OpenWeather and Google Maps

I use a file called private_info.py to store the values  
Values needed:  
    home_zip = "XXXXX" (for weather)
    home_address = "123+n+example+street+los+angeles+ca" (for travel)
    work_zip = "XXXXX" (for weather)
    work_address = "456+s+fake+road+los+angeles+ca" (for travel)
    weather_api_key = "XXXXXXXXXXXXX" (OpenWeather)
    maps_api_key = "XXXXXXXXXXXX" (Google Maps)
  
You will need the requests library. pip install requests

With how the OpenWeather API works I plan on having the  
program run in the morning to give me the "current" temp  
and the "high" which will be 6 hours from the "current"