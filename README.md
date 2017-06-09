The objectives of this task is to implement login and registration step for normal user and seller of Shopee.
The website was developed in python-flask.

To run the website, the developer should make sure that virtualenv installed and the dependencies has already updated. You can do it by executing:
sudo virtualenv venv
. venv/bin/activate
pip install -r requirements.txt

Having them set up, continue to execute the python program:
python bws.py

To open the website, please hit http://127.0.0.1:29000/.

What has already implemented in this project are following:
1. User Login
Users should type their username and password. 
If the system finds the user in the database and matches the given password, it will forward the user to the seller registration page.
If the password is wrong, the system will show an error message.
If the system does not find the user. it would display an error message with registration link.

2. Normal User Registration
Users should input their email, username, and password. After that, the system will put it into a database.



Unfortunately, form validation and seller registration have not yet implemented.

The screenshot of working web system has already added as screenshot.zip.

Thank you.
