from manager_man import manager
import time
import random

#Death------------
def death():
    print ('You DIE') 

#Player-----------
def Player_Profile():
    print ('        Character         ')
    print ('|------------------------|')
    print ('|                        |') 
    print ('|        ???????         |') 
    print ('|        |-  - |         |') 
    print ('|        | |   |         |') 
    print ("|        |  -  /         |") 
    print ("|        ''''''          |")        
    print ('|                        |')     
    print ('|  Name- Valaban         |')                 
    print ('|  Class- Chef Traveler  |')                      
    print ('|  Stamina = 10 at start |') 
    print ('|                        |') 
    print ('|------------------------|') 
stamina = 10
Health = 10
Gold = 5
def gold():
    print ("You have "+ str(Gold)+ " gold")
Attack = 1
Borest_REP = 0
#Items-------------
Rejuvination_Amulet = True
Gleaming_sword = True
#Rumors------------
def rumours():
    rand_num = random.randint(1,5)

    rumour_one = 'I hear there are expensive truffles in skaldar forest.'
    rumour_two = 'The skaldur forest is full of dangerous goblin natives'
    rumour_three = 'I heer triteem is forming a expidition group to kill the trolls'
    rumour_four = 'The elves in Calduin can enchant your weapons'
    rumour_five = 'The runes of Norecast in Aldren are full of vualuable items and unique plants'

    total_rumours = []
    total_rumours.append(rumour_one)
    total_rumours.append(rumour_two)
    total_rumours.append(rumour_three)
    total_rumours.append(rumour_four)
    total_rumours.append(rumour_five)

    return total_rumours[rand_num - 1]


#Enemies----------
bandits_level = 3
def bandits():
    global Health
    bandits_level = 3
    Health -= bandits_level
    if Health <= 0:
        death()
    else:
        print ('Your health is now ' + str(Health))

#Quests-----------
lost_boy = True
sob_woman = True
def Sobbing_Woman():
    global lost_boy
    global Gold
    global Borest_REP
    global sob_woman
    if lost_boy == False:
        print ("Im so grateful, please tak this as a reward")
        sob_woman = False
        Gold += 10
    if sob_woman == True:
        print ('Please travler help me she exclaims, my boy is lost and I cant find him!')
    else:
        print ("Are you looking for him!")
        Borest()
    desc ="She looks to you"
    choice_one = 'Say you will help the Lady(1)'
    choice_two = 'Say keep track of your own kid(2)'
    choice_three ='Leave the sobbing woman(3)'

    start_game = manager(desc, choice_one, choice_two, choice_three)
    start_game.build()


    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('The lady is so grateful and gives you a hug')
            Borest_REP += 1
            print ('Your reputation is now '+ str(Borest_REP))
            sob_woman = False
            Borest()
            break
        elif response == '2':
            print ("You tell her off and she yells and spits in your face while everyone watches")
            Borest_REP -= 1
            print ("Your reputation went down 1")
            print ("Your reputation is " + str(Borest_REP))
            break
        elif response == '3':
            print ("You leave the woman to her own misery ")
            Borest()
            break
        else:
            print("Invalid input")
            continue


#Sewers-----------------
def Sewer_Choice():
    desc = 'The beast is gone but you can hear more scraping'
    choice_one = 'Enter Borest(1)'
    choice_two = 'Leave to borest road(2)'
    choice_three ='Fight more rats(3)'

    start_game = manager(desc, choice_one, choice_two, choice_three)
    start_game.build()


    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('You are glad to leave the disgusting sewers')
            Borest()
            break
        elif response == '2':
            print ("You are glad to leave the disgusting sewers ")
            borest_road
            break
        elif response == '3':
            print ("The rats stand no chance ")
            Sewers()
            break
        else:
            print("Invalid input")
            continue
