. ./venv/bin/activate

find . -type d -name '__pycache__' -delete
find . -type f -name '*.py[co]' -delete

alias dev="SETTINGS=app.settings.development python3 tasks.py"
alias prod="SETTINGS=secure.production python3 tasks.py"
