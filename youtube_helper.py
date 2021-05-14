class helper:
    def __init__(self):
        self.keywords = []
        print("hello youtuber i am the youtube helper but you can call me helper")
        print("I was created to make your youtube keyword research less of a head ach")
        print("I do this by keeping track of all the your keyword scores from the different keyword databases")
        print("as well as i have the abilty to export all of your keywords in a comma seperated format")
        print("so that you have the ability to copy and paste it to youtube")
        print("wow that was a mouth full")
        length = True
        while(length):
            database = input("what will the name of the database be")
            self.keywords.append(database)
            user = input("would you like to enter another databases name if so please type yes")
            if (user.upper() == "YES"):
                pass
            #could have put length = True if that makes it easier for you
            else:
                length = False