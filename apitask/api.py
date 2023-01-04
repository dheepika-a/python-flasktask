from flask import Flask,render_template,request
import json
import requests

app=Flask(__name__)


list=[123654]
@app.route("/")
def ad():
    url="https://api.mfapi.in/mf/"+str(list[0])
    resp=requests.get(url)
    return render_template("index.html",data=resp.json().get("data")[0].get("nav"))
    
'''
list=[139619,139618,139616,139617,148921,148920,148918,148919]
d=[]
@app.route("/", methods=["POST","GET"])
def ad():
    for i in range(len(list)):
         res=requests.get("https://api.mfapi.in/mf/"+str(list[i]))

         fund=res.json().get("meta").get("fund_house")
         nav = res.json().get("data")[i].get("nav")
         dic ={"id":list[i],"fund":fund,"nav":nav}
         d.append(dic)

    return render_template("index.html", data = d)'''
    
if __name__ == "__main__":
    app.run(debug=True) 





