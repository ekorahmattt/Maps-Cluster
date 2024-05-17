from flask import Flask, render_template, redirect, request, url_for, session
from flask_mysqldb import MySQL
from sklearn.cluster import KMeans

app = Flask(__name__)

app.secret_key = 'cluster1234'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'map_cluster'

mysql = MySQL(app)

##################################### HALAMAN UTAMA #########################################################
@app.route('/', methods=['GET'])
def index():
    data = []
    kec = []

    cluster1 = []
    cluster2 = []
    cluster3 = []

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM data_cluster')

    for x in cur.fetchall():
        data.append(list(i for i in x if i != x[0] and i != x[4] and i != x[5]))
        kec.append(list(x))

    kmeans = KMeans(n_clusters=3)
    kmeans.fit(data)
    y = kmeans.predict(data)

    for i in range(len(y)):
        if y[i] == 0:
            cluster1.append(kec[i])
        elif y[i] == 1:
            cluster2.append(kec[i])
        else:
            cluster3.append(kec[i])

    return render_template('index.html', data=data, cluster1=cluster1, cluster2=cluster2, cluster3=cluster3)

##################################### LOGIN ########################################################
@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            session['loggedin'] = True
            return redirect(url_for('admin'))
        else:
            warn = 'salah'
            return render_template('index.html', warn=warn)

######################################## LOGOUT #####################################################
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    return redirect(url_for('index'))

######################################## HALAMAN DASHBOARD ADMIN #####################################################
@app.route('/admin', methods=['GET','POST'])
def admin():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM data_cluster')
    data = cur.fetchall()
    data = enumerate(data)
    cur.close()
    return render_template('admin.html', data=data)

######################################## UPDATE DATA ####################################################
@app.route('/update', methods=['POST'])
def update_data():
    if request.method == "POST":
        kecamatan = request.form['kecamatan']
        data1 = request.form['2021']
        data2 = request.form['2022']
        data3 = request.form['2023']

        cur = mysql.connection.cursor()
        cur.execute('''UPDATE data_cluster SET data_1=%s, data_2=%s, data_3=%s WHERE kecamatan=%s ''', (data1, data2, data3, kecamatan))
        
        mysql.connection.commit()
    return redirect(url_for('admin'))

######################################## RUNING DATA ####################################################
if __name__ == "__main__":
    app.run(debug=True)