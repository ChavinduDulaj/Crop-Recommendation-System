import joblib
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home_1.html')

@app.route('/Predict')
def prediction():
    return render_template('Index.html')

@app.route('/form', methods=["POST"])
def brain():
    Nitrogen=float(request.form['Nitrogen'])
    Phosphorus=float(request.form['Phosphorus'])
    Potassium=float(request.form['Potassium'])
    Temperature=float(request.form['Temperature'])
    Humidity=float(request.form['Humidity'])
    Ph=float(request.form['ph'])
    Rainfall=float(request.form['Rainfall'])
     
    values=[Nitrogen,Phosphorus,Potassium,Temperature,Humidity,Ph,Rainfall]
    
    if Ph>0 and Ph<=14 and Temperature<100 and Humidity>0:
        joblib.load('crop_app','r')
        model = joblib.load(open('crop_app','rb'))
        arr = [values]
        predicted_class_index = model.predict(arr)

        # Define the class names dictionary
        class_names = {
    20: 'Rice', 11: 'Maize', 3: 'Chickpea', 9: 'Kidneybeans', 18: 'Pigeonpeas',
    13: 'Mothbeans', 14: 'Mungbean', 2: 'Blackgram', 10: 'Lentil', 19: 'Pomegranate',
    1: 'Banana', 12: 'Mango', 7: 'Grapes', 21: 'Watermelon', 15: 'Muskmelon',
    0: 'Apple', 16: 'Orange', 17: 'Papaya', 4: 'Coconut', 6: 'Cotton', 8: 'Jute',
    5: 'Coffee'
         }

        # Map the predicted class index to the class name
        predicted_class = class_names[predicted_class_index[0]]
           # print(acc)
        return render_template('prediction.html', prediction=str(predicted_class))
    else:
        return "Sorry...  Error in entered values in the form Please check the values and fill it again"



if __name__ == '__main__':
    app.run(debug=True)















