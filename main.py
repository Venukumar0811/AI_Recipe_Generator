from boltiotai import openai
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def generate():
    ans = ""
    if request.method == "POST":
        ingredients = request.form.get('items')

        # Set OpenAI API key
        openai.api_key = os.getenv("OPENAI_API_KEY")
                
        # Send request to OpenAI
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": f"Suggest  two recipies using these items listd as available.Make sure you have a nice name for this recipe listed at the start.Also, include a funny version of the name of the recipe on the following line. Then share the recipe in a step-by-step manner. In the end, write a fun fact about the recipe or any of the items used in the recipe. Here are the items available: {ingredients}.Haldi, Chilly Powder, Tomato Ketchup, Water,oil"
            }]
        )

        ans = response['choices'][0]['message']['content']
    
    return render_template("index.html", ans=ans)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
