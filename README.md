# Todo-App

### Live demo of App

#### [Todo-App-Demo](https://todo-app-mayank2107.vercel.app/)

### To run this project locally:

``` bash
git clone https://github.com/Mayankkumar21/Todo-app.git
```
Ensure you have latest python and pip installed
``` pip
$ pip install flask
$ python -m pip install pymongo
```
Now your local is setup, time for database
MongoDB - 
1) Sign up at https://www.mongodb.com/
2) Create a cluster in any region for free
3) Create user and password for that cluster with admin access
4) Replace incoming connections to 0.0.0.0 (to allow access from all IPs)
5) Create database named "mydb" inside which a collection named todos
6) Replace your username and password in the MongoDB URI

Then just run to run the app in development mode.
```bash
$ python app.py
```
