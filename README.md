# mypy

## Setup Python Virtual Env

```
python3 -m venv myvenv
source myvenv/bin/activate
pip install --upgrade pip
pip install -r requirement.txt
```

## Updating Requriment File

```
source myvenv/bin/activate
pip install <new-package>
pip freeze > requirement.txt
```