import logging

def notify_failure(**context):
    task_instance = context.get('task_instance')
    if task_instance:
        msg = f"Task {task_instance.task_id} failed. Run ID: {context.get('run_id')}"
    else:
        msg = "A task failed, but context is missing."
    # You could send emails, post to Slack, etc. Here, just log:
    logging.error(msg)
