
#def ch(choice):
    #if choice == 'me':
     #   return 1
    #elif choice == 'you':
   #     return 2
  #  elif choice == 'them':
 #       return 3
#print(ch('them'))

#def bh(numb):
    #if numb == 1:
     #   return 'me'
    #elif numb == 2:
   #     return 'you'
  #  elif numb == 3:
 #       return 'them'
#print(bh(2))

#by using dictionaries
def ch(choice):

    return{'me':1 , 'you':2, 'them':3}[choice]
print(ch('them'))


def bh (numb):
    return{1:'me', 2:'you', 3:'them'}[numb]
print(bh(2))