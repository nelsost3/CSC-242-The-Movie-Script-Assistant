# Steven Nelson, Programmer
# October 16th, 2022
# CSC 242 Lab 08


class MovieScript(object):
    # begin the class definition
    # declare a data element as a list
    script = []

    # the class constructor
    def __init__(self):
        # pass
        print(" ")  #"A class object has been constructed\n"

    # a class member function
    def getScript(self):
        return self.script

    # a class member function
    def setScript(self, s):
        script = s

    # end the class definition