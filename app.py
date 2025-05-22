from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load model dari file .pkl
model = joblib.load('model_prediksi_harga_rumah.pkl')

@app.route('/')
def index():
    return render_template('index.html', predicted_price=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Prediksi harga rumah berdasarkan input user
    '''
    # Ambil nilai dari form
    floorarea = float(request.form['listing-floorarea'])
    bed = int(request.form['bed'])

    # Siapkan data input dalam bentuk array 2 dimensi
    data = [[floorarea, bed]]

    # Prediksi harga
    prediction = model.predict(data)
    output = round(prediction[0], 2)

    # Tampilkan hasil ke template
    return render_template(
        'index.html',
        predicted_price=output,
        floorarea=floorarea,
        bed=bed
    )

if __name__ == '__main__':
    app.run(debug=True)
