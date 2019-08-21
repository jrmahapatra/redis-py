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


obj = RedisDB("customer4") # create redis index as main db 


# lets insert some records, 
customerData = {
    "name": "Mr. ben",
    "address": "123 Main Steet",
    "city": "Chandler",
    "state": "AZ"
  }
obj.insert(123, customerData)
result = obj.search("123")
print(result)

customerData = {
    "name": "Jaakki",
    "address": "123 Main Steet",
    "city": "Chandler",
    "state": "AZ",
    "sasa":"sasass"
  }
obj.insert(123, customerData)
result = obj.search("123")
print(result)

#result = obj.search("123","name")
#print(result)