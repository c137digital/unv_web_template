. ./venv/bin/activate

find . -type d -name '__pycache__' -delete
find . -type f -name '*.py[co]' -delete

alias dev="python3 fabfile.py dev"
alias prod="python3 fabfile.py prod"
