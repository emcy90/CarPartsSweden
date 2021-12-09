from pymongo import MongoClient

# client = MongoClient(f"mongodb://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
client = MongoClient(f"mongodb://root:s3cr37@localhost:27017")
db = client.CarPartsSweden


def find_all_customers():
    result = db.customers.find()
    for item in result:
        print(item)


def main():
    result = db.customers.find({'country': 'sweden'})
    for item in result:
        print(item)

    # find_all_customers()


if __name__ == '__main__':
    main()
