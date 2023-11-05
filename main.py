from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [
    {
        'title': 'Frontend Developer',
        'company': 'WebTech Solutions',
        'location': 'New York, NY',
        'salary': '$60,000 - $80,000 per year',
        'description': 'Join our team as a Frontend Developer and work on exciting web projects. We\'re looking for someone with strong HTML, CSS, and JavaScript skills.'
    },
    {
        'title': 'Data Scientist',
        'company': 'Data Insights Inc.',
        'location': 'San Francisco, CA',
        'salary': '$80,000 - $100,000 per year',
        'description': 'We\'re seeking a talented Data Scientist to analyze and interpret complex data. If you have a passion for data-driven insights, apply now!'
    },
    {
        'title': 'UX/UI Designer',
        'company': 'Creative Solutions Ltd.',
        'location': 'Los Angeles, CA',
        'salary': '$70,000 - $90,000 per year',
        'description': 'We\'re looking for a creative UX/UI Designer to help us create stunning user experiences. Do you have an eye for design? Apply now!'
    },
    {
        'title': 'Marketing Manager',
        'company': 'Marketing Pro Inc.',
        'location': 'Chicago, IL',
        'salary': '$75,000 - $95,000 per year',
        'description': 'Are you a dynamic Marketing Manager with a passion for driving results? Join our team and lead successful marketing campaigns.'
    }
]
@app.route('/')
def main():
  return render_template("index.html", jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)



