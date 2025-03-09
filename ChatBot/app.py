from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_bot_response(user_input):
    # Простейшая логика обработки запроса
    user_input = user_input.lower()
    if "привет" in user_input:
        return "Здравствуйте! Чем могу помочь?"
    elif "проблема" in user_input:
        return "Опишите, пожалуйста, вашу проблему подробнее."
    elif "спасибо" in user_input:
        return "Пожалуйста, рад был помочь!"
    else:
        return "Извините, я не понимаю ваш запрос. Можете уточнить?"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_response():
    user_input = request.form["msg"]
    response = get_bot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)