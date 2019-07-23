import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://ray:qwe123@cluster0-xwcsn.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
collection = db.students

condition = {'id': '20170101'}
student = collection.find_one(condition)

student['name'] = 'Alice'

result = collection.update_one(condition, {'$set': student})

print(result)

# student = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }

# result = collection.insert_one(student)

# print(result)
