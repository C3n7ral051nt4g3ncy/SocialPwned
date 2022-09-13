#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

socialpwned = []

class SocialPwned:

    def __init__(self,id,name = "",linkedin = {},instagram = {},twitter = {},leaks = {"pwndb":[],"dehashed":[],"ghunt":{}}):
        
        self.id = id
        self.name = name
        self.linkedin = linkedin
        self.instagram = instagram
        self.twitter = twitter
        self.leaks = leaks

        socialpwned.append(self)

    def getTargets():
        return socialpwned

    def getListOfTargets():
        return json.loads(SocialPwned.toJSON())

    def toJSON():
        return json.dumps([ob.__dict__ for ob in socialpwned], default=lambda o: o.__dict__, indent=4)

    def create_json(self):
        socialpwned_json = f'{self}/socialpwned.json'
        with open(socialpwned_json, "w") as file:
            file.write(SocialPwned.toJSON())

    def checkID(self):

        targets = SocialPwned.getListOfTargets()
        return any(target.get("id") == self for target in targets)

    def updateLinkedin(self, linkedin_list):
        for pwn in socialpwned:
            if pwn.__dict__.get("id") == self:
                pwn.__dict__.get("linkedin").update(linkedin_list)
                return True
        return False

    def updateInstagram(self, instagram_list):
        for pwn in socialpwned:
            if pwn.__dict__.get("id") == self:
                pwn.__dict__.get("instagram").update(instagram_list)
                return True
        return False

    def updateTwitter(self, twitter_list):
        for pwn in socialpwned:
            if pwn.__dict__.get("id") == self:
                pwn.__dict__.get("twitter").update(twitter_list)
                return True
        return False

    def updateLeaksPwnDB(self, pwndb):

        for pwn in socialpwned:
            if pwn.__dict__.get("id") == self:
                pwn.__dict__.get("leaks")["pwndb"].append(pwndb)
                return True
        return False

    def updateLeaksDehashed(self, dehashed):
        for pwn in socialpwned:
            if pwn.__dict__.get("id") == self:
                pwn.__dict__.get("leaks")["dehashed"].append(dehashed)
                return True
        return False

    def updateLeaksGhunt(self, ghunt):
        for pwn in socialpwned:
            if pwn.__dict__.get("id") == self:
                pwn.__dict__.get("leaks").get("ghunt").update(ghunt)
                return True
        return False
