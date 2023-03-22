from flask import Flask,render_template,request
from pymongo import MongoClient

app=Flask(__name__)

client=MongoClient("mongodb://localhost:27017")

@app.route("/", methods=["POST","GET"])
def add():
    datas=request.json
    print(datas)
    database=client.user
    collection=database.add
    for i in datas:
        collection.insert_one({
            "name":i.get("name"),
            "course":i.get("course")

        })
    print("inserted")
    client.close()
    return datas

@app.route("/all", methods=["POST","GET"])
def sub(): 
    datas=request.json
    database=client.user
    collection=database.add
    collection.insert_many(datas)
    print("inserted")
    client.close()
    return"inserted"

@app.route("/dop/<age>", methods=["POST","GET"])
def wen(age): 
    database=client.data
    collection=database.api
    res=collection.find({"age":int(age)})
    print(res)
    a=[]
    for i in res:
        a.append(i)
    client.close()
    return render_template("index.html",data=a)

if __name__=="__main__":
    app.run(debug=True)