from flask import Flask, render_template
import pymongo
import scrape_mars


app = Flask(__name__)


client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_facts



@app.route('/scrape')
def scrape():
    db.collection.remove({})
    insert = scrape_mars.scrape()
    db.mars_facts.insert_one(insert)
    return db.mars_facts

@app.route("/")
def home():
    mars = list(db.collection.find())
    return render_template("index.html", mars = mars)


if __name__ == "__main__":
    app.run(debug=True)
