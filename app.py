from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/migrate_template', methods=['POST'])
def migrate_template():
    if request.method == 'POST':
        template = request.args.get('template_name', '')
        firs_instance = request.args.get('firs_instance', '')
        second_instance = request.args.get('second_instance', '')
        return 'Move template {' + template + '} from {' + firs_instance + '} to {' + second_instance + '} instance ' \
                                                                                                        'with success '
    else:
        return 'Sent right request the request parameters'


@app.route('/upload_all_metadata/<metadata_list>', methods=['GET', 'POST'])
def upload_all_metadata(metadata_list):
    if request.method == 'POST':
        return metadata_list + ' received from post'
        # return 'Update metadata list with success: ' + jsonify({"metadata_list": metadata_list})
    elif request.method == 'GET':
        return metadata_list + ' received from get'
    else:
        return 'Sent right request the request parameters'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
