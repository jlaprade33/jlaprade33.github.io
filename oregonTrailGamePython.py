#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 14:27:49 2018

@author: Jeff LaPrade
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import random
import turtle


#Beginning menu where the user is prompted for names
def begin():
    """Begins the game with an intro and records 
    who the leader and companions are"""
    
    print("\nThis program simulates a trip over the Oregon Trail from") 
    print("Independence Missouri to Oregon City, Oregon in 1847.")
    print("Your family of five will cover the 2040 mile Oregon Trail")    
    print("in 5-6 months -- if you make it alive.")
                 
    leader = input("What is the first name of the wagon leader?")
    print("What are the first names of the four other companions in your party?")
    print("1.", leader)
    comp1 = input("2. ")
    comp2 = input("3. ")
    comp3 = input("4. ")
    comp4 = input("5. ")
    name_tuple = (leader, comp1, comp2, comp3, comp4)
    return name_tuple
 
#def drawLine(t, x, y, l):
    '''This function is called in the turtle hunting function'''
    '''t.penup()
    t.goto(x, y)                #aligns the turtle to draw a line
    t.pendown()
    t.forward(l)                #draws the line of length l units'''
    
   

#Prompt for the user to choose a starting date
def start_date():  
    """Prompts the user to choose a starting date for the game"""
    #is protected input errors
    print("\nIt is 1847. Your jumping off place for Oregon is Independence,")
    print("Missouri. You must decide which month to leave Independence,")
    print("remember that must arrive in Oregon City by November 11th, 1847.\n")
    print("1. Default date is March 3rd, 1847.")
    print("2. March")
    print("3. April")
    print("4. May")
    start_decision = 'n'
    while start_decision == 'n' or start_decision == 'N' or start_decision == 'no' or start_decision == 'No':
        start_month = input("What is your choice for the beginning month?")
        if start_month == '1' or start_month == 'March':
            start_month = 'March'
            start_day = str(3)
            print("\nYou will begin your journey on", start_month, start_day+',', "1847.")
            start_decision = input("Are you sure this is the start date you would like (Y/N)?\n")
        elif start_month == '2' or start_month == 'March' or start_month == 'march':
            start_month = 'March'
            start_day = input("Which day in March would you like to begin on?")
            while start_day != '1' and start_day != '2' and start_day != '3' and start_day != '4' and start_day != '5' and start_day != '6' and start_day != '7' and start_day != '8' and start_day != '9' and start_day != '10' and start_day != '11' and start_day != '12' and start_day != '13' and start_day != '14' and start_day != '15' and start_day != '16' and start_day != '17' and start_day != '18' and start_day != '19' and start_day != '20' and start_day != '21' and start_day != '22' and start_day != '23' and start_day != '24' and start_day != '25' and start_day != '26' and start_day != '27' and start_day != '28' and start_day != '29' and start_day != '30' and start_day != '31': 
                print("You must choose a number between 1 and 31.")
                start_day = input("Which day in March would you like to begin on?")
            print("\nYou will begin your journey on", start_month, start_day+',', "1847.")
            start_decision = input("Are you sure this is the start date you would like (Y/N)?\n")
        elif start_month == '3' or start_month == 'April' or start_month == 'april':
            start_month = 'April'
            start_day = input("Which day in April would you like to begin on?")
            while start_day != '1' and start_day != '2' and start_day != '3' and start_day != '4' and start_day != '5' and start_day != '6' and start_day != '7' and start_day != '8' and start_day != '9' and start_day != '10' and start_day != '11' and start_day != '12' and start_day != '13' and start_day != '14' and start_day != '15' and start_day != '16' and start_day != '17' and start_day != '18' and start_day != '19' and start_day != '20' and start_day != '21' and start_day != '22' and start_day != '23' and start_day != '24' and start_day != '25' and start_day != '26' and start_day != '27' and start_day != '28' and start_day != '29' and start_day != '30': 
                print("You must choose a number between 1 and 30.")
                start_day = input("Which day in April would you like to begin on?")
            print("\nYou will begin your journey on", start_month, start_day+',', "1847.")
            start_decision = input("Are you sure this is the start date you would like (Y/N)?\n")
        elif start_month == '4' or start_month == 'May' or start_month == 'may':
            start_month = 'May'
            start_day = input("Which day in May would you like to begin on?")
            while start_day != '1' and start_day != '2' and start_day != '3' and start_day != '4' and start_day != '5' and start_day != '6' and start_day != '7' and start_day != '8' and start_day != '9' and start_day != '10' and start_day != '11' and start_day != '12' and start_day != '13' and start_day != '14' and start_day != '15' and start_day != '16' and start_day != '17' and start_day != '18' and start_day != '19' and start_day != '20' and start_day != '21' and start_day != '22' and start_day != '23' and start_day != '24' and start_day != '25' and start_day != '26' and start_day != '27' and start_day != '28' and start_day != '29' and start_day != '30' and start_day != '31': 
                print("You must choose a number between 1 and 31.")
                start_day = input("Which day in May would you like to begin on?")
            print("\nYou will begin your journey on", start_month, start_day+',', "1847.")
            start_decision = input("Are you sure this is the start date you would like (Y/N)?\n")
        else: 
            print("Error in month choice. Try again.")
        
    
    startDate_tuple = (start_month, start_day, "1847")
    return startDate_tuple

