alphabet='abcdefghijklmnopqrstuvwxyz'
key=4
newmsg = ''
message=input('enter new message  ')

for character in message :

    position = alphabet.find(character)
    newposition = (position+key) % 26
    newchar = alphabet[newposition]
    print('encrypted value is ',newchar)
    newmsg+=newchar
print('encrypted msg is ', newmsg)


