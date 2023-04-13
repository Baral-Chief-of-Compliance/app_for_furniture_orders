from app import app, jsonify, request, Blueprint


@app.route('/admin_panel/api/v1.0/')
def index():
    return jsonify("hello world")