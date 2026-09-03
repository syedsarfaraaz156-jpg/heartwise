from flask import Flask, render_template, request
from openai import OpenAI
import os

app = Flask(__name__)

api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)


@app.route("/", methods=["GET", "POST"])
def home():

    response = None

    if request.method == "POST":

        question = request.form.get("question")

        if question:

            result = client.chat.completions.create(
                model="openrouter/free",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are HeartWise, a thoughtful and empathetic "
                            "relationship advisor. Give practical, respectful "
                            "and balanced relationship advice. "
                            "Do not judge either person."
                        )
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

            response = result.choices[0].message.content

    return render_template("index.html", response=response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
