from pymongo import MongoClient
import csv

client=MongoClient("mongodb://127.0.0.1:27017")

header=["name","age","course"]

with open("detail.csv") as csv_file:
      csvreader=csv.reader(csv_file,delimiter=",")
      # for each in csvreader:
      #   print(each[0])




# database=client.user
# collection=database.add
# collection.insert_one({
#   "name":"dheepika",
#   "age":20,
#   "course":"python"
# })
# print("inserted")
# client.close()
