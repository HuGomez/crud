#encoding:utf-8
from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
IMPORT_FILE_TYPES = ['.sql',' .txt', ]

class LoginCaptchaForm(forms.Form):
	captcha = CaptchaField(label = "Código de Seguridad")

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))
	

class RegisterForm(forms.Form):
	first_name = forms.RegexField(label="Nombre",regex=r'^[a-zA-Z][a-zA-Z ]+$', max_length=20, widget=forms.TextInput())
	last_name = forms.RegexField(label="Apellido",regex=r'^[a-zA-Z][a-zA-Z ]+$', max_length=20, widget=forms.TextInput())
	username = forms.RegexField(label='Nombre de Usuario',regex=r'^[\w]+$', max_length=15, widget=forms.TextInput())
	#is_staff = forms.BooleanField(label = 'Es Administrador?',widget=forms.TextInput(),help_text = 'Marque la casilla si desea crear un administrador'),
	email = forms.EmailField(label='E-mail',widget=forms.TextInput())
	password_one = forms.CharField(label='Password',widget=forms.PasswordInput(render_value=False))
	password_two = forms.CharField(label='Confirmar Password',widget=forms.PasswordInput(render_value=False))

	#Password mínimo de X dígitos
	def clean_password_one(self):
		password = self.cleaned_data.get('password_one')
		if len(password) < 1:
			raise forms.ValidationError('Contraseña mínimo de 8 caracteres')
		return password

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Ese nombre de usuario ya existe')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Ese email ya está registrado')

	def clean_password(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('Las contraseñas no coinciden')

class UploadForm(forms.Form):
    docfile = forms.FileField(
    	required = True,
    	label='Selecione el archivo (*.sql ó *.txt)',
    	help_text='máximo 42 Mb'
    )
                              
    def clean_docfile(self):
        import os
        docfile = self.cleaned_data['docfile']
        extension = os.path.splitext( docfile.name )[1]
        if not (extension in IMPORT_FILE_TYPES):
            raise forms.ValidationError( u'%s no es un archivo válido.' % extension )
        else:
            return docfile