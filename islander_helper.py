keyword = []

class helper:
    def __init__(self):
        # keyword_2 = []
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
            keyword.append(databases)
        for data in keyword:
            print(data)
