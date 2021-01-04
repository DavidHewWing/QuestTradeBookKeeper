# QuestTradeBookKeeper
A personal automated book keeper for keeping track of how well your portfolio is doing. 

Right now will only work for one account. 

Used GCP (Cloud Functions, Cloud Scheduler, Google Sheets API), QuestTrade API and Python.

Python Version: 3.7.4

## Running the Script
1. Update an .env:
QT_API_KEY="consumer_key for personal app in questrade"
2. 
```
python3 -m venv packages
source packages/bin/activate
pip3 install -r requirements.txt
```

## Adding Packages
```
pip freeze > requirements.txt
```
