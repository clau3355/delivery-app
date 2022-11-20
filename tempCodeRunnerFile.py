import os

from flask import Flask, request, render_template
import gmplot

app = Flask(__name__)

@app.route('/')
def my_map(): 
    return 0

# commit nuevo

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
