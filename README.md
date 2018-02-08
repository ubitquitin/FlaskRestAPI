# FlaskRestAPI
==========================================
README FOR REST API RESTAURANT EXAMPLE USING PYTHON AND FLASK

Author: ROHAN KHOPKAR (khopkar.rohan@gmail.com)
==========================================

1. Overview

   The REST API sample has been developed using Python, Python Flask and Python Flask Cache. 
   This allows for easy install and speedy flexible development using python. 
   MySQL has been used as the backend repository and all db calls are
   abstracted into DatabaseManager class which can be easily replaced with any
   other DB if needed. All REST microservices are in restaurant.py
   All REST calls return JSON where applicable. For brevity xml is 
   currently not supported. This application has been deployed on AWS cloud.
   
   Server URL: http://ec2-13-58-211-147.us-east-2.compute.amazonaws.com:5000/

2. Resources used

   a) AWS RHEL ec2 instance
   b) MYSQL DB on ec2 instance
   c) Python Flask Microframework

3. How to install ?

   a) sudo yum install python-pip ==> Installs python package manager (More info => https://www.liquidweb.com/kb/how-to-install-pip-on-centos-7/)

   b) sudo pip install flask ==> Installs Python Flask (More info ==> http://flask.pocoo.org/docs/0.12/installation/)
   
   c) sudo pip install Flask-caching ==> Installs Python Flask Cache 
   
   d) Create a dir flask in your $HOME and copy attached files 
      i)   restaurants.py 
      ii)  databasemanager.py
      iii) RestData.sql
      iv)  unittests.sh
      v)   unittests.log

   e) On MySQL server create a database schema "RestData" and run the attached script RestData.sql to create necessary tables.
      If running unittests.sh, schema will be automatically created.

4. How to run ?

   a) cd $HOME/flask

      Edit databasemanager.py and change the following credentials for MySQL
      to your MySQL credentials 

      MYSQLSERVER = "localhost"
      MYSQLUSER = "ec2_user"
      MYSQLPASS = "Toragpwns96"
     
   b) chmod +x unittests.py
      chmod +x restaurant.py
      
      ./restaurant.py 
      * Running on http://ec2-13-58-211-147.us-east-2.compute.amazonaws.com:5000/ (Press CTRL+C to quit)

   c) From another terminal session, run the unit tests as follows

      ./unittests.sh

      Correct output from unit tests should match the provided file unittests.log.
      
5. Additional Comments 
    a.) Why Python Flask?
          Here are some good features of Flask, based on my experience of using it for a few personal projects:
            i.)The documentation and developer tools are excellent and OpenShift cloud has build-in support for it with free accounts
            ii.) The Flask "core" is simple, but there are a large number of extentions which integrate with it very well.
            iii.) Flask is actively maintained and developed
            iv.) Scalability, Simplicity and useful Python libraries
            v.) Extensive documentation :)
    b.) Database concerns
            i.) Flash-caching was used to implement server side caching on GET operations.
            ii.) Cache clearing was implemented for POST and DELETE operations.
            iii.) For scalability, database load balancing software would be implemented.
  

Thats all folks !! 
