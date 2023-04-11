from faker import Faker
from pymongo import MongoClient
import time

# Ask the user for the number of data values required
num_data = int(input("Enter the number of data values required: "))

# Connect to the MongoDB database
client = MongoClient("mongodb+srv://jatinkumarpradhan354:jatinkumarpradhan@cluster0.nkn3qfn.mongodb.net/?retryWrites=true&w=majority")
db = client["BigDataDB"]
collection = db["identities"]

# Generate fake identities and store them in the collection using batch inserts
fake = Faker("en_IN") # Set the Faker locale to India
batch_size = 10000
num_batches = num_data // batch_size
remaining = num_data % batch_size
start_time = time.time()

# Generate and insert the main batches of data
for i in range(num_batches):
    batch = []
    for j in range(batch_size):
        name = fake.name()
        phone = fake.numerify(text="9#########") if fake.boolean(chance_of_getting_true=50) else fake.numerify(text="98########")
        address = fake.address()
        credit_card = fake.credit_card_full()
        identity = {"name": name, "phone": phone, "address": address, "credit_card": credit_card}
        batch.append(identity)
    collection.insert_many(batch)
    print(f"{len(batch)} fake identities added to the collection.")

# Generate and insert the remaining data
if remaining > 0:
    batch = []
    for i in range(remaining):
        name = fake.name()
        phone = fake.numerify(text="9#########") if fake.boolean(chance_of_getting_true=50) else fake.numerify(text="98########")
        address = fake.address()
        credit_card = fake.credit_card_full()
        identity = {"name": name, "phone": phone, "address": address, "credit_card": credit_card}
        batch.append(identity)
    collection.insert_many(batch)
    print(f"{len(batch)} fake identities added to the collection.")

# Print the time taken to generate and store the fake identities
end_time = time.time()
time_taken = end_time - start_time
print(f"{num_data} fake identities added to the collection in {time_taken:.2f} seconds.")
