'''this is a class devloped to help youtubers organize there keywords'''
import os
import sys # you will need these two modules
class helper:
    def __init__(self):
        '''initialzing the class'''
        self.keyword = {}
        self.key = []
        self.keyword["Keyword"] = []
        self.key.append("Keyword")
        print("Hello youtuber I am the youtube keyword planner but you can call me helper if you would like.")
        print("I was created to make your youtube keyword research less of a head ache.")
        print("I do this by keeping track of all your keyword scores from different databases for each video")
        print("after we gather all of the scores you will then have the ability to sort the keywords by the given databases you have"
              " provided")
        print("or if you would like you may also find the top keywords you have given as well")
        print("OOOO I also have the ability to export the keywords in a comma seperated value format so that you can copy those keywords"
              "straight in to youtuber")
        print("that was a mouth full")
        while (True):
            try: # asking python to please try to let this run
                count = int(input("with all of that being said how many databases will we be using today ")) #this is the line that python will try
                break # if the line above is sucesfull this line will run
            except ValueError:
                print("Please enter a number not a character")
        for i in range(count):
            databases = input("what is the name a database we will be looking at today ")
            self.keyword[databases] = []
            self.key.append(databases)
    def clear_line(self):
        '''this is the function where you will be able to clear the screen'''
        user = input("type yes to clear the screen otherwise enter any key to continue ")
        if (user.upper() == "YES"):
            if (sys.platform == "win32"): # allows you to have the ability to tell what operating system you are running
                os.system("cls") #allows you to print that command directly into the system
            else:
                os.system("clear")
    def insert(self):
        print("Hello Youtuber now that we have the databases that you will be using why dont we start adding some keywords")
        size = 0
        count = 0
        # user_decsion = input("is there a specifc number of keywords you would like to enter please type yes if there is or any key if not")
        # if (user_decsion.upper() == "YES"):
        #     size = int(input("how many keywords will you be entering"))
        # we are going to convert this to a more efficient way
        try:
            user_decsion = int(input("enter the specific number of keywords you would like to enter\n"
                "if you do not have a specific number of keywords you would like to enter press any character "))
            size = user_decsion
        except ValueError:
            user_decsion = None
        keep_going = True
        while(keep_going):
            for key in self.key:
                if key == "Keyword":
                    self.keyword[key].append(input("what keyword will you like to enter "))
                else:
                    while(True):
                        try:
                            self.keyword[key].append(int(input(f"what is the score from {key} for that keyword ")))
                            break
                        except ValueError:
                            print("please enter a number")
            if(user_decsion is None):
                user_decsion = input("please type no if you have no more keywords you would like to add otherwise press"
                                     " any key to contine ")
                if (user_decsion.upper() == "NO"):
                    keep_going = False
                else:
                    user_decsion = None
            if(size == count+1):
                print("seems you have reached your keyword limit")
                keep_going = False
            if(size>0):
                count+=1
    def driver(self):
        self.clear_line()
        self.insert()