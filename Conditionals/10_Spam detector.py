#Buy now, Subscribe this, Rewards, click this. Write a Program to detect these spams in mail.

spam_keywords = ["Buy now", "Subscribe this", "Rewards", "click this"]
message = input("Enter the email message: ")
is_spam = any(keyword in message for keyword in spam_keywords)
if is_spam:
    print("This email is detected as spam.")
else:
    print("This email is not detected as spam.  ")

    

