class helper:
    def __init__(self):
        self.keywords = {} #changed this
        self.key = [] # added this
        self.keywords["keyword"] = []#added this
        print("hello youtuber i am the youtube helper but you can call me helper")
        print("I was created to make your youtube keyword research less of a head ach")
        print("I do this by keeping track of all the your keyword scores from the different keyword databases")
        print("as well as i have the abilty to export all of your keywords in a comma seperated format")
        print("so that you have the ability to copy and paste it to youtube")
        print("wow that was a mouth full")
        length = True
        while(length):
            database = input("what will the name of the database be")
            self.keywords[database] = [] #changed this
            self.key.append(database) #added this
            user = input("would you like to enter another databases name if so please type yes")
            if (user.upper() == "YES"):
                pass
            #could have put length = True if that makes it easier for you
            else:
                length = False
    def insert(self):
        print("Hello youtuber now that we have gotten that out of the way why dont we start adding"
              "some keywrds")
        size = None
        count = 0
        user_decsion = input("is there a specifc number of keywords you would like to enter"
                             "please type yes if there is or any key to continue on")
        if user_decsion.upper() == "YES":
            size = int(input("how many keywords do you want to enter"))

        keep_going = True
        while (keep_going):
            if (size != None):
                count+=1
                if (size == count):
                    print("seems you have reached your limit")
                    break
            for key in self.key:
                if key == "keyword":
                    self.keywords[key].append(input("what will the keyword be"))
                else:
                    self.keywords[key].append(int(input(f"what will the score from {key} be")))