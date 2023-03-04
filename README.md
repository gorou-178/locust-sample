## locust-sample

## Usage
set up python and locust
```shell
$ python3 -m venv venv
$ pip3.9 install -r requirements.txt
$ source venv/bin/activate
```

Prepare and start local API server
```shell
$ cd test
$ uvicorn server:app --reload
```

start locust UI 
```shell
$ cd src
$ locust -f locust-files/locust_todos_test.py --config locust-config/local.conf
# Access http://localhost:8089/ in your browser
```
