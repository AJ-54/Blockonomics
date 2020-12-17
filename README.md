# Blockonomics Django Demo 

This Demo uses Blockonomics Payment API - https://www.blockonomics.co/views/api.html#payments. 
The Demo is hosted at https://blockonomics.herokuapp.com

## How to SetUp

* `git clone https://github.com/AJ-54/Blockonomics.git`
* Install packages via `pip install -r requirements.txt`
* Login to blockonomics account and visit https://www.blockonomics.co/merchants#/page3
* Inside Blockonomics folder, go to settings.py file and place your blockonomics API KEY to the API_KEY variable
* Also provide your HTTP Callback URL, in my case which is https://blockonomics.herokuapp.com/payments/receive  
* `python manage.py migrate`
* `python manage.py runserver`

## Tech Stack

* Python
* Django
* HTML
* CSS
* Boostrap
* JavaScript
