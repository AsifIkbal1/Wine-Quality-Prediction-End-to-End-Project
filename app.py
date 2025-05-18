from flask import Flask, render_template, request
import os 
import numpy as np
from mlProject.pipeline.prediction import PredictionPipeline

# 🧪 Flask অ্যাপ্লিকেশন তৈরি করা হলো
app = Flask(__name__)

# 🏠 হোম পেইজ রেন্ডার করবে (index.html দেখাবে)
@app.route('/', methods=['GET'])
def homePage():
    return render_template("index.html")

# 🎯 মডেল ট্রেইন করার জন্য route (main.py ফাইল রান করাবে)
@app.route('/train', methods=['GET'])
def training():
    try:
        os.system("python main.py")  # ⚙️ মেইন পাইপলাইন রান করে
        return "✅ Model training completed successfully!"
    except Exception as e:
        return f"❌ Error during training: {e}"

# 🤖 প্রেডিকশন করার রাউট
@app.route('/predict', methods=['POST', 'GET'])
def predictRoute():
    if request.method == 'POST':
        try:
            # 📥 ইউজার ইনপুটগুলো নেওয়া
            input_features = [
                float(request.form['fixed_acidity']),
                float(request.form['volatile_acidity']),
                float(request.form['citric_acid']),
                float(request.form['residual_sugar']),
                float(request.form['chlorides']),
                float(request.form['free_sulfur_dioxide']),
                float(request.form['total_sulfur_dioxide']),
                float(request.form['density']),
                float(request.form['pH']),
                float(request.form['sulphates']),
                float(request.form['alcohol']),
            ]

            # 🧮 ইনপুট ডেটা numpy array তে রূপান্তর
            data = np.array(input_features).reshape(1, -1)

            # 🔮 PredictionPipeline দিয়ে প্রেডিকশন করা
            obj = PredictionPipeline()
            prediction = obj.predict(data)

            # 🧾 প্রেডিকশন রেজাল্ট দেখানো
            return render_template('results.html', prediction=str(prediction))

        except Exception as e:
            print('❌ Exception occurred: ', e)
            return '⚠️ কিছু একটা ভুল হয়েছে। দয়া করে আবার চেষ্টা করুন।'

    else:
        return render_template('index.html')


# 🚀 Flask অ্যাপ চালু করা হচ্ছে
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5001, debug=True)
