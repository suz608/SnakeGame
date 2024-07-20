# This program creates animation of the classic snake game
import random
from turtle import*

xys=[]
# xys is a list that stores the positions of the treats
neon_green=0,255,0
#sets a color
# treat function creates treats for the snake in random place
# number is the number of treats
# the function returns a list of treats, 
# otherwise, it would be impossible to control them outside the function
def treat(number):
    treats=['t']*number
    for i in range(number):
        x=random.randint(-300,300)
        y=random.randint(-300,300)
        # This parameter is based on the screensize
        xys.append([x,y])
        treats[i]+=str(i)
        treats[i]=Turtle('square')
        treats[i].color('pink','black')
        treats[i].penup()
        treats[i].goto(x,y)
    return treats

# snake function creates a snake
# snakeSize must be a positive integer under 10
# the function returns a list of snakes, 
# otherwise, it would be impossible to control them outside the function
def snake(snakeSize):
    snakes=['s']*snakeSize
    for i in range(snakeSize):
        snakes[i]+=str(i)
        snakes[i]=Turtle('square')
        snakes[i].color(neon_green,'black')
        snakes[i].penup()
        if i<5:
            dis=(i-1)*22
            snakes[i].fd(dis)
        elif i<10:
            snakes[i].fd(66)
            snakes[i].lt(90)
            dis=(i-4)*22
            snakes[i].fd(dis)
    return snakes

# This function receives a snake, and a position of one treat
# And drives the snake to eat the treat
def snakesEat(snakeList,treatpos):
    a=0
    while a<20:
        for i in range(len(snakeList)):
            dx=treatpos[0]
            dy=treatpos[1]-22*(i+1)
            spos=snakeList[i].pos()
            fdx=(dx-spos[0])/10
            fdy=(dy-spos[1])/10
            snakeList[i].goto(spos[0]+fdx,spos[1]+fdy)
        a+=1
    # The while loop creates a gradual movement. 
    # If deleted, the snake will still reach the treat with the for loop below,
    # but the movement will be finished instantly, in only one step.
    for i in range(len(snakeList)):
        dx=treatpos[0]
        dy=treatpos[1]-22*(i+1)
        snakeList[i].goto(dx,dy)

def main():
    while True:
        n1=input('How many treats do you want to set up for the snake?(Please enter a positive integer)) ')
        if n1.isnumeric():
            break
        else:
            print('Please enter a postive integer.')
    while True:
        n2=input('What is the snakes initial size?(Please enter an integer from 1 to 9)')
        if n2.isnumeric():
            if 0<int(n2)<10:
                break
            else:
                print('Invalid number. Try again.')
        else:
            print('Invalid input. Try again.')
    screensize(400,400)
    colormode(255)
    bgcolor('black')
    treats=treat(int(n1))
    snakes=snake(int(n2))
    for i in range(len(treats)):
        snakesEat(snakes,xys[i])
        treats[i].color(neon_green,'black')
        snakes.append(treats[i])
        # After the snake eats a treat, the treat becomes part of the snake
        # Its color changes to the same color as the snake
    mainloop()
main()