#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sqlite3 as lite
import sys

db = None 
# a. Connect to the database in pets.db
try:
    db = lite.connect('pets.db') 
    db.row_factory = lite.Row 
    
# b. Ask the user for a person’s ID number
    while True:
        ID_choice = input('Please enter an ID #: ')
        
# e. Keep doing this until the user enters in a 1,
# which is an indication to exit the program
        if ID_choice == '-1':
            sys.exit() 
        
        else:
            try:
                ID_choice = int(ID_choice)
                
# d. Otherwise print an error message
            except:
                print ("Invalid ID please enter another: ")
                continue

            cur = db.cursor()
            cur.execute("SELECT * FROM person WHERE id =?", [(ID_choice)]) 
            row = cur.fetchone() 

# c. If that user exists:
# i. Print out data on the person (e.g. James Smith, 41 years old)
# ii. Print out all the data on that person’s pets (e.g., James Smith owned Rusty, a
# dalmatian, that was 4 years old)    

        if row == None:
            print ("Invalid ID please enter another: ")
            continue

        print (row['first_name'] + ' ' + row['last_name'] + ' is ' + str(
            row['age']) + ' yrs old.')


        for row in db.execute(
            "SELECT * FROM person_pet WHERE person_id =?", [(ID_choice)]):

            for name in db.execute(
                "SELECT * FROM person WHERE id =?", [(ID_choice)]):
                pet_owner = name['first_name'] + ' ' + name['last_name']


            for row_pet in db.execute(
                "SELECT * FROM pet WHERE id =?", [(row['pet_id'])]):

                if row_pet['dead'] == 0:
                    print (pet_owner + ' owned ' + row_pet[
                    'name'] + ', a ' + row_pet['breed'] + ' who was ' + str(
                        row_pet['age']) + ' years old.')
            else:
                if row_pet['dead'] != 0:
                    print (pet_owner + ' owns ' + row_pet[
                        'name'] + ', a ' + row_pet['breed'] + ' who is ' + str(
                            row_pet['age']) + ' years old.')

except lite.Error as e:
    print ("Closing.")
    print ("Error: %s " % e.args[0])
    sys.exit(1)

finally:
    if db:
        db.close()