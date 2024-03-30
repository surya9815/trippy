from pymongo import MongoClient

if __name__ == "__main__":
    cluster = "mongodb://localhost:27017/"
    client = MongoClient(cluster)
    print(client)
    db = client['test2']    #create database
    collection = db["todo2"]   #create table
    
    # data = {'name':'Suryansh','marks':34}
    # collection.insert_one(data)    #insert data

    insertthese = [
        {"name":"Singh","Location":'banglore',"Marks":45},
        {"name":"King","Location":'delhi',"Marks":22},
        {"name":"del","Location":'mumbai',"Marks":77},
        {"name":"kyi","Location":'hp',"Marks":95}
                   ]
    collection.insert_many(insertthese)
