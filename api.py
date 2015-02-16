#!/usr/bin/env python

# **************************************************************************************
"""
description = Unofficial nairaland API written in python.
author = Pystar
author_email = aitoehigie@gmail.com.
Date = 19/01/2013
Revised: June 2014, February 2015
"""

# **************************************************************************************

import requests

BOARDS = dict(
                        Technology=8, Programming=34,
                        software_programmer_market=76,
                        Webmasters=30, web_market=52, Computers=22,
                        computer_market=74, Phones=16,
                        phone_internet_market=75,
                        Graphics_video=45, graphics_video_market=51,
                        Technology_market=54, Entertainment=12, Jokes=15,
                        Tv_movies=4, satelite_tv_tech=58, Music_radio=3,
                        rap_battles=60, music_business=59, Celebrities=46,
                        Fashion=37, fashion_clothing_market=39, Events=7,
                        Sports=14, european_football=66, Gaming=10,
                        video_games_and_gadgets_for_sale=71, Forum_games=33,
                        Literature_writing=11, poems_for_review=36,
                        Pictures=81,
                        Nairaland_general=9, foreign_affairs=61,
                        ethnic_racial_or_sectarian_politics=40,
                        violent_disgusting_non_celebrity_crimes=1, Romance=21,
                        dating_and_meeting_zone=38, Business=24,
                        business_to_business=49, adverts=32, Jobs_vacancies=29,
                        Career=35, certification_and_training_adverts=62,
                        NYSC=79,
                        Education=13, educational_services=57, Autos=26,
                        Cartalk=78,
                        Properties=47, Health=19, Travel=2, travel_ads=77,
                        Family=5,
                        Culture=55, Religion=17, islam_for_muslims=44, Food=41,
                        Nairaland_ads=80
)
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36'

NAME = "nairaland username"
PASSWORD = "nairaland password"
ROOT_URL = "http://www.nairaland.com/"


def login(name=NAME, password=PASSWORD)
    #Nairaland login function
    login_params = dict(name = NAME, password = PASSWORD)
    session = requests.Session()
    user = session.post(ROOT_URL+"do_login", data=login_params)
    return user


