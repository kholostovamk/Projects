from xml.dom.xmlbuilder import DocumentLS
import pymongo
from tomlkit import document

client = pymongo.MongoClient("localhost", 27017)

db = client['my_db']

##creating collection

collection = db['Northeastern_Database']

# Check if the collection exists
if collection in db.list_collection_names():
    # Drop the collection if it exists
    db[collection].drop()

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

insert_result = collection.insert_many(documents)

print(f'Inserted {len(insert_result.inserted_ids)} documents')

#updating name

filter = {'Employees.name': 'John Adams'}

cursor = collection.find(filter)

update = [ { '$set': {
    'Employees.$.name': "Johny Adams Jr."
}}]

result = collection.update_one(filter, update)

if result.modified_count > 0:
    print("Update succeeful")
else:
    print('No document matched the filter')

