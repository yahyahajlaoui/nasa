from flask import Flask, render_template, request , url_for , session , redirect
import os
from result import predict_res
app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def home():
       if request.method == 'POST':
         x1 = (float)(request.form["name"])
         x2 = (float)(request.form["name_a"])
         x3 = (float)(request.form["name_b"])
         x4 = (float)(request.form["name_c"])
         x5 = (float)(request.form["name_d"])
         x6 = (float)(request.form["name_e"])
         x7 = (float)(request.form["name_f"])
         li=[]
         li.append(x1)
         li.append(x2)
         li.append(x3)
         li.append(x4)
         li.append(x5)
         li.append(x6)
         li.append(x7)
         text=predict_res(li)
         if text=='There is a storm , ATTENTION !':
            xx=True
         else:
            xx=False

         

         return render_template('layout.html',upload=True,text=text,xx=xx)

       return render_template('layout.html',upload=False)
if __name__ =="__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)