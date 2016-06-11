#!/usr/bin/env python

# **************************************************************************************
"""
description = Unofficial nairaland API written in python.
version = 0.9.1
author = Pystar
author_email = aitoehigie@gmail.com.
Date = 19/01/2013
Revised: June 2014, February 2015, June 2015
"""

# **************************************************************************************

import requests
from splinter import Browser
browser = Browser("zope.testbrowser")

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
HEADERS = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/41.0.2228.0 Safari/537.36"
headers = {"User-Agent": HEADERS}

NAME = "nairaland username"
PASSWORD = "nairaland password"
ROOT_URL = "http://www.nairaland.com/"


class NairalandUser():
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.payload = dict(name=self.name, password=self.password)
        self.login()

    def login(self):
        self.user = requests.Session()
        self.user.post(ROOT_URL+"do_login", data=self.payload, headers=headers)
        return self.user

    def logout(self):
        self.payload = self.user.cookies["session"]
        self.user.post(ROOT_URL+"do_logout", data=self.payload, headers=headers)

    def postNewTopic(self, title, body, board):
        self.payload = dict(title=title, body=body, board=board, session=self.user.cookies["session"])
        self.user.post(ROOT_URL+"do_newtopic", data=self.payload, headers=headers)

#   def editProfile(self):
#         self.user.post(ROOT_URL+"do_editprofile", data=payload, headers=headers)

#   def changeEmail(self, newEmail):
#       self.payload = dict(email=newEmail, session=self.user.cookies["session"])
#       self.user.post(ROOT_URL+"do_changeemail_", data=self.payload, headers=headers)
#       TODO incomplete functionality

    def changePassword(self, oldPassword, newPassword):
        self.payload = dict(oldpassword=oldPassword, password=newPassword, password2=newPassword, session=self.user.cookies["session"])
        self.user.post(ROOT_URL+"do_changepass", data=self.payload, headers=headers)

    def followMember(self, memberid=None, username=None):
        self.payload = dict(session=self.user.cookies["session"], member=memberid, redirect="%2F"+username)
        self.user.post(ROOT_URL+"do_followmember", data=self.payload, headers=headers)

    def deactivateAccount(self):
        self.payload = dict(session=self.user.cookies["session"])
        self.user.post(ROOT_URL+"send_confirmation_email_for_account_deactivation", data=self.payload, headers=headers)
        self.user.post(ROOT_URL+"do_send_confirmation_email_for_account_deactivation", data=self.payload, headers=headers)

    def editProfile(self):
        pass


if __name__ == "__main__":
    NairalandUser(USERNAME, PASSWORD)
