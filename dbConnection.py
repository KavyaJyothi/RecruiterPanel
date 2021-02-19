from pymongo import MongoClient
uri = "mongodb://root:Dzt9FZk3Ndh2hqshEJsWx2CS0VRg4AJZtimis8hHLlr9HWi8hQVffFU2IojChNOR@localhost:27020/workex?authSource=admin"
client =MongoClient(uri)
print(client.get_database().name)
db=client.workex
print(db)
mycol=db.user_profile
print(mycol)

new_col=db.user_profile.update({"mobile_no":"9538596331", "roles":"EMPLOYER"},{"$set":{"mobile_no":"8147898955"}})
      #
      # #print "customers" after the update:
      # for item in new_col:
      #   print(item)