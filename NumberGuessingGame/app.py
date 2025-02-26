from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

random_number = random.randint(1, 100)
attempts = 5

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    global attempts, random_number
    data = request.get_json()
    guess = data["guess"]
    
    if attempts <= 0:
        return jsonify({"message": f"Game Over! The number was {random_number}.", "status": "lose", "attempts": attempts})
    
    attempts -= 1

    if guess == random_number:
        message = "🎉 Congratulations! You guessed it right!"
        status = "win"
    elif guess < random_number:
        message = "⬆️ Too low! Try a greater number."
        status = "continue"
    else:
        message = "⬇️ Too high! Try a lower number."
        status = "continue"

    if attempts == 0 and guess != random_number:
        message = f"😢 Game Over! The correct number was {random_number}."
        status = "lose"

    return jsonify({"message": message, "status": status, "attempts": attempts})

if __name__ == "__main__":
    app.run(debug=True)
