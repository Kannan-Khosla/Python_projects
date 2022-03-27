#This represents a race game between 2 players in which a 13 '-' long track is defined in which
                                                                                   #movement of players is decided by the number they get on rolling a dice







import random #importing random for random numbers on a dice throw.






class Player: #A player class is defined so that all the characteristics and details regarding both the players can be initiated using it.
    def __init__(self, name):#initializing
        self.name=name #player name can be o or x
        self.player_position=0 #this indicates that players are on the starting position
        self.track_length=12 #there are 12 '-' in which the race will be held
        self.track=[self.name] #it is a list whose firt element is the player's name that is o or x
        for i in range(0,12):
            self.track.append(' - ') #adding 12 '_' in the self.track list

    #a random number is generated using a dice
    def dice_roll(self): # a dice is rolled
        number=random.randint(1,6)
        print(f'Player{self.name} rolled {number}')
        print('*' * 40)
        return number #returns a random number coming on die

    # defines the movemnet of the player
    def movement(self, new_position):
        self.player_position = new_position # represents new positionof the player after movement
        self.track[self.track.index(self.name)] = ' - ' #player name replaces '-' during the movement
        self.track[new_position]=self.name #new position is aquired by the player name

    # conditions for the movement 
    def update_movement(self, number_rolled):
        next_position = self.player_position+number_rolled #gives the next position according the number obtained on dice roll
        if next_position> self.track_length: #if last number obtained is greater than the number required; the player fill be sent to the first position
            self.movement(0)
        elif next_position<self.track_length: # if number obtained is less than the track end ; player will move to the next position
            self.movement(next_position)
        elif next_position==self.track_length:# if number obtained is equal to the track length; player will move ahead
            self.movement(next_position)
            
            
            
            
    # it defines the termination of the game
    def continue_game(self):
        if self.player_position==self.track_length: # if player's track position is equal to track length player has won
            print('*' * 40)
            print('Player', self.name, 'has won!')
            exit()

    def display(self):
        print('Player'+self.name+':',''.join(self.track))

#end of the player class


# some  game related user defined functions



#it defines the initial position of the players
def starting_position(x,o): #x and o are the player names represneting player 1 and player2 
    print('Players begin in the starting position')
    print('*' * 50)
    x.display() #will display the name and track of player 1 that is x 
    o.display() #will display the name and track of player 2 that is o
    
    
    
    
    

def game_loop(x,o):
    #this game loop will iterate until a player wins

    continue_game=True
    while continue_game:
       #for player x
        print('*' * 40)
        input('Player x press enter to roll! ')
        x.update_movement(x.dice_roll()) #updating players movemnet according to dice roll
        x.display()   #display credentials for player 1 that is x
        o.display()   #display credentials for player 2 that is o
        x.continue_game() #if players 1 wins the game continue game is false and it terminates the loop

        #for player o
        print('*' * 40)
        input('Player o press enter to roll! ')
        o.movement(o.dice_roll()) #updating players movemnet according to dice roll
        x.display() #display credentials for player 1 that is x
        o.display()#display credentials for player 2 that is o
        o.continue_game() #if players 2 wins the game continue game is false and it terminates the loop
        

def main():
    
    # creating players x and o using player class
    x=Player(' x ') 
    o=Player(' o ')
    starting_position(x,o) 
    game_loop(x,o) 


        
main()

