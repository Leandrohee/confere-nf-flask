# CREATING API WITH FLASK AND VERCEL

1. Create the venv folder and start it.
    
```bash
python3 -m venv venv
source venv/bin/activate
```
    
2. Install the flask dependencies
    
```bash
pip install flask
```
    
3. Create requiremetns.txt
    
```bash
pip freeze > requirements.txt
```
    

4. Create an file app.py on root folder, and start flask
    
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flas on Vercel!"

if (__name__ == "__main__"):
    app.run()
```

# SETTING UP THE PROJECT TO WORK WITH VERCEL

1. Install vercel cli globally

```
```
