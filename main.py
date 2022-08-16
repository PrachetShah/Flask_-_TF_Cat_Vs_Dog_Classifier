from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')
 
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        return render_template('index.html', var1=request.form['image'])
    return render_template('index.html')
 
if __name__ == '__main__':
    app.run(debug=True)