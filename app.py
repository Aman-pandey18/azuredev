from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'AMAN PANDEY & 2201330100036'

if __name__ == '__main__':
    app.run(port=5000)
