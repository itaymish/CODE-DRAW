from turtle import *
while 1:
  command = input('>>> ')
  arr = command.split(' ')
  word = arr[0]
  num = arr[1]
  goto(0, 0)
  if word == 'forward':
    forward(int(num))
  if word == 'backward':
    backward(int(num))
  if word == 'right':
    right(int(num))
  if word == 'left':
    left(int(num))
  if word == 'circle':
    circle(int(num))
  if word == 'dot':
    dot(int(num))
  if word == 'speed':
    speed(int(num))
  if word == 'pensize':
    pensize(int(num))
  if word == 'pencolor' and num == '0':
    pencolor('blue')
  if word == 'pencolor' and num == '1':
    pencolor('yellow')
  if word == 'pencolor' and num == '2':
    pencolor('green')
  if word == 'pencolor' and num == '3':
    pencolor('red')
  if word == 'pencolor' and num == '4':
    pencolor('black')
  if word == 'pencolor' and num == '5':
    pencolor('white')
  if word == 'color' and num == '0':
    color('blue')
  if word == 'color' and num == '1':
    color('yellow')
  if word == 'color' and num == '2':
    color('green')
  if word == 'color' and num == '3':
    color('red')
  if word == 'color' and num == '4':
    color('black')
  if word == 'color' and num == '5':
    color('white')
  if word == 'fillcolor' and num == '0':
    fillcolor('blue')
  if word == 'fillcolor' and num == '1':
    fillcolor('yellow')
  if word == 'fillcolor' and num == '2':
    fillcolor('green')
  if word == 'fillcolor' and num == '3':
    fillcolor('red')
  if word == 'fillcolor' and num == '4':
    fillcolor('black')
  if word == 'fillcolor' and num == '5':
    fillcolor('white')
  if word == 'reset' and num == '0':
    reset()
  if word == 'hide' and num == '0':
    hideturtle()
  if word == 'show' and num == '0':
    showturtle()
  if word == 'shape' and num == '0':
    shape('classic')
  if word == 'shape' and num == '1':
    shape('triangle')
  if word == 'shape' and num == '2':
    shape('square')
  if word == 'shape' and num == '3':
    shape('circle')
  if word == 'shape' and num == '4':
    shape('turtle')
  if word == 'shape' and num == '5':
    shape('arrow')
