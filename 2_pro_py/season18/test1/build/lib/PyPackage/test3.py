from PyPackage import MongoClient 

client=MongoClient(host='localhost',port=27017)
print(client)

dbtest=client['dbtest']
print(dbtest)

person=dbtest['person']
print(person)


person.insert_many([{'name':'Niko','age':23},{'name':'nikol'}])

print('dbs :')
for db in client.list_database_names():
    print(db)
print('collections: ')
for collections in dbtest.list_collection_names():
    print(collections)