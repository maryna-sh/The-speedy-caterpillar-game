def new_game():
    from turtle import Turtle, Screen
    import turtle as t
    from food import Food
    from score import Score
    from caterpillar import Snake
    screen = Screen()
    screen.setup(width=600, height=600)
    t.colormode(255)
    screen.bgcolor(0, 0, 0)
    t.hideturtle()
    screen.tracer(0)

    import time
    screen.title('The Speedy Caterpillar')

    snake = Snake()
    food = Food()
    score = Score()

    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)

    game = True


    while game:
        time.sleep(0.1)
        screen.update()
        snake.move()
        if snake.snakes[0].distance(food) < 15:
            food.refresh()
            score.inc_score()
            snake.extend()

        if snake.snakes[0].xcor() > 290 or snake.snakes[0].ycor() > 290 or snake.snakes[0].xcor() < -290 or \
                snake.snakes[0].ycor() < -290:
            score.reset_score()
            score.game_over()
            u_r = screen.textinput(title='New Game', prompt="Shall we play again? (Y/N)").lower()
            if u_r == 'yes' or u_r == 'y' or u_r == 'sure':
                score.reset_score()
                screen.clear()
                new_game()
            else:
                score.reset_score()
                screen.clear()
                score.goodbye()
                game = False
                screen.bye()

        for s in snake.snakes[1:]:
            if snake.snakes[0].distance(s) < 3:
                score.reset_score()
                score.game_over()
                u_r = screen.textinput(title='New Game', prompt="Shall we play again?").lower()
                if u_r == 'yes' or u_r == 'y' or u_r == 'sure':
                    score.reset_score()
                    screen.clear()
                    new_game()

                else:
                    score.reset_score()
                    screen.clear()
                    score.goodbye()
                    game = False
                    screen.bye()



    screen.exitonclick()


new_game()
