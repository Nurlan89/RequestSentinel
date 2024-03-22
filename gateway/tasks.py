from celery import Celery


app = Celery("RequestSentinel", broker="redis://localhost:6379/0")


@app.task
def process_request(headers, body):
    send_to_receiver(headers, body)


def send_to_receiver(headers, body):
    pass
