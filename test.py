mystr = "['bing', 'bong']"
mylist = mystr.strip('[]').split(', ')
mylist = [i.strip("''") for i in mylist]
for a in mylist:
    print(a)

mydict = {'name': 'Joseph',
          'pronoun': 'He/He',
          'thing': 'spoon'}
with open('test.txt','w') as f:
    f.write(str(mydict))
