from flask import Flask,render_template,request
import pickle
import numpy as np

final_model=pickle.load(open(r"C:\Users\shind\Downloads\BTC_PROJECT\btc\model.pkl",'rb'))

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    Open=float(request.form.get('Open'))
    Low=float(request.form.get('Low'))
    Close=float(request.form.get('Close'))
    user_data = np.zeros(3)
    user_data[0]=Open
    user_data[1]=Low
    user_data[2]=Close

    result = final_model.predict((user_data).reshape(1,3))
    return str(f'Predicted High Is {result[0]}')


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)
