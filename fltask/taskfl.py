from flask import Flask, render_template

app = Flask(__name__)

my_post = ["monday","tuesday","wedn","thursday","friday"]
 


@app.route("/")
def hello_world():
    return render_template("index.html", data =my_post)
    

@app.route("/<dheep>")
def user_info(dheep):
    return render_template("index.html", data = dheep)


#if __name__=="__main__":
app.run(debug=True)



