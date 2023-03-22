from flask import Flask,render_template,request,url_for
from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")

app=Flask(__name__)

@app.route("/", methods=["POST","GET"])
def show():
    client=MongoClient("mongodb://localhost:27017")
    database=client.college
    collect=database.student
    temp=collect.find({})
    print(temp)
    a=[]
    for i in temp:
        a.append(i)
    return render_template("index.html",data=a)

@app.route("/insert", methods=["POST","GET"])
def ins():
    client=MongoClient("mongodb://localhost:27017")
    if request.form.get("id")!=None:
       id=request.form.get("id")
       name=request.form.get("name")
       degree=request.form.get("degree")
       database=client.college
       collect=database.student
       collect.insert_one({
          "id":id,
          "name":name,
          "degree":degree })
       client.close()
    return render_template("insert.html")



@app.route("/update/<id>", methods=["POST","GET"])
def update(id):
        client=MongoClient("mongodb://localhost:27017")
        if request.form.get("id")!=None:
            id=request.form.get("id")
            name=request.form.get("name")
            degree=request.form.get("degree")
        database=client.college
        collect=database.student
        x=collect.find_one({"id":int(id)})
        print(x.get("name"))
        temp={"id":x.get("id"),"name":x.get("name"),"degree":x.get("degree")}
        new={"$set":{"id":id,"name":name,"degree":degree}}
        collect.update_one(temp,new)
        client.close()
    
        return render_template("update.html",data=x)

if __name__=="__main__":
    app.run(debug=True)

    




