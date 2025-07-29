class Criter():
    def __init__(self,name):
        print('A new critter is born.')
        self.name = name

    def __str__(self):
        rep = "Critter object\n"
        rep += f'Name: {self.name}'
        return rep
        
    def talk(self):
        print(f'Hi\n I am {self.name}.')
    
    def shout(self):
        print('Wooy\n I am shouting!!')

crit1 = Criter('Poppy')
crit1.talk()
print(crit1)

crit2 = Criter('Mimi')
crit2.shout()
print(crit2)



input('\nPress enter to exit')
