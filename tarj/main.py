from flask import Flask


app = Flask(__name__)

import os
os.makedirs('arquivos_temp', exist_ok=True)


from views import *


if __name__ == "__main__":
    app.run(debug=True)