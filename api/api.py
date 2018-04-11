from flask import Flask, render_template, request

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from datetime import datetime

from datuak import Tenperatura

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
def bidaliPonpa():
    return '1'

@app.route ('/bozgoragailua/')
    return '1'

@app.route ('/ledgorria/')
def bidaliledgorria():
    rs = ses.query(Tenperatura).order_by(Tenperatura.ordua.desc()).first()

    print(rs.tenperatura)
    return '1'

@app.route ('/ledurdina/')
def bidaliledurdina():
    return '1'

@app.route ('/ledtxuria/')
def bidaliledtxuria():
    return '1'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
