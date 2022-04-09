from . import main_blueprint
from flask import render_template, url_for, request, redirect, Blueprint, json, flash, session
from ..tasks import send_celery_email



@main_blueprint.route('/')
def index():

    message_data={
        'subject': 'Hello from the flask app!',
        'body': 'This email was sent asynchronously using Celery.',
        'recipients': 'sarathlal@zennode.com',

    }
    send_celery_email.apply_async(args=[message_data])

    return render_template('main/index.html')