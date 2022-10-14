# Blogga
This is a blog being built by Team 6 JustProjects. [View Live Project Here](https://blogga-team6.netlify.app/).  
[Figma Board Here](https://www.figma.com/file/55YRkKLgPcHzerXFOV8b7M/Multi-Author-Blog?node-id=494%3A3950)

## Follow these commands to run the proect on your local machine :
## Feel free to create a README.md in all folders if you need to
Clone the project 
```
git clone https://github.com/jegedenifemi/Team6-Blog.git
```

Enter the project directory 

```
cd Team6-Blog
```

Create a virtual env

```
python -m venv env 
```

Activate your env(for windows)

```
./env/Scripts/activate 	 
```
(for linux or mac)

```
source env/bin/activate 
``` 


# PIP install the requirements.txt file to install project dependencies by
```
pip install -r requirements.txt
```

## To run the server you include 'django_extensions' as an app in the settings.py file in blog folder if it isn't already there
### make sure to generate a secret key named DJANGO_SECRET_KEY by using the command `python manage.py generate_secret_key`
### create a .env file and  in it:
```
DJANGO_SECRET_KEY = 'secret key that was generated'
``` 
## After this you can run the server to check if it was configured correctly 
by running
```
python manage.py makemigrations
python manage.py migrate
``` 
``` 
python manage.py runserver
```

## To contribute :

### NOTE :
# Please do not push your virtual environment folder, add the name to the .gitignore file
# Don't push to the main branch
- Create a branch and switch to it ` git checkout -b (branchname)` *Don't include brackets*
- After finishing your tasks run 
# git pull origin main  
then 


```
git add .
git commit -m " The task you did, please make your commit messages descriptive "
```
# git push (your branchname)

