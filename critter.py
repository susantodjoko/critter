class Criter():
    def __init__(self):
        print('A new critter is born.')
   
        
    def talk(self):
        print('Hi\n I am instance of class Critter.')
    
    def shout(self):
        print('Wooy\n I am shouting!!')

crit1 = Criter()
crit2 = Criter()

crit1.talk()
crit2.shout()

print(crit1)
input('\nPress enter to exit')
