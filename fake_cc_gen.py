from faker import Faker
from pymongo import MongoClient
import random
import datetime
import time

# Set up Faker instance for Philippines
fake = Faker('en_PH')

# Connect to MongoDB
client = MongoClient('mongodb+srv://jatinkumarpradhan354:jatinkumarpradhan@cluster0.nkn3qfn.mongodb.net/?retryWrites=true&w=majority')
db = client['CreditDaddy']
collection = db['credit_cards']

# Ask user for number of credit card details to generate
num_cards = int(input('How many credit card details do you want to generate? '))

# Define function for generating fake credit card details
def generate_card():
    return {
        'name': fake.name(),
        'card_number': fake.credit_card_number(card_type=None),
        'expiration_date': fake.credit_card_expire(start='now', end='+10y', date_format='%m/%y'),
        'cvv': random.randint(100, 999),
        'address': fake.address()
    }

# Generate fake credit card details and insert them in batches
start_time = time.time()
num_inserted = 0
batch_size = 10000
cards = []
for i in range(num_cards):
    cards.append(generate_card())
    if len(cards) == batch_size:
        result = collection.insert_many(cards, ordered=False)
        num_inserted += len(result.inserted_ids)
        cards = []
if len(cards) > 0:
    result = collection.insert_many(cards, ordered=False)
    num_inserted += len(result.inserted_ids)

end_time = time.time()
elapsed_time = end_time - start_time

# Print summary
print(f'Successfully generated {num_inserted} credit card details in {elapsed_time:.2f} seconds.')
