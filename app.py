from flask import Flask

app = Flask(__name__)

@app.route("/") #Match the empty page with just /
def HelloWorld():
  return "Hello Pigs!"

if __name__ == "__main__":
  print(app.run(host="0.0.0.0", debug=True))




