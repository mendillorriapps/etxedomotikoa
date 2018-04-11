from flask import Flask, render_template, request
app = Flask(__name__,static_url_path='/static')

@app.route ('/tenperatura/<T>')
def jasoTemperatura(T):
    print(T)
    return 'OK'

@app.route ('/argia/<argi>')
def jasoArgia(argi):
    print(argi)
    return 'OK'

@app.route ('/mugimendua/<mug>')
def jasoMugimendua(mug):
    print(mug)
    return 'OK'

@app.route ('/ponpa/')
def bidaliPonpa(ponpa):
    return '1'

@app.route ('/bozgoragailua/')
def bidaliBozg(bozg):
    return '1'

@app.route ('/ledgorria/')
def bidaliledgorria():
    return '1'

@app.route ('/ledurdina/')
def bidaliledurdina():
    return '1'

@app.route ('/ledtxuria/')
def bidaliledtxuria():
    return '1'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
