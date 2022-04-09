from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from dochours.models import User, Tenant


# class NewAccount(FlaskForm):
# 	name = StringField('Your Name', validators=[DataRequired()], render_kw={"placeholder": "Your Name"})
# 	email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
# 	phone = StringField('Phone', validators=[DataRequired()], render_kw={"placeholder": "Phone"})
# 	org_name = StringField('Organization Name', validators=[DataRequired()], render_kw={"placeholder": "Organization Name"})
# 	submit = SubmitField('Submit')

class RegistrationForm(FlaskForm):
	# username = StringField('Username')
	email = StringField('Email',
						validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
	password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40, message="Password should contain minimum 6 characters")], render_kw={"placeholder": "Password"})
	confirm_password = PasswordField('Confirm Password',
									 validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm Password"})
	submit = SubmitField('Sign Up')

	def validate_email(self, email):
		user = Tenant.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Enter your email"})
	password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Enter your password"})
	remember = BooleanField('Remember me next time', render_kw={"checked": True})
	submit = SubmitField('Sign in')


class UpdateAccountForm(FlaskForm):
	# username = StringField('Username',
	# 					   validators=[DataRequired(), Length(min=2, max=40)])
	email = StringField('Email',
						validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[])
	confirm_password = PasswordField('Confirm Password',
									 validators=[EqualTo('password')])
	picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
	submit = SubmitField('Update')

	def validate_password(form, field):
		if len(field.data) > 0:
			if len(field.data) < 6:
				raise ValidationError('Password should have minimum 6 characters')

	def validate_email(form, email):
		user = User.query.filter_by(email=email.data).first()
		if user and email.data != current_user.email:
			raise ValidationError('Email already registered.')




	# def validate_username(self, username):
	#     if username.data != current_user.username:
	#         user = User.query.filter_by(username=username.data).first()
	#         if user:
	#             raise ValidationError('That username is taken. Please choose a different one.')

	# def validate_email(self, email):
	#     if email.data != current_user.email:
	#         user = User.query.filter_by(email=email.data).first()
	#         if user:
	#             raise ValidationError('That email is taken. Please choose a different one.')


class RequestResetForm(FlaskForm):
	email = StringField('Email',
						validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
	submit = SubmitField('Request Password Reset')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError('There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
	password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40, message="Password should contain minimum 6 characters")], render_kw={"placeholder": "New password"})
	confirm_password = PasswordField('Confirm Password',
									 validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm new password"})
	submit = SubmitField('Reset Password')
