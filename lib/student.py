#!/usr/bin/env python

from user import User

knowledge = []

class Student(User):

    def __init__(self,first_name,last_name):
        super().__init__(first_name, last_name)
        self.knowledge= knowledge
    
    def learn(self, knowledge_detail):
        self.knowledge.append(knowledge_detail)
        