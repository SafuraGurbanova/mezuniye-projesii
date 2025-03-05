#Kütüphaneler
import openai
import  aiohttp, requests
from flask import Flask, render_template,request, redirect
from flask import Flask, jsonify

#Veritabanı kütüphanesi
from flask_sqlalchemy import SQLAlchemy
openai.api_key = 'YOUR_KEY'


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        answer = response['choices'][0]['message']['content']
        return {"answer": answer}
    except Exception as e:
        print("Hata:", e)
        return {"answer": "Bir hata oluştu. Lütfen tekrar deneyin."}

if __name__ == "__main__":
    app.run(debug=True)
