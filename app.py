from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS = [
{
  'id':1,
  'title': 'Data Scientist',
  'location': 'Addis Ababa',
  'salary':'100k'
  },
{
  'id':2,
 'title' :'Data analyst',  
  'location': 'Addis Ababa',
  'salary': '120k'
  
},
  {
    'id':3,
    'title': 'Data Engineer',
    'location': 'Addis Ababa',
    'salary': '150k'
  },
  {
    'id':4,
    'title': 'Full stack developer',
         'location': 'Remote',
         'salary': '200k'
         }
]


@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='JJ')
  
@app.route('/api/jobs')
def jobs_list():
  return jsonify(JOBS)
             
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080 , debug=True)
