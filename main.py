from flask import Flask, render_template, redirect, request, url_for, jsonify
from flask_mysqldb import MySQL
from sklearn.cluster import KMeans
import json

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'map_cluster'

mysql = MySQL(app)

##############################################################################################
@app.route('/', methods=['GET'])
def index():
    data = []
    kec = []

    cluster1 = []
    cluster2 = []
    cluster3 = []

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM data_cluster')
    row_headers = [x[0] for x in cur.description]

    for x in cur.fetchall():
        data.append(tuple(i for i in x if i != x[0]))
        kec.append(list(x))
        # kec.append(dict(zip(row_headers, x)))

    kmeans = KMeans(n_clusters=3)
    kmeans.fit(data)
    y = kmeans.fit_predict(data)

    for i in range(len(y)):
        if y[i] == 0:
            cluster1.append(kec[i])
        elif y[i] == 1:
            cluster2.append(kec[i])
        else:
            cluster3.append(kec[i])

    return render_template('index.html', cluster1=cluster1, cluster2=cluster2, cluster3=cluster3)

#############################################################################################
@app.route('/admin', methods=['GET','POST'])
def admin():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM data_cluster')
    data = cur.fetchall()
    data = enumerate(data)
    cur.close()
    return render_template('admin.html', data=data)

############################################################################################
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

############################################################################################
if __name__ == "__main__":
    app.run(debug=True)