from flask import Flask, request, jsonify, send_from_directory, redirect
import sys
import os
import subprocess

app = Flask(__name__, static_folder='.')

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/models.html')
def models():
    return send_from_directory('.', 'models.html')

@app.route('/training.html')
def training():
    return send_from_directory('Training', 'training.html')

@app.route('/launch/<model_type>', methods=['GET'])
def launch_model(model_type):
    try:
        if model_type == 'linear-regression':
            subprocess.Popen(['streamlit', 'run', 'lr/a.py'])
            return jsonify({'status': 'success', 'url': 'http://localhost:8501'})
        
        elif model_type == 'random-forest':
            subprocess.Popen(['streamlit', 'run', 'rf/app.py'])
            return jsonify({'status': 'success', 'url': 'http://localhost:8501'})
        
        elif model_type == 'xgboost':
            subprocess.Popen(['streamlit', 'run', 'xgb/ap.py'])
            return jsonify({'status': 'success', 'url': 'http://localhost:8501'})
        
        elif model_type == 'training':
            subprocess.Popen(['streamlit', 'run', 'Training/t.py'])
            return jsonify({'status': 'success', 'url': 'http://localhost:8501'})
        
        else:
            return jsonify({'error': 'Invalid model type'}), 400
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)