# -*- coding:utf-8 -*-                                

from flask import Flask, Response                     
app = Flask(__name__)                                 

@app.route("/")                                       
def hello():                                          
    return '<br/>'.join(['%s:: %s' % (key, value) for (key, value) in request.headers..items()])

@app.route("/favicon.ico")                            
def favicon():                                        
    resp = Response(status=200, mimetype='image/png') 
    return resp                                       

if __name__ == "__main__":                            
    app.run()                                         