#The original store to begin the game
def beginning_store(money, oxen, food, bullets, medkit, wagon_parts):
    """The first stop at the store to begin the game"""
  
    print("You had saved $2000  to spend for the trip, and you've just")
    print("paid $200 for a wagon. You will need to spend the rest of your")
    print("money on the following items:\n")
    print("-Oxen. You can spend $100-$200 on your team. The more you spend,")
    print("the faster you'll go because you'll have better animals.\n")
    print("-Food. The more you have, the less chance there is of getting sick.\n")
    print("-Ammunition. You will need bullets for attacks by animals and bandits,")
    print("and for hunting for food.\n")
    print("-Miscellaneous supplies. This includes medicine and other things you")
    print("will need for sickness and emergency repairs.\n")
    
    print("You can spend all your money before you start the trip, or")
    print("you can save some of your cash to spend at forts along the way")
    print("when you run low. However, items cost more at the forts.")
    print("You can also go hunting along the way to get more food.")
    
    print("The Following are available purchase categories:")
    print("1. Oxen")
    print("2. Food")
    print("3. Bullets")
    print("4. Miscellaneous Supplies")
    
    buy_decision = input("Please enter the number from the category above that you wish to purchase from: ")
    
    #making sure that the user enters a correct option
    while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
        print("You must enter a number from the above categories.")
        buy_decision = input("Please choose a number from the four categories above: ")
        
    total_cost = 0
    oxen_spend = 0
    bullet_price = 0
    misc_supplies = 0
    lbs_spend = 0
    lbs = 0
    continue_buying = 'y'
        
    #User's chance to make a purchase is realized
    while total_cost <= money and continue_buying != 'no' and continue_buying != 'No' and continue_buying != 'n' and total_cost <= 1600:
        #oxen purchase section - DONE
        if (buy_decision == '1' or buy_decision == 'Oxen' or buy_decision == 'oxen') and oxen_spend <= 160:
            print("\nThere are two oxen in a yoke, and the price of each yoke is $40.")
            if oxen_spend >= 120 and oxen_spend < 200:
                buy_more = input("Would you like to 1 or 2 more yokes?")
                if buy_more != '1' and buy_more != '2':
                    while buy_more != '1' and buy_more != '2':
                        print("You can only buy 1 or 2 more yokes. Please try again")
                        buy_more = input("Would you like to 1 or 2 more yokes?")
                oxen_spend = oxen_spend + int(buy_more)*40
                if oxen_spend == 160:
                    buy_more = input("Would you like to another yoke and reach your limit for the current store?")
                    if buy_more == 'y' or buy_more == 'Y' or buy_more == 'yes':
                        oxen_spend = oxen_spend + 40

            #Makes sure your user's got straight cash   
            if money < 120:
                print("Once choosing Oxen, you must spend between $100 and $200")
                print("You do not have enough money to purchase a yoke in the range specified")
                oxen_spend = 0
                #total_cost = int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies)
                print('Current bill is: $', int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies))
                continue_buying = input("Would you like to make another purchase (Y/N)")
                while continue_buying !='y' and continue_buying !='Y' and continue_buying !='yes' and continue_buying !='no' and continue_buying !='n' and continue_buying !='N':
                    print("Your input was incorrect.")
                    continue_buying = input("Would you like to make another purchase (Y/N)?")
                if continue_buying == 'yes' or continue_buying == 'y' or continue_buying == 'Yes':
                    print("The Following are available purchase categories:")
                    print("1. Oxen")
                    print("2. Food")
                    print("3. Bullets")
                    print("4. Miscellaneous Supplies")
                    buy_decision = input("Through which of the above four categories would you like to make a purchase?")      
                    while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                        print("You must enter a number from the above categories.")
                        buy_decision = input("Please choose a number from the four categories above: ")
            #Oxen purchase when all is dandy in the financial world of the free folk
            while oxen_spend < 100 and money >= 120:
                print("Once choosing Oxen, you must spend between $100 and $200")
                #reset purchase since it was not in the allowed range
                spend = input("How many yokes would you like to purchase?")
                while spend != '1' and spend != '2' and spend != '3' and spend != '4' and spend != '5' and spend != '6':
                    print("You did not enter a correct amount. You must choose a quantity between 1-6.")
                    spend = input("How many yokes would you like to purchase?")
                oxen_spend = oxen_spend + int(spend)*40
                #fixes if oxen_spend is under 100
                while oxen_spend < 100:
                    oxen_spend = 0
                    print("You did not meet the purchase requirements. Let's try again.")
                    spend = input("How many yokes would you like to purchase?")
                    oxen_spend = oxen_spend + int(spend)*40
                #if oxen_spend
                if total_cost > money:
                    print("You do not have enough money to buy that quantity. Please try again.")
                    oxen_spend = 0
                #makes sure the user purchases an amount in the range specified
                if oxen_spend > 200:
                    oxen_spend = 0
                    print("Please try again, you cannot spend more than $200, or 5 yokes")
                    spend = input("How many yokes would you like to purchase?")
                    oxen_spend = oxen_spend + int(spend)*40
                #incrementing the oxen count
                oxen = oxen + int(spend)*2
                #total_cost = int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies)
                print('Current bill is: $', int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies))
                continue_buying = input("Would you like to make another purchase (Y/N)")
                while continue_buying !='y' and continue_buying !='Y' and continue_buying !='yes' and continue_buying !='no' and continue_buying !='n' and continue_buying !='N':
                    print("Your input was incorrect.")
                    continue_buying = input("Would you like to make another purchase (Y/N)?")
                if continue_buying == 'yes' or continue_buying == 'y' or continue_buying == 'Yes':
                    print("The Following are available purchase categories:")
                    print("1. Oxen")
                    print("2. Food")
                    print("3. Bullets")
                    print("4. Miscellaneous Supplies")
                    buy_decision = input("Through which of the above four categories would you like to make a purchase?")   
                    while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                        print("You must enter a number from the above categories.")
                        buy_decision = input("Please choose a number from the four categories above: ")
                        while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                            print("You must enter a number from the above categories.")
                            buy_decision = input("Please choose a number from the four categories above: ")
        #stop people from buying too many oxen   
        elif (buy_decision == '1' or buy_decision == 'Oxen' or buy_decision == 'oxen') and oxen_spend > 160:
            print("You have already met the limit for oxen purchases.")
            continue_buying = input("Would you like to make another purchase (Y/N)")
            while continue_buying !='y' and continue_buying !='Y' and continue_buying !='yes' and continue_buying !='no' and continue_buying !='n' and continue_buying !='N':
                    print("Your input was incorrect.")
                    continue_buying = input("Would you like to make another purchase (Y/N)?")
            if continue_buying == 'yes' or continue_buying == 'y' or continue_buying == 'Yes':
                print("The Following are available purchase categories:")
                print("1. Oxen")
                print("2. Food")
                print("3. Bullets")
                print("4. Miscellaneous Supplies")
                buy_decision = input("Through which of the above four categories would you like to make a purchase?")   
                while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                    print("You must enter a number from the above categories.")
                    buy_decision = input("Please choose a number from the four categories above: ")
        #food purchase section - DONE
        elif buy_decision == '2' or buy_decision == 'Food' or buy_decision == 'food' and (continue_buying != 'n' and continue_buying != 'N'):
            print("\nThe store owner recommends at least 200 lbs. per person, at 50 cents per pound.")
            #Makes sure the settlers got cash on hand
            if money < 0.5:
                print("You do not have enough money to purchase food.")
                continue_buying = input("Would you like to make another purchase (Y/N)")
                while continue_buying !='y' and continue_buying !='Y' and continue_buying !='yes' and continue_buying !='no' and continue_buying !='n' and continue_buying !='N':
                    print("Your input was incorrect.")
                    continue_buying = input("Would you like to make another purchase (Y/N)?")
                if continue_buying == 'yes' or continue_buying == 'y' or continue_buying == 'Yes':
                    print("The Following are available purchase categories:")
                    print("1. Oxen")
                    print("2. Food")
                    print("3. Bullets")
                    print("4. Miscellaneous Supplies")
                    buy_decision = input("Through which of the above four categories would you like to make a purchase, besides food?")    
                    while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                        print("You must enter a number from the above categories.")
                        buy_decision = input("Please choose a number from the four categories above: ")
            #if total_cost > money:
             #       print("You do not have enough money to buy that quantity. Please try again.")
              #      oxen_spend = 0        
            while money >= lbs and money >= 0.5 and continue_buying != 'No' and continue_buying != 'n' and buy_decision == '2':      
                pounds = input("How many pounds of food do you wish to purchase?")
                lbs_spend = lbs_spend + float(pounds)*0.5
                lbs = lbs + lbs_spend*2
                if money < lbs_spend:
                    print("You do not have enough money to purchase that amount of food. Try again or exit the store.")
                    #total_cost += int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies)
                    print('Current bill is: $', int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies))
                    continue_buying = input("Would you like to make another purchase (Y/N)")
                    while continue_buying !='y' and continue_buying !='Y' and continue_buying !='yes' and continue_buying !='no' and continue_buying !='n' and continue_buying !='N':
                        print("Your input was incorrect.")
                        continue_buying = input("Would you like to make another purchase (Y/N)?")
                    if continue_buying == 'yes' or continue_buying == 'y' or continue_buying == 'Yes':
                        print("The Following are available purchase categories:")
                        print("1. Oxen")
                        print("2. Food")
                        print("3. Bullets")
                        print("4. Miscellaneous Supplies")
                        buy_decision = input("Through which of the above four categories would you like to make a purchase, besides food?")            
                        while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                            print("You must enter a number from the above categories.")
                            buy_decision = input("Please choose a number from the four categories above: ")
                #increments the total food count
                else:
                    food = food + int(lbs_spend)*2
                    #total_cost += int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies)
                    print('Current bill is: $', int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies))
                    continue_buying = input("Would you like to make another purchase (Y/N)")
                    while continue_buying !='y' and continue_buying !='Y' and continue_buying !='yes' and continue_buying !='no' and continue_buying !='n' and continue_buying !='N':
                        print("Your input was incorrect.")
                        continue_buying = input("Would you like to make another purchase (Y/N)?")
                    if continue_buying == 'yes' or continue_buying == 'y' or continue_buying == 'Yes':
                        print("The Following are available purchase categories:")
                        print("1. Oxen")
                        print("2. Food")
                        print("3. Bullets")
                        print("4. Miscellaneous Supplies")
                        buy_decision = input("Through which of the above four categories would you like to make a purchase, besides food?")    
                        while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                            print("You must enter a number from the above categories.")
                            buy_decision = input("Please choose a number from the four categories above: ")
            #if the user has paid too much money, this will restart the purchase for food    
            if total_cost > money:
                print("You do not have enough money to buy that quantity. Please try again.")
                lbs_spend = 0 
                continue_buying = input("Would you like to make another purchase (Y/N)")
                while continue_buying !='y' and continue_buying !='Y' and continue_buying !='yes' and continue_buying !='no' and continue_buying !='n' and continue_buying !='N':
                    print("Your input was incorrect.")
                    continue_buying = input("Would you like to make another purchase (Y/N)?")
                if continue_buying == 'yes' or continue_buying == 'y' or continue_buying == 'Yes':
                    print("The Following are available purchase categories:")
                    print("1. Oxen")
                    print("2. Food")
                    print("3. Bullets")
                    print("4. Miscellaneous Supplies")
                    buy_decision = input("Through which of the above four categories would you like to make a purchase?")  
                    while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                        print("You must enter a number from the above categories.")
                        buy_decision = input("Please choose a number from the four categories above: ")
        #bullet purchase section - DONE
        elif buy_decision == '3' or buy_decision == 'bullets' or buy_decision == 'Bullets':
            
            #makes sure the user has enough money to buy bullets
            if money < 2:
                print("You do not have enough money to purchase even a single box of bullets.")
                #total_cost = int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies)
                print("Current bill is: $", int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies))
                continue_buying = input("Would you like to make another purchase (Y/N)")
                while continue_buying !='y' and continue_buying !='Y' and continue_buying !='yes' and continue_buying !='no' and continue_buying !='n' and continue_buying !='N':
                    print("Your input was incorrect.")
                    continue_buying = input("Would you like to make another purchase (Y/N)?")
                if continue_buying == 'yes' or continue_buying == 'y' or continue_buying == 'Yes':
                    print("The Following are available purchase categories:")
                    print("1. Oxen")
                    print("2. Food")
                    print("3. Bullets")
                    print("4. Miscellaneous Supplies")
                    buy_decision = input("Through which of the above four categories would you like to make a purchase, besides bullets?")
                    while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                        print("You must enter a number from the above categories.")
                        buy_decision = input("Please choose a number from the four categories above: ")
            #the purchase takes place here if the user has enough money
            elif money >=2:
                print("\nA box of 20 bullets costs $2.")
                bullet_boxes = input("How many boxes of bullets would you like to buy?")
                bullet_price = int(bullet_boxes)*2
                #total_cost = int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies)
                print("Current bill is: $", int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies))
                #increments the amount of bullets the user owns
                bullets = bullets + int(bullet_boxes)*20
                
                continue_buying = input("Would you like to make another purchase (Y/N)")
                while continue_buying !='y' and continue_buying !='Y' and continue_buying !='yes' and continue_buying !='no' and continue_buying !='n' and continue_buying !='N':
                    print("Your input was incorrect.")
                    continue_buying = input("Would you like to make another purchase (Y/N)?")
                if continue_buying == 'yes' or continue_buying == 'y' or continue_buying == 'Yes':
                    print("The Following are available purchase categories:")
                    print("1. Oxen")
                    print("2. Food")
                    print("3. Bullets")
                    print("4. Miscellaneous Supplies")
                    buy_decision = input("Through which of the above four categories would you like to make a purchase?")    
                    while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                        print("You must enter a number from the above categories.")
                        buy_decision = input("Please choose a number from the four categories above: ")
                #print("Your current bill is $", oxen_spend + lbs + bullet_price)
            
        #rest of the purchase options - Should be done
        elif buy_decision == '4' or buy_decision == 'miscellaneous supplies' or buy_decision == 'Miscellaneous Supplies':
            #checks to see if the user has enough money for a purchase
            if money < 10:
                print("You do not have enough money to purchase any misc. supplies.")
                continue_buying = input("Would you like to make another purchase (Y/N)")
                while continue_buying !='y' and continue_buying !='Y' and continue_buying !='yes' and continue_buying !='no' and continue_buying !='n' and continue_buying !='N':
                    print("Your input was incorrect.")
                    continue_buying = input("Would you like to make another purchase (Y/N)?")
                if continue_buying == 'yes' or continue_buying == 'y' or continue_buying == 'Yes':
                    print("The Following are available purchase categories:")
                    print("1. Oxen")
                    print("2. Food")
                    print("3. Bullets")
                    print("4. Miscellaneous Supplies")
                    buy_decision = input("Through which of the above four categories would you like to make a purchase, besides misc. supplies?")
                    while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                        print("You must enter a number from the above categories.")
                        buy_decision = input("Please choose a number from the four categories above: ")
            #makes sure the user has enough money for supplies
            elif money >= 10:
                print("\nA wagon part (wheels, axels, tongues) costs $10")
                wagon_part_purchase = input("How many wagon parts would you like to buy?")
                if money < 15:
                    print("You do not have enough money to purchase a medical kit.")
                    medical_kit = 0
                elif money >=15:
                    print("\nA medical kit costs $15.")
                    medical_kit = input("How many medical kits would you like to purchase?")
                misc_supplies = int(wagon_part_purchase)*10 + int(medical_kit)*15
                #increment misc supplies
                wagon_parts = wagon_parts + int(wagon_part_purchase)
                medkit = medkit + int(medical_kit)
                #total_cost = int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies)
                print("Current bill is: $", int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies))
                continue_buying = input("Would you like to make another purchase (Y/N)")
                while continue_buying !='y' and continue_buying !='Y' and continue_buying !='yes' and continue_buying !='no' and continue_buying !='n' and continue_buying !='N':
                    print("Your input was incorrect.")
                    continue_buying = input("Would you like to make another purchase (Y/N)?")
                if continue_buying == 'yes' or continue_buying == 'y' or continue_buying == 'Yes':
                    print("The Following are available purchase categories:")
                    print("1. Oxen")
                    print("2. Food")
                    print("3. Bullets")
                    print("4. Miscellaneous Supplies")
                    buy_decision = input("Through which of the above four categories would you like to make a purchase?")    
                    while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                        print("You must enter a number from the above categories.")
                        buy_decision = input("Please choose a number from the four categories above: ")
               
    #print(int(oxen_spend), float(lbs_spend), int(bullet_price), int(misc_supplies))
    total_cost = int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies)   
    
    if (continue_buying == 'no' or continue_buying == 'n' or continue_buying == 'No') and total_cost <= 1600:
        money = money - total_cost
        supply_array = (money, oxen, bullets, food, medkit, wagon_parts)
        return supply_array  
    
    #IF they spend too much, we start over and call the function recursively
    if total_cost > 1600:
        print("\n\n\n\nYou spent too much money. Let's start over.")
        print("1. Oxen")
        print("2. Food")
        print("3. Bullets")
        print("4. Miscellaneous Supplies")
        total_cost = 0
        oxen_spend = 0
        bullets = 0
        food = 0
        oxen = 0
        bullets = 0
        wagon_parts = 0
        medkit = 0
        money = 1600
        continue_buying = 'y'
        
        redo_array = beginning_store(money, oxen, food, bullets, medkit, wagon_parts)
        
        money = redo_array[0]
        oxen = redo_array[1]
        bullets = redo_array[2]
        food = redo_array[3]
        medkit = redo_array[4]
        wagon_parts = redo_array[5]
        
        supply_array = (money, oxen, bullets, food, medkit, wagon_parts)
        return supply_array  
    
     

