from google.cloud import firestore
import json

def download_document(doc_id='all'):
    db = firestore.Client(project='hakoona-matata-298704')
    users_ref = db.collection(u'users')
    docs = users_ref.stream()
    for doc in docs:
        if doc_id in (str(doc.id),'all'):
            with open('download/'+str(doc.id)+".json",'w') as file_obj:
                data = doc.to_dict()
                json.dump(data,file_obj,indent=2)
            file_obj.close()
            print("file downloaded")
def upload_document(doc_id='all'):
    db = firestore.Client(project='hakoona-matata-298704')
    collection_ref =  db.collection('users')
    with open('download/user1.json','r') as file_obj:
        data=json.load(file_obj)
        doc_ref = collection_ref.document('python_test')
        doc_ref.set(data)
    file_obj.close()
