from locust import HttpUser, TaskSet, task, between

class TaskPredict(TaskSet):
    @task
    def predict(self):
        request_body = {"data": "test"}
        self.client.post('/predict', json=request_body)



class TaskLoadTest(HttpUser):
    tasks = [TaskPredict]
    host = 'http://127.0.0.1'
    stop_timeout = 20
    wait_time = between(1, 5)