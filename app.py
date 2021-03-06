from flask import Flask, render_template, request
from utils.Entropy import password_entropy

magicKey = 'this_IS_a_53cret_key_you_should_change'

app = Flask(
    __name__,
    static_folder='./static',
    static_url_path='/assets',
    template_folder='templates')

app.secret_key = magicKey
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        password = request.form['password']
    entropy = password_entropy(password)
    brute = pow(2, entropy)
    if entropy < 128:
        if entropy < 112:
            if entropy < 80:
                if entropy < 64:
                    label = "VERY WEAK"
                else:
                    label = "Weak"
            else:
                label = "Moderate"
        else:
            label = "Strong"
    else:
        label = "VERY STRONG"
    return render_template("result.html", **locals())

# APP LAUNCHING:
if __name__ == "__main__":
    app.run()