#Function for all of the stores coming after the original store
def travel_store(visits, money, oxen, bullets, food, medkit, wagon_parts):
    """Function for all of the stores coming after the intial shop"""
  
    print("You have $"+str(money), "remaining to spend for the trip. You will")
    print("need to spend the rest of your money on the following items:\n")
    print("-Oxen. You can spend $100-$200 on your team. The more you spend,")
    print("the faster you'll go because you'll have better animals.\n")
    print("-Food. The more you have, the less chance there is of getting sick.\n")
    print("-Ammunition. You will need bullets for attacks by animals and bandits,")
    print("and for hunting for food.\n")
    print("-Miscellaneous supplies. This includes medicine and other things you")
    print("will need for sickness and emergency repairs.\n")
    
    print("The Following are available purchase categories:")
    print("1. Oxen")
    print("2. Food")
    print("3. Bullets")
    print("4. Miscellaneous Supplies")
    
    buy_decision= input("Please enter the number from the category above that you wish to purchase from: ")
    #makes sure the user selects a correct category
    while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
        print("You must enter a number from the above categories.")
        buy_decision = input("Please choose a number from the four categories above: ")
    
    price_increase = 1
    price_increase += visits*0.25
    total_cost = 0
    oxen_spend = 0
    bullet_price = 0
    misc_supplies = 0
    lbs_spend = 0
    lbs = 0
    total_cost = 0
    continue_buying = 'y'
    #print('starting food', food)
    
    #User's chance to make a purchase is realized
    while total_cost <= money and continue_buying != 'no' and continue_buying != 'No' and continue_buying != 'n' and money > 0:
        #oxen purchase section - DONE
        if (buy_decision == '1' or buy_decision == 'Oxen' or buy_decision == 'oxen') and oxen_spend <= 160*price_increase:
            print("\nThere are two oxen in a yoke, and the price of each yoke is $", price_increase*40.) 
            if oxen_spend >= 120*price_increase and oxen_spend < 200*price_increase:
                buy_more = input("Would you like to 1 or 2 more yokes?")
                if buy_more != '1' and buy_more != '2':
                    while buy_more != '1' and buy_more != '2':
                        print("You can only buy 1 or 2 more yokes. Please try again")
                        buy_more = input("Would you like to 1 or 2 more yokes?")
                oxen_spend = oxen_spend + int(buy_more)*(40*price_increase)
                if oxen_spend == 160*price_increase:
                    buy_more = input("Would you like to another yoke and reach your limit for the current store?")
                    if buy_more == 'y' or buy_more == 'Y' or buy_more == 'yes':
                        oxen_spend = oxen_spend + 40*price_increase
                    else:
                        buy_more = ''
            #Makes sure your user's got straight cash   
            if money < 120*price_increase:
                print("Once choosing Oxen, you must spend between $", 100*price_increase, " and $", 200*price_increase)
                print("You do not have enough money to purchase a yoke in the range specified")
                oxen_spend = 0
                #total_cost = int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies)
                print('Current bill is: $', int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies))
                continue_buying = input("Would you like to make another purchase (Y/N)")
                while continue_buying !='y' and continue_buying !='Y' and continue_buying !='yes' and continue_buying !='no' and continue_buying !='n' and continue_buying !='N':
                    print("Your input was incorrect.")
                    continue_buying = input("Would you like to make another purchase (Y/N)?")
                if continue_buying == 'yes' or continue_buying == 'y' or continue_buying == 'Yes':
                    print("The Following are available purchase categories:")
                    print("1. Oxen")
                    print("2. Food")
                    print("3. Bullets")
                    print("4. Miscellaneous Supplies")
                    buy_decision = input("Through which of the above four categories would you like to make a purchase?")      
                    while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                        print("You must enter a number from the above categories.")
                        buy_decision = input("Please choose a number from the four categories above: ")
            #Oxen purchase when all is dandy in the financial world of the free folk
            while oxen_spend < 100*price_increase and money >= 120*price_increase:
                print("Once choosing Oxen, you must spend between $", 100*price_increase, " and $", 200*price_increase)
                #reset purchase since it was not in the allowed range
                spend = input("How many yokes would you like to purchase?")
                while spend != '1' and spend != '2' and spend != '3' and spend != '4' and spend != '5' and spend != '6':
                    print("You did not enter a correct amount. You must choose a quantity between 1-6.")
                    spend = input("How many yokes would you like to purchase?")
                oxen_spend = oxen_spend + int(spend)*(40*price_increase)
                #fixes if oxen_spend is under 100
                while oxen_spend < 100*price_increase:
                    oxen_spend = 0
                    print("You did not meet the purchase requirements. Let's try again.")
                    spend = input("How many yokes would you like to purchase?")
                    oxen_spend = oxen_spend + int(spend)*(40*price_increase)
                #if oxen_spend
                if total_cost > money:
                    print("You do not have enough money to buy that quantity. Please try again.")
                    oxen_spend = 0
                #makes sure the user purchases an amount in the range specified
                if oxen_spend > 200*price_increase:
                    oxen_spend = 0
                    print("Please try again, you cannot spend more than $", 200*price_increase, ", or 5 yokes")
                    spend = input("How many yokes would you like to purchase?")
                    oxen_spend = oxen_spend + int(spend)*(40*price_increase)
                #incrementing the oxen count
                oxen = oxen + int(spend)*2
                #total_cost = int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies)
                print('Current bill is: $', int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies))
                continue_buying = input("Would you like to make another purchase (Y/N)")
                while continue_buying !='y' and continue_buying !='Y' and continue_buying !='yes' and continue_buying !='no' and continue_buying !='n' and continue_buying !='N':
                    print("Your input was incorrect.")
                    continue_buying = input("Would you like to make another purchase (Y/N)?")
                if continue_buying == 'yes' or continue_buying == 'y' or continue_buying == 'Yes':
                    print("The Following are available purchase categories:")
                    print("1. Oxen")
                    print("2. Food")
                    print("3. Bullets")
                    print("4. Miscellaneous Supplies")
                    buy_decision = input("Through which of the above four categories would you like to make a purchase?")   
                    while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                        print("You must enter a number from the above categories.")
                        buy_decision = input("Please choose a number from the four categories above: ")
        #stop people from buying too many oxen   
        elif (buy_decision == '1' or buy_decision == 'Oxen' or buy_decision == 'oxen') and oxen_spend > 160*price_increase:
            print("You have already met the limit for oxen purchases.")
            continue_buying = input("Would you like to make another purchase (Y/N)")
            while continue_buying !='y' and continue_buying !='Y' and continue_buying !='yes' and continue_buying !='no' and continue_buying !='n' and continue_buying !='N':
                    print("Your input was incorrect.")
                    continue_buying = input("Would you like to make another purchase (Y/N)?")
            if continue_buying == 'yes' or continue_buying == 'y' or continue_buying == 'Yes':
                print("The Following are available purchase categories:")
                print("1. Oxen")
                print("2. Food")
                print("3. Bullets")
                print("4. Miscellaneous Supplies")
                buy_decision = input("Through which of the above four categories would you like to make a purchase?")   
                while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                        print("You must enter a number from the above categories.")
                        buy_decision = input("Please choose a number from the four categories above: ")
        #food purchase section - DONE
        elif buy_decision == '2' or buy_decision == 'Food' or buy_decision == 'food' and (continue_buying != 'n' and continue_buying != 'N'):
            print("\nThe store owner recommends at least 200 lbs. per person, at ", 50*price_increase, "cents per pound.")
            #Makes sure the settlers got cash on hand
            if money < 0.5:
                print("You do not have enough money to purchase food.")
                continue_buying = input("Would you like to make another purchase (Y/N)")
                while continue_buying !='y' and continue_buying !='Y' and continue_buying !='yes' and continue_buying !='no' and continue_buying !='n' and continue_buying !='N':
                    print("Your input was incorrect.")
                    continue_buying = input("Would you like to make another purchase (Y/N)?")
                if continue_buying == 'yes' or continue_buying == 'y' or continue_buying == 'Yes':
                    print("The Following are available purchase categories:")
                    print("1. Oxen")
                    print("2. Food")
                    print("3. Bullets")
                    print("4. Miscellaneous Supplies")
                    buy_decision = input("Through which of the above four categories would you like to make a purchase, besides food?")    
                    while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                        print("You must enter a number from the above categories.")
                        buy_decision = input("Please choose a number from the four categories above: ")
            while money >= lbs and money >= 0.5*price_increase and continue_buying != 'No' and continue_buying != 'n' and buy_decision == '2':      
                pounds = input("How many pounds of food do you wish to purchase?")
                lbs_spend = lbs_spend + float(pounds)*(0.5*price_increase)
                lbs = lbs + lbs_spend*(2*price_increase)
                #lbs = lbs_spend*(2*price_increase)
                if money < lbs_spend:
                    print("You do not have enough money to purchase that amount of food. Try again or exit the store.")
                    lbs_spend = 0
                    lbs = 0
                    #total_cost += int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies)
                    print('Current bill is: $', int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies))
                    continue_buying = input("Would you like to make another purchase (Y/N)")
                    while continue_buying !='y' and continue_buying !='Y' and continue_buying !='yes' and continue_buying !='no' and continue_buying !='n' and continue_buying !='N':
                        print("Your input was incorrect.")
                        continue_buying = input("Would you like to make another purchase (Y/N)?")
                    if continue_buying == 'yes' or continue_buying == 'y' or continue_buying == 'Yes':
                        print("The Following are available purchase categories:")
                        print("1. Oxen")
                        print("2. Food")
                        print("3. Bullets")
                        print("4. Miscellaneous Supplies")
                        buy_decision = input("Through which of the above four categories would you like to make a purchase, besides food?")            
                        while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                            print("You must enter a number from the above categories.")
                            buy_decision = input("Please choose a number from the four categories above: ")
                #increments the total food count
                else:
                    food = food + int(pounds)
                    #food = int(lbs_spend)*(2*price_increase)
                    #total_cost += int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies)
                    print('Current bill is: $', int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies))
                    continue_buying = input("Would you like to make another purchase (Y/N)")
                    while continue_buying !='y' and continue_buying !='Y' and continue_buying !='yes' and continue_buying !='no' and continue_buying !='n' and continue_buying !='N':
                        print("Your input was incorrect.")
                        continue_buying = input("Would you like to make another purchase (Y/N)?")
                    if continue_buying == 'yes' or continue_buying == 'y' or continue_buying == 'Yes':
                        print("The Following are available purchase categories:")
                        print("1. Oxen")
                        print("2. Food")
                        print("3. Bullets")
                        print("4. Miscellaneous Supplies")
                        buy_decision = input("Through which of the above four categories would you like to make a purchase, besides food?")    
                        while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                                print("You must enter a number from the above categories.")
                                buy_decision = input("Please choose a number from the four categories above: ")
            #if the user has paid too much money, this will restart the purchase for food    
            if total_cost > money:
                print("You do not have enough money to buy that quantity. Please try again.")
                lbs_spend = 0 
                continue_buying = input("Would you like to make another purchase (Y/N)")
                while continue_buying !='y' and continue_buying !='Y' and continue_buying !='yes' and continue_buying !='no' and continue_buying !='n' and continue_buying !='N':
                    print("Your input was incorrect.")
                    continue_buying = input("Would you like to make another purchase (Y/N)?")
                if continue_buying == 'yes' or continue_buying == 'y' or continue_buying == 'Yes':
                    print("The Following are available purchase categories:")
                    print("1. Oxen")
                    print("2. Food")
                    print("3. Bullets")
                    print("4. Miscellaneous Supplies")
                    buy_decision = input("Through which of the above four categories would you like to make a purchase?")  
                    while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                        print("You must enter a number from the above categories.")
                        buy_decision = input("Please choose a number from the four categories above: ")
        #bullet purchase section - DONE
        elif buy_decision == '3' or buy_decision == 'bullets' or buy_decision == 'Bullets':
            
            #makes sure the user has enough money to buy bullets
            if money < 2:
                print("You do not have enough money to purchase even a single box of bullets.")
                #total_cost = int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies)
                print("Current bill is: $", int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies))
                continue_buying = input("Would you like to make another purchase (Y/N)")
                while continue_buying !='y' and continue_buying !='Y' and continue_buying !='yes' and continue_buying !='no' and continue_buying !='n' and continue_buying !='N':
                    print("Your input was incorrect.")
                    continue_buying = input("Would you like to make another purchase (Y/N)?")
                if continue_buying == 'yes' or continue_buying == 'y' or continue_buying == 'Yes':
                    print("The Following are available purchase categories:")
                    print("1. Oxen")
                    print("2. Food")
                    print("3. Bullets")
                    print("4. Miscellaneous Supplies")
                    buy_decision = input("Through which of the above four categories would you like to make a purchase, besides bullets?")
                    while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                        print("You must enter a number from the above categories.")
                        buy_decision = input("Please choose a number from the four categories above: ")
            #the purchase takes place here if the user has enough money
            elif money >=2:
                print("\nA box of 20 bullets costs $",2*price_increase,".")
                bullet_boxes = input("How many boxes of bullets would you like to buy?")
                bullet_price = int(bullet_boxes)*(2*price_increase)
                #total_cost = int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies)
                print("Current bill is: $", int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies))
                #increments the amount of bullets the user owns
                bullets = bullets + int(bullet_boxes)*20
                
                continue_buying = input("Would you like to make another purchase (Y/N)")
                while continue_buying !='y' and continue_buying !='Y' and continue_buying !='yes' and continue_buying !='no' and continue_buying !='n' and continue_buying !='N':
                    print("Your input was incorrect.")
                    continue_buying = input("Would you like to make another purchase (Y/N)?")
                if continue_buying == 'yes' or continue_buying == 'y' or continue_buying == 'Yes':
                    print("The Following are available purchase categories:")
                    print("1. Oxen")
                    print("2. Food")
                    print("3. Bullets")
                    print("4. Miscellaneous Supplies")
                    buy_decision = input("Through which of the above four categories would you like to make a purchase?")    
                    while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                        print("You must enter a number from the above categories.")
                        buy_decision = input("Please choose a number from the four categories above: ")
                #print("Your current bill is $", oxen_spend + lbs + bullet_price)
            
        #rest of the purchase options - Should be done
        elif buy_decision == '4' or buy_decision == 'miscellaneous supplies' or buy_decision == 'Miscellaneous Supplies':
            #checks to see if the user has enough money for a purchase
            if money < 10*price_increase:
                print("You do not have enough money to purchase any misc. supplies.")
                continue_buying = input("Would you like to make another purchase (Y/N)")
                while continue_buying !='y' and continue_buying !='Y' and continue_buying !='yes' and continue_buying !='no' and continue_buying !='n' and continue_buying !='N':
                    print("Your input was incorrect.")
                    continue_buying = input("Would you like to make another purchase (Y/N)?")
                if continue_buying == 'yes' or continue_buying == 'y' or continue_buying == 'Yes':
                    print("The Following are available purchase categories:")
                    print("1. Oxen")
                    print("2. Food")
                    print("3. Bullets")
                    print("4. Miscellaneous Supplies")
                    buy_decision = input("Through which of the above four categories would you like to make a purchase, besides misc. supplies?")
                    while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                        print("You must enter a number from the above categories.")
                        buy_decision = input("Please choose a number from the four categories above: ")
            #makes sure the user has enough money for supplies
            elif money >= 10*price_increase:
                print("\nA wagon part (wheels, axels, tongues) costs $", 10*price_increase)
                wagon_part_purchase = input("How many wagon parts would you like to buy?")
                if money < 15*price_increase:
                    print("You do not have enough money to purchase a medical kit.")
                    medical_kit = 0
                elif money >=15*price_increase:
                    print("\nA medical kit costs $15.")
                    medical_kit = input("How many medical kits would you like to purchase?")
                misc_supplies = int(wagon_part_purchase)*(10*price_increase) + int(medical_kit)*(15*price_increase)
                #increment misc supplies
                wagon_parts = wagon_parts + int(wagon_part_purchase)
                medkit = medkit + int(medical_kit)
                #total_cost = int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies)
                print("Current bill is: $", int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies))
                continue_buying = input("Would you like to make another purchase (Y/N)")
                while continue_buying !='y' and continue_buying !='Y' and continue_buying !='yes' and continue_buying !='no' and continue_buying !='n' and continue_buying !='N':
                    print("Your input was incorrect.")
                    continue_buying = input("Would you like to make another purchase (Y/N)?")
                if continue_buying == 'yes' or continue_buying == 'y' or continue_buying == 'Yes':
                    print("The Following are available purchase categories:")
                    print("1. Oxen")
                    print("2. Food")
                    print("3. Bullets")
                    print("4. Miscellaneous Supplies")
                    buy_decision = input("Through which of the above four categories would you like to make a purchase?")    
                    while buy_decision != '1' and buy_decision != '2' and buy_decision != '3' and buy_decision != '4': 
                        print("You must enter a number from the above categories.")
                        buy_decision = input("Please choose a number from the four categories above: ")
               
    #print(int(oxen_spend), float(lbs_spend), int(bullet_price), int(misc_supplies))
    total_cost = int(oxen_spend) + float(lbs_spend) + int(bullet_price) + int(misc_supplies)   
    if money <= 0:
        print("You ran out of money and cannot make any purchases. Good luck the rest of the way.")
        money = 0
    
    #print('you bought this much food', food)
    if continue_buying == 'no' or continue_buying == 'n' or continue_buying == 'No':
        money = money - total_cost
        supply_array = (money, oxen, bullets, food, medkit, wagon_parts)
        return supply_array   
    

