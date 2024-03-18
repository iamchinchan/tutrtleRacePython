import turtle as t
import random

screen = t.Screen()
screen.setup(width=700,height=500)
turtleProperties={
  "violet":{
    "x":-340,
    "y":150
  },
  "indigo":{
    "x":-340,
    "y":100
  },
  "blue":{
    "x":-340,
    "y":50
  },
  "green":{
    "x":-340,
    "y":0
  },
  "yellow":{
    "x":-340,
    "y":-50
  },
  "orange":{
    "x":-340,
    "y":-100
  },
  "red":{
    "x":-340,
    "y":-150
  }
}
user_bet = screen.textinput(title="make your bet",prompt=f"Which turtle will win the race? Enter a color from {list(turtleProperties.keys())}")
print(user_bet)
turtles=[]
def createTurtles():
  for key in turtleProperties.keys():
    magTheTurtle = t.Turtle(shape="turtle")
    magTheTurtle.speed("fastest")
    magTheTurtle.color(key)
    magTheTurtle.penup()
    magTheTurtle.goto(x=turtleProperties[key]["x"],y=turtleProperties[key]["y"])
    turtles.append(magTheTurtle)
    # exec(key + " = t.Turtle(shape='turtle')") #works 
    #above line will make different turtles with a name exactly as color
    # exec(key) = t.Turtle(shape='turtle') #does not work
  # magTheTurtle.forward(100)
  
createTurtles()
# print(turtles)
isGameOn =True
while isGameOn:
  for turtle in turtles:
    randomDistance = random.randint(0,10)
    turtle.forward(randomDistance)
    if turtle.xcor()>330:
      isGameOn=False
      if(user_bet == turtle.pencolor()):
        print(f"You've won!, The {turtle.pencolor()} is the winner!")
      else:
        print(f"You've lost!, The {turtle.pencolor()} is the winner!")

# turtles[0].goto(x=-350,y=0)
# turtles[1].goto(y=0,x=350)
screen.exitonclick()