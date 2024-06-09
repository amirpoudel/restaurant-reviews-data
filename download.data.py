import os
import json
from dotenv import load_dotenv
import pymongo

# Load environment variables from .env file
load_dotenv()

# Print the MongoDB URL to verify it's loaded correctly
print(os.getenv("MONGODB_URL"))

# Connect to MongoDB
myclient = pymongo.MongoClient(os.getenv("MONGODB_URL"))
mydb = myclient["rms-production"]
mycol = mydb["feedbacks"]

# Retrieve data from the collection
data_list = list(mycol.find())

# Convert MongoDB documents to JSON-serializable format
for data in data_list:
    data["_id"] = str(data["_id"])  # Convert ObjectId to string

# Save data to a JSON file with UTF-8 encoding
with open('feedbacks.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_list, json_file, indent=4, ensure_ascii=False)

print(f'Data saved to feedbacks.json')