def Sewers(): 
    global Gold
    global Health
    global Attack
    print ("You hate these sewers and despise the smell, you can hear scraping noises from all over")
    print ("A RAT! you exclaim as a huge on tries to attack you")
    print ("The rat is level 2\n")
    if Attack > 2:
        print ("You slay the beast with ease")
        Gold += 1
        print ("You earned 1 gold")
        Sewer_Choice()
    else:
        Health -= 2
        if Health <= 0:
            death()   
        else: 
            print ('You lost 2 health')
            print ('Your health is '+ str(Health))
            print ("You earned 1 gold")
            Gold += 1  
            print ('You have '+str(Gold)+ "gold.")
            Sewer_Choice()
    
#Kindom Borest----------
def Keep():
    print ('The high ceiling and perfectly decorated hall makes you feel a little bit stuffy and go up to the king')
    print (' The friendly and jovial king says, "you have really made an name for yourself here, and im getting bored with the Hogs Heads plain "food"\n Will you become my personal chef? "  ')
    print ('1. Become his chef (1)')
    print ('2. Your real goal is to start your own resturant, politly decline (2)')
def Enter_Keep():
    if Borest_REP < 4:
        print ("The guards simply look at you and luagh at the boldness of a stranger they dont even know and turn away(!You need better reputation!)")
        Borest()
    if Borest_REP >= 4:
        print ('the guards welcome you into the hold hearing of your good deeds')
        Keep()
beggar_instance = True
def beggar():
    global beggar_instance
    global Borest_REP
    
    desc = 'THe beggar lifts his head and attempts a smile, "Can you spare a coin" he asks'
    choice_one = 'give the poor man some coin(1)'
    choice_two = 'KIll the begger(2)'
    choice_three = 'Leave the beggar(3)'
    start_game = manager(desc, choice_one, choice_two, choice_three)
    start_game.build()


    valid = True
    while valid == True:
        response = input()
        if response == '1':
            if Gold >= 1:
                print ('You give the man some coin and wish him the best, he seems very grateful')
                Borest_REP += 1
                print ("You have 1 better reputation in Borest")
                beggar_instance = False
                Borest()
            break
        elif response == '2':
            print ("The mans gutteral screams chill your bones ")
            print ("You have lost 1 reputation")
            Borest_REP -= 2
            print ("Your reputation in Borest is "+str(Borest_REP))
            beggar_instance = False
            if Borest_REP < -1:
                print ("You are now reconized as a bandit")
                print ("Borest ")
            Borest()
            break
        elif response == '3':
            print ("You leave the beggar to his own filth")
            Borest()
        else:
            print("Invalid input")
            continue
def Hogs_Head():
    global Health
    global stamina
    global Gold
    print ('You sit and eye the travelers around you\n')
    print ('1. Listen in on rumors(1)\n')
    print ('2. Ask bartender for some food(2)\n')
    print ('3. Ask bartender to stay the night(3)\n')
    print ("4. Leave the Hogs Head(4)")

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('You hear them say...' + rumours())
            Hogs_Head()
            break
        elif response == '2':
            print ("You ask the bartender for some some food but become astonished as he comes out with a pile of glop. You cant believe he calls it food, but you eat it anyway\n")
            Health += 1
            Gold -= 1
            print ("You health is now " + str(Health)+ "\n")
            Hogs_Head()
            break
        elif response == '3':
            print ("You lay down in the comfy bed providede and drift off to the horrifying dreams of glop \n")
            stamina += 3
            Gold -= 1
            print ("Your stamina is now "+ str(stamina)+ "\n")
            Hogs_Head()
            break
        elif response == '4':
            print ("You exit the comfy inn into Borest \n")
            Borest()
        else:
            print("Invalid input")
            continue
