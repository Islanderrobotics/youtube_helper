keywords = []
class helper:
    def __init__(self):
        # self.keywords = []
        print("hello youtuber i am the youtube helper but you can call me helper")
        print("I was created to make your youtube keyword research less of a head ach")
        print("I do this by keeping track of all the your keyword scores from the different keyword databases")
        print("as well as i have the abilty to export all of your keywords in a comma seperated format")
        print("so that you have the ability to copy and paste it to youtube")
        print("wow that was a mouth full")
        count = int(input("how many databases will you like to enter"))
        i = 0
        while (i < count):
            database = input("what will the name of the database be")
            keywords.append(database)
            i+=1
        for i in keywords:
            print(i)