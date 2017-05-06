# CS122 Deliverable 3 - Pixie Dust Website
### Installing the code and running the website locally
1. Download Python 3.6 (https://www.python.org/downloads/)
2. Open command line and enter `pip install django==1.8`
4. Change directory to `CS122Del3/del3` and enter
     * `python manage.py migrate auth`
     * `python manage.py migrate sessions`
     * `python manage.py migrate admin`
     * `python manage.py createsuperuser` (any username except jude, nikki, jayce, or kemp)
5. Open another command line for MYSQL inside `CS122Del3/other files` and enter
     * `CREATE DATABASE del3db;`
     * `SOURCE setup.sql;`
     * `SOURCE populate.sql;`
6. Finally, run `python manage.py runserver`
7. To reset the database, drop the database, create it, and do step 5 again
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
