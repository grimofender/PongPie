import globalvar, paddle
import pygame, math, time, random


ballimage = pygame.image.load("Ball.png")
random.seed(time.time())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update
    globalvar.clock.tick()

    # Movement
    globalvar.ballx += math.cos(globalvar.ballangle) * globalvar.ballspeed * globalvar.clock.get_time()
    globalvar.bally += math.sin(globalvar.ballangle) * globalvar.ballspeed * globalvar.clock.get_time()

    if globalvar.bally <= 0 or globalvar.bally >= globalvar.height - globalvar.ballw:
        globalvar.ballangle = math.atan2(-math.sin(globalvar.ballangle), math.cos(globalvar.ballangle))

    if globalvar.ballx >= globalvar.width:
        # Player 1 scored
        paddle.PlayerScored(1)
    else:
        if globalvar.ballx <= (0 - globalvar.ballw):
           paddle.PlayerScored(2)

    # Draw
    globalvar.screen.fill((0,0,0))
    ballimage = pygame.transform.scale(ballimage, (globalvar.ballw, globalvar.ballh))
    globalvar.screen.blit(ballimage, (globalvar.ballx, globalvar.bally))
    pygame.display.flip()

