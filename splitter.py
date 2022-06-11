import json

with open("accounts.json", "r") as f:
    accounts = json.load(f)

def checkForDuplicates():
    duplicates = []
    for account in accounts:
        if accounts.count(account) > 1:
            duplicates.append(account)
    print(f"There are {len(duplicates)} duplicates!")

def removeDuplicates():
    for account in accounts:
        if accounts.count(account) > 1:
            accounts.remove(account)

def splitAccounts():
    count = int(input("How many accounts per file? "))
    for i in range(0, len(accounts), count):
        with open(f"accounts{i}.json", "w") as f:
            json.dump(accounts[i:i+count], f, indent=4)

checkForDuplicates()
removeDuplicates()
splitAccounts()
