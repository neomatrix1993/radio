Make sure you have python3:
  If not install it using 'brew install python3'
 

For ubuntu you can install the basic things:

```
sudo apt-get install python3.5 python3-dev libmysqlclient-dev
```

Create a virtual environment to work on

```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```
