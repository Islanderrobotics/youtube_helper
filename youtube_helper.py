class helper:
    def __init__(self):
        self.keywords = {} #changed this
        self.key = [] # added this
        self.key.append("keyword")#added this
        self.keywords["keyword"] = []#added this
        print("hello youtuber i am the youtube helper but you can call me helper")
        print("I was created to make your youtube keyword research less of a head ach")
        print("I do this by keeping track of all the your keyword scores from the different keyword databases")
        print("as well as i have the abilty to export all of your keywords in a comma seperated format")
        print("so that you have the ability to copy and paste it to youtube")
        print("wow that was a mouth full")
        count = int(input("how many databases will you like to enter"))
        i = 0
        length = True
        while(i<count):
            database = input("what will the name of the database be")
            self.keywords[database] = [] #changed this
            self.key.append(database) #added this
            i+=1
    def insert(self):
        print("Hello youtuber now that we have gotten that out of the way why dont we start adding"
              "some keywords")
        size = 0
        count = 0
        user_decsion = input("is there a specifc number of keywords you would like to enter"
                             " please type yes if there is or any key to continue on")
        if user_decsion.upper() == "YES":
            size = int(input("how many keywords do you want to enter"))

        keep_going = True
        while (keep_going):
            for key in self.key:
                if key == "keyword":
                    self.keywords[key].append(input("what will the keyword be"))
                else:
                    self.keywords[key].append(int(input(f"what will the score from {key} be")))
            if (size ==0):
                data = input("would you like to add more keywords please enter yes if you do"
                             " or any key if you would not like to")
                if (data.upper() == "YES"):
                    pass
                else:
                    keep_going = False
            if (size == count+1):
                print("seems you have reached your limit")
                keep_going = False
            if (size > 0):
                count += 1
