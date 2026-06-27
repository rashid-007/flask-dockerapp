from flask import Flask, jsonify
import time
app=Flask(__name__)
start_time=time.time()
@app.route('/')
def home():
    return jsonify({
        'message': 'Hello from dockerized flask app! Webhook has successfully been added',
	'status': 'running'
    })
@app.route('/stress')
def stress():
    x=0
    for i in range(1000000):
	x+=i*i
    return jsonify({ 'status': 'ok', 'result': x})
@app.route('/health')
def health():
    uptime = time.time() - start_time
    return jsonify ({
        'status':'ok',
        'uptime_seconds': round(uptime, 2)
    })
if __name__=='__main__':
    app.run(host='0.0.0.0',port=4000, debug=False)

