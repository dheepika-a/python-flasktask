from flask import Flask,render_template,request
from pymongo import MongoClient

app=Flask(__name__)

client=MongoClient("mongodb://127.0.0.1:27017")

@app.route("/", methods=["POST","GET"])
def add():
    name=request.json
    print(name)
    database=client.data
    collection=database.api
    for i in name:
        collection.insert_one({
        "name":i.get("name"),
        "age":i.get("age"),
        "course":i.get("course")
        })
    print("inserted")
    client.close()
    return name


@app.route("/call", methods=["POST","GET"])
def bulk():
    client=MongoClient("mongodb://127.0.0.1:27017")
    name=request.json
    print(name)
    database=client.data
    collection=database.api
    collection.insert_many(name)
    print("inserted")
    client.close()
    return "inserted"

@app.route("/read/<age>", methods=["POST","GET"])
def new(age):
    client=MongoClient("mongodb://127.0.0.1:27017")
    database=client.data
    collection=database.api
    result=collection.find({"age":int(age)})
    print(result)
    a=[]
    for i in result:
        a.append(i)
    client.close()
    return render_template("table.html",data=a) 

if __name__=="__main__":
    app.run(debug=True)