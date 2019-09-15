#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:07:39 2019

@author: wuchenhao

to do
read database, strip white space, including start line
"""
import datetime

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()
        
    def load(self):
        self.file = open(self.filename, 'r')
        self.users = {}
        
        for line in self.file:
            email, password, firstName, createdDate = line.strip().split(';')
            self.users[email] = (password, firstName, createdDate)
            
        self.file.close()
        
    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1
        
    def add_user(self, email, password, firstName):
        if email.strip() not in self.users:
            self.users[email.strip()]=(password.strip(),firstName.strip(),DataBase.get_date())
            self.save()
            return 1
        else:
            print('Email exists already')
            return -1
    
    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False
        
    def save(self):
        with open(self.filename, 'w') as f:
            for user in self.users:
                f.write(user + ';' + self.users[user][0] + ';' + self.users[user][1] + ';' + self.users[user][2]+'\n')
    
    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(' ')[0]
            
        