from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
  if request.method=='POST':
    return render_template('index.html')

@app.route('/tentangKami',methods=['GET','POST'])
def tentangKami():
  return render_template('tentangKami.html')

@app.route('/grooming',methods=['GET','POST'])
def grooming():
  return render_template('grooming.html')

@app.route('/makanan',methods=['GET','POST'])
def makanan():
  #makanan = list(db.makanan.find({}))  
  return render_template('makanan.html', makanan=makanan)

@app.route('/aksesoris',methods=['GET','POST'])
def aksesoris():
  #aksesoris = list(db.aksesoris.find({}))  
  return render_template('aksesoris.html', aksesoris=aksesoris)

@app.route('/klinik',methods=['GET','POST'])
def klinik():
  return render_template('klinik.html')

@app.route('/pethotel',methods=['GET','POST'])
def pethotel():
  return render_template('pethotel.html')

@app.route('/pacak',methods=['GET','POST'])
def pacak():
  return render_template('pacak.html')

if __name__ == '__main__':
  #DEBUG is SET to TRUE. CHANGE FOR PROD
  app.run('0.0.0.0',port=5000,debug=True)