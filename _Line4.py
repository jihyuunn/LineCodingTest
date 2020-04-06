def solution(snapshots, transactions):
    answer = []
    transId = [False]*100001
    accounts = {}
    for i in snapshots:
        accounts[i[0]] = int(i[1])
    print(accounts)
    for transaction in transactions:
        idn, action, account, amount = transaction
        if transId[int(idn)] == False:
            transId[int(idn)] = True
            if account not in accounts:
                if action == 'SAVE':
                    accounts[account] = int(amount)
                elif action == 'WITHDRAW':
                    accounts[account] = -int(amount)
            else:
                if action == 'SAVE':
                    accounts[account] += int(amount)
                elif action == 'WITHDRAW':
                    accounts[account] -= int(amount)
    answer = [[a,str(b)] for a,b in accounts.items()]
    print(answer)
    return 

snapshots = [["ACCOUNT1", "100"], ["ACCOUNT2", "150"]]
transactions = [["1", "SAVE", "ACCOUNT2", "100"],["2", "WITHDRAW", "ACCOUNT1", "50"], ["1", "SAVE", "ACCOUNT2", "100"], ["4", "SAVE", "ACCOUNT3", "500"], ["3", "WITHDRAW", "ACCOUNT2", "30"]]
solution(snapshots, transactions)