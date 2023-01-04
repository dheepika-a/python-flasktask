from flask import Flask,render_template,request
import json
import requests

app=Flask(__name__)
'''
d=[]
@app.route("/",methods=["POST","GET"])
def add():
    dot=request.form.get("numbers")
    print(dot)
    res=requests.get("https://api.mfapi.in/mf/"+str(dot))
    fund=res.json().get("meta").get("fund_house")
    nav = res.json().get("data").get("nav")
    dic ={"id":dot,"fund":fund,"nav":nav}
    d.append(dic)

    return render_template("index.html", data = d)'''
'''
d=[]
@app.route("/", methods=["POST","GET"])
def ad():
   sa=[]
   dot=request.form.get("number")
   sa.append(dot)
   res=requests.get("https://api.mfapi.in/mf/"+str(sa[0]))
   fund=res.json().get("meta").get("fund_house")
   nav = res.json().get("data")[0].get("nav")
   dic ={"id":dot,"fund":fund,"nav":nav}
   d.append(dic)

   return render_template("index.html", data = d)'''

@app.route("/dheep", methods=["POST","GET"])
def ra():
        dot=request.json.get("number")
        res=requests.get("https://api.mfapi.in/mf/"+str(dot))
        fund=res.json().get("meta").get("fund_house")
        nav = res.json().get("data")[0].get("nav")
        dic ={"id":dot,"fund":fund,"nav":nav}
        return dic

    
if __name__ == "__main__":
    app.run(debug=True) 





