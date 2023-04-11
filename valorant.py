from pymongo import MongoClient
from faker import Faker
import random
import time

# Connect to MongoDB
client = MongoClient("mongodb+srv://jatinkumarpradhan354:jatinkumarpradhan@cluster0.nkn3qfn.mongodb.net/?retryWrites=true&w=majority")
db = client["valorant"]
collection = db["players"]

# Faker instance for generating fake data
faker = Faker()

# List of agent names in Valorant
agents = [
    "Astra", "Breach", "Brimstone", "Cypher", "Jett", "Killjoy", "Omen",
    "Phoenix", "Raze", "Reyna", "Sage", "Skye", "Sova", "Viper", "Yoru",
    "KAY/O", "Astra", "Viper", "Skye", "Brimstone", "Breach", 
    "Sova", "Cypher", "Killjoy", "Phoenix", "Jett", "Omen", 
    "Sage", "Fade", "Gekko", "Harbor"
]

# Ranks in Valorant with their different stages
ranks = {
    "Unranked": ["", "", ""],
    "Iron": ["1", "2", "3"],
    "Bronze": ["1", "2", "3"],
    "Silver": ["1", "2", "3"],
    "Gold": ["1", "2", "3"],
    "Platinum": ["1", "2", "3"],
    "Diamond": ["1", "2", "3"],
    "Ascendant": ["1", "2", "3"],
    "Immortal": ["1", "2", "3"],
    "Radiant": ["", "", ""]
}

# Get number of players to generate from user input
num_players = int(input("How many players do you want to generate? "))
batch_size = int(input("What is the batch size? "))
country = input("Enter the name of the country to generate player names: ")

# Generate fake player data and save it to MongoDB in batches
start_time = time.time()
for i in range(0, num_players, batch_size):
    batch_data = []
    for j in range(batch_size):
        if i+j >= num_players:
            break
        rank = random.choice(list(ranks.keys()))
        rank_stage = random.choice(ranks[rank])
        data = {
            "name": faker.name().split()[0] + " " + faker.last_name(),
            "age": random.randint(18, 30),
            "rank": f"{rank} {rank_stage}" if rank_stage else rank,
            "agent": random.choice(agents),
            "hours_played": random.randint(50, 500),
            "headshot_percentage": round(random.uniform(0.2, 0.8), 2),
            "win_rate": round(random.uniform(0.4, 0.7), 2),
            "kda_ratio": round(random.uniform(0.5, 1.5), 2),
            "avg_damage": random.randint(100, 500),
            "accuracy": round(random.uniform(0.2, 0.8), 2),
            "clutch_rounds": random.randint(0, 10),
            "team": faker.word(),
            "country": country
        }
        batch_data.append(data)
    collection.insert_many(batch_data)
end_time = time.time()

print(f"Successfully generated and saved {num_players} players to MongoDB in {end_time - start_time} seconds.")