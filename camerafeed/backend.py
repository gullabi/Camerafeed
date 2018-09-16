from pymongo import MongoClient

class FeedDB(object):
    def __init__(self,project_name):
        self.db_name = 'camerafeed'
        self.collection_name = project_name

    def connect(self):
        client = MongoClient("localhost", 27017)
        db = client[self.db_name]
        self.backend = db[self.collection_name]

    def insert(self, element):
        # element should be a dictionary with elements meta and time
        if not element.get('meta') or not element.get('time'):
            raise ValueError('feed element does not have the expected fields')
        self.backend.insert(element)

    def get(self, start, end):
        pass