#Completed Graph EXTRA CREDIT
def display_supples(money, oxen, food, bullets, medkit, wagon_parts):
    """This function will give the player the option to view their supplies
    as a graph"""
    x= ('Money', 'Oxen', 'Food', 'Bullets', 'Medkits', 'Wagon Parts')
    y_pos = np.arange(len(x))
    y = (money, oxen, food, bullets, medkit, wagon_parts)
    
    plt.bar(y_pos, y, align='center', alpha=0.5, color='blue')
    plt.xticks(y_pos, x)
    plt.ylabel('Amount')
    plt.title('Supplies Remaining')
    
    plt.show()


#Needs to come after each turn
def update_current_day(current_month, current_day, days_per_turn):
    '''Gives the current day at the start of each turn'''
    day = int(current_day)
    month = current_month
    #The following if statements update the current day and month based 
    #on each month's total calendar days
    if month == "March":
        day += days_per_turn
        if day > 31:
            day = day% 31
            month = "April"
    elif month == "April":
        day += days_per_turn
        if day > 30:
            day = day%30
            month = "May"
            
    elif month == "May":
        day += days_per_turn
        if day > 31:
            day = day%31
            month = "June"
            
    elif month == "June":
        day += days_per_turn
        if day > 30:
            day = day%30
            month = "July"
        
    elif month == "July":
        day += days_per_turn
        if day > 31:
            day = day%31
            month = "August"
        
    elif month == "August":
        day += days_per_turn
        if day > 31:
            day = day%31
            month = "September"
        
    elif month == "September":
        day += days_per_turn
        if day > 30:
            day = day%30
            month = "October"
        
    elif month == "October":
        day += days_per_turn
        if day > 31:
            day = day%31
            month = "November"
        
    elif month == "November":
        day += days_per_turn
        if day > 30:
            day = day%30
            month = "December"   
    else:
        print("Month error")
    
    current_date_array = [month, day]
    return current_date_array

