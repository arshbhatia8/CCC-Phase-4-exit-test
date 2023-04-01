def processLogs(logs, threshold):
    # Write your code here
    
    
    # Create a dictionary to count the number of transactions for each user
    user_count = {}
    for log in logs:
        sender, recipient, amount = log.split()
        user_count[sender] = user_count.get(sender, 0) + 1
        if sender != recipient:
            user_count[recipient] = user_count.get(recipient, 0) + 1
    
    # Find the suspicious users who have at least threshold transactions
    suspicious_users = []
    for user, count in user_count.items():
        if count >= threshold:
            suspicious_users.append(user)
    

    return sorted(suspicious_users, key=int)
