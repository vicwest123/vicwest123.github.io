from flask import Flask, jsonify
import openai



@app.route("/prompt")
def prompt():
    data = {'name': 'David'}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

