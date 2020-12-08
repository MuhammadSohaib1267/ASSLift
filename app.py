from flask import Flask , render_template ,request ,flash , redirect , url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI']="mongodb+srv://Sohaib:sohaib12439@cluster0-5ij3o.gcp.mongodb.net/AutonomousServingSystem?retryWrites=true&w=majority"
mongo=PyMongo(app)

@app.route("/")
def lift():
    cur=mongo.db.Lift
    data=cur.find_one({"Title":"Lift"})
    return render_template("elevator.html",data=data)

if __name__=='__main__':
    app.run(debug = True,port=1267)
