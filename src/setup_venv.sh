# to use: `source setup_venv.sh`
# if using vscode, set Python interpreter to `src/nodex-venv/bin/python3.10`

set -e # stops script on error

python3 -m venv nodex-venv

source nodex-venv/bin/activate
# use `deactivate` to leave the virtual environment

pip3 install -r requirements.txt