# commute_info
Weather and traffic info about morning and afternoon commute  
It is assumed this will be run in the morning  
If you run in afternoon or night logic doesn't quite work  

I'm pulling info from OpenWeather and Google Maps
I'm using gmail to send the email

I use a file called private_info.py to store the values  
Values needed:  
    home_zip = "XXXXX" (for weather)
    home_address = "123+n+example+street+los+angeles+ca" (for travel)
    work_zip = "XXXXX" (for weather)
    work_address = "456+s+fake+road+los+angeles+ca" (for travel)
    weather_api_key = "XXXXXXXXXXXXX" (OpenWeather)
    maps_api_key = "XXXXXXXXXXXX" (Google Maps)
    sender_email = 'example@gmail.com'
    receiver_email = 'example@gmail.com'
    password = 'xxxxxxxxxx'
To use gmail you need to create an app password

With how the OpenWeather API works I plan on having the  
program run in the morning to give me the "current" temp  
and the "high" which will be 6 hours from the "current"