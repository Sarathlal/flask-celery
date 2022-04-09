from . import main_blueprint
from flask import render_template, url_for, request, redirect, Blueprint, json, flash, session



@main_blueprint.route('/')
def index():
    return render_template('main/index.html')

