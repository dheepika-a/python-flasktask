from flask import Flask,render_template,request,redirect
import sqlite3 as sql
app=Flask(__name__)

@app.route("/", methods=["POST","GET"])
def dataone():
            if request.form.get("image")!=None:
                new=request.form.get("image")
                dot=request.form.get("video")
                conn=sql.connect("youtubeurl.db")
                cur=conn.cursor()
                cur.execute("insert into urldata(VIDEOS,IMAGES) values(?,?)",(new,dot,))
                conn.commit()
            return render_template("add.html")

@app.route("/dheep", methods=["POST","GET"])
def dheep():
                
                conn=sql.connect("youtubeurl.db")
                #conn.row_factory=sql.Row
                cur=conn.cursor()
                cur.execute("select * from urldata")
                # data1=cur.fetchall()
                row=cur.fetchall()
                print(row)
                a=[]
                b=[]
                for i in row:
                 a.append(i[0])
                 b.append(i[1])
                return render_template("index.html",data=a,data1=b)

                # conn.commit()
                # return render_template("add.html",data=data1)




# @app.route('/view',methods=['POST','GET'])
# def select():
#     conn=sql.connect('url.db')
#     cur=conn.cursor()
#     cur.execute("Select * from connect")
#     row=cur.fetchall()
#     print(row)
#     a=[]
#     b=[]
#     for i in row:
#         a.append(i[0])
#         b.append(i[1])
#     return render_template("index.html",data=a,data1=b)

if __name__ == "__main__":
    app.run(debug=True)