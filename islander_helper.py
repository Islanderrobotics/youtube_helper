

class helper:
    def __init__(self):
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
        count = int(input("with all of that being said how many databases will we be using today"))
        for i in range(count):
            databases = input("what is the name a database we will be looking at today")
            self.keyword[databases] = []
            self.key.append(databases)

    def insert(self):
        print("Hello Youtuber now that we have the databases that you will be using why dont we start adding some keywords")
        size = 0
        count = 0
        user_decsion = input("is there a specifc number of keywords you would like to enter please type yes if there is or any key if not")
        if (user_decsion.upper() == "YES"):
            size = int(input("how many keywords will you be entering"))
        keep_going = True
        while(keep_going):
            for key in self.key:
                if key == "Keyword":
                    self.keyword[key].append(input("what keyword will you like to enter"))
                else:
                    self.keyword[key].append(int(input(f"what is the score from {key} for that keyword")))
            if(size == 0):
                user_decsion = input("please type yes if you would like to enter more keywords or any key to continue")
                if (user_decsion.upper() == "YES"):
                    pass
                else:
                    keep_going = False
            if(size == count+1):
                print("seems you have reached your keyword limit")
                keep_going = False
            if(size>0):
                count+=1
    def driver(self):
        self.insert()