'''def update_miles_traveled(miles_traveled, miles_from_turn):
   ''' '''Updates the distance traveled after turn''' '''
    miles_traveled = miles_traveled + miles_from_turn
    return miles_traveled
    
def update_miles_to_go(miles_traveled, miles_to_go):
  '''  '''Updates the distance remaining in the trip after each turn''' '''
    miles_to_go = miles_to_go - miles_traveled
    return miles_to_go   
    '''
    
def next_landmark(miles_traveled):
    '''Displays the next landmark on the trek'''
    landmark_name = ''
    if miles_traveled < 554:
        landmark_name = "Chimney Rock"
        distance = 554 - miles_traveled
    elif miles_traveled < 830:
        landmark_name = "Independence Rock"
        distance = 830 - miles_traveled
    elif miles_traveled < 932:
        landmark_name = "South Pass"
        distance = 932- miles_traveled
    elif miles_traveled < 1295:
        landmark_name = "Soda Springs"
        distance = 1295- miles_traveled
    elif miles_traveled < 1808:
        landmark_name = "Blue Mountains"
        distance = 1808 - miles_traveled
    else:
        landmark_name = "Oregon City"
        distance = 2040 - miles_traveled
        
    landmark_array = [landmark_name, distance]
    return landmark_array
    
#All GOOD
def status_update(current_month, current_day, miles_to_go, miles_traveled, store_list):
    '''Update given at the start of each turn'''
    #display graph of supplies
    print("\nBelow are your current supplies for each category.")
    money = store_list[0]
    oxen = store_list[1]
    bullets = store_list[2]
    food = store_list[3]
    medkit = store_list[4]
    wagon_parts = store_list[5] 
    display_supples(money, oxen, food, bullets, medkit, wagon_parts)
    print("The current day is", current_month, str(current_day)+",",str(1847)+".")
    #Miles traveled is run through the miles_traveled function
    print("You have traveled", miles_traveled,"miles so far in this trip.")
    print("There are", miles_to_go, "remaining miles until you reach your destination.")
    
    #Display upcoming landmarks
    landmark_array = next_landmark(miles_traveled)
    landmark_name = landmark_array[0]
    distance = landmark_array[1]
    print("The next landmark will be", landmark_name, "in", distance, "miles.")
 
def puzzle():
    '''The puzzle decides if the player is successful when
    when defending against raiders'''
    number = random.randrange(0,11)
    return number

def tusken_raiders(money, wagon_parts, bullets, oxen, food, miles_traveled):
    '''At the end of each turn, this function will run a
    probability to determine if the player is attacked by raiders'''
    
    #THE ALL KNOWING PROBABILITY
    attack_probability = round((((miles_traveled/100)**2)+72)/(((miles_traveled/100)**2)+12)-1)
    attack_generator = random.randrange(1,101)
    if attack_generator == attack_probability:
        print("You are about to be attacked by raiders. You have three options:")
        print('1. Run, leaving behind one Ox, 10 lbs of food, and 1 wagon part.')
        print('2. Fight, but risk losing a significant amount of money and bullets.')
        print('3. Surrender and lose one quarter of your cash reserves.')
        attack_decision = input('What is the attack option you choose?:')
        if attack_decision == '1':
            oxen = oxen - 1
            food = food - 10
            wagon_parts = wagon_parts - 1
            print("Good thinking, running seemed like the best option this time!")
        elif attack_decision == '2':
            puzzle_guess = input("In order to be achieve success in the attack, you must enter a number between 1-10:")
            puzzle_answer = puzzle()
            if puzzle_answer == puzzle_guess:
                food += 50
                bullets += 50
                print("Congratulations! You showed those raiders who's boss. You gained 50 lbs of food and 50 bullets!")
            else:
                print("Well, you certainly gave it your all. The raiders were just too much to overcome.")
                print("They took a quarter of your cash and you used up 50 bullets trying to stop them.")
                money = money*0.75
                if bullets >= 50:
                    bullets = bullets - 50
                else:
                    bullets = 0        
        elif attack_decision == '3':
            print("Surrending sometimes can be the safest option. You lost a quarter of your money, but nobody was harmed.")
            money = money*.75
            
    raider_array = [money, wagon_parts, bullets, oxen, food]
    return raider_array

'''def writeText(t, x, y, text):
    #Used in the turtle hunting function
    #t = turtle.Turtle()
    t.setheading(0)
    t.penup()
    t.goto(x, y)            #aligns the turtle to write
    t.pendown()
    t.write(text, move=True, align="left", font=("Arial", 8, "normal"))  #writes text input

def turtle_hunting(rabbit_found, fox_found, deer_found, bear_found, moose_found):
    #Didn't like the odds for hunting through the puzzle, so I created a turtle 
    #race to decide if hunting is successful EXTRA CREDIT
    wn = turtle.Screen()
    wn.bgcolor('lightgray') 
    t = turtle.Turtle()
    # 3. Create a grid to track our turtles' progress.
    writeText(t, -270, 240, "Hunting Start") 
    drawLine(t,-240, 240, 500)
    writeText(t, -270, -250, "Out of range")  
    drawLine(t,-240, -250, 500)
    rabbit_attempt = 'n'
    fox_attempt = 'n'
    deer_attempt = 'n'
    bear_attempt = 'n'
    moose_attempt = 'n'
     
    if rabbit_found:
        rabbit = turtle.Turtle()
        rabbit.color('darkgray')
        rabbit.shape('turtle')
        rabbit.penup()
        rabbit.goto(-77.5, 240)
        rabbit.pendown()           #pen down makes this turtle ready to draw when called upon
        rabbit.setheading(270)   #makes the turtle face south for the race
        rabbit_position = 0
        writeText(t, -77.5, 240, "rabbit")  
        
    if fox_found:
        fox  = turtle.Turtle()
        fox.color('darkorange')
        fox.shape('turtle')
        fox.penup()
        fox.goto(-37.5, 240)
        fox.pendown()           #pen down makes this turtle ready to draw when called upon
        fox.setheading(270)   #makes the turtle face south for the race
        fox_position = 0
        writeText(t, -37.5, 240, "fox")  
        
    if deer_found:
        deer  = turtle.Turtle()
        deer.color('brown')
        deer.shape('turtle')
        deer.penup()
        deer.goto(0, 240)
        deer.pendown()           #pen down makes this turtle ready to draw when called upon
        deer.setheading(270)   #makes the turtle face south for the race
        deer_position = 0
        writeText(t, 0, 240, "deer")  
        
    if bear_found:
        bear  = turtle.Turtle()
        bear.color('black')
        bear.shape('turtle')
        bear.penup()
        bear.goto(37.5, 240)
        bear.pendown()           #pen down makes this turtle ready to draw when called upon
        bear.setheading(270)   #makes the turtle face south for the race
        bear_position = 0
        writeText(t, 37.5, 240, "bear")  
        
    if moose_found:
        moose  = turtle.Turtle()
        moose.color('maroon')
        moose.shape('turtle')
        moose.penup()
        moose.goto(77.5, 240)
        moose.pendown()           #pen down makes this turtle ready to draw when called upon
        moose.setheading(270)   #makes the turtle face south for the race
        moose_position = 0
        writeText(t, 77.5, 240, "moose")  

    
      # 6. Send them moving down the screen
    for i in range(0,1000,10):                    #turtle race going up to 1000 units in increments of 10
        if rabbit_found:
            rabbit_random = random.randrange(1,10)
            rabbit.forward(rabbit_random) 
            rabbit_position += rabbit_random
            #print(rabbit_position)
        if fox_found:
            fox_random = random.randrange(1,10)
            fox.forward(fox_random) 
            fox_position += fox_random
            #print(fox_position)
        if deer_found:
            deer_random = random.randrange(1,10)
            deer.forward(deer_random) 
            deer_position += deer_random 
            #print(deer_position)
        if bear_found:
            bear_random = random.randrange(1,10)
            bear.forward(bear_random) 
            bear_position += bear_random
           # print(bear_position)
        if moose_found:
            moose_random = random.randrange(1,10)
            moose.forward(moose_random) 
            moose_position += moose_random
            #print(moose_position)
            
    if rabbit_found and rabbit_position < 496:
        rabbit_attempt = 'y'
    if fox_found and fox_position < 496:
        fox_attempt = 'y'
    if deer_found and deer_position < 496:
        deer_attempt = 'y'
    if bear_found and bear_position < 496:
        bear_attempt = 'y'
    if moose_found and moose_position < 496:
        moose_attempt = 'y'
    
    turtle_array = [rabbit_attempt, fox_attempt, deer_attempt, bear_attempt, moose_attempt]
    wn.exitonclick()
    return turtle_array'''
    
