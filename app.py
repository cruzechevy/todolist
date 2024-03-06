"""THis is simple Flask Application to add,update and delete Task Planner"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize a list to store tasks
tasks = []

"""Fetch the template index file from the html folder"""

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    priority = request.form['priority']
    due_date = request.form['due_date']
    tasks.append({'task': task, 'priority': priority, 'due_date': due_date, 'completed': False})
    return redirect(url_for('index'))


"""The below task is used to show the task as completed when Complete button on the Flask App is clicked"""

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if task_id < len(tasks):
        tasks[task_id]['completed'] = True
    return redirect(url_for('index'))

@app.route('/delete_completed')
def delete_completed():
    global tasks
    tasks = [task for task in tasks if not task['completed']]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)