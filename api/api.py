from flask import Flask, render_template, request, jsonify

from sqlalchemy import create_engine,update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from datetime import datetime

from datuak import Tenperatura

from datuak import Argia

from datuak import Mugimendua

from datuak import Ponpa

from datuak import Konfigurazioa

#from datuak import Ledtxuria

tmax=24
ar=500

eng = create_engine('sqlite:///test.db')

Base = declarative_base()

Base.metadata.bind = eng        
Base.metadata.create_all()        
        
Session = sessionmaker(bind=eng)
ses = Session() 

app = Flask(__name__,static_url_path='/static')

@app.route ('/tenperatura/<T>')
def jasoTemperatura(T):
    print(T)
    t1 = Tenperatura(tenperatura=T,ordua=datetime.now())
    ses.add(t1)
    ses.commit()
    return jsonify (
        status = "OK"
    )

@app.route ('/argia/<argi>')
def jasoArgia(argi):
    print(argi)
    a1= Argia(argia=argi,ordua=datetime.now())
    ses.add(a1)
    ses.commit()
    return jsonify (
        status = "OK"
    )

@app.route ('/mugimendua/<mug>')
def jasoMugimendua(mug):
    print(mug)
    m1= Mugimendua(mugimendua=mug,ordua=datetime.now())
    ses.add(m1)
    ses.commit()
    return jsonify (
        status = "OK"
    )

@app.route ('/ponpa/')
def bidaliPonpa():
    return '1'

def bozgo():
    rs = ses.query(Mugimendua).order_by(Mugimendua.ordua.desc()).first()
    if rs.mugimendua == 1:
        return '1'
    else:
        return '0'

@app.route ('/bozgoragailua/')
def bidaliBozg():
    return jsonify(    
      bozg = bozgo()
      )




def lgorria():
    rs = ses.query(Tenperatura).order_by(Tenperatura.ordua.desc()).first()
    tmin = ses.query(Konfigurazioa,giltza="tmin")
    if rs.tenperatura<tmin:
        return '1'
    else:
        return '0'

@app.route ('/ledgorria/')
def bidaliledgorria():
    return jsonify(    
        ledgorria = lgorria()
    )



def lurdina():
    rs = ses.query(Tenperatura).order_by(Tenperatura.ordua.desc()).first()
    if rs.tenperatura>tmax:
        return '1'
    else:
        return '0'

@app.route ('/ledurdina/')
def bidaliledurdina():
    return jsonify(
        ledurdina = lurdina()
    )



def ltxuria():
    rs = ses.query(Argia).order_by(Argia.ordua.desc()).first()
    if rs.argia < ar:
        return '1'
    else:
        return '0'

@app.route ('/ledtxuria/')
def bidaliledtxuria():    
    return jsonify(
        ledtxuria = ltxuria()
    )



@app.route ('/guztia/')
def bidaliguztia():    
    return jsonify(
        ledtxuria = ltxuria(),
        ledurdina = lurdina(),
        bozg = bozgo(),
        ledgorria = lgorria()  
    )


@app.route ('/tmin/<T>')
def eguneratuTmin(T):
    rs = ses.query(Konfigurazioa).filter(Konfigurazioa.giltza=="tmin").first()
    rs.balioa=T
    ses.commit()
    return jsonify (
        status = "OK"
    )

@app.route ('/tmax/<T>')
def eguneratuTmin(T):
    rs = ses.query(Konfigurazioa).filter(Konfigurazioa.giltza=="tmax").first()
    rs.balioa=T
    ses.commit()
    return jsonify (
        status = "OK"
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
