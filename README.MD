

##Good health blog is  application where users subscribe to our post and reviews on health issue
### september, 20TH,  2018
#### By **[GABRIEL NWACHUKWU](https://github.com/gabrielcoder247)**

## Description
#fill the form to subscribe then you will be notified on your subscription and upcoming article 


## Specifications
Get the specs [here](https://github.com/gabrielcoder247/health-blog/blob/master/SPECS.md)

## Set-up and Installation

### Prerequiites
    - Python 3.6
    - Ubuntu software

### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/gabrielcoder247/health-blog  && cd PitchIt on your machine terminal`

Install [Postgres](https://www.postgresql.org/download/)

### Create a Virtual Environment
Run the following commands in the same terminal:
`sudo apt-get install python3.6-venv`
`python3.6 -m venv virtual`
`source virtual/bin/activate, to activate the virtual environment`

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements`

### Prepare environment variables
```bash
export DATABASE_URL='postgresql+psycopg2://username:password@localhosthealthblog
export SECRET_KEY='Your secret key'
```

### Run Database Migrations
```
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
```

### Running the app in development
In the same terminal type:
`python3 manage.py server`

Open the browser on `http://localhost:5000/`

## Known bugs
SQLAlchemy errors, automatic sign out has a short time span

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

## Support and contact details
Contact me on gabrielcoder@gmail.com for any comments, reviews or advice.

### License
Copyright (c) **Gabriel Nwachukwu**