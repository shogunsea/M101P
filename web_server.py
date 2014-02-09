import bottle
import pymongo

# this is the handler for the default path of the web server

@bottle.route('/')
def index():

	#connect to mongoDB
	connection = pymongo.MongoClient('localhost', 27017)

	#attach to test database
	db = connection.test

	# get handle for mycollection collection
	col = db.mycollection

	# find a single document
	item = col.find_one()

	return '<h1>Hello %s!</h1>' % item['hello']

bottle.run(host = 'localhost', port = 8082)