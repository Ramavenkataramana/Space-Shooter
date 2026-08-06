import pygame
import random
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚀 Space Shooter")
clock = pygame.time.Clock()
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,170,255)
RED = (255,60,60)
YELLOW = (255,255,0)
font = pygame.font.SysFont("Arial",30)
player_x = WIDTH//2
player_y = HEIGHT-60
player_speed = 7
enemy_x = random.randint(50,750)
enemy_y = -40
enemy_speed = 4
bullet_x = 0
bullet_y = 0
bullet_speed = 10
bullet_active = False
score = 0
stars = []
for i in range(80):
    stars.append([
        random.randint(0,WIDTH),
        random.randint(0,HEIGHT),
        random.randint(1,3)
    ])
game_over = False
def collision(x1,y1,x2,y2):
    distance=((x1-x2)**2+(y1-y2)**2)**0.5
    return distance<30
running=True
while running:
    clock.tick(60)
    screen.fill((5,5,25))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and not bullet_active:
                bullet_active=True
                bullet_x=player_x
                bullet_y=player_y
            if event.key==pygame.K_r and game_over:
                score=0
                enemy_x=random.randint(50,750)
                enemy_y=-40
                enemy_speed=4
                bullet_active=False
                player_x=WIDTH//2
                game_over=False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if player_x < 20:
        player_x = 20
    if player_x > WIDTH - 20:
        player_x = WIDTH - 20
    for star in stars:
        pygame.draw.circle(
            screen,
            WHITE,
            (star[0], star[1]),
            star[2]
        )
        star[1] += 2
        if star[1] > HEIGHT:
            star[0] = random.randint(0, WIDTH)
            star[1] = 0
    if not game_over:
        enemy_y += enemy_speed
        if enemy_y > HEIGHT:
            game_over = True
    if bullet_active:
        bullet_y -= bullet_speed
        if bullet_y < 0:
            bullet_active = False
    if bullet_active:

        if collision(
            bullet_x,
            bullet_y,
            enemy_x,
            enemy_y
        ):
            score += 1
            bullet_active = False
            enemy_x = random.randint(50,750)
            enemy_y = -40
            enemy_speed += 0.3
    pygame.draw.polygon(
        screen,
        BLUE,
        [
            (player_x, player_y-25),
            (player_x-20, player_y+20),
            (player_x+20, player_y+20)
        ]
    )
    pygame.draw.rect(
        screen,
        BLUE,
        (
            player_x-8,
            player_y+15,
            16,
            20
        )
    )
    if not game_over:
        pygame.draw.circle(
            screen,
            RED,
            (enemy_x, enemy_y),
            20
        )
        pygame.draw.circle(
            screen,
            BLACK,
            (enemy_x - 7, enemy_y - 5),
            3
        )
        pygame.draw.circle(
            screen,
            BLACK,
            (enemy_x + 7, enemy_y - 5),
            3
        )
        pygame.draw.arc(
            screen,
            BLACK,
            (enemy_x - 8, enemy_y - 2, 16, 10),
            3.14,
            6.28,
            2
        )
    if bullet_active:
        pygame.draw.rect(
            screen,
            YELLOW,
            (
                bullet_x - 2,
                bullet_y - 15,
                4,
                20
            )
        )
    score_text = font.render(
        "Score : " + str(score),
        True,
        WHITE
    )
    screen.blit(score_text, (20, 20))
    if game_over:
        game_text = pygame.font.SysFont(
            "Arial",
            60
        ).render(
            "GAME OVER",
            True,
            RED
        )
        restart_text = pygame.font.SysFont(
            "Arial",
            28
        ).render(
            "Press R to Restart",
            True,
            WHITE
        )
        final_score = pygame.font.SysFont(
            "Arial",
            32
        ).render(
            "Final Score : " + str(score),
            True,
            YELLOW
        )
        screen.blit(
            game_text,
            (WIDTH//2 - 170, HEIGHT//2 - 70)
        )
        screen.blit(
            final_score,
            (WIDTH//2 - 90, HEIGHT//2)
        )
        screen.blit(
            restart_text,
            (WIDTH//2 - 120, HEIGHT//2 + 50)
        )
    pygame.display.update()
pygame.quit()