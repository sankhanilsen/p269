
# Import Libraries
from flask import Flask,request,jsonify,render_template


app = Flask(__name__)

@app.route('/')
def load_html():
   print('HTML page is loaded!')
   return render_template('home.html')


# Route and define the index function to render the home.html.




# Call the app.run()

if __name__ == "__main__":
    app.run()

