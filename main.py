import flask 
#from Flask import flask, request, jsonify 

app = Flask (__name__)

@app.route("/")
def home():
   return "Home"

if __name__ == "__main__":
    app.run(debug=True)
