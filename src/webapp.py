from flask import Flask, render_template, request
import math,time

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def response():    
    if request.method == 'GET':
        gmt = time.gmtime()
        return render_template('index.html', 
                               time = time.strftime('%c',gmt),
                               number = '1', 
                               log = '0')
    else:
        num = request.form['number']
        gmt = time.gmtime()
        return render_template('index.html', 
                               time = time.strftime('%c',gmt),
                               number = num, 
                               log = str(math.log(float(num))))
         
if __name__ == '__main__':    
    app.run(debug=True, host='0.0.0.0')    