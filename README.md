# commute_info
Weather and traffic info about commute

I'm pulling info from OpenWeather and Google Maps

I use a file called private_info.py to store the values  
of my home and work zip code as well as my API keys.  
If you look at the variable names I import that will give you an idea  
of how to set up your variables.  
  
You will need the requests library. pip install requests

With how the OpenWeather API works I plan on having the  
program run in the morning to give me the "current" temp  
and the "high" which will be 6 hours from the "current"