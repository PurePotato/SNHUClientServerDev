from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = user
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31443
        DB = 'AAC'
        COL = 'animals'
        #HOST = host
        #PORT = port
        #DB = db
        #COL = coll
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        try:
            if data is not None:
                self.collection.insert_one(data)  # data should be dictionary 
                return True           
            else:
                return False
                raise Exception("Nothing to save, because data parameter is empty")
        except Exception as e:
            print(f"Error during insert: {e}")
            return False
        
# Create method to implement the R in CRUD.
    def read(self, query):
        try:    
            cursor = self.collection.find(query)
            return list(cursor)
        except Exception as e:
            print(f"Error during query: {e}")
            
     
# Update method to implement the U in CRUD.   
    def update(self, query, update_data):
        try:
            result = self.collection.update_many(query, {"$set": update_data})
            return result.modified_count
        except Exception as e:
            print(f"Error during update: {e}")
            return 0
# Delete method to implement the D in CRUD
    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Error during delete: {e}")
            return 0 
        
