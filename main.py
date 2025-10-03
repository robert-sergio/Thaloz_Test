from fastapi import FastAPI

app = FastAPI()

@app.post('/project')
def add_project():
    ...

@app.get('projects/{project_id}')
def get_project():
    ...

@app.put('projects/{project_id}')
def updt_project():
    ...

@app.delete('projects/{project_id}')
def del_project():
    ...


@app.post('/projects/{project_id}/tasks/')
def add_task():
    ...

@app.get('/projects/{project_id}/tasks/')
def get_task():
    ...

@app.put('/tasks/{task_id}')
def updt_task():
    ...

@app.delete('/tasks/{task_id}')
def del_task():
    ...