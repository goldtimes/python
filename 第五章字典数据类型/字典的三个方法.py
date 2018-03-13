spam = {'color':'red','age':42}
print(spam.keys())
print(spam.values())
print(spam.items())
for k,v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))