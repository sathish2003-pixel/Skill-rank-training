from flask import Flask, jsonify,render_template
from pymongo import MongoClient
from bson.objectid import ObjectId
app = Flask(__name__)

# MongoDB connection setup
connection="mongodb+srv://sathish:pass1234@cluster0.mpiauov.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection) 
db = client["Db1"]  
collection = db["user"]  

#defining the url path

@app.route('/api/json/<id>', methods=['GET'])

def data_id(id):
        # Convert id to ObjectId
        object_id = ObjectId(id)

    # Fetch the one data we use a find one based on the id we pass in the url
        result = collection.find_one({"_id": object_id})
  
        if result:
  # Typecasting the  ObjectId to string
            result["_id"] = str(result["_id"])  
            return jsonify(result)
        else:
            return jsonify({ "Document not found"})

if __name__ == '__main__':
    app.run(debug=True)
