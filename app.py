from flask import Flask, render_template, redirect, url_for, request
from utils.entropy import entropy
import math

magicKey = 'this_IS_a_53cret_key_you_should_change'

app = Flask(__name__, static_folder='./static', static_url_path='/assets', template_folder='templates')

app.secret_key = magicKey
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def hello():
	if request.method == 'GET':
		return render_template("index.html")
	else:
		password = request.form['password']
    	entropy_value = entropy(password)
    	return render_template("result.html", **locals())

# APP LAUNCHING:
if __name__ == "__main__":
        app.run()
