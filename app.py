import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd
import sklearn
    ##Name app as 'app'
app=Flask(__name__)
    ## Load regmodel and name it 'regmodel'
regmodel=pickle.load(open('regmodel.pkl','rb'))
    ## load 'scaler.pkl' to scale input data.
scaler=pickle.load(open('scaling.pkl','rb'))

@app.route('/')

   
def home():
    return render_template('home.html')
    ## 
@app.route('/predict_api',methods=['POST'])

## Convert input to json.
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
        ## collect values of data as list and convert it to array, and make it two diamensional

    new_data=scaler.transform(np.array(list(data.values())).reshape(1,-1))
        ## Transform to scale of 1

    output=regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict', methods=['POST'])

##Receive input, convert it to float, two diamensional array, and transform to scale, 
## Then, predict house price and insert in html page as an asnwer.2:06
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scaler.transform(np.array(data).reshape(1,-1))
    output=regmodel.predict(final_input)[0]
    return render_template("home.html",prediction_text="The House price prediction is {}".format(output))


if __name__=="__main__":
    app.run(debug=True)
