from flask import Flask
from flask_restful import Resource, Api


from connectDB.testAPI import NameCollectionAPI

app = Flask(__name__)
api = Api(app)

api.add_resource(NameCollectionAPI, '/name', methods = ['GET', 'POST'])


if __name__ == '__main__':
	try:
		app.run(host='192.168.1.7', port=3001, debug=True)
	except Exception as exp:
		print (exp)