def Grumpy_Merchant():
    global Gold
    global Attack
    global Health
    global Rejuvination_Amulet
    global Gleaming_sword
    print ('The Merchant opens a few chests and displays what he has\n')
    if Gleaming_sword is True:
        print ('A gleaming sword (+ 3 damage (- 7 gold) (1)\n')
    else:
        print ('SOLD')
        
    if Rejuvination_Amulet is True:
        print ('A Rejuvination amulet (gives back 3 health after a fight(50 gold) (2)\n')
    else: 
        print ('SOLD')
    print ('A tasty looking glowing pear from the Lumin Forest (gives 2 health(1 gold) (3)\n')
    print ('Leave the merchant(4)')
    gold()
    valid = True
    while valid == True:
        response = input()
        if response == '1':
            if Gold >= 7:
                print ("When you pick up the sword you feel more sturdy and menacing")
                Attack += 3
                Gleaming_sword = False
                gold()
                Grumpy_Merchant()
            else:
                print ('!You dont have enought gold!')
                Grumpy_Merchant()
            break
        elif response == '2':
            print ("The expensive amulet must be very magical, it teems with energy")
            if Gold >= 50:
                print ('You place the amulet around your neck and feeled reassured with its protection')
                Gold -= 50
                Rejuvination_Amulet = False
                gold()
                Grumpy_Merchant
            else:
                print ('!Not enough gold!')
                Grumpy_Merchant()
            break
        elif response == '3':
            print ("You pick up the glowing pear and salivate wondering the amazing tast might be..\n")
            print ('You eat thae pear and fireworks of flavor burst into existence, you savor the sweet inside\n')
            Gold -= 1
            Health += 2
            print ('Your Health is now ' + str(Health))
            gold()
            Grumpy_Merchant()
            break
        elif response == '4':
            print ("You turn away and walk towards- ")
            Borest()
            break
        else:
            print("Invalid input")
            continue

def borest_road():
    print ('You are on the Borest road (kindom roads allow you to travel to other kindoms) and can travel to..')
    print ('Lumin Forest (1)')
    print ('Darqthaal Cave(2)')
    print ('Aldren Kindom(3)')
    print ('Calduin Kindom(4)')
    print ('Triteem Kindom(5)')

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print (' You travel to the Lumin Forest in search of some new ingredients!')
            Lumin_Forest()
            break
        elif response == '2':
            print ("You travel to Darqthaal Cave and see a fimiliar glow emitting from its gaping maw")
            Darqthaal()
            break
        else:
            print("Invalid input")
            continue
def Enter_Borest():
     print ('You enter Borest and are exited to see Hogs Head(Tavern), a merchant, and the Kings Keep. \n You also see lonely beggar, a sobbing woman and the accursed sewers.\n')
def Borest():
    global beggar_instance
    global sob_woman
    print ('Enter the Hogs Head(1)\n')
    print ('Talk to Merchant(2)\n')
    print ('Request a audience for the king(3)\n')
    if sob_woman == True:
        print ('Talk to sobbing woman(4)\n')
    else:
        print ('The woman is waiting(4)\n')
    if beggar_instance == True:
        print ('Talk to lonely beggar(5)\n')
    else:
        print ("The beggar has left(5)\n")
    print ('Enter the sewers(6)\n')
    print ('Leave Borest(7)\n')

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('You enter the Hogs Head Tavern and the warm glow of the fire welcomes you. the bartender announces that to stay the night is 1 gold and food is 1 gold.\nThere are also groups of people saying rumors.')
            Hogs_Head()
            break
        elif response == '2':
            print ("You walk up to the grumpy looking merchant and ask to browse his wares. He flashes a greedy grin ")
            Grumpy_Merchant()
            break
        elif response == '3':
            print ("You go up to the guards and ask for a audience with the king.")
            Enter_Keep()
            break
        elif response == '4':
            if sob_woman == False:
                print ("The woman is waiting")
                Borest()
            else:
                print ("You walk up to the sobbing woman and gently coax her into telling you what happened")
                Sobbing_Woman()
            break
        elif response == '5':
            if beggar_instance == True:
                print ("You walk up to the lonely beggar and feel sorry for the knarled old man")
                beggar()
            else:
                print ("The beggar is gone")
                Borest()
            break
        elif response == '6':
            print ("You go to the sewers and a disgusting stench fills your nostrils ")
            Sewers()
            break
        elif response == '7':
            print ("You walk out onto Borest Road ready for more adventure and especially food! ")
            borest_road()
            break
        else:
            print("Invalid input")
            continue
