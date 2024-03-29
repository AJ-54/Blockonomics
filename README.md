# Blockonomics Django Demo 

This Demo uses Blockonomics Payment API - https://www.blockonomics.co/views/api.html#payments. 
The Demo is hosted at https://blockonomics.herokuapp.com

## How to SetUp

* `git clone https://github.com/AJ-54/Blockonomics.git`
* Install packages via `pip install -r requirements.txt`
* Create your Blockonomics Account- [here](https://www.blockonomics.co/merchants?ref=hPga3rGcrDj45w1C2jzkDMUPGBkCRYxNE6)
* Login to blockonomics account and visit https://www.blockonomics.co/merchants#/page3
* Provide your HTTP Callback URL, in my case which is https://blockonomics.herokuapp.com/payments/receive and also note your API Key.
* Inside Blockonomics folder, go to settings.py file and place your blockonomics API KEY to the API_KEY variable  
* `python manage.py migrate`
* `python manage.py runserver`

Note that Python 3.6 or higher version is required to run the project

## Tech Stack

* Python
* Django
* HTML
* CSS
* Boostrap
* JavaScript
