from flask import Flask,render_template,request,redirect
import requests
import sqlite3 as sql
app=Flask(__name__)

# @app.route("/dheep")
# def dheep():
#     conn=sql.connect("bb.db")
#     conn.row_factory=sql.Row
#     cur=conn.cursor()
#     cur.execute("select * from post")
#     data=cur.fetchall()
#     return render_template("index.html",data=data)




@app.route("/add", methods=["POST","GET"])
def datadheep():
            dic=None
            if request.form.get("number")!=None:
                dot=request.form.get("number")
                res=requests.get("https://api.mfapi.in/mf/"+str(dot))
                fund=res.json().get("meta").get("fund_house")
                nav = res.json().get("data")[0].get("nav")
                dic ={"id":dot,"fund":fund,"nav":nav}
                conn=sql.connect("datacode.db")
                cur=conn.cursor()
                cur.execute("insert into datafund (ID,FUND,NAV) values(?,?,?)",(dot,fund,nav))
                conn.commit()
            return render_template("vk.html")

@app.route("/dheep", methods=["POST","GET"])
def dheep():
        
                conn=sql.connect("datacode.db")
                conn.row_factory=sql.Row
                cur=conn.cursor()
                cur.execute("select * from datafund")
                data1=cur.fetchall()
                conn.commit()
                return render_template("index.html",data=data1)



# @app.route("/")
# def dheep():
#     conn=sql.connect("data.db")
#     conn.row_factory=sql.Row
#     cur=conn.cursor()
#     cur.execute("select * from tab")
#     data=cur.fetchall()
#     return render_template("index.html",data=data)


# @app.route("/sam",methods=["POST","GET"])
# def fun1():
#     a=request.form.get("id")
#     conn=sql.connect("data.db")
#     conn.row_factory=sql.Row
#     cur=conn.cursor()
#     cur.execute("select * from tab where id=?",(a,))
#     data=cur.fetchone()
#     return render_template("one.html",data=data)



if __name__ == "__main__":
    app.run(debug=True)