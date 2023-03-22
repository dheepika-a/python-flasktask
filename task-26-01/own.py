from flask import Flask,render_template,request,url_for
import sqlite3 as sql
app=Flask(__name__)

@app.route("/")
def show():
    con=sql.connect("owndb.db")
    con.row_factory=sql.Row
    res=con.cursor()
    res.execute("select * from qual")
    data=res.fetchall()
    con.commit()
    return render_template("show.html",data=data)

@app.route("/insert",methods=["post","get"])
def insert():
    if request.form.get("id")!=None:
        id=request.form.get("id")
        name=request.form.get("name")
        degree=request.form.get("degree")
        con=sql.connect("owndb.db")
        con.row_factory=sql.Row
        res=con.cursor()
        res.execute("insert into qual(ID,NAME,DEGREE)values(?,?,?)",(int(id),name,degree))
        con.commit()
    return render_template("insert.html")

@app.route("/update/<id>",methods=["post","get"])
def update(id):
    if request.form.get("id")!=None:
        id=request.form.get("id")
        name=request.form.get("name")
        degree=request.form.get("degree")
        con=sql.connect("owndb.db")
        con.row_factory=sql.Row
        res=con.cursor()
        res.execute("update qual set name=?,degree=? where id=?",(name,degree,int(id)))
        con.commit()
        return render_template("show.html")
    con=sql.connect("owndb.db")
    con.row_factory=sql.Row
    res=con.cursor()
    res.execute("select * from qual where ID=?",(int(id),))
    data=res.fetchone()
    con.commit()
    return render_template("update.html",data=data)
   
@app.route("/delete/<id>",methods=["post","get"])
def delete(id):
    con=sql.connect("owndb.db")
    res=con.cursor()
    res.execute("delete from qual where id=?",(int(id),))
    con.commit()
    return "deleted sucessfully"













if __name__=="__main__":
    app.run(debug=True)



