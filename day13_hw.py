import turtle as t
import random

# 500 by 500 사각형 만들기
t.up()
t.goto(-250,-250)
t.down()
t.pensize(2)
t.goto(250,-250)
t.goto(250,250)
t.goto(-250,250)
t.goto(-250,-250)

# 사각형 가운데로
t.up()
t.goto(0,0)

# 거북이 움직이기
t.down()
t.shape("turtle")
t.pensize(1)

# 랜덤 설정된 각도로 회전 후 벽까지 이동

a=random.randint(0,360) # a를 0도부터 360도까지 랜덤 설정

t.setheading(a)
while -250<t.xcor()<250 and -250<t.ycor()<250:
    t.forward(1)

while True: # 아래를 무한 반복
    b=t.heading() # 현재 바라보는 각도 저장
    
    if 0<b<45 or 135<b<180 or 225<b<270:
        if -250<t.xcor()<250:
            t.setheading(360-b)
            t.forward(1)
            while -250<t.xcor()<250 and -250<t.ycor()<250:
                t.forward(1)
        else:
            t.setheading(180-b)
            t.forward(1)
            while -250<t.xcor()<250 and -250<t.ycor()<250:
                t.forward(1)
                
    if 45<b<135 or 270<b<315:
        if -250<t.xcor()<250:
            t.setheading(360-b)
            t.forward(1)
            while -250<t.xcor()<250 and -250<t.ycor()<250:
                t.forward(1)
        else:
            t.setheading(540-b)
            t.forward(1)
            while -250<t.xcor()<250 and -250<t.ycor()<250:
                t.forward(1)
                
    if 180<b<225 or 315<b<360:
        if -250<t.xcor()<250:
            t.setheading(360-b)
            t.forward(1)
            while -250<t.xcor()<250 and -250<t.ycor()<250:
                t.forward(1)
        else:
            t.setheading(540-b)
            t.forward(1)
            while -250<t.xcor()<250 and -250<t.ycor()<250:
                t.forward(1)

    if a==0 or a==45 or a==90 or a==135 or a==180 or a==225 or a==270 or a==315 or a==360:
        t.left(180)
        t.forward(1)
        while -250<t.xcor()<250 and -250<t.ycor()<250:
            t.forward(1)
            
            
