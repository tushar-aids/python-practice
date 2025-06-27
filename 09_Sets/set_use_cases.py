# 1. Removing duplicates from a list
emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com"]
unique_emails = list(set(emails))
print("Unique Emails:", unique_emails)

# 2. Finding common users (intersection)
followers_twitter = {"tushar", "amit", "neha", "rohit"}
followers_instagram = {"neha", "rohit", "priya"}

common_followers = followers_twitter.intersection(followers_instagram)
print("Common Followers:", common_followers)

# 3. Users who follow on only one platform (symmetric difference)
unique_followers = followers_twitter.symmetric_difference(followers_instagram)
print("Unique Followers (one platform only):", unique_followers)

# 4. Checking banned usernames
banned = {"admin", "null", "root"}
username = "admin"
if username in banned:
    print("Username is not allowed!")
else:
    print("Username is good to go.")



# output:
# Unique Emails: ['c@gmail.com', 'b@gmail.com', 'a@gmail.com']
# Common Followers: {'neha', 'rohit'}
# Unique Followers (one platform only): {'tushar', 'amit', 'priya'}
# Username is not allowed!
