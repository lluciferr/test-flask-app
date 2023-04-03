from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Flask app working properly and well done ’

if __name__ == '__main__':
   app.run()