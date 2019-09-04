python3 -m venv ./venv

. activate.sh

pip install --upgrade pip wheel
pip install -e .[dev]
