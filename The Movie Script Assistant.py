# Steven Nelson, Programmer
# October 16th, 2022
# CSC 242 Lab 08

from MovieScript import *

# the movie text and sequences
seq = []
seq.append("opening teaser sequence")
seq.append("main titles with theme song")
seq.append("the plot unfolds")
seq.append("meeting with the superiors")
seq.append("the gadgets are issued")
seq.append("the mission begins")
seq.append("subplot: martini ... shaken, not stirred")   # step five
seq.append("a romance ensues")
seq.append("subplot: she tries to steal the briefcase")  # step five
seq.append("thwarted but persistent")
seq.append("subplot: the Aston Martin makes a getaway")  # step five
seq.append("physical confrontation with the enemy")
seq.append("the enemy is defeated")
seq.append("the loose ends unfold")
seq.append("on to the next mission")

# convert the sequence list to a dictionary

seq_dictionary = dict(enumerate(seq, start=1))

# create a new movie script object
ms = MovieScript()
ms.script = seq
theScript = ms.getScript()

spy_word_list = ["007", "agent", "American", "Aston", "attack", "beach", "beautiful", "bomb", "Bond", "briefcase",
                 "British", "CIA", "camera", "car", "chase", "confrontation", "defeated", "double", "dress", "eat",
                 "enemy", "England", "flower", "gadget", "green", "gun", "GoldenEye", "James", "kill", "kiss",
                 "license", "love", "Martin", "martini", "meeting", "MI6", "mission", "next", "opening", "physical",
                 "plot", "Q", "rain", "romance", "Russia", "secret", "seduce", "sequence", "service", "shaken", "snow",
                 "song", "space", "spy", "stirred", "suit", "superiors", "teaser", "theme", "thwart", "title",
                 "unfolds", "villain", "watch", "woman", "world"]

character_dictionary = {1: 'James Bond', 2: "no character", 3: 'Moneypenny', 4: 'M', 5: 'Q', 6: 'James Bond',
                        7: 'James Bond', 8: 'Honey Ryder', 9: 'Honey Ryder', 10: 'James Bond', 11: "Aston Martin",
                        12: 'Jaws', 13: 'James Bond', 14: 'Honey Ryder', 15: 'M'}

scene_length = ("6 minutes", "3 minutes", "12 minutes", "4 minutes", "5 minutes", "15 minutes", "3 minutes",
                "9 minutes", "2 minute", "3 minutes", "6 minutes", "5 minutes", "3 minutes", "8 minutes", "2 minutes")

unit_directors = ("first director", "second director", "first director", "second director", "first director",
                  "first director", "second director", "first director", "first director", "first director",
                  "second director", "second director", "second director", "first director", "first director")


def movie_title():
    """the first console print informing the user of the spy movie assistant options for the program"""

    print("*******************************************************************************************")
    print("* Welcome to the spy movie scene assistant, please select from the following options below:")
    print("* Search by keyword to find the the scene number and description of film scene. Selection 1")
    print("* Search a list of keywords associated with the spy application and spy movies. Selection 2")
    print("* View the characters in the script and what scene they appear in the film.     Selection 3")
    print("* View the scene minute timings along with what scene they appear in the film.  Selection 4")
    print("* View which scenes were directed by the first or second unit film directors.   Selection 5")
    print("* If you are all done and would like to exit the spy movie application.         Selection 6")
    print("*******************************************************************************************")


def movie_main():
    """the main area of the program that will control what other functions are called in the application."""

    movie_title()
    user_choice = (input("Please make a selection: "))
    if (user_choice == '1'):
        keyword_search()
    elif (user_choice == '2'):
        step_five()
    elif (user_choice == '3'):
        list_characters()
    elif (user_choice == '4'):
        scene_timings()
    elif (user_choice == '5'):
        director_list()
    elif (user_choice == '6'):
        print("Thank you for using the spy movie program, we hope you have an adventurous day.")
        exit()
    else:
        print("Please make a valid number selection to continue, thank you.")
        movie_main()


def keyword_search():
    """a function for the keyword search from our lab eight starter code"""

    print("*******************************************************************************************")
    print("Please enter a keyword to search the movie sequences.", "\n")
    keyword = input("Keyword entry: ").strip()
    print("")   # proper spacing

    """
    for x in range(len(theScript)) :
    print (u"\u2022", theScript[x], end = "\n")
    print ("\n")
    """

    for i in range(len(seq)):
        if (keyword in seq[i]):
            print(f"Keyword found! Here is the keyword with the sequence number and plot location")
            print("Located in scene sequence number ", i + 1)
            print("\"", seq[i], "\"")
    print("**************** Returning to the main menu options of the movie assistant ****************")
    movie_main()


