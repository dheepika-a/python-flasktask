from flask import Flask,render_template,redirect,request

app=Flask(__name__)

post=[{"title":"This is the title 2","content":"this is the content 2","published":True,"id":2,"created_at":"2022-12-15T08:41:44.888493+05:30"},{"title":"This is the title 4","content":"this is the content 4","published":True,"id":4,"created_at":"2022-12-15T08:42:21.689495+05:30"},{"title":"This is the title 5","content":"this is the content 5","published":True,"id":5,"created_at":"2022-12-15T08:42:29.122437+05:30"},{"title":"This is the title 6","content":"this is the content 6","published":True,"id":6,"created_at":"2022-12-15T08:48:46.036579+05:30"},{"title":"This is the title 7","content":"this is the content 7","published":True,"id":7,"created_at":"2022-12-15T08:49:36.170970+05:30"},{"title":"This is the title 8","content":"this is the content 8","published":True,"id":8,"created_at":"2022-12-15T08:54:30.602010+05:30"}]

# @app.route("/")
# def dheep():
#     return post

# @app.route("/one")
# def one():
#     return render_template("new.html")

# @app.route("/<index>")
# def get(index):
#     return render_template("new.html", data=post[int(index)])
# @app.route("/two")
# def two():
#     #c= post[0]["content"]+post[1]["content"]
#     ar=[]
#     for i in range(len(post)):
#         ar.append(post[i].get("title"))
#         ar.append(post[i].get("content"))
#     return render_template("new.html",data=ar)

# @app.route("/three")
# def three():
#     post[0]["title"]=["hello"]
#     post[0]["content"]=["hello"]
#     return render_template("new.html",data=post)

# days=["mon","tues","wed","thurs"]

# @app.route("/four")
# def four():
#     return render_template("new.html",data=days)

# @app.route("/five",methods=["POST","GET"])
# def five():
#         title=request.form.get("title")
#         content=request.form.get("content")
#         print(title)
#         print(content)
#         dic={"title":title,"content":content}
#         post.append(dic)
#         return render_template("need.html",data=post)
# @app.route("/five",methods=["POST","GET"])
# def five():
#         title=request.form.get("title")
#         content=request.form.get("content")
#         print(title)
#         print(content)
#         dic={"title":title,"content":content}
#         post.append(dic)
#         #post[0]=dic
#         return render_template("need.html",data=post)

dheep=[{"id":1,"name":"dheep","message":"hi"},{"id":2,"name":"sam","message":"hello"},{"id":3,"name":"anu","message":"good"},{"id":4,"name":"jack","message":"per"}]

# @app.route("/",methods=["POST","GET"])
# def six():
#     return dheep

# @app.route("/",methods=["POST","GET"])
# def seven():
#     id=request.json.get("id")
#     name=request.json.get("name")
#     message=request.json.get("message")
#     dic={"id":id,"name":name,"message":message}
#     dheep.append(dic)
#     return dheep

@app.route("/<api>",methods=["POST","GET"])
def seven(api):
    id=request.json.get("id")
    name=request.json.get("name")
    message=request.json.get("message")
    dheep[int(api)]["id"]=id
    dheep[int(api)]["name"]=name
    dheep[int(api)]["message"]=message
    return dheep

if(__name__)=="__main__":
    app.run(debug=True)