def lets_go_hunting(food, bullets, sick_members, family_remaining):
    '''If the user decides to hunt for food, this function is called
    where the probabilities are laid out for each animal and food/bullets
    are adjusted accordingly'''
    #a hunt takes 1 day
    days_per_turn = 1
    
    #set the attempts to n, only to be changed if prompted by the user
    rabbit_attempt = "n"
    deer_attempt = "n"
    fox_attempt = "n"
    bear_attempt = "n"
    moose_attempt = "n"
    
    #Sick members are able to rest and become healthy when hunting
    sick_members = [False, False, False, False, False]
    
    rabbit = random.randrange(1,3)   #50% chance of finding a rabbit
    fox = random.randrange(1,5)    #25% chance of finding a fox
    deer = random.randrange(1,6)    #20% chance of finding a deer
    bear = random.randrange(1,11)   #10% chance of finding a bear
    moose = random.randrange(1,21)   #5% chance of finding a moose
    
    if rabbit == 1:
        rabbit_found = True
    else:
        rabbit_found = False
    if fox == 1:
        fox_found = True
    else:
        fox_found = False
    if deer == 1:
        deer_found = True
    else:
        deer_found = False
    if bear == 1:
        bear_found = True
    else:
        bear_found = False
    if moose == 1:
        moose_found = True
    else:
        moose_found = False
    
    if rabbit_found:
        rabbit_attempt = input("It appears there is a rabbit nearby, would you like to try to hunt it? (Y/N)")
    if fox_found:
        fox_attempt = input("A fox is on the horizon, would you like to try to hunt it? (Y/N)")
    if deer_found:
        deer_attempt = input("A nice juicy deer is within shooting range, would you like to try to hunt it? (Y/N)")
    if bear_found:
        bear_attempt = input("Watch out, there is massive bear closeby, would you like to try to hunt it? (Y/N)")
    if moose_found:
        moose_attempt = input("Woah, there is a moose in your vicinity, would you like to try to hunt it? (Y/N)")
    
    if bullets < 10:
        print("Oh no! You do not have enough bullets to attempt a hunt.")
        hunting_array = [food, bullets, days_per_turn, sick_members]
        return hunting_array
    
    elif bullets >= 10:
        #puzzle section
        puzzle_guess = input("In order to be achieve success in the hunt, you must enter a number between 1-10:")
        puzzle_answer = puzzle()
        if puzzle_guess == puzzle_answer:
            print("Congratulations, your hunt was successful!")
            #need to print about what they hunted and how much... and adjust food accordingly
            if rabbit_attempt == '1' or rabbit_attempt == 'Y' or rabbit_attempt == 'y' or rabbit_attempt == 'yes':
                print("You gained 2 lbs. of food hunting the rabbits!")
                food += 2
                bullets = bullets - 10
            if fox_attempt == '1' or fox_attempt == 'Y' or fox_attempt == 'y' or fox_attempt == 'yes':
                print("You gained 5 lbs. of with the successful fox hunt!")
                food += 5
                bullets = bullets - 8
            if deer_attempt == '1' or deer_attempt == 'Y' or deer_attempt == 'y' or deer_attempt == 'yes':
                deer_lbs = random.randrange(35, 61)
                bullets = bullets - 5
                print("You gained",deer_lbs,"lbs. of food hunting for deer!")
                food += deer_lbs
            if bear_attempt == '1' or bear_attempt == 'Y' or bear_attempt == 'y' or bear_attempt == 'yes':
                bear_lbs = random.randrange(100,301)
                bullets = bullets - 10
                print("You gained", bear_lbs, "lbs. of food hunting for the bear!")
                food += bear_lbs
            if moose_attempt == '1' or moose_attempt == 'Y' or moose_attempt == 'y' or moose_attempt == 'yes':
                moose_lbs = random.randrange(300,701)
                bullets = bullets - 10
                print("You gained", moose_lbs, "lbs. of food with the successful moose hunt!")
                food += moose_lbs
        else:
            print("Unfortunately, your hunt was unsuccessful.")
            
    #player decides how much to eat
    eating_decision = input("How well would you like to eat today: Poorly, Moderately, or Well?")
    if eating_decision == 'Poorly' or eating_decision == 'poorly':
        food = food - (2*sum(family_remaining))
        food_consumed = 2*sum(family_remaining)
        print("By choosing to eat", eating_decision, "you consumed", food_consumed, "lbs of food.")  
    elif eating_decision == 'Moderately' or eating_decision == 'moderately':
        food = food - (3*sum(family_remaining))
        food_consumed = 3*sum(family_remaining)
        print("By choosing to eat", eating_decision, "you consumed", food_consumed, "lbs of food.")  
    elif eating_decision == 'Well' or eating_decision == 'well':
        food = food - (5*sum(family_remaining))
        food_consumed = 5*sum(family_remaining)
        print("By choosing to eat", eating_decision, "you consumed", food_consumed, "lbs of food.")  
    
    if food > 1000:
        food_total = food
        left_behind = food_total - 1000
        food = 1000
        print("\nYou had", food_total, "lbs of food, but your oxen are getting tired as the journey progresses and can only hold 1000 lbs.")
        print("Unfortunately, you must leave behind", left_behind, "lbs of food behind.")
    
    hunting_array = [food, bullets, days_per_turn, sick_members]
    return hunting_array
 
def continue_on_trail(store_list, family_remaining, miles_traveled, sick_members, turn):
    '''Option for the player at the beginning of the game to continue instead
    of resting'''
    days_per_turn = 14
    #position in milestone_distances to determine the next stop
    #inputted values
    i = turn
    money = store_list[0]
    oxen = store_list[1]
    bullets = store_list[2]
    food = store_list[3]
    medkit = store_list[4]
    wagon_parts = store_list[5]
    
    #print('food before eating', food)    ####
    food_eaten = 3*sum(family_remaining)*days_per_turn
    food = food - food_eaten
    #print('food after eating', food)     ####
    
    milestone_distances = [102,185,304,554,640,830,932,989,1151,1295,1395,1534,1648,1808,1863]
    miles_from_turn = random.randrange(70,141)
    milestone_measure = miles_traveled + miles_from_turn
    
    while miles_traveled < milestone_measure:
        miles_traveled = miles_traveled + 1
        if miles_traveled == milestone_distances[i]:
            milestone_stop_array = milestone_stop(miles_traveled, money, oxen, bullets, food, medkit, wagon_parts, sick_members, days_per_turn, turn)
            sick_members = milestone_stop_array[0] 
            days_per_turn = milestone_stop_array[1] 
            store_list = milestone_stop_array[2]
            money = store_list[0]
            oxen = store_list[1]
            bullets = store_list[2]
            food = store_list[3]
            medkit = store_list[4]
            wagon_parts = store_list[5] 
            #print("food in while loop", food)
            i = i + 1
    
    turn = i
    #update everything after milestone stops are checked
    continue_array = [money, oxen, bullets, food, medkit, wagon_parts, days_per_turn, miles_from_turn, miles_traveled, turn]
    print("As you continued on the trail, you traveled", miles_from_turn, " miles and ate", food_eaten, "lbs of food.")
    return continue_array


def rest_stop(food, sick_members, family_remaining):
    '''This function generates the number of days that the player
    rests when choosing to do so'''
    rest_days = random.randrange(1, 4)
    food_eaten = (3*sum(family_remaining)*rest_days)
    food = food - food_eaten
    sick_members = [False, False, False, False, False]
    rest_array = [food, sick_members, rest_days]
    #print('rest stop food', food)
    print("\nBy choosing to rest, you spent", rest_days, "day(s) off the trail, in which any sick family members were able to strengthen and heal.")
    print("You consumed", food_eaten, "lbs of food, and have", food, "lbs remaining.")
    return rest_array

#status_update(current_month, current_day, start_year, miles_to_go, miles_traveled, store_list)
def sickness(sick_members, family_remaining, name_tuple):
    '''This function tracks sickness and is only called inside of
    each turn()'''
    #names of family members
    leader = name_tuple[0]
    comp1 = name_tuple[1]
    comp2 = name_tuple[2]
    comp3 = name_tuple[3]
    comp4 = name_tuple[4]
    
    #choose someone to get sick randomly   
    sick_decider = random.randrange(1,6)
    diseases = ['dysentary', 'constipation', 'mad cow disease', 'typhoid fever', 'cholera', 'measels', 'small pox', 'flu', 'mumps', 'gray scale']
    disease_type = random.choice(diseases)
    if sick_decider == 1:
        if sick_members[0] == True:
            print("Your leader has died of sickness. You lose")
            family_remaining[0] = 0
        else:
            print("Oh no!", leader, "has come down with", disease_type, "and is very sick.")
    elif sick_decider == 2:
        if sick_members[1] == True:
            print(comp1, "has died from sickness, you may continue on the trail however.")
            family_remaining[1] = 0
        else:
            print(comp1, "has come down with", disease_type, "and is very sick.")
    elif sick_decider == 3:
        if sick_members[2] == True:
            print(comp2, "has died from sickness, you may continue on the trail however.")
            family_remaining[2] = 0
        else:
            print("Oh no!,", comp2, "has come down with", disease_type, "and is very sick.")   
    elif sick_decider == 4:
        if sick_members[3] == True:
            print(comp3, "has died from sickness, you may continue on the trail however.")
            family_remaining[3] = 0
        else:    
            print("Oh no!,", comp3, "has come down with", disease_type, "and is very sick.")
    elif sick_decider == 5:
        if sick_members[4] == True:
            print(comp4, "has died from sickness, you may continue on the trail however.")
            family_remaining[4] = 0
        else:
            print("Oh no!,", comp4, "has come down with", disease_type, "and is very sick.")
        
    sickness_function_array = [sick_members, family_remaining]
    return sickness_function_array