def step_five():
    """supplement the above code segment by creating a searchable list of keywords associated with this spy application
    and spy movies in general, such as the words: enemy, gadgets, mission, etc. also supplement the starter code with
    three additions to the movie sequence list."""

    print("*******************************************************************************************")
    print("* Search the vast list of keywords to see if a word is currently in the list.  Selection 1")
    print("* Search to see if the keyword is both in spy list and in the spy application. Selection 2")
    print("* If you would like to add a spy keyword which isn't present to the word list. Selection 3")
    print("* If you would like to see a printout of all spy keywords in the current list. Selection 4")
    print("* If you would like to return back to the main menu of this spy application.   Selection 5")
    print("*******************************************************************************************")

    user_choice = (input("Please make a selection: "))
    if (user_choice == '1'):
        print("Please enter a keyword to search the list of spy keywords.", "\n")
        keyword = input("Keyword entry: ").strip()
        for i in range(len(spy_word_list)):
            if (keyword in spy_word_list[i]):
                print(f"Keyword '{keyword}' found! It is currently located within the spy keyword list.")
                print("Returning back to main submenu of selection 2 of the application.")
                step_five()
    if (user_choice == '2'):
        global seq
        print("Please enter a keyword to check if it is both in the spy word list and within the current script.", "\n")
        keyword = input("Keyword entry: ").strip()
        seq_word_list = sum([i.rstrip(".").split(" ") for i in seq], [])
        seq_check = keyword in seq_word_list
        spy_word_list_check = keyword in spy_word_list
        if seq_check == True and spy_word_list_check == True:
            print(f"The keyword '{keyword}' is in the vast list and is also written in the spy movie script.")
            print("Returning back to main submenu of selection 2 of the application.")
            step_five()
        else:
            print(f"The keyword '{keyword}' is not located in either the spy word list or the current script.")
            print("Returning back to main submenu of selection 2 of the application.")
            step_five()
    if (user_choice == '3'):
        print("Please enter a keyword you would like to add to the vast list of spy genre keywords.")
        keyword = input("Keyword entry: ").strip()
        spy_word_list.append(keyword)
        print(f"The keyword '{keyword}' has been added to our spy genre list of words, thank you for helping.")
        print("Returning back to main submenu of selection 2 of the application.")
        step_five()
    if (user_choice == '4'):
        print("*******************************************************************************************")
        print("Here is a complete print out of the current spy genre words within the vast program list:")
        print(" ")  # proper spacing
        print("\n".join([", ".join(spy_word_list[i:i + 11]) for i in range(0, len(spy_word_list), 11)]))
        print(" ")  # proper spacing
        print("The complete list is shown above, returning back to main submenu two of the application.")
        step_five()
    if (user_choice == '5'):
        movie_main()
    else:
        print("** Please make a valid number selection between selection options of 1 through 5, thank you. **")


def list_characters():
    """create a list of fictitious characters that will be a part of our spy movie. you can even match each movie
    sequence number to those characters that will appear in a specific scene."""

    print("*******************************************************************************************")
    print("* See a console printout of main characters that are in the current spy film.  Selection 1")
    print("* See a printout of the character names and a description of their spy scenes. Selection 2")
    print("* If you would like to return back to the main menu of this spy application.   Selection 3")
    print("*******************************************************************************************")

    user_choice = (input("Please make a selection: "))
    if (user_choice == '1'):
        print("Here is a list of the unique character possibilities found within the spy character list:")
        #print(" ")  # proper spacing
        character_set = set(character_dictionary.values())
        for character in character_set:
            print(character)
        print(f"There are currently {len(character_set)} character name possibilities in the spy movie script.")
        print("Returning to the main submenu of option selection 3:")
        list_characters()
    if (user_choice == '2'):
        print("Here is a printout of the film scene summaries along with the scene's character emphasis:")
        print(" ")  # proper spacing
        character_dictionary_values = list(character_dictionary.values())
        print(''.join([str(f"* Scene {seq.index(a) + 1}: " + a) + (" - featuring " + b + " as the scene's main character. \n") for a,b in zip(seq,character_dictionary_values)]))
        print("Returning to the main submenu of option selection 3:")
        list_characters()
    if (user_choice == '3'):
        print("Returning to the main menu of the spy movie script application:")
        movie_main()


def scene_timings():
    """for each of the elements in the movie sequence list, create a parallel list of scene timings. for example,
    for the sequence " the gadgets are issued " you can use 7 minutes as the length of this scene."""

    print("Here is a printout of the spy scene descriptions along with their time duration in minutes:")
    print(" ")  # proper spacing
    print(''.join([str(f"* Scene {seq.index(a) + 1}: " + a) + (" - with a screen time length of " + b + ".\n") for a, b in zip(seq, scene_length)]))

    print("The printout above is in sequential order of the movie scenes.")
    print("Returning to the main menu of the spy movie script application:")
    movie_main()


def director_list():
    """second unit directors are often utilized to film important but remote or lengthy scenes for feature films.
    create another parallel list that matches movie sequences with either the first unit or second unit directors."""

    print("Here is a printout of the spy scene descriptions along with the unit director who produced the scene:")
    print(" ")  # proper spacing
    print(
        ''.join([str(f"* Scene {seq.index(a) + 1}: " + a) + (" - produced by the " + b + ".\n") for a, b in zip(seq, unit_directors)]))

    print("Returning to the main menu of the spy movie script application:")
    movie_main()


movie_main()


