from flask import Flask, jsonify,render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection setup
connection="mongodb+srv://sathish:pass1234@cluster0.mpiauov.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection) 
db = client["Db1"]  
collection = db["user"]  

@app.route('/json', methods=['GET'])
def get_data():
    # Select the data from the Mongodb
    results = collection.find()
    # Convert the results to a list of dictionaries
    data_set = []
    for document in results:
        document["_id"] = str(document["_id"])
        data_set.append(document)

    #Return the data_set objects we use a jsonify
    return jsonify(data_set)

if __name__ == '__main__':
    app.run(debug=True)
