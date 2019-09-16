from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return 'Jobs and jobs for all'

@app.route('/template_job')
def templage_job():
  return 'Endpoint for template job'
  
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)