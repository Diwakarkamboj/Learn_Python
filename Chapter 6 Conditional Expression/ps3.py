spam_comment = input("Enter the comment to check if it is spam")

# if(spam_comment == "make a lot of money"):
#     print("This comment is spam")
# elif(spam_comment == "buy now"):
#     print("This comment is spam")
# elif(spam_comment == "subscribe this"):
#     print("This comment is spam")
# elif(spam_comment == "click this"):
#     print("This comment is spam")
# else:
#     print("This comment is not spam")

if(spam_comment == "make a lot of money" or spam_comment == "buy now" or  spam_comment == "subscribe this" or spam_comment == "click this"):
     print("This comment is spam")
else:
    print("This comment is not spam")