from flask import Flask,render_template,request
import requests
from pymongo import MongoClient

app=Flask(__name__)

client=MongoClient("mongodb://localhost:27017")

@app.route("/", methods=["POST","GET"])
def call():
    dat=[145488,146679,147951,147719]
    tab=[]
     
    for i in dat:
        url="https://api.mfapi.in/mf/"+str(i)
        resp=requests.get(url)

        temp=resp.json().get("meta").get("fund_house")
        nav=resp.json().get("data")[0].get("nav")
        dic={"fund":temp,"nav":nav}
        tab.append(dic)
    client=MongoClient("mongodb://127.0.0.1:27017")
    database=client.user
    collection=database.add
    collection.insert_many(tab)
    deep={"fund":"Aditya Birla Sun Life Mutual Fund"}
    newdeep={"fund":"Dheepika Is Good Girl"}
    print("inserted")
    client.close()
    return render_template("index.html",data=tab)

@app.route("/update", methods=["POST","GET"])
def up():
    client=MongoClient("mongodb://127.0.0.1:27017")
    database=client.user
    collection=database.add
    deep={"fund":"Aditya Birla Sun Life Mutual Fund"}
    newdeep={"$set":{"fund":"Dheepika Is Good Girl"}}
    collection.update_one(deep,newdeep)
    print("inserted")
    client.close()
    return"updated"

@app.route("/delete", methods=["POST","GET"])
def dot():
    client=MongoClient("mongodb://127.0.0.1:27017")
    database=client.user
    collection=database.add
    newdeep={"fund":"Dheepika Is Good Girl"}
    collection.delete_one(newdeep)
    client.close()
    return"deleted"





if __name__=="__main__":
    app.run(debug=True)