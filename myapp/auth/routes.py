from flask import render_template, url_for, flash, redirect, request, Blueprint, session, json
# from myapp import db, bcrypt
from myapp.models import Plugin
# from dochours.auth.forms import (LoginForm, UpdateAccountForm,
#                                    RequestResetForm, ResetPasswordForm)

from myapp.plugin.utils import *


plugin = Blueprint('plugin', __name__)

@plugin.route("/", methods=['GET', 'POST'])
def index():
    return render_template('plugin/index.html')