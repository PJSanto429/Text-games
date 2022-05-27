def instructions():
  #print("Throughout this game, you will be eatig new people ")
  print("To make choices in this game, you will be making your decisions by typing the number that corresponds with what you would like to choose. For example, you might get a choice between eating a hotdog(1) or a hamburger(2). To make your choice, you will type either 1 or 2")
bruh=input("Start Game? y/n ")
yes=['y','Y','yes','Yes','YES']
no=['n','N','no','No','NO']
if bruh in yes:

    drbirdspellings=['dr. bird','dr. nolan bird','dr. nolan','nolan bird','nolan','bird']
    jeffspellings=['JEFF','jeff','Jeff']

    characterslist=[drbirdspellings+jeffspellings]
    playerInventory=[]
    suspects=[]

    #Here are the things that I need to add
    #Nothing yet

    #This part of the game will be used once. It is where the player makes the main decisions about what to do first in the game
    def firstchoices():
        print("You can now make a decision on what you would like to do. Here are your choices: ")
        print("(1) - look further into Dr. Nolan Bird's life")
        print("(2) - go to Quiet Times")
        print("(3) - investigate the body")
        print("(4) - talk to his neighbor Jeff")
        print("(5) - talk to his boss and co-workers")
        print("(6) - view suspects")
        choice=int(input("Please make your choice now: "))
        if choice==1:
          choice1_DrBirdsLife()
        elif choice==2:
          choice2_QuietTimes()
        elif choice==3:
          choice3_investigate_body()
        elif choice==4:
          choice4_Jeff()
        elif choice==5:
          choice5_bossCoworkers()
        elif choice==6:
          suspects()
        else:
          print("Oops! It seems that what you chose was either not available or not a number. You will be redirected to make your choice again")
          print(" ")
          choices()

    #this will be use most it is where the player makes a new decision after everything
    def choices():
        print("You can make another decision now. Here are your choices:")
        print(" ")
        print("(1) - look further into Dr. Nolan Bird's life")
        print("(2) - go to Quiet Times")
        print("(3) - investigate the body")
        print("(4) - talk to his neighbor Jeff")
        print("(5) - talk to his boss and co-workers")
        choice=int(input("Please make your choice now: "))
        if choice==1:
          choice1_DrBirdsLife()
        elif choice==2:
          choice2_QuietTimes()
        elif choice==3:
          choice3_investigate_body()
        elif choice==4:
          choice4_Jeff()
        elif choice==5:
          choice5_bossCoworkers()
        elif choice==6:
          suspects()
        else:
          print("Oops! It seems that what you chose was either not available or not a number. You will be redirected to make your choice again")
          print(" ")
          choices()

    #Below is the suspects function. It is used when the player wants to view or add suspects and arrest someone
    def suspects():
        if len(suspects)==0:
            print("You have no suspects at this time.")
            question=input("Would you like to add someone to the suspects list? Yes(1) or No(2)")
            if question==1:
                person=input("Who would you like to add to your list of suspects")
            elif question==2:
              print("Ok. Come back any time to view or add suspects to the list.")
              choices()
            else:
              print("Opps! It seems that what you typed didn't compute. You will be redirected back to suspects")
              print(' ')
              suspects()

        elif len(suspects)>=1:
            question=input("Would you like to add someone to the suspects list? Yes(1) or No(2)")
            if question==1:
              print("Here are your suspects")
              for name in suspects:
                print(name)
              addition=input("Please type the name of the person that you would like to sdd to the list of suspects: ")
              addition=addition.upper()
              suspects.append(addition)
              print(" ")
              print("Addition successful! You have added "+addition+' to the list!')

    #Below is the gameplay for the first option, to look into Dr. Birds life
    def choice1_DrBirdsLife():
        while True:
            print(" ")
            print("To try and find out as much as you can about Dr. Bird, you head over to his house.")
            print("Dr. Nolan Bird is, according to the trophies in his house, one of the best surgeons in LA. He is also well known for donating a lot of money to all sorts of different charities. It seems that everyone loved him, so why would someone kill him?")
            print(" ")
            print("You did find a message on the answering machine from the FBI saying that they have something incriminating on him. It doesn't go into too much detail, but it does give you some sort of a lead.")
            print(" ")
            choice2=int(input("Would you like to look deeper into Dr. Bird's life(1), see what the FBI has on him(2), or look into something else(3)?"))

            if choice2==1:
                print("You spend hours searching through different parts of Dr. Bird's life, but you cannot find anything about him that might make someone want to kill him. You did find his laptop, which could be helpful, but you can't crack the elaborate firewall that is installed.")
                print(" There might be info about what the FBI wanted with Dr. Bird on this laptop, but you need to find someone with better hacking skills than you in order see whats inside")
                playerInventory.append("D.N.B. Laptop")
                print("")
            elif choice2==2:
                FBI()
            elif choice2==3:
            	choices()

    #Below is the file that the FBI might give you
    def FBI_File():
        print(" ")
        print("The file on Dr. Bird is very large and it seems that they were close to busting him. After looking through the file a little bit longer, you discover that the FBI had the evidence to put Dr. Bird away for a long time, possibly life. The risk of being caught might have made Dr. Bird's criminal associates freak out and want to kill him. You might need to look into this some more.")
        print("Another thing that you found out about Dr. Bird is that he had several offshore bank accounts, each with a ton of money in them. Here are the names and amount in each of the accounts:")
        print(' ')
        print("Cayman Banking Benefits: $12,383,521")
        print("Singapore Simple Services: $65,174,092")
        print("Belize Banking and Co: $59,384,789")
        print(" ")
        choices()

    #Below is gameplay for if you talk to the FBI
    def FBI():
        import random
        print("When you ask the FBI for what they have on Dr. Bird, they say that you must be American to look at the files. This is a problem for you since you are from Britain.")
        print(' ')
        print("You can give them your real ID(1) or you can them a fake ID(2). If you give them a fake ID, there is a chance that they will catch you and you will have to sit in jail for a while")
        ID_Chance=random.randint(1,2)
        ID_Choice=int(input("Please make your decision now: "))
        if ID_Choice==1:
            print("When you give the FBI your real ID, they see that you are not American and tell you to get lost.")
            choices()
        elif ID_Choice==2:
            if ID_Chance==1:
                print('When you give the FBI your fake ID, they seem to look at it for an eternity. Finally, they give it back to you and get you the file you wanted')
                FBI_File()

            elif ID_Chance==2:
                print("When you give your fake ID to the FBI, they inspect it and finds something wrong. The name on the ID does not match the name that you gave her when you first arrived. this causes you to be placed under arrest for the time being")
                print("You will have to wait in jail until the FBI is ready to talk to you and you can figure out a solution")
                print(" ")
                print("When something like this happens, you will have to press enter to 'wait'. It won't take long in real time, but in the game, things will continue to happen")
                wait=input("Waiting...")
                wait=input("Waiting...")
                wait=input("Waiting...")
                wait=input("Waiting...")
                wait=input("Waiting...")
                wait=input("Waiting...")
                wait=input("Waiting...")
                print("Finally, after what feels like an eternity, the FBI is ready to talk to you")
                print(" ")
                print("They begin interrogating you about what you need their files for and why you are here. This is really boring, so you don't listen much. Pretty much what happens if that you are told to drop the case and go back to what ever country that you came from.")
                print(" ")
                print("The FBI releases you, but now you have a blemish on your otherwise perfect record and are not supposed to be in America anymore. You also might not be allowed to the crime scene anymore, but who knows.")
                choices()
    #----------------------------------Above is everything on option 1. --------below is everything in option 2----------------------------------------
    #Below is the second choice, if you look into quiet times
    def choice2_QuietTimes():
        print("Quiet Times is  a fairly normal coffee shop, although the prices seem a bit high. You do get a coffee, but you can't seem to figure out why Dr. Bird liked this place so much.")
        print(" ")
        print("The manager said that Dr. Bird was here every Monday and Tursday at 7:30 PM for open mic night. Dr. Bird enjoyed watching everyone on stage do their thing, but he seemed to really like one female singer in particular. The manager cannot remember her name, but she was 'not much to look at', as he said.")
        print(" ")
        print("You look around Quiet Times a little while longer, but cannot find anything useful. You did find some some weird stuff like a mouse, an upside down hat shaped like a pizza, and a large man riding a small pony in a circle. He won't talk to you no matter how hard you try, but he seems useless anyways.")
        print("You can now look for the mystery lady that Dr. Bird liked(1) or you can look into something else(2)")
        bruh=int(input("Please make your decison now: "))
        if bruh==1:
          mystery_woman()
        elif bruh==2:
          choices()

    #Below is if you try and find the woman that Dr. Bird liked
    def mystery_woman():
      print(" ")
      print("You spend a few hours trying to find the mystery girl, and you finally find her. Here is what you found on her: ")
      print("Name: Savannah Perkins")
      print("DOB: 11/13/98 (23 years old)")
      print("Occupation: full time singer/songwriter (unemployed)")
      print("Net worth: $27.93")
      print("Crimminal Record: parking ticket from 2 years ago (she paid it)")
      print("Outstanding warrants: none")
      print("Debt: $24,927.73")
      print("Adress: 2798  Lowndes Hill Park Road")
      print("Social security number: 770-38-8459")
      print(" ")
      print("Savannah Perkins is a very normal trust fund kid. She was getting money from her parents and when they got mad that she wasn't working, they stopped giving her money. This made her have to try to get a job, and she decided that being a musician was right for her. According to her bank accounts, she was not a very good musician and could only find work at open mics. It seems that Savannah Perkins is not the killer. The worst thing that she has done, other than thinking that she could have been a successful musician, was parking in a hadnicapped spot.")
      print(" ")
      choices()
    #-------------------------------------above is choice2------------below is choice3-----------------------------------------------------------------
    #below is choice3, if you look at the body
    def choice3_investigate_body():
      print("Dr. Bird's body was found floating face down in his swimmming pool. There is a bloody bump on the back of his head, along with a needle hole in his arm. The coroner says that there were trace amounts of arsenic in the blood stream. The nervous system is also damaged, along with some vomit residue in the back of the throat. It seems that whomever killed Dr. Bird wanted him to die quickly, but also be in a lot of pain.")
      print(" ")
      print("After seeing the body, you can come the the conclusion that Dr. Bird probably didn't kill himself. If he were to kill himself, he probably would have picked a way that would not hurt as much and since he was a doctor, he had access to the correct materials. He also would not have done it floating face down in the pool, he would have chosen somewhere more comfortable.")
      print(" ")
      choices()
    #-------------------------------------above is choice 3---------------below is choice 4------------------------------------------------------------
    #below is choice 4, if you talk to jeff
    def choice4_Jeff():
      print(" ")
      print("The neighbor Jeff is a retired engineer who made millions designing the bolts that hold waterpark slides together. Unsurprisingly, he is very strange man with an even stranger house. Jeff is like a mix between Elton John and Albert Einstein, both personality and looks. Other than knowing that Dr. Bird liked going to Quiet Times, Jeff is useless. He keeps trying to show you a history of the bolts that he designed for various waterparks, but you are not interested.")
      print(" ")
      print("Jeff will not stop trying to show you his work, but he cannot seem to focus on one thing for long. His work area is also extremely messy, with papers and ther assorted junk strewn everywhere. Despite the mess, Jeff seems to know exactly where everything is and everything as a place in the mess.")
      print(" ")
      choices()
    #----------------------------------------above is choice 4---------------------below is choice 5---------------------------------------------------
    #below is choie5, if you talk to the boss and co-workers
    def choice5_bossCoworkers():
      print(" ")
      print("First, you talk to Dr. Bird's co-workers and fellow doctors. Everyone that he worked with tells you that he was not very good at communicating, unless it was about doctor stuff. What he lacked in communication skills, he made up for it with his excellent skills as a doctor. He was also known around the hospital as the guy who could fix the vending machine if it ever broke.")
      print(" ")
      print("Next, you talk to Dr. Bird's boss, a man called Dr. Graves. He says that Dr. Bird was a good employee, but he sometimes did his own thing. When he would tell Dr. Bird to do something, there was a chance that Dr. Bird would not do it or he would do it but in a totally different way. He was a good employee, but could smetimes get on Dr. Graves' nerves.")
      print(" ")
      print("It seems that other than sometimes doing his own thing, Dr. Bird was a good employee and co-worker. No one that he worked with would want to kill or even harm him in the slightest.")
      choices()

    #--------------------------------------------------------------------------------------------------------------------------------------------------
    #these first few lines are just the intro where it tell you the game and gets your name
    print("Welcome to DETECTIVE: LOS ANGELES. ")
    print("In this game, you are the worlds greatest private detective, and you must solve the murder of one Dr. Nolan Bird in the beautiful county of Los Angeles.")
    ok=input("Do you need instructions on how to play? yes or no  ")
    if ok in yes:
      instructions()
    playerName=input('Before we begin, what is your name? ')
    playerName=playerName.capitalize()
    print('Welcome to LA, Detective '+playerName)
    wait=input("Press enter to continue")
    print("")

    #Here is where the game begins
    print('')
    print("According to his neighbor Jeff, Dr. Nolan Bird pretty much only went to work and then stayed at home. The only place that Jeff saw him going to was a book store called QUIET TIMES.")
    print("")
    firstchoices()


elif bruh in no:
    print("Ok. Game over")