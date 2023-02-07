from flask import Flask
from google.cloud import firestore
import os

app = Flask(__name__)

@app.route('/get_data',methods=['GET'])
def get_data():
    db = firestore.Client(project='hakoona-matata-298704')
    collection_ref =  db.collection(u'users')
    docs = collection_ref.stream()
    doc_list = []
    for doc in docs:
        doc_list.append(doc.id)
    return str(doc_list[0])+"__"+"200"

@app.route("/ping")
def ping():
    return "Ping OK from Flask"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))