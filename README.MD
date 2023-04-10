### introduction
the is todo app using flask and mmongodb
### setup


connect mongo db to the app with:
```sh
MongoClient = MongoClient('localhost', 27017)


```

### virtualenv


2- Install requirements

```sh
pip install -r requirements.txt
```
### Start the project

after the installation and running the mongoserver  server with (systemctl start mongod) run this command to run the app on localhost:5000
)
```bash
flask run
```
### Run the tests
for running the test write this commant in the terminal:
```bash
 pytest test.py
```

### Documentation
>The project architecture
```sh
.
├── static
├── templates
├── app.py
├── requirements.txt
├── test.py

```
### ScreenShots

the page:

<img
  src="/screenshots/Screenshot from 2023-04-10 05-04-57.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">
