from flask import Flask, render_template, request
import pickle
import numpy as np

app=Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))



@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":

            N=int(request.form['N'])
            P=int(request.form['P'])
            K=int(request.form['K'])
            temperature=float(request.form['temperature'])
            humidity=float(request.form['humidity'])
            ph=float(request.form['ph'])
            rainfall=float(request.form['rainfall'])

            data = np.array([[N, P, K,
                          temperature,
                          humidity,
                          ph,
                          rainfall]])

            prediction = model.predict(data)

            return render_template('result.html',
                               prediction_text=
                               f"Recommended Crop is: {prediction[0]}")
    return render_template('index.html')


if __name__ == '__main__':
     app.run(debug=True)



