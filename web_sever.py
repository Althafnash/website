from flask import Flask
from blueprint import Nashweb
import time 

app = Flask(__name__)
app.register_blueprint(Nashweb , url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True ,  port=8000 )

time.sleep(10)
