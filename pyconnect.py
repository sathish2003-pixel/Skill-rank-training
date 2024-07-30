from pymongo import MongoClient
import json
#creating a method for insert a data in mongo db
def insert_data():
    # Mongo DB connection
    con_str = "mongodb+srv://sathish:pass1234@cluster0.mpiauov.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    try:
        # Try block is used to connect to give the conection with the mongodb
        client = MongoClient(con_str)
        # Create a database name
        db = client['Db1']
        #Name of the colllection
        collection = db['user']   
        # Here we are mentioninga file path 
        file_path="E:/Skill rank/sample.json"
        #opening the file in  a read mode and load the json in a data_set variable
        with open(file_path, "r") as file:
            data_set = json.load(file)
        #This is the size of the data 
        data_size=10000000
        #In the for loop it starts from 0 and ends with length data set that we given
        for i in range(0,len(data_set),data_size):
        #here doing a slicing operation the slice starts at index i and ends at i + batch_size
            size=data_set[i:i+data_size]
        #The insert operation is done here by using a insert.many

            # result = collection.insert_many(size)
            # print(f"Inserted {len(result.inserted_ids)} Data")
        filter = {
    "language": "isiZulu",
    "version": {"$gte": 8}
}

# Fetch the data
        results = collection.find(filter)

# Print the results
        for document in results:
            print(document)
        

        
    finally:
        # Close the connection of mongodb
        client.close()

#Giving a data_set values in a json format

#calling the method
insert_data()