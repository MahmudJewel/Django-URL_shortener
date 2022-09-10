This is a URL-Shortener App where user/anonymous user can convert long url to short url.
# Requirements ==> 
The project will have following features-
* Given a URL, your service should generate a shorter and unique alias
of it.
* This link should be short enough to be easily copied and pasted into
applications.
* When users access a short link, our service should
redirect them to the original link.
* Users should optionally be able to pick a custom short link for their
URL.
* Links will expire after a standard default timespan. Users should
be able to specify the expiration time.
* Shortened links should not be predictable.
* Full-fledged registration and login system
* Proper validation for each form
* Option for private URL
* Basic statistics
* Basic Admin Panel

N.B: Application can be used both in logged in or guest users. But for using the full
potential features, you should be logged in.
## API
This project will have two basic API endpoints to create and retrieve shortened
links. Standard token-based authentication system needs to be implemented
here.

# Developed API
| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *POST* | ```/jwt/create/``` | _Login user_| _All users_|
| *POST* | ```/jwt/refresh/``` | _Refresh the access token_|_All users_|
| *POST* | ```/jwt/verify/``` | _Verify the validity of a token_|_All users_|
| *POST* | ```/api/create/``` | _Create new short urls_|_Allow any_|
| *GET* | ```/api/list/``` | _List all urls_|_Adminuser_|

# Tools
### Back-end
#### Language:
	Python (3.9.0)

#### Frameworks:
	Django(4.1.1)
	django rest framework (3.13.1 )
	
#### Other libraries / tools:
	asgiref                       3.5.2
	autopep8                      1.7.0
	certifi                       2022.6.15
	cffi                          1.15.1
	charset-normalizer            2.1.1
	coreapi                       2.3.3
	coreschema                    0.0.4
	cryptography                  38.0.1
	defusedxml                    0.7.1
	django-templated-mail         1.1.1
	django-widget-tweaks          1.4.12
	djangorestframework-jwt       1.11.0
	djangorestframework-simplejwt 5.2.0
	djoser                        2.1.0
	gunicorn                      20.1.0
	idna                          3.3
	itypes                        1.2.0
	Jinja2                        3.1.2
	MarkupSafe                    2.1.1
	oauthlib                      3.2.0
	pip                           20.2.3
	pycodestyle                   2.9.1
	pycparser                     2.21
	PyJWT                         1.7.1
	python3-openid                3.2.0
	pytz                          2022.2.1
	requests                      2.28.1
	requests-oauthlib             1.3.1
	setuptools                    49.2.1
	six                           1.16.0
	social-auth-app-django        4.0.0
	social-auth-core              4.3.0
	sqlparse                      0.4.2
	toml                          0.10.2
	uritemplate                   4.1.1
	urllib3                       1.26.12
	whitenoise                    6.2.0

### Front-end
####  Frameworks:
	Bootstrap
	
### Database:
	SQLite3

# Setup
The first thing to do is to clone the repository:
```sh
$ https://github.com/MahmudJewel/Django-URL_shortener
```
### Back-end
Create a virtual environment to install dependencies in and activate it:
```sh
$ cd Django-URL_shortener
$ python -m venv venv
$ source venv/bin/activate
```
Then install the dependencies:
```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python manage.py migrate
(venv)$ python manage.py runserver 8000
```

# Screenshot
### Custom Short URL Genaration:
![Custom Short URL Genaration](https://github.com/MahmudJewel/Django-URL_shortener/blob/dev/screenshot/shorturl-custom%20url.jpg)

### Home page for Guest User
![Home page for Guest User](https://github.com/MahmudJewel/Django-URL_shortener/blob/dev/screenshot/shorturl-1.jpg)

### Home page for Authenticated User
![Home page for Authenticated User](https://github.com/MahmudJewel/Django-URL_shortener/blob/dev/screenshot/shorturl-2.jpg)

### User Dashboard
![User Dashboard](https://github.com/MahmudJewel/Django-URL_shortener/blob/dev/screenshot/shorturl-3.jpg)


### Admin Dashborad
![Admin Dashborad](https://github.com/MahmudJewel/Django-URL_shortener/blob/dev/screenshot/shorurl-4.jpg)

### Sign-Up Page
![Sign-Up Page](https://github.com/MahmudJewel/Django-URL_shortener/blob/dev/screenshot/shorturl-signup.jpg)

### Login Page
![Login Page](https://github.com/MahmudJewel/Django-URL_shortener/blob/dev/screenshot/shorturl-login.jpg)

