from pymongo import MongoClient
import re

# connect to the MongoDB database
client = MongoClient('mongodb+srv://jatinkumarpradhan354:jatinkumarpradhan@cluster0.nkn3qfn.mongodb.net/?retryWrites=true&w=majority')
db = client['CreditDaddy']

# define the regular expression pattern to validate credit card numbers
cc_pattern = re.compile(r'^\d{16}$')

# define the collection to fetch credit card details from
cc_collection = db['credit_cards']

# define the collection to store valid credit cards in
valid_cc_collection = db['valid_cards']

# fetch all the credit cards from the cc_collection
all_cc = cc_collection.find()

# loop through all the credit cards and validate them
for cc in all_cc:
    cc_number = cc['card_number']
    # validate the credit card number using the regular expression pattern
    if cc_pattern.match(cc_number):
        # if the credit card number is valid, store it in the valid_cc_collection
        valid_cc_collection.insert_one(cc)
