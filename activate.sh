. ./venv/bin/activate

find . -type f -name '*.py[co]' -delete
find . -type d -name '__pycache__' -delete

alias dev="SETTINGS=app.settings.development python3 tasks.py"
alias prod="SETTINGS=secure.production python3 tasks.py"
