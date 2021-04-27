from flask import Flask, render_template, redirect, request
import TEMP1

app=Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/', methods= ['POST'])
def marks():
    if request.method == 'POST':
        f=request.files['userfile']
        path="./static/{}".format(f.filename)
        f.save(path)

        result= TEMP1.predict(path)
        result_dic={
            'image': path,
            'Result':result
        }
        
    return render_template("index.html", result_out= result_dic)


if __name__=='__main__':
    app.run(debug=True)

