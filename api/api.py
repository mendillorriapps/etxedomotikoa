from flask import Flask, render_template, request
app = Flask(__name__,static_url_path='/static')

@app.route (/tenperatura/<T>)
def jasoTemperatura(T):
    pass

@app.route (/argia/<argi>)
def jasoArgia(argi):
    pass

@app.route (/mugimendua/<mug>)
def jasoMugimendua(mug):
    pass

@app.route (/ponpa/<ponpa>)
def bidaliPonpa(ponpa):
    return 1

@app.route (/bozgoragailua/<bozg>)
def bidaliBozg(bozg):
    return 1

@app.route (/ledgorria/<ĺedgorria>)
def bidaliledgorria(ledgoriia)
    return 1

@app.route (/ledurdina/<ĺedurdina>)
def bidaliledurdina(ledurdina)
    return 1

@app.route (/ledtxuria/<ĺedtxuria>)
def bidaliledtxuria(ledtxuria)
    return 1

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
