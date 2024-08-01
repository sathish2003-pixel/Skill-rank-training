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
        
      
        # Extract 'id' and other fields from the body of the POST request
        body = event.get('body')
        
        if body is None:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Request body is required'})
            }
        
       
        
        id_value = body.get('id')
        
        # Check if 'id' is provided
        if not id_value:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'id parameter is required'})
            }
        
        # Remove the id here because we don't need to update id
        update_fields = body.copy()
        del update_fields['id']
        
        # Attempt to convert 'id' to ObjectId
        try:
            object_id = ObjectId(id_value)
        except (errors.InvalidId, TypeError) as e:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Invalid ID format'})
            }
        
        # Update the document by ObjectId
        result = collection.update_one({'_id': object_id}, {'$set': update_fields})
        
        # Check if a document was updated
        if result.matched_count == 1:
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Document updated successfully'})
            }
        else:
            # If no document was found to update, return 404
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
