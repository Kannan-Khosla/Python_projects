#In this game we will focus on creating a simple painting application using pygame. This program will allow the user to move a 
#paintbrush inside of a window and leave a trail of color. We can change the color by pressing on specific keys, in particular we can press B to change 
#the color trail to blue, G to change the color trail to green, R to change the color trail to red, and Y to change the color trail to yellow. 
#We will also set the spacebar to change to the color trail to black so that it could be used as an eraser for our program. 
#The movement of the paintbrush will be done using the arrow keys.

import pygame #importing pygame.


# User-defined functions

def main():
    # initialize all pygame modules (some need initialization)
    pygame.init()
    # create a pygame display window
    pygame.display.set_mode((500, 400))
    # set the title of the display window
    pygame.display.set_caption('Painting')
    # get the display surface
    w_surface = pygame.display.get_surface()
    # create a game object
    game = Game(w_surface)
    # start the main game loop by calling the play method on the game object
    game.play()
    # quit pygame and clean up the pygame window
    pygame.quit()

# creating a game class for game specific objects

class Game:
   
    def __init__(self, surface):
        # Initialize a Game.
        # - self is the Game to initialize
        # - surface is the display window surface object

        # === objects that are part of every game that we will discuss
        self.surface = surface
        self.bg_color = pygame.Color('black')

        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True

        # === game specific objects
        color='red'
        self.paintbrush_left=245
        self.paintbrush_right=195
        self.paintbrush_width=10
        self.paintbrush_height=10
        self.paintbrush_initial_velocity=[0,0]
        self.paintbrush_velocity=[1,1]
        self.paintbrush=Paintbrush(color,self.paintbrush_left,self.paintbrush_right,self.paintbrush_width,self.paintbrush_height,self.paintbrush_velocity,self.surface)
        self.max_frames = 150
        
        self.frame_counter = 0
        
        # in beginning no key is being pressed
        self.UP_down= False  
        self.DOWN_down= False
        self.LEFT_down= False
        self.RIGHT_down= False
    
        

    def play(self):
        # Play the game until the player presses the close box.
        # - self is the Game that should be continued or not.

        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_events()
            self.draw()
            self.update()
            self.game_Clock.tick(self.FPS)  # run at most with FPS Frames Per Second

    def handle_events(self):
        # Handle each user event by changing the game state appropriately.
        # - self is the Game whose events will be handled

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True
            if event.type == pygame.KEYDOWN:
                self.change_color(event)
    # =====================================================================================================================================        
            if event.type== pygame.KEYDOWN:  #using keyboard key events when key is pressed down key.down is true and key.UP is false and vice-versa
        
                if event.key == pygame.K_UP:
                    self.UP_down= True          
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_UP:
                    self.UP_down=False
    # =====================================================================================================================================           
            if event.type== pygame.KEYDOWN:        
                if event.key == pygame.K_DOWN:
                    self.DOWN_down= True
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_DOWN:
                    self.DOWN_down=False
    # =====================================================================================================================================          
            if event.type== pygame.KEYDOWN:
        
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_down= True
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    self.RIGHT_down=False
    # =====================================================================================================================================  
            if event.type== pygame.KEYDOWN:        
                if event.key == pygame.K_LEFT:
                    self.LEFT_down= True
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    self.LEFT_down=False                    
    # =====================================================================================================================================                        
    def handle_keydown(self,event):
        if event.key == pygame.K_UP:       #for Upward
            Paintbrush.set_top(Paintbrush.get_top()+self.paintbrush_velocity[1])
        if event.key == pygame.K_DOWN:   #for downward
            Paintbrush.set_top(Paintbrush.get_top()-self.paintbrush_velocity[1])
              
    
        if event.key == pygame.K_LEFT: #for left
            Paintbrush.set_top(Paintbrush.get_top()+self.paintbrush_velocity[0])
        if event.key == pygame.K_RIGHT:  #for right
            Paintbrush.set_top(Paintbrush.get_top()-self.paintbrush_velocity[0])
                      
        
        
    
    
    
    
    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw

        self.paintbrush.draw()
        pygame.display.update()  # make the updated surface appear on the display

    def update(self):
        #movemnet of brushes  
        if self.UP_down: # for Upward movement
            if self.paintbrush.get_brush().top-self.paintbrush_velocity[1]>0 : 
                self.paintbrush.set_top(self.paintbrush.get_top()-self.paintbrush_velocity[1])   
        if self.DOWN_down:# for lower movement
            if self.paintbrush.get_brush().bottom+self.paintbrush_velocity[1]<self.surface.get_height():
                self.paintbrush.set_top(self.paintbrush.get_top()+self.paintbrush_velocity[1])              
        
        if self.LEFT_down: #for right movement
            if self.paintbrush.get_brush().left-self.paintbrush_velocity[1]>0 :
                self.paintbrush.set_left(self.paintbrush.get_left()-self.paintbrush_velocity[1])   
    
        if self.RIGHT_down: #for left movement
            if self.paintbrush.get_brush().left+self.paintbrush_velocity[1]<self.surface.get_width():
                self.paintbrush.set_left(self.paintbrush.get_left()+self.paintbrush_velocity[1])             
        

    def change_color(self, event): #changing color of the brush

        
        
        if event.key == pygame.K_b:
            self.paintbrush.set_color('blue') #Key B for blue
        if event.key == pygame.K_g:
            self.paintbrush.set_color('green')     #Key G for green
        if event.key == pygame.K_r:
            self.paintbrush.set_color('red')     #Key R for Red       
        if event.key == pygame.K_y:
            self.paintbrush.set_color('yellow') #Key Y for yellow
        if event.key == pygame.K_SPACE:
            self.paintbrush.set_color('black') #Key space for black or to erase

    


class Paintbrush: # this class has all the properties linked to paintbrush 
    
    def __init__(self,color,  left ,top, width, height,  velocity, surface):
        # Initializing a Paintbrush

        self.color = pygame.Color(color)
        self.left=left
        self.top=top
        self.width=width
        self.height=height
        self.velocity = velocity
        self.surface = surface


    def set_top(self,new_top): #changinf the value of the top 
        self.top=new_top
     
     
    def set_left(self,new_left): #changing the value of left
        self.left=new_left
     
    def get_top(self):   #returning thr value of top
        return self.top
    
    def get_left(self): # returning the value of left
        return self.left
    
    def set_color(self, color):   
        # Changes the color of the paint
    
        self.color = pygame.Color(color)

    def draw(self): #drawing brush

        self.brush_params = pygame.Rect(self.left, self.top, self.width, self.height)
        pygame.draw.rect(self.surface, self.color, self.brush_params)
        
        
        
    def get_brush(self): #returns the parameters of brush
        return self.brush_params

main()

