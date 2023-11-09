from xml.dom.xmlbuilder import DocumentLS
import pymongo
from tomlkit import document
import pprint

client = pymongo.MongoClient("localhost", 27017)

db = client['my_db']

##creating collection

collection_name = db['Northeastern_Database']

# Check if the collection exists
if collection_name in db.list_collection_names():
    # Drop the collection if it exists
    db[collection_name].drop()

documents = [ {'Students':[ {
    'id': 1,
    'name': 'Jane Doe',
    'email': 'janedoe@northeastern.edu',
    'year': 'Sophomore',
    'major': 'Enviromantal Studies'
}, {
    'id': 2,
    'name': 'Alan Myers',
    'email': 'a.myers@northeastern.edu',
    'year': 'Senior',
    'major': 'Computer Science'
}]}, {
    'Employees':[ {
        'id': 101,
        'name': 'John Adams',
        'email': 'j.adams@northeastern.edu',
        'job_title': 'Academic Adviser'
    }, {
        'id': 102,
        'name': 'Sam Adams',
        'email': 's.adams@northeastern.edu',
        'job_title': 'Teaching Assistant'
    }]}
]

insert_result = collection_name.insert_many(documents)

print(f'Inserted {len(insert_result.inserted_ids)} documents')

#updating name

filter = {'Employees.name': 'John Adams'}

cursor = collection_name.find(filter)

update = {  '$set': {
    'Employees.$.name': "Johny Adams Jr."
}}

result = collection_name.update_one(filter, update)

if result.modified_count > 0:
    print("Update successful")
else:
    print('No document matched the filter')



#adding a name to the collection

new_student = {
    'id': 3,
    'name': 'William More',
    'email': 'w,more@northeastern.edu',
    'year': 'Freshman',
    'major': 'Biology'
}

filter = {}

update = {'$push': {'Students': new_student}}

result2 = collection_name.update_one(filter, update)

if result2.modified_count > 0:
    print("Update successful")
else:
    print('No document matched the filter')

#printing out collection
pp = pprint.PrettyPrinter(indent=4)

cursor = collection_name.find({})

for document in cursor:
   pp.pprint(document)