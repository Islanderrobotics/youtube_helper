'''this is a class devloped to help youtubers organize there keywords'''
import os
import sys # you will need these two modules
from colorama import Back,Fore,init
from islander_sort import Islander_sort
class helper:
    def __init__(self):
        '''initialzing the class'''
        self.keyword = {}
        self.key = []
        self.keyword["Keyword"] = []
        self.key.append("Keyword")
        self.number_of_char = 0 # this is going to be used in the new function
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
    def size(self,number):
        '''this function is going to be used to allow the user to know how many chracters they have left'''
        self.number_of_char+=number
        percent_full = self.number_of_char/self.total
        character_left = self.total-self.number_of_char
        if (percent_full >=1):
            print("Sorry creator but you have reached your character limit")
            return False
        elif (percent_full>=0.75):
            print(f"{Fore.RED}{Back.RED} |||||||||||||||||||||||||||||||||||||||||||||||||||| {Back.RESET} you have {character_left} left")

        elif (percent_full>0.50):

            print(f"{Fore.YELLOW}{Back.YELLOW} |||||||||||||||||||||||||||||||||||||||||||||||||||| {Back.RESET} you have {character_left} left")
        elif (percent_full >= 0.25):

            print(f"{Fore.MAGENTA}{Back.MAGENTA} |||||||||||||||||||||||||||||||||||||||||||||||||||| {Back.RESET} you have {character_left} left")
        elif (percent_full >=0.0):

            print(f"{Fore.GREEN}{Back.GREEN} |||||||||||||||||||||||||||||||||||||||||||||||||||| {Back.RESET} you have {character_left} left")
        return True
    def insert(self):
        print("Hello Youtuber now that we have the databases that you will be using why dont we start adding some keywords")
        size = 0
        count = 0
        try:
            self.total = int(input("the default character limit is 500 enter any character to continue, or enter the character limit you would like "))
        except ValueError:
            self.total = 500
        try:
            user_decsion = int(input("enter the specific number of keywords you would like to enter\n"
                "if you do not have a specific number of keywords you would like to enter press any character "))
            size = user_decsion
        except ValueError:
            user_decsion = None
        keep_going = True
        print("the bar bellow represents how many character you have left\n"
            "green means you are good, magenta means you have filled 25% of your limit\n"
            "yellow means your character limit is halfway full\n"
            "red means you have filled 75% or more of your character limit")
        print(f"{Fore.GREEN}{Back.GREEN} |||||||||||||||||||||||||||||||||||||||||||||||||||| {Back.RESET} you have {self.total} left")
        while(keep_going):
            for key in self.key:
                if key == "Keyword":
                    keyword = input("what keyword will you like to enter ")
                    self.keyword[key].append(keyword)
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
            self.clear_line()
            keep_going = self.size(len(keyword))
        init(autoreset = True)
    def sort(self):
        """this function is made to have the user decided which database 
        they will have there data sorted by then pass it to islander_sorts"""
        for i in range(1, len(self.key)):
            print(f" you have the choice press of {i} to have your data sorted by")
            print(f"{self.key[i]}")

            while (True):
                try:
                    user = int(input("please enter the databases you will sort by"))
                    break
                except ValueError:
                    print("please enter one of the options")
            self.sort = Islander_sort(number_list = self.keyword[self.key[user]],
                string_list = self.keyword["Keyword"])
            self.sort.driver()
            self.sorted_number_list = self.sort.number
            self.sorted_string_list = self.sort.string

    def driver(self):
        self.clear_line()
        self.insert()
        user = "what"
        while (user.upper() != "Q"):
            print("hello user now that you have entered all the data from the databases")
            print("why dont we start manipulating that data")
            print("you have the option to type sort to have your data to be sorted by\n"
                " which ever database you would like")
            print("or you can enter top to see the data data points")
            print("finally you can enter csv to have your data exported to a file")
            user = input("enter any of the options to continue or if you want to exit the selection just press q")

            if (user.upper() == "SORT"):
                self.sort()
                self.clear_line()
            elif (user.upper() == "TOP"):
                pass

            elif (user.upper() == "CSV"):
                pass