#Forests----------
peach = 2
dragon_egg = 1 
coco_beans = 3
def lumin_road():
    desc = 'You are on the Lumin road and can travel to..'
    choice_one = 'Borest (1)'
    choice_two = 'Darqthaal Cave(2)'
    
    start_game = manager(desc, choice_one, choice_two)
    start_game.build()


    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print (' You travel on to Borest and see a sprawling city of pure white spires with a navy blue pointed roofs. Its majesticness leaves you in awe')
            Borest()
            break
        elif response == '2':
            print ("You travel to Darqthaal Cave and see a fimiliar glow emitting from its gaping maw")
            Darqthaal()
            break
        else:
            print("Invalid input")
            continue
def Lumin_Forest():
    global Health
    global peach 
    global dragon_egg
    global coco_beans
    print ('By looking around you can see a shadowed section, a cove on top of a hill, and  some stumps')
    print ('1. Examine shaded trees(1)')
    print ('2. Look in cove(2)')
    print ('3. Examine the stumps(3)')
    print ('4. Leave the Lumin Forest(4)')
    valid = True
    while valid == True:
        response = input()
        if response == '1':
            if peach > 0:
                print ('By looking in the trees you discover some Glowing Peaches!')
                print ('You got ' + str(peach) +' glowing peaches!')
                peach -= 2
                Lumin_Forest()
            else:
                print ("There are no peaches growing")
                Lumin_Forest()
            break
        elif response == '3':
            if coco_beans > 0:
                print ("You found some rich coco beans! ")
                print ("You got "+str(coco_beans)+' coco beans')
                coco_beans -= 3
                Lumin_Forest()
            else:
                print ("there are no coco_beans right now")
                Lumin_Forest()
            break
        elif response == '2':
            if dragon_egg > 0:
                print ("The cove suddenly illuminates with dragons fire! You run to a dragon egg pick it up and run out as fast as you can\n you are skimmed however and lose 4 health  ")
                print ("You got "+ str(dragon_egg)+" dragon egg")
                Health -= 4
            if Health <= 0:
                death()
            else:
                print ("There arent any dragon eggs right now")
                Lumin_Forest()
            break
        elif response == '4':
            print ("You leave the peaceful forest behind")
            coco_beans +=3
            peach += 2
            dragon_egg += 1
            lumin_road()
        else:
            print("Invalid input")
            continue


#Caves------------
def darqthaal_road():
    desc = 'You are on the Darthaal road and can travel to..'
    choice_one = 'Borest (1)'
    choice_two = 'Lumin forest(2)'
    
    start_game = manager(desc, choice_one, choice_two)
    start_game.build()


    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print (' You travel on to Borest and see a sprawling city of pure white spires with a navy blue pointed roofs. Its majesticness leaves you in awe')
            Enter_Borest()
            Borest()
            break
        elif response == '2':
            print ("You travel to Lumin Forest and find enjoyement in the lush undergrowth fantasizing about the delectible ingredients you might find ")
            Lumin_Forest()
            break
        else:
            print("Invalid input")
            continue
def Darqthaal():
    global bandits_level
    print ('You stride down the cave and suddenly hear voices and a glow coming down the passage. You know this is a bandit hideout \nbecuase of the grim voices, you huddle behind a rock decide what you should do')
    print ('The bandits are level ' + str(bandits_level) + '(level coincides with damage)\n')
    print ('1. Attack the bandits!(1)\n')
    print ('2. Retreat from the cave(2)\n')
   
    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('You approach the bandits, ready for the fight and they give you a ferocious growl underneath their bandanas and begin THE CONFLICT')
            bandits()
            print ('You finish the fight and exit proud to rid the world of those cruel fellows')
            darqthaal_road()
            break
        elif response == '2':
            print ("You retreat from the cave glad to escape the conflict that could of arisen. ")
            darqthaal_road()
            break
        else:
            print("Invalid input")
            continue




