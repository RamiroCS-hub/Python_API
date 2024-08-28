from flask import Flask, request, jsonify, make_response
from db.db import init_db, close_db
from Services.services import Service
from Utils.messageAndStatus import message_and_status

app = Flask(__name__)

@app.route('/start', methods=['GET'])
def init_adventure():
	try:
		service = Service()

		firstSituation = service.get_first_situation()
		options = service.get_options_by_situation_id(firstSituation[0])

		return make_response(jsonify({
			'description': firstSituation[1],
			'options': options 
		}), 200)
	except Exception as e:
		errorResponse = message_and_status(e)
		return make_response(str(errorResponse['message']), errorResponse['status'])

@app.route('/choose', methods=['POST'])
def choose_option():
	try:
		service = Service()
		optionId = request.args.get('id')
		situation = service.get_situation_id_by_option_id(optionId)
		options = service.get_options_by_situation_id(situation[0])
		return make_response(jsonify({
			'description': situation[1],
			'options': options 
		}), 200)
	except Exception as e:
		errorResponse = message_and_status(e)
		return make_response(str(errorResponse['message']), errorResponse['status'])

@app.teardown_appcontext
def close_connection(exception):
	if exception:
		print(f'An error has ocurred: {exception}')
		exit(1)
	close_db()

if __name__ == '__main__':
	init_db()
	app.run(debug=True)