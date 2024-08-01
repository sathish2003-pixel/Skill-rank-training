from pymongo import MongoClient,errors
import json
#creating a method for insert a data in mongo db
def lambda_handler(event,context):
    # Mongo DB connection
    con_str = "mongodb+srv://sathish:pass1234@cluster0.mpiauov.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    try:
        # Try block is used to connect to give the conection with the mongodb
        client = MongoClient(con_str,serverSelectionTimeoutMS=5000)
        # Create a database name
        db = client['Db1']
        #Name of the colllection
        collection = db['user']   
        results = collection.find()

# Print the results
        for document in results:
            document['_id'] = str(document['_id'])
        return {
            'statusCode': 200,
            'body': json.dumps(document)
        }
    finally:
        # Close the connection of mongodb
        client.close()


