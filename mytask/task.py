from flask import Flask,render_template,request,redirect

import json

app=Flask(__name__)
sub=[]
pos=[]
prod=[]
list=[]

@app.route("/home")
def show():
    return "Hi iam dheepika"


@app.route("/one",methods=["POST","GET"])
def dheep():
    print(request.form.get("subscribers"))
    print(request.form.get("post"))
    print(request.form.get("products"))
    subscribers=request.form.get("subscribers")
    post=request.form.get("post")
    products=request.form.get("products")
    sub.append(subscribers)
    pos.append(post)
    prod.append(products)
    dic={"subscribers":subscribers,"post":post,"products":products}
    list.append(dic)
    return render_template("index.html",data=list) 




if __name__=="__main__":
    app.run(debug=True)


