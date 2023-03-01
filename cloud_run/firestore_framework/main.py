from flask import Flask,request
from google.cloud import firestore
import os

app = Flask(__name__)

@app.route('/get_data',methods=['GET'])
def get_data():
    db = firestore.Client(project=os.environ.get('project_id'))
    collection_ref = db.collection(request.args.get('collection'))
    docs = collection_ref.stream()
    doc_list = []
    for doc in docs:
        doc_list.append(doc.id)
    return str(doc_list[0]) + "__" + "200"

@app.route('/set_data',methods=['PUT','POST','GET'])
def set_data(): #modify payload and doc_id as parameters based on your usecase
    db = firestore.Client(project=os.environ.get('project_id'))
    collection_ref =  db.collection(request.args.get('collection'))
    #payload
    payload = {"test":"ok"}
    doc_id = 'docker_test'
    doc_ref = collection_ref.document(doc_id)
    doc_ref.set(payload)
    return ("Operation Successful",200)

@app.route("/ping")
def ping():
    return "Ping OK from Flask"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))