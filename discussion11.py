import unittest
import sqlite3
import json
import os
# starter code

# Create Database
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn


# Creates list of species ID's and numbers
def create_species_table(cur, conn):

    species = ["Rabbit",
    "Dog",
    "Cat",
    "Boa Constrictor",
    "Chinchilla",
    "Hamster",
    "Cobra",
    "Parrot",
    "Shark",
    "Goldfish",
    "Gerbil",
    "Llama",
    "Hare"
    ]

    cur.execute("DROP TABLE IF EXISTS Species")
    cur.execute("CREATE TABLE Species (id INTEGER PRIMARY KEY, title TEXT)")
    for i in range(len(species)):
        cur.execute("INSERT INTO Species (id,title) VALUES (?,?)",(i,species[i]))
    conn.commit()

# TASK 1
# CREATE TABLE FOR PATIENTS IN DATABASE
def create_patients_table(cur, conn):
    cur.execute('drop table if exists Patients')
    cur.execute('create table Patients (pet_id INTEGER PRIMARY KEY, name TEXT, species_id NUMBER, age INTEGER, cuteness INTEGER, aggressiveness NUMBER)')
    conn.commit()



# ADD FLUFFLE TO THE TABLE
def add_fluffle(cur, conn):
    cur.execute('insert into Patients (pet_id, name, species_id, age, cuteness, aggressiveness) values(?, ?, ?, ?, ?, ?)', (0, 'Fluffle', 0, 3, 90, 100))
    conn.commit()
    

# TASK 2
# CODE TO ADD JSON TO THE TABLE
# ASSUME TABLE ALREADY EXISTS
def add_pets_from_json(filename, cur, conn):
    
    # WE GAVE YOU THIS TO READ IN DATA
    f = open(filename)
    file_data = f.read()
    f.close()
    json_data = json.loads(file_data)

    pet_id = 0
    for i in json_data:
        pet_id += 1
        name = i['name']
        if i['species'] == 'Rabbit':
            species_id = 0
        if i['species'] == 'Dog':
            species_id = 1
        if i['species'] == 'Cat':
            species_id = 2
        if i['species'] == 'Boa Constrictor':
            species_id = 3
        if i['species'] == 'Chinchilla':
            species_id = 4
        if i['species'] == 'Hamster':
            species_id = 5
        if i['species'] == 'Cobra':
            species_id = 6
        if i['species'] == 'Parrot':
            species_id = 7
        if i['species'] == 'Shark':
            species_id = 8
        if i['species'] == 'Goldfish':
            species_id = 9
        if i['species'] == 'Gerbil':
            species_id = 10
        if i['species'] == 'Llama':
            species_id = 11
        if i['species'] == 'Hare':
            species_id = 12

        age = int(i['age'])
        cuteness = int(i['cuteness'])
        aggressiveness = int(i['aggressiveness'])

        cur.execute('insert into Patients (pet_id, name, species_id, age, cuteness, aggressiveness) values(?, ?, ?, ?, ?, ?)', (pet_id, name, species_id, age, cuteness, aggressiveness))
        conn.commit()


# TASK 3
# CODE TO OUTPUT NON-AGGRESSIVE PETS
def non_aggressive_pets(aggressiveness, cur, conn):
    pass



def main():
    # SETUP DATABASE AND TABLE
    cur, conn = setUpDatabase('animal_hospital.db')
    create_species_table(cur, conn)

    create_patients_table(cur, conn)
    add_fluffle(cur, conn)
    add_pets_from_json('pets.json', cur, conn)
    ls = (non_aggressive_pets(10, cur, conn))
    print(ls)
    
    
if __name__ == "__main__":
    main()

