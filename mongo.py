import pymongo

client = pymongo.MongoClient('localhost')
db = client['localhost']
collection = db['user']

condition = {'account': 'xiaoxiaohong1'}

user = collection.find_one()

print(user)

result = collection.update_one(condition, {'$set': dict({
    'name': 'test',
    'url': '',
    'account': 'xiaoxiaohong',
    'location': 'x',
    'following': 344
})}, True)

# print(result)

# student = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }

# result = collection.insert_one(student)

# print(result)
