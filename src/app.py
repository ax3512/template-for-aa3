from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/user', methods=['GET'])
def get_user():
    # 사번을 JSON 형태로 반환
    return jsonify({"employee_id": "[사번]"})  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

