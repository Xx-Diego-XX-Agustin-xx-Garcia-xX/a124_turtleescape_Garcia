import turtle as trtl
import random as rand

# maze configuration variables
num_sides = 15
path_width = 25 
wall_color = "blue"
speed = 5

def draw_door(pos):
  maze_drawer.forward(pos)
  maze_drawer.penup()
  maze_drawer.forward(path_width*2)
  maze_drawer.pendown()

def draw_barrier(pos):
  maze_drawer.forward(pos)
  maze_drawer.left(90)
  maze_drawer.forward(path_width*2)
  maze_drawer.backward(path_width*2)
  maze_drawer.right(90)

# event handlers for changing direction
def go_up():
  maze_runner.setheading(90)
def go_down():
  maze_runner.setheading(270)
def go_left():
  maze_runner.setheading(180)
def go_right():
  maze_runner.setheading(0)

# config the maze
maze_drawer = trtl.Turtle()
maze_drawer.pensize(5)
maze_drawer.pencolor(wall_color)
maze_drawer.speed("fastest")
maze_drawer.penup()
maze_drawer.goto(path_width*2, -path_width*2)
maze_drawer.pendown()

# config the maze runner
maze_runner = trtl.Turtle(shape="turtle")
maze_runner.fillcolor("green")
maze_runner.penup()
maze_runner.goto(-path_width*2, path_width*2)
maze_runner.pendown()

def slow_speed():
  maze_runner.forward(5)
def medium_speed():
  maze_runner.forward(10)
def high_speed():
  maze_runner.forward(20)



# draw maze from the middle out
wall_len = path_width
for w in range(num_sides): 
  wall_len += path_width

  if (w > 4): 
    maze_drawer.left(90)

    # randomize location of doors and barriers in wall
    door = rand.randint(path_width*2, (wall_len - path_width*2))
    barrier = rand.randint(path_width*2, (wall_len - path_width*2))
    # if a door and barrier would be rendered on top of each other, get a new value
    while abs(door - barrier) < path_width:
      door = rand.randint(path_width*2, (wall_len - path_width*2))

    if (door < barrier):
      draw_door(door)
      draw_barrier(barrier - door - path_width*2)
      # draw the rest of the wall
      maze_drawer.forward(wall_len - barrier)
    else: 
      draw_barrier(barrier)
      draw_door(door - barrier)
      # draw the rest of the wall
      maze_drawer.forward(wall_len - door - path_width*2)


maze_drawer.hideturtle()

# listen for events
wn = trtl.Screen()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')
wn.onkeypress(slow_speed, 'q')
wn.onkeypress(medium_speed, 'w')
wn.onkeypress(high_speed, 'e')
wn.listen()

wn.mainloop()
