# CS122 Deliverable 3 - Pixie Dust Website
### Installing the code and running the website locally
1. Download Python 3.6 (https://www.python.org/downloads/)
2. Open command line and enter `pip install django==1.8`
3. Download MySQLClient (https://pypi.python.org/pypi/mysqlclient). Enter `pip install {MySQLClient file name here}`
4. Open another command line for MYSQL inside `CS122Del3/other files` and enter
     * `CREATE DATABASE del3db;`
5. Change cmd directory to `CS122Del3/del3` and enter
     * `python manage.py migrate auth`
     * `python manage.py migrate sessions`
     * `python manage.py migrate admin`
     * `python manage.py createsuperuser` (any username except jude, nikki, jayce, or kemp)
6. Back to MYSQL (still in other files folder), enter
     * `SOURCE setup.sql;`
     * `SOURCE populate.sql;`
6. Finally, run `python manage.py runserver` (still in CS122Del3/del3)
7. To reset the database, run `python manage.py flush`, and do step 6 again
### Steps for connecting to PythonAnywhere
Link - Quillot.pythonanywhere.com

Run git pull, and then source django/bin/activate

source /home/Quillot/CS122Del3/other files/setupweb.sql;
1. Fix code section.
    * Source code: /home/Quillot/CS122Del3/del3/del3
    * Working directory: /home/Quillot
    * Python Version: 3.6
2. Set virtual environment
    * /home/Quillot/django
3. Configure WSGI file
    * path: /home/Quillot/CS122Del3/del3
    * django settings module: del3.settings
4. Configure settings.py template folder
    * Dirs: /home/Quillot/CS122Del3/del3/del3/templates
5. Configure settings.py database connection
    * Name: Quillot$databasename
    * Host: Quillot.mysql.pythonanywhere-services.com

### Setting up on pixiedust.pythonanywhere.com for deployment
1. Using bash, enter `git clone {repo url}`
2. Create a database named `pixiedustdb`
3. Make a virtual environment, follow https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/
4. In the venv, run `pip install django==1.8`, and `pip install mysqlclient`
5. Go to web > add a new web app. Choose manual configuration with python 3.6
6. Under Virtualenv, enter `/home/pixiedust/.virtualenvs/django`
7. Under code, enter into:
    * Source code: `/home/pixiedust/CS122Del3/del3/del3`
8. Configure the WSGI file
9. Migrate auth first, then just migrate
10. source /home/pixiedust/CS122Del3/setupweb.sql;
11. Set up static `/static/` and `/home/pixiedust/CS122Del3/del3/del3/static`

