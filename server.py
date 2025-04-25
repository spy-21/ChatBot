from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure the Gemini API
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    raise ValueError("Please set the GEMINI_API_KEY environment variable")
genai.configure(api_key=api_key)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        message = data.get('message', '')
        
        # Initialize the model with gemini-2.0-flash
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        # Generate response
        response = model.generate_content(message)
        
        return jsonify({
            'response': response.text
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 