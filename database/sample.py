from flask import Flask,render_template,request,redirect
import json
import requests
import sqlite3 as sql

app=Flask(__name__)

# dic=[{"add":"dheep","title":"good"},{"add":"sam","title":"good"}]
# @app.route("/<ind>")
# def dheep(ind):
#     add=request.json.get("add")
#     title=request.json.get("title")
#     dot={"add":add,"title":title}
#     dic[int(ind)]["add"]=add
#     dic[int(ind)]["title"]=title
#     #dic.append(dot)
#     return dic

# list=[124479,100027,100028,100029]
# @app.route("/dheep")
# def sam():
#     dot=requests.get("https://api.mfapi.in/mf/"+str(list[0]))
#     return render_template("vk.html",data=dot.json().get("data")[0].get("nav"))

# list=[124479,100027,100028,100029]
# @app.route("/dheep",methods=["post","get"])
# def sam():
#     fun=None
#     if(request.form.get("number"))!=None:
#         one=request.form.get("number")
#         dot=requests.get("https://api.mfapi.in/mf/"+str(one))
#         fund=dot.json().get("meta").get("fund_house")
#         nav=dot.json().get("data")[0].get("nav")
#         fun={"num":one,"fund":fund,"nav":nav}
#     return render_template("vk.html", data= fun)

# @app.route("/dheep",methods=["post","get"])
# def sam():
#     fun=None
#     if(request.form.get("number"))!=None:
#         one=request.form.get("number")
#         dot=requests.get("https://api.mfapi.in/mf/"+str(one))
#         fund=dot.json().get("meta").get("fund_house")
#         nav=dot.json().get("data")[0].get("nav")
#         conn=sql.connect("navdat.db")
#         res=conn.cursor()
#         res.execute("update post set fundname=?, nav=? where number=?",(fund,nav,one))
#         conn.commit()
#     return render_template("vk.html")

@app.route("/",methods=["post","get"])
def alone():
    fun=None
    if(request.form.get("number"))!=None:
        one=request.form.get("number")
        dot=requests.get("https://api.mfapi.in/mf/"+str(one))
        fund=dot.json().get("meta").get("fund_house")
        nav=dot.json().get("data")[0].get("nav")
        conn=sql.connect("navdat.db")
        cur=conn.cursor()
        cur.execute("insert into post(NUMBER,FUNDNAME,NAV)values(?,?,?)",(one,fund,nav,))
        conn.commit()
    return render_template("vk.html")




if __name__ == "__main__":
    app.run(debug=True)