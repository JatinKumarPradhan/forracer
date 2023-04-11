from pymongo import MongoClient
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Connect to the MongoDB database
client = MongoClient("mongodb+srv://jatinkumarpradhan354:jatinkumarpradhan@cluster0.nkn3qfn.mongodb.net/?retryWrites=true&w=majority")
db = client["BigDataDB"]
collection = db["identities"]

# Get the data from the collection and convert it to a Pandas dataframe
data = pd.DataFrame(list(collection.find()))

# Select the features to be used in the model
features = ["name","phone", "address", "credit_card"]

# Convert the selected features to numerical values
for feature in features:
    data[feature] = pd.factorize(data[feature])[0]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data[features], data["name"], test_size=0.2, random_state=42)

# Train the logistic regression model
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
