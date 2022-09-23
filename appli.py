from flask import Flask, render_template, request

app = Flask(__name__)


# element of the database
DB_HOST = "localhost"
DB_NAME = "sampledb"
DB_USER = "postgres"
DB_PASS = "root"


@app.route('/')
def create_product():
	return render_template('pageProdcut.html')

@app.route('/add')
def add_product():
	return render_template('pageProdcut.html')

@app.route('/delete')
def delete_product():
	return render_template('pageProdcut.html')




# main driver function
if __name__ == '__main__':
     app.run()

