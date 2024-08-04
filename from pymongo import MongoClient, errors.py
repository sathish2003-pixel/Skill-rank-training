from pymongo import MongoClient, errors
import json
from bson.objectid import ObjectId

def lambda_handler(event, context):
    # MongoDB connection string
    con_str = "mongodb+srv://sathish:pass1234@cluster0.mpiauov.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    try:
        # Connect to MongoDB
        client = MongoClient(con_str, serverSelectionTimeoutMS=5000)
        
        # Specify the database and collection
        db = client['Db1']
        collection = db['user']
        
        # Extract 'id' from the query parameters of the DELETE request
        id_value = event.get('queryStringParameters').get('id')
        
        # Check if 'id' is provided
        if not id_value:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'id parameter is required'})
            }
        
        # Attempt to convert 'id' to ObjectId
        try:
            object_id = ObjectId(id_value)
        except (errors.InvalidId, TypeError) as e:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Invalid ID format'})
            }
        
        # Delete the document by ObjectId
        result = collection.delete_one({'_id': object_id})
        
        # Check if a document was deleted
        if result.deleted_count == 1:
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Document deleted successfully'})
            }
        else:
            # If no document was found to delete, return 404
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Document not found'})
            }
    except Exception as e:
        # Return 500 status code if any other error occurs
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'An error occurred', 'error': str(e)})
        }
    finally:
        # Ensure the MongoDB connection is closed
        client.close()
