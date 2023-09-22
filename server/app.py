from flask import Flask,render_template

app = Flask(__name__)

@app.route("/members")
def members():
    return {"members": ["Shailendra","Ranjeet","Sandesh"]}
    #return "<p>Hello, World Ranjeet!</p>"

if __name__=="__main__":
    app.run(debug=True)