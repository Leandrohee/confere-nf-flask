# CREATING API WITH FLASK USING PIPENV

1. Install pipenv globally using (only if you dont have):

```bash
brew install pipenv
```

2. Create the virtual enviroment with pipenv:

```bash
pipenv install
```

It will generate 2 files
- Pipfile: similar to package.json
- Pipfile.lock : similtar to yarn.lock

3. Running Your Application in the Virtual Environment and deactivating

```bash
pipenv shell
exit
```

4. Installing dependencias
```bash
pipenv install flask
```

It automaticly includes the flask in the Pipfile and the Pipfile.lock

5. To see where the depenndencias are store type:

```bash
pipenv --venv
```

# CREATING API WITH FLASK USING PIP

1. Create the venv folder and start it.
    
```bash
python3 -m venv venv
source venv/bin/activate
```

    1.1. To exit the venv type:

    ```bash
    deactivate
    ```
    
2. Install the flask dependencies
    
```bash
pip install flask
```
    
3. Create requiremetns.txt
    
```bash
pip freeze > requirements.txt
```

    3.1. If you delete the venv folder you can reinstall all the packages with:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
    

4. Create an file app.py on root folder, and start flask
    
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {
        "success": "true",
        "msg": "Hello, Flas on Vercel!"
    }


if (__name__ == "__main__"):
    app.run()
```

# SETTING UP THE PROJECT TO WORK WITH VERCEL

1. Install Vercel CLI globally
    
```bash
npm install -g vercel
```
    

2. Create a **vercel.json** file in the root folder in the flask project
    
```json
{
    "version": 2,
    "builds": [
        {
        "src": "app.py",
        "use": "@vercel/python"
        }
    ],
    "routes": [
        {
        "src": "/(.*)",
        "dest": "app.py"
        }
    ]
    }
    
```
    

3. In vercel linked with you github import the project related
    - **Project Name**: same as github repository
    - **Framework Preset:** Other
    - **Root Directory:** ./


# Run your code

```bash
python3 app.py
```