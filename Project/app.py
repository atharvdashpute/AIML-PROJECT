from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    name = request.form['name']
    age = request.form['age']
    skills = request.form['skills']
    interests = request.form['interests']

    # Simulate AI prediction (Replace with real ML model later)
    suggested_careers = ["Software Engineer", "Data Scientist", "UI/UX Designer"]
    
    return jsonify({
        'name': name,
        'suggested_careers': suggested_careers
    })

if __name__ == '__main__':
    app.run(debug=True)
