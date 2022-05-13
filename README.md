# Fruit Vending

## Author 
Built by: [Timothy Mugendi](https://github.com/Timoh97)

# Description
This is an online fruit vending site

#### Prerequisites 
* python3.8
* pip
* Flask

## User Story
* Sign in to the application to start using.
* See your profile.
* Search for different users fruits their usernames.
* order fruits
* Leave a comment on comment box.

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the application | On application load | Display of Login Form |
| Create account by Sign Up | Enter email, username and password| Redirect to login|
| Login selected | Enter username and password you signed up with| Redirect to home page|
| Post remark/complaint button selected | Post | Input details in a form and upload |
| Click the other buttons on navbar | CLick | Redirected to page wih all the comments made on the post |
| Click the user profile icon | Select Profile | Redirected to profile page where you can edit profile |
| Click the user profile icon | Select Logout | Logout and redirected to login page |

# Setup and Installation
#### Cloning the repository
* Open Terminal:
```bash
        $ https://github.com/Timoh97/FruitVending.git
        $ cd FruitVending
        $ code . or atom . based on your text editor 
```
* Navigate into the folder, install and activate virtual environment
```bash
      $ python -m venv virtual

      $ source virtual/bin/acivate
```
* Install all dependencies in requirements.txt
```bash
      $ pip install -r requirements.txt
```
#### Setup the Database
* Setup the database username, password, host then make migrations  
```bash
      $ flask db init
 
```
* Run migrations
```bash
      $ flask db migrate -m"commit message"
```
```bash
      $ flask db upgrade  
      
      (each time the database models change repeat the migrate and upgrade commands.)
```
```bash
      $ flask db --help   
      
      (to see all commands )
```
### Running the Application
* To run the application, open the cloned repo in terminal and run the following commands:
```bash
      $ python3.8 manage.py runserver
```
### Testing the Application       
* To run unittests for the class application and check if it functions well:
```bash
      $ python3 manage.py test ---
```
## Known Bugs
* No known bugs so far, incase a bug is spotted pull requests are allowed.


## Technologies Used
* markdown

* flask-bootstrap4 - for bootstrap version 4

* Heroku - online deployment


## Support and contact details
Incase of any issues at hand, please email me at timohmugendi@gmail.com
## Preview

### License
<a href='https://github.com/Timoh97/FruitVending/blob/master/LICENSE'>MIT LICENSE</a>
 [**TIMOTHY MUGENDI**]