#---------------
def three_one():
    desc = 'You arrive in Borest but as you begin to enter through the gates the guards start to question you'
    choice_one = 'Try to persuade them that you mean no harm (1)'
    choice_two = 'Walk around the walls and try to find a way in (2)'
    choice_three ='Demand entrance to the city(3)'

    start_game = manager(desc, choice_one, choice_two, choice_three)
    start_game.build()


    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('You explain were youve come from and they thank you for the native tribes info. You pass through')
            Enter_Borest()
            Borest()
            break
        elif response == '2':
            print ("As you walk you find a sketchy sewer drain that has broken bars and enter ")
            Sewers()
            break
        elif response == '3':
            death()
            break
        else:
            print("Invalid input")
            continue
def three_two():
    Lumin_Forest()
def three_three():
  Darqthaal()
#---------------
def three():  
    global stamina
    desc = 'You run away and stumble apon a high bluff and can see the entire island your on. However travel is limited'
    choice_one = 'Closest to you is the kindom Borest(1)'
    choice_two = 'Medium distance is a lush forest(2)'
    choice_three ='Farthest is a mysterious cave(3)'

    start_game = manager(desc, choice_one, choice_two, choice_three)
    start_game.build()


    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('You travel on to Borest and see a sprawling city of pure white spires with a navy blue pointed roofs. Its majesticness leaves you in awe.')
            stamina -= 1
            print ("Your stamina is now " + str(stamina)) 
            three_one()
            break
        elif response == '2':
            print ("You travel to the lush forest known as the Lumin Forest and are exited to see what sort of delectible ingredients you could find!")
            stamina -= 2
            print ("Your stamina is now " + str(stamina)) 
            three_two()
            break 
        elif response == '3':
            print ("You run to the cave known as Darqthaal and notice a suprising amount of light emitted from its maw as night falls. ")
            stamina -= 3
            print ("Your stamina is now " + str(stamina))
            three_three()
            break
        else:
            print("Invalid input")
            continue

def two():
    desc = 'These shrooms could flatten the natives around you but you are unsure about the risk it could put you in'
    choice_one = 'Throw it at the natives in hopes to destroy them (1)'
    choice_two = ' slowly tear apart the shroom and pull out the flammable goo and burn your bonds (2)'
    choice_three ='threaten the natives and force them to let you go(3)'

    start_game = manager(desc, choice_one, choice_two, choice_three)
    start_game.build()


    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('Your attempts are foolish, as you throw the mushroom it explodes and you die with the natives')
            death()
            break
        elif response == '2':
            print (" Your bonds burn away and you slowly creep away into the darkness")
            three()
            break
        elif response == '3':
            print ("The natives are frightened and you feel powerful as you exit the camp unharmed")
            three()
            break
        else:
            print("Invalid input")
            continue
#---------------
    

def start():
    desc = 'You awake to the sound of continious drumming from the ferocious natives \nand wonder how everything couldve gone so wrong. Your group of traveling chefs had \nonly been scouting for delicious mushrooms after all. Everything you have is gone \nexept your most favorite forest green cloke that had many pockets. As you survey\n the sourrounding area you realize you only have a couple options.'
    choice_one = 'You challenge the natives'
    choice_two = 'You reach into your cloak'
    choice_three = 'You try to loosen your bonds'    

    start_game = manager(desc, choice_one, choice_two, choice_three)
    start_game.build()


    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('The natives are so offended they chop your head of and ironically being a chef serve you to thier king on a silver plater')
            death()
            break
        elif response == '2':
            print ("you feel around in the cloak and to your astonishment find your beloved exploding shrooms. The natives thought they were harmless but you know the truth")
            two()
            break
        elif response == '3':
            print ("You will find that they weren't as tight as you expected. You slowly creep into the darkness.")
            three()
            break
        else:
            print("Invalid input")
            continue



Player_Profile()
start()
