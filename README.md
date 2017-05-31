# Babel - localization tests

Testing babel flask integration

## Stack
Babel is a simple `Flask` application


## Installation

```
mkvirtualenv venv
pip install -r requirements.txt
cd babel
python manage.py runserver  # Run Babel
```

## Updating list of strings to translate
``
source venv/bin/activate
cd babel
pybabel extract -F babel.cfg -o messages.pot application
``

## Generating a language catalog
``
source venv/bin/activate
cd babel
pybabel init -i messages.pot -d application/translations -l pt
``

## Updating the .mo files
``
source venv/bin/activate
cd babel
pybabel compile -d application/translations
``
