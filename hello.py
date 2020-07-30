from flask import Flask,request,jsonify
import pickle
import sklearn
from classluis import luis2
from clean import clean
import numpy as np
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Meeting Intent API</h1><p>Will return predictions for meeting, urgency and none.</p>"

@app.route('/predict',methods=['POST'])
def predict():    
    data = request.get_json(force=True)
    q = data['query']
    res2=clf.predict_proba([q])
    
    res2=np.concatenate((vec.transform([q]).toarray(),res2,np.array(luis.predict_proba([q]))),axis=1)
    prediction = stack.predict_proba(res2)
    print(prediction)
    s=jsonify(
    meeting=prediction[0][0],
    urgent=prediction[0][1],
    none=prediction[0][2]
    )
    return(s)

if __name__ == '__main__':        

    vec = pickle.load(open('pickles/vec.pkl','rb'))
    clf = pickle.load(open('pickles/clf1.pkl','rb'))
    luis = pickle.load(open('pickles/luis.pkl','rb'))
    stack = pickle.load(open('pickles/stack.pkl','rb'))
    app.run(port=5000)