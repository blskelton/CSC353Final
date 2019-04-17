from datetime import datetime
import csv
from pymongo import MongoClient
from pymongo import errors


FIELDS = ['Name', 'Scientific Name', 'Smells Like ', 'Description', 'History', "Botany", 'Chemistry', 'Horticulture', 'Fun Facts', 'Tags', 'Uses', 'Dangers', 'References']

"""
Make connection with MongoClient

Returns:
    client - MongoClient instance
"""
def make_connection():
    client = MongoClient()
    client = MongoClient('localhost', 27017)
    return client



"""
Create database called tennis and populate it with data

Parameters:
    client - MongoClient instance
Returns:
    populated tennis database
"""
def create_database(client):
    db = client.plants
    return populate_database(db)


"""
Create three collections for tennis database: tournament_names, players, and matches.

The tournament_names collection contains each unique tournament name and its surface type. The players collection contains each unique player and his hand, height, country, and most recent rank. The matches collection contains a winner ID, loser ID, the score of the match, the tournament's ID, year, and date.

Parameters:
    db - MongoDB database
Returns:
    List of the three collections: [tournament_names, players, matches]
"""
def populate_database(db):

    plants = db.plants

    # Drop collection if it exists
    if plants.count() > 0:
        plants.drop()

    # Create unique index for the plant key in the plant collection using it's scientific name
    plants.create_index({'Name', 'Scientific Name'}, unique=True)


    filename = "Scentopedia.csv"
    # Read through file
    with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=FIELDS)
            reader.next() # consume the first line, which is just column headers
            i = 0
            for row in reader:
                print(i)
                if not bool(row['Name']):
                    # BLANK ROW
                    continue

                # Parse row
                plant_name = row['Name']
                scientific_name = row['Scientific Name']
                """
                WHAT IS GOING ON HERE
                try:
                    smells_like = row['Smells Like']
                except ValueError:
                    # No data entered
                    print("in except")
                    smells_like = None
                """    
                try:
                    description = row['Description']
                except ValueError:
                    # No data entered
                    description = None
                try:
                    history = row['History']
                except ValueError:
                    # No data entered
                    history = None
                try:
                    botany = row['Botany']
                except ValueError:
                    # No data entered
                    botany = None  
                
                try:
                    chemistry = row['Chemistry']
                except ValueError:
                    # No data entered
                    chemistry = None
                    
                try:
                    horticulture = row['Horticulture']
                except ValueError:
                    horticulture = None
                """   
                # Insert document into tournament_names collection and store tournament's ID
                tournament_id = tournament_names.insert_one(tournament_names_post).inserted_id
                except errors.DuplicateKeyError:
                    # Tournament already inserted into tournament_names collection
                    # Find its ID
                    tournament_id = tournament_names.find_one({"tourney_name": tourney_name})["_id"]
                
                try:
                    # players document
                    player_post = {
                        "player_name": winner_name,
                        "player_hand": winner_hand,
                        "player_height": winner_height,
                        "player_country": winner_country,
                        "player_rank": winner_rank
                    }
                    # Insert document into players collection and store player's ID
                    winner_id = players.insert_one(player_post).inserted_id

                except errors.DuplicateKeyError:
                    # Player already inserted into players collection
                    # Find his ID
                    winner_id = players.find_one({"player_name": winner_name})["_id"]

                try:
                    # players document
                    player_post = {
                        "player_name": loser_name,
                        "player_hand": loser_hand,
                        "player_height": loser_height,
                        "player_country": loser_country,
                        "player_rank": loser_rank
                    }
                    # Insert document into players collection and store player's ID
                    loser_id = players.insert_one(player_post).inserted_id

                except errors.DuplicateKeyError:
                    # Player already inserted into players collection
                    # Find his ID
                    loser_id = players.find_one({"player_name": loser_name})["_id"]
                """ 
                # plants document
                plant_post = {
                    "plant_name": plant_name,
                    "scientific_name": scientific_name,
                    "description": description,
                    "history": history,
                    "botany": botany,
                    "chemistry": chemistry,
                    "horticulture": horticulture
                }
                # Insert document into matches collection
                plants.insert_one(plant_post)
                i = i + 1
    print("Complete")

    return [plants]


def print_collections(collections):
    for db in collections:
        print db
        for document in db.find({}):
            print document
        print


"""
Make connection with MongoClient
Create database and populate it with data
Print each collection and its contents
"""
def main():
    client = make_connection()
    collections = create_database(client)
    print_collections(collections)


main()


