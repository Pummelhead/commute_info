from weather_functions import make_weather_home_call, make_weather_work_call
from traffic_functions import make_traffic_call
from email_functions import send_email

def main():
    home_location, current_temp_home, current_weather_home, six_hour_temp_home, six_hour_weather_home = make_weather_home_call()
    work_location, current_temp_work, current_weather_work, six_hour_temp_work, six_hour_weather_work = make_weather_work_call()
    trip_duration = make_traffic_call()

    body = f'''
            The current temperature at {home_location} is: {current_temp_home}
            The current weather at {home_location} is: {current_weather_home}
            The current temperature at {work_location} is: {current_temp_work}
            The current weather at {work_location} is: {current_weather_work}
            Your commute if you leave now will be: {trip_duration}
            ----------------------------------------------------------------------------------------
            The temperature when you leave {work_location} will be: {six_hour_temp_work}
            The weather when you leave {work_location} will be: {six_hour_weather_work}
            The temperature when you get home to {home_location} will be: {six_hour_temp_home}
            The weather when you get home to {home_location} will be: {six_hour_weather_home}
            '''

    if current_temp_home >= 50 and current_temp_work >= 50:
        warm_enough = True
    else:
        warm_enough = False

    if current_weather_home == "shower rain" or "thunderstorm" or "snow":
        home_weather_good_now = False
    else:
        home_weather_good_now = True

    if current_weather_work == "shower rain" or "thunderstorm" or "snow":
        work_weather_good_now = False
    else:
        work_weather_good_now = True

    if six_hour_weather_home == "shower rain" or "thunderstorm" or "snow" or "rain":
        home_weather_six_hour_good = False
    else:
        home_weather_six_hour_good = True

    if six_hour_weather_work == "shower rain" or "thunderstorm" or "snow" or "rain":
        work_weather_six_hour_good = False
    else:
        work_weather_six_hour_good = True

    if warm_enough and home_weather_good_now and work_weather_good_now and home_weather_six_hour_good and work_weather_six_hour_good:
        subject = "IT'S A MOTORCYCLE DAY!"
    elif current_temp_home >=40 and current_temp_home <50 and home_weather_good_now and work_weather_good_now and home_weather_six_hour_good and work_weather_six_hour_good:
        subject = "It's a cold one today. Bundle up on the bike!"
    elif warm_enough and not home_weather_good_now or not work_weather_good_now or not home_weather_six_hour_good or not work_weather_six_hour_good:
        subject = "Weather is looking rough but warm. May want to drive today."
    else:
        subject = "Unfortunately you will have to use 4 wheels today."

    send_email(subject, body)


if __name__ == "__main__":
    main()