def bad_weather(food, days_per_turn, sick_members, family_remaining):
    '''Function to handle the weather random occurances inside of
    the misfortunes funciton'''
    weather_array = ['heavy rain', 'hail', 'storm', 'blizzard', 'hurricane']
    weather = random.choice(weather_array)
    sick_members = [False, False, False, False, False]
    if weather == 'heavy rain' or weather == 'hail':
        days_per_turn += 1
        print("Your group has been caught in some", weather, "and must stay put for a day.")
        food = food - (3*sum(family_remaining))
    elif weather == 'storm' or weather == 'blizzard':
        days_per_turn += 3
        print("Your traveling group did not listen to the weather gods and were led straight into a", weather,"therefore causing your group to stay put for 3 days until it passes.")
        food = food - (3*3*sum(family_remaining))
    elif weather == 'hurricane':
        days_per_turn += 5
        print("Hold your horses, a nasty midwestern hurricane is on the horizon. You better take cover for 5 days to be safe.")
        food = food - (3*5*sum(family_remaining))
    weather_array = [days_per_turn, food, sick_members]
    return weather_array

def misfortunes(name_tuple, oxen, food, wagon_parts, money, sick_members, family_remaining, miles_traveled, miles_to_go, days_per_turn):
    '''This function handles the probability of a misfortune occuring during
    the game and creates the result of that misfortune'''
    print("\nOh no, it appears you have encountered a misfortune on your adventure.")
    misfortune_type = random.randrange(1,7)
    #print('misfortune food', food)   ##########
    #Sickness is chosen
    if misfortune_type == 1:
        print("Someone in your group is not feeling well.")
        sickness_function_array = sickness(sick_members, family_remaining, name_tuple)
        sick_members = sickness_function_array[0]
        family_remaining = sickness_function_array[1]
    #Oxen dies
    elif misfortune_type == 2:
        oxen = oxen - 1
        print("One of your oxen has been injured and must be left behind. You still have", oxen, "remaining.")
    #A thief attacks at night
    elif misfortune_type == 3:
        thief_attack = random.randrange(10,26)
        food = food - thief_attack
        print("It appears a thief snuck into your wagon last night and stole", thief_attack, "lbs of food. You have", food, "lbs of food remaining.")    
    #A piece of the wagon breaks
    elif misfortune_type == 4:
        food = food - 3*sum(family_remaining)
        if wagon_parts == 0:
            print("Well, your wagon is broken, and you cannot repair it. You lose.")
            food = 0
        else:
            wagon_parts = wagon_parts - 1
            sick_members = [False, False, False, False, False]
            broken_part_array = ['wheels', 'axels', 'tongues']
            broken_part = random.choice(broken_part_array)
            print("Ah shucks, one of your wagon's", broken_part, "has broken. You will need to stop for a day to fix it.")     
    #Bad weather
    elif misfortune_type == 5:
        weather_array = bad_weather(food, days_per_turn, sick_members, family_remaining)
        days_per_turn = weather_array[0]
        food = weather_array[1]
        sick_members = weather_array[2]  
    #Happy event
    elif misfortune_type == 6:
        happy_array = happy_event(food, money, wagon_parts, sick_members, miles_traveled, miles_to_go)
        food = happy_array[0]
        money = happy_array[1]
        wagon_parts = happy_array[2]
        sick_members = happy_array[3]
        miles_traveled = happy_array[4]
        miles_to_go = happy_array[5]
    
    misfortunes_array = [food, oxen, wagon_parts, money, sick_members, family_remaining, miles_traveled, miles_to_go, days_per_turn]
    return misfortunes_array


def happy_event(food, money, wagon_parts, sick_members, miles_traveled, miles_to_go):
    '''Spreading the love through random acts of fortune'''
    happy_event = random.randrange(1,6)
    if happy_event == '1':
        print("It looks like you have stumbled upon a long lost ark of some sort. Inside is $1000 worth of gold, take it and run.")
        money = money + 1000
    elif happy_event == '2':
        miles_saved = random.randrange(20,49)
        print("Your friendliness towards the Natives nearby has rewarded you with a shortcut. It looks like it will save you", miles_saved, "from your original path.")
        miles_traveled += miles_saved
        miles_to_go = miles_to_go - miles_saved
    elif happy_event == '3':
        print("Woah, there appears to be an abandoned wagon nearby.")
        print("After further inspection, there were 400 lbs of canned food along with 6 salvageable wagon parts!")
        food = food + 400
        wagon_parts += 6
    elif happy_event == '4':
        print("Somehow, you just managed to find a hitchhiking doctor traveling on the trail.")
        print("Luckily, you offered the doctor a ride and he managed to heal everyone in your group from any ailments they possessed.")
        sick_members = [False, False, False, False, False]
    else:
        print("Well, after successfully fermenting some old wheat into beer, you were able to sell it for quite a profit.")
        print("Your family was able to gain $200 off of the travel brew you worked up.")
        money += 200
        
    happy_array = [food, money, wagon_parts, sick_members, miles_traveled, miles_to_go]
    return happy_array

#    
#just need to figure out where to put milestones in main()   
#    
    
def next_milestone(miles_traveled):
    '''Figures out the next milestone on the trek'''
    milestone_name = ""
    river_depth = 0
    landmark = False
    river_crossing = False
    fort = False
    
    if miles_traveled == 102:
        milestone_name = "Kansas River Crossing"
        river_depth = 4
        river_crossing = True
        landmark = False
        fort = False
    elif miles_traveled == 185:
        milestone_name = "Big Blue River Crossing"
        river_depth = 3
        river_crossing = True
        landmark = False
        fort = False
    elif miles_traveled == 304:
        milestone_name = "Fort Kearney"
        river_depth = 2
        river_crossing = False
        landmark = False
        fort = True
    elif miles_traveled == 554:
        milestone_name = "Chimney Rock"
        river_crossing = False
        landmark = True
        fort = False
    elif miles_traveled == 640:
        milestone_name = "Fort Laramie"
        river_depth = 3
        river_crossing = False
        landmark = False
        fort = True
    elif miles_traveled == 830:
        milestone_name = "Independence Rock"
        river_depth = 0
        river_crossing = False
        landmark = True
        fort = False
    elif miles_traveled == 932:
        milestone_name = "South Pass"
        river_depth = 0
        river_crossing = False
        landmark = True
        fort = False
    elif miles_traveled == 989:
        milestone_name = "Fort Bridger"
        river_depth = 4
        river_crossing = False
        landmark = False
        fort = True
    elif miles_traveled == 1151:
        milestone_name  = "Green River Crossing"
        river_depth = 5 
        river_crossing = True
        landmark = False
        fort = False
    elif miles_traveled == 1295:
        milestone_name = "Soda Springs"
        river_depth = 0
        river_crossing = False
        landmark = True
        fort = False
    elif miles_traveled == 1395:
        milestone_name = "Fort Hall"
        river_depth = 5
        river_crossing = False
        landmark = False
        fort = True
    elif miles_traveled == 1534:
        milestone_name = "Snake River Crossing"
        river_depth = 5   
        river_crossing = True
        landmark = False
        fort = False
    elif miles_traveled == 1648:
        milestone_name = "Fort Boise"
        river_depth = 6
        river_crossing = False
        landmark = False
        fort = True
    elif miles_traveled == 1808:
        milestone_name = "Blue Mountains"
        river_depth = 0
        river_crossing = False
        landmark = True
        fort = False
    elif miles_traveled == 1863:
        milestone_name = "Fort Walla Walla"
        river_depth = 7
        river_crossing = False
        landmark = False
        fort = True
    '''elif miles_traveled == 2040:
        milestone_name = "Oregon City"
        river_depth = 0
        river_crossing = False
        landmark = False
        fort = False'''
      
    milestone_array = [milestone_name, river_depth, landmark, river_crossing, fort]
    return milestone_array

def milestone_stop(miles_traveled, money, oxen, bullets, food, medkit, wagon_parts, sick_members, days_per_turn, turn):
    '''This function handles the stop options for the player depending
    on what type of milestone is present'''
    #take in info from next_milestone() functions
    milestone_array = next_milestone(miles_traveled)
    milestone_name = milestone_array[0]
    river_depth = milestone_array[1]
    landmark = milestone_array[2]
    river_crossing = milestone_array[3]
    fort = milestone_array[4]
    
    #Events at the river crossing
    while river_crossing == True:
        print("\nYou have arrived at", milestone_name,". The river is", river_depth, "feet deep.")
        print("You may choose one of the following options:")
        print("1. Stop and rest for a day.")
        print("2. Cross the river to continue the journey")
        stop_decision = input("Which of the above options would you like to choose?\n")
        while (stop_decision == 'rest for a day' or stop_decision == 'rest' or stop_decision == '1') and stop_decision != '2':
            print("You have chosen to stop and rest for a day.")
            days_per_turn +=1
            sick_members = [False, False, False, False, False]
            print("After resting would you may choose to:")
            print("1. Rest for another day.")
            print("2. Cross the river to continue the journey")
            stop_decision = input("Which of the above options would you like to choose?\n")
        if stop_decision == 'continue' or stop_decision == '2':
            print("You have chosen to continue and cross the river.")
            if river_depth <= 3:
                print("Because it only three feet deep, you can cross easily with your wagon.")
                stop_decision == 'done'
                river_crossing = False
            elif river_depth > 3:
                print("Because the river is deeper than three feet, you must pay $5 to cross via ferry.")
                money = money - 5
                stop_decision == 'done'
                river_crossing = False
        elif stop_decision != '1' and stop_decision != '2':
            while stop_decision != '1' and stop_decision != '2':
                stop_decision = input('Please try again. Would you like to 1.) Rest, or 2.) Continue?')
            
    #landmark events   
    while landmark == True:
        print("You have arrived at the", milestone_name, "landmark.")
        stop_decision = input("Would you like to rest for a turn?(Y/N)")
        while stop_decision != 'y' and stop_decision != 'Y' and stop_decision != 'yes' and stop_decision != 'No' and stop_decision != 'N' and stop_decision != 'n':
            print("You did not enter a correct option, try again.")
            stop_decision = input("Would you like to rest for a turn?(Y/N)")
        while stop_decision == "y" or stop_decision == 'Y' or stop_decision == '1' or stop_decision == 'yes':
            print("You have chosen to rest for a turn.")
            days_per_turn +=1
            sick_members = [False, False, False, False, False]
            stop_decision = input("Would you like to (1) rest again or (2) continue on the trail?")
        if stop_decision == 'n' or stop_decision == 'N' or stop_decision == '2' or stop_decision == 'no':
            print("You decided to continue on your journey.")
            landmark = False
    #fort events
    while fort == True:
        print("You have arrived at", milestone_name, "You may choose one of the following stop options:")
        print("1. Stop and rest for a turn.")
        print("2. Visit the store")
        print("3. Continue on the trail.")
        stop_decision = input("Which above option would you like to choose?")
        while stop_decision == 'rest for a day' or stop_decision == 'rest' or stop_decision == '1':
            print("You have chosen to stop and rest for a day.")
            days_per_turn +=1
            sick_members = [False, False, False, False, False]
            print("After resting would you may choose to:")
            print("1. Stop and rest for another turn.")
            print("2. Visit the store")
            print("3. Continue on the trail.")
            stop_decision = input("Which above option would you like to choose?")
        if stop_decision == 'Visit the store' or stop_decision == 'visit the store' or stop_decision == 'store' or stop_decision == '2':
            visits = river_depth
            travel_store_array = travel_store(visits, money, oxen, bullets, food, medkit, wagon_parts)
            money = travel_store_array[0]
            oxen= travel_store_array[1]
            bullets= travel_store_array[2]
            food= travel_store_array[3]
            medkit= travel_store_array[4]
            wagon_parts= travel_store_array[5]
            store_list = [money, oxen, bullets, food, medkit, wagon_parts]
            fort = False
            if money < 0:
                money = 0
        elif stop_decision == 'continue' or stop_decision == 'Continue' or stop_decision == '3' or stop_decision == 'continue on the trail.':
            print("You have chosen to continue on the trail.")
            fort = False
    '''if miles_traveled >= 2040: #river_crossing == False and landmark == False and fort == False:
        print("You have arrived at Oregon City!")'''
    
    store_list = [money, oxen, bullets, food, medkit, wagon_parts]  
    milestone_stop_array = [sick_members, days_per_turn, store_list, turn]
    return milestone_stop_array


def each_turn(date_array, miles_traveled, miles_to_go, next_landmark, store_list, sick_members, family_remaining, name_tuple, turn, quit_decision):
    '''Calls on the functions for each turn which extends over 
    a two week period'''
    days_per_turn = 0
    current_day = date_array[1]
    current_month = date_array[0]
    
    #Give a status update showing the day, miles traveled, supplies remaining, and next landmark
    status_update(current_month, current_day, miles_to_go, miles_traveled, store_list)
    
    #Menu for choosing what to do during the turn
    print("This is the beginning of your turn.")
    print("You may:")
    print("1. Stop to rest.")
    print("2. Continue of the trail.")
    print("3. Hunt.")
    print("4. Quit the game.")
    turn_decision = input("Which of the above options do you choose?")
    
    money = store_list[0]
    oxen = store_list[1]
    bullets = store_list[2]
    food = store_list[3]
    medkit = store_list[4]
    wagon_parts = store_list[5]
    
    #stop to rest
    if turn_decision == '1':
        rest_array = rest_stop(food, sick_members, family_remaining)
        food = rest_array[0]
        sick_members = rest_array[1]
        days_per_turn = rest_array[2]
     
    #This is where the stores will happen and milestone stops... it was hell to create
    elif turn_decision == '2':
        continue_array = continue_on_trail(store_list, family_remaining, miles_traveled, sick_members, turn)
        money = continue_array[0]
        oxen = continue_array[1]
        bullets = continue_array[2]
        food = continue_array[3]
        medkit = continue_array[4]
        wagon_parts = continue_array[5]
        #store_list = continue_array[0]
        days_per_turn = continue_array[6]
        #miles_from_turn = continue_array[2]
        miles_traveled = continue_array[8]
        miles_to_go = 2040 - miles_traveled
        turn = continue_array[9]
        #print('food passed through continue', food)

        
    #hunting function is called
    elif turn_decision == '3':
        hunting_array = lets_go_hunting(food, bullets, sick_members, family_remaining)            
        food = hunting_array[0]
        bullets = hunting_array[1]
        days_per_turn = hunting_array[2]
        sick_members = hunting_array[3]
    #quit... setting leader to 0 (dead) will end the game in the main() while loop 
    elif turn_decision == '4':
        quit_decision = 1
    
    else:
        print('\nSince you could not make a coherent decision, your family stepped up and chose to continue on the trail.\n')
        continue_array = continue_on_trail(store_list, family_remaining, miles_traveled, sick_members, turn)
        money = continue_array[0]
        oxen = continue_array[1]
        bullets = continue_array[2]
        food = continue_array[3]
        medkit = continue_array[4]
        wagon_parts = continue_array[5]
        #store_list = continue_array[0]
        days_per_turn = continue_array[6]
        #miles_from_turn = continue_array[2]
        miles_traveled = continue_array[8]
        miles_to_go = 2040 - miles_traveled
        turn = continue_array[9]
        
    #Misfortunes
    #print('before misfortune chance', food)
    misfortune_chance = random.randrange(1,11)  
    if misfortune_chance == 1 or misfortune_chance == 2 or misfortune_chance == 3:
        #print('before misfortune called', food)
        misfortunes_array = misfortunes(name_tuple, oxen, food, wagon_parts, money, sick_members, family_remaining, miles_traveled, miles_to_go, days_per_turn)
        food = misfortunes_array[0]
        oxen = misfortunes_array[1]
        wagon_parts = misfortunes_array[2]
        money = misfortunes_array[3]
        sick_members = misfortunes_array[4]
        family_remaining = misfortunes_array[5]
        miles_traveled = misfortunes_array[6]
        miles_to_go = misfortunes_array[7]
        days_per_turn = misfortunes_array[8]
    #update current date
    date_array = update_current_day(current_month, current_day, days_per_turn)
    current_month = date_array[0]                                                           
    current_day = date_array[1] 
    
    #raider attack function
    #THE ALL KNOWING PROBABILITY
    attack_probability = round((((miles_traveled/100)**2)+72)/(((miles_traveled/100)**2)+12)-1)
    attack_generator = 0  #random.randrange(1,101)
    if attack_generator == attack_probability:
        raider_array = tusken_raiders(money, wagon_parts, bullets, oxen, food, miles_traveled)
        money = raider_array[0]
        wagon_parts = raider_array[1]
        bullets = raider_array[2]
        oxen = raider_array[3]
        food = raider_array[4]
        
    #print('turn array food', food)
    turn_array = [current_day, current_month, money, food, bullets, oxen, wagon_parts, sick_members, family_remaining, miles_traveled, miles_to_go, medkit, turn, quit_decision]
    return turn_array





def main():
    """This is where the functions are called so the game can be played"""
    
    #variables assigned before the game starts
    miles_to_go = 2040
    money = 2000
    #location = "Independence, Missouri"
    food = 0
    oxen = 0
    bullets = 0
    wagon_parts = 0
    medkit = 0
    miles_traveled = 0
    family_remaining = [1, 1, 1, 1, 1]
    sick_members = [False, False, False, False, False]
    quit_decision = 0
    #sickness_tracker = [0, 0, 0, 0, 0]
    
    #starts the game by taking in the names of the leader and companions
    name_tuple = begin()
    
    #Next, the following lines record the starting date chosen by the leader
    startDate_tuple = start_date()
    start_month = startDate_tuple[0]
    start_day = startDate_tuple[1]
    start_year = startDate_tuple[2]
    
    #First trip to the store
    store_list = beginning_store(money, oxen, food, bullets, medkit, wagon_parts)
    money = store_list[0]
    oxen = store_list[1]
    bullets = store_list[2]
    food = store_list[3]
    medkit = store_list[4]
    wagon_parts = store_list[5] 
    
    #Begin keeping track of days
    current_month = start_month
    current_day = start_day
    current_year = start_year
    date_array = [current_month, current_day, current_year]
    turn = 0
    #While loop to run each turn after the initial supplies are set
    #This makes sure the player does not run out of food, oxen, and that
    #the leader does not die
    while food > 0 and oxen > 0 and family_remaining[0] != 0 and quit_decision != 1 and miles_traveled < 2040: 
        #each turn
        turn_array = each_turn(date_array, miles_traveled, miles_to_go, next_landmark, store_list, sick_members, family_remaining, name_tuple, turn, quit_decision)
        current_day = turn_array[0] 
        current_month = turn_array[1] 
        money = turn_array[2] 
        food = turn_array[3] 
        bullets = turn_array[4] 
        oxen = turn_array[5] 
        wagon_parts = turn_array[6] 
        sick_members = turn_array[7] 
        family_remaining = turn_array[8]  
        miles_traveled = turn_array[9] 
        miles_to_go = turn_array[10] 
        medkit = turn_array[11]
        turn = turn_array[12]
        quit_decision = turn_array[13]
        store_list = [money, oxen, bullets, food, medkit, wagon_parts]
     
    if food <= 0:
        print("Your party ran out of food and starved to death.")
        return
    elif oxen <= 0:
        print("All of you oxen have been lost, and your party will be unable to finish the trip to Oregon City.")
        return
    elif family_remaining[0] == 0:
        print("The leader in your group has died. There is nobody to guide the companions. You lose.")
        return
    elif quit_decision == 1:
        print("You simply gave up. Try again later.")
        #wn.exitonclick()
    elif miles_traveled >= 2040:
        print("Congratulations! You have successfully made it to Oregon City!")
        
#if '___name___' == '___main___':
main()
    
    
    
    