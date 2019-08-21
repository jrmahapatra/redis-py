import redis
import json

class RedisDB:
    def __init__(self,redisKey,redisHost="localhost",redsPort=6379,redisDb=0):
        self.redisKey = redisKey

        # We need to create the index such a way so that we can search it easily
        # So we have to do something eg: return all the customer details by customer id
        # redisIndex['customerId'] = customer Details
        self.conn = redis.StrictRedis(host=redisHost, port=redsPort, db=0)
    
    def all(self):
        return self.conn.hgetall(self.redisKey)

    def remove(self, keyIndex):
        self.conn.hdel(self.redisKey, keyIndex)

    """
    Delete all the keys of the currently selected DB. This command never fails.
    The time-complexity for this operation is O(N), N being the number of keys in the database
    """
    def flush(self):
        self.conn.flushdb()
        return True

    def insert(self, keyIndex,jsonData):
        if self.conn.hexists(self.redisKey, keyIndex):
            self.remove(keyIndex)
        self.conn.hset(self.redisKey,keyIndex, json.dumps(jsonData))
        return self

    def keys(self):
        return self.conn.hkeys(self.redisKey)

    def search(self, keyIndex, search=""):
        data = json.loads(self.conn.hget(self.redisKey, keyIndex))
        if search!="":
                return data[search]
        else:
            return data


obj = RedisDB("customer") #customer4 = table name
# obj.flush()
#lets insert some records, 
obj.insert(120, {
    "name": "Test Customer1",
    "address": "123 Main Steet",
    "city": "Chandler",
    "state": "AZ",
    "sasa":"sasass"
  })
obj.insert(121, {
    "name": "Test Customer1",
    "address": "123 Main Steet",
    "city": "Chandler",
    "state": "AZ",
    "sasa":"sasass"
  })
obj.insert(122, {
    "name": "Test Customer1",
    "address": "123 Main Steet",
    "city": "Chandler",
    "state": "AZ",
    "sasa":"sasass"
  })
# search by index
result = obj.search("120")
print(result)

# search by index and a key
result = obj.search("120","name")
print(result)