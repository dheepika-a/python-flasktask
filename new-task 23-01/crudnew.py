from flask import Flask,request,render_template,redirect,url_for
import sqlite3 as sql

app=Flask(__name__)

@app.route("/insert",methods=["post","get"])
def new():
    if request.form.get("id")!=None:
        id=request.form.get("id")
        name=request.form.get("name")
        course=request.form.get("course")
        con=sql.connect("user.db")
        res=con.cursor()
        res.execute("insert into new(ID,NAME,COURSE)values(?,?,?)",(int(id),name,course))
        con.commit()
    return render_template("index.html")


@app.route("/update/<id>",methods=["post","get"])
def up(id):
    if request.form.get("id")!=None:
        id=request.form.get("id")
        name=request.form.get("name")
        course=request.form.get("course")
        con=sql.connect("user.db") 
        res=con.cursor()
        res.execute("update new set name=?, course=? where id=?",(name,course,int(id)))  
        con.commit()
        return render_template("index.html")
    con=sql.connect("user.db")
    con.row_factory=sql.Row
    res=con.cursor()
    res.execute("select * from new where ID=?",(int(id),))
    a=res.fetchone()
    return render_template("update.html",data=a)

@app.route("/delete/<id>",methods=["post","get"])
def dot(id):
    con=sql.connect("user.db")
    con.row_factory=sql.Row
    res=con.cursor()
    res.execute("delete from new where id=?",(int(id),))
    con.commit()
    return "<h1>Removed Successfully</h1>"     


if __name__=="__main__":
    app.run(debug=True)