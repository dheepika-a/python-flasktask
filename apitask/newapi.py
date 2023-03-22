from flask import Flask , render_template,request
import json
import requests
app=Flask(__name__)


# @app.route("/")
# def dheep():
#     url="https://api.mfapi.in/mf/123654"
#     resp=requests.get(url)
#     return render_template("index.html", data=resp.json().get("data")[0].get("nav"))
# list=[148921]
# @app.route("/")
# def one():
#     url="https://api.mfapi.in/mf/"+str(list[0])
#     resp=requests.get(url)
#     return render_template("index.html", data=resp.json().get("data")[0].get("nav"))

# list=[148921,148920,148918]
# c=[]
# @app.route("/")
# def one():
#     for i in range(len(list)):
#      url="https://api.mfapi.in/mf/"+str(list[i])
#      resp=requests.get(url)
#      data=resp.json().get("data")[0].get("nav")
#      c.append(data)
#     return render_template("index.html", data=c)


if(__name__)=="__main__":
    app.run(debug=True)