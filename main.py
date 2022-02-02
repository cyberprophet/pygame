import pygame as pg

pg.init()

screen_width = 480
screen_height = 640
screen = pg.display.set_mode((screen_width, screen_height))

pg.display.set_caption('Nado Game')

clock = pg.time.Clock()

background = pg.image.load('/mnt/c/Users/T2/source/pygame_test/background.png')

character = pg.image.load('/mnt/c/Users/T2/source/pygame_test/character.png')
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_position = (screen_width / 2) - (character_width / 2)
character_y_position = screen_height - character_height

to_x = 0
to_y = 0

character_speed = 2

enemy = pg.image.load('/mnt/c/Users/T2/source/pygame_test/enemy.png')
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_position = (screen_width / 2) - (enemy_width / 2)
enemy_y_position = (screen_height / 2) - enemy_height

game_font = pg.font.Font(None, 40)

total_time = 10

start_ticks = pg.time.get_ticks()

running = True

while running:
    dt = clock.tick(60)

    for event in pg.event.get():
        match event.type:
            case pg.KEYDOWN:
                match event.key:
                    case pg.K_LEFT:
                        to_x -= character_speed

                    case pg.K_RIGHT:
                        to_x += character_speed

                    case pg.K_UP:
                        to_y -= character_speed

                    case pg.K_DOWN:
                        to_y += character_speed

            case pg.KEYUP:
                match event.key:
                    case pg.K_LEFT | pg.K_RIGHT:
                        to_x = 0

                    case pg.K_UP | pg.K_DOWN:
                        to_y = 0

            case pg.QUIT:
                running = False

    character_x_position += to_x * character_speed
    character_y_position += to_y * character_speed

    if character_x_position < 0:
        character_x_position = 0

    if character_x_position > screen_width - character_width:
        character_x_position = screen_width - character_width

    if character_y_position < 0:
        character_y_position = 0

    if character_y_position > screen_height - character_height:
        character_y_position = screen_height - character_height

    character_rect = character.get_rect()
    character_rect.left = character_x_position
    character_rect.top = character_y_position

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_position
    enemy_rect.top = enemy_y_position

    if character_rect.colliderect(enemy_rect):
        running = False

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_position, character_y_position))
    screen.blit(enemy, (enemy_x_position, enemy_y_position))

    elapsed_time = (pg.time.get_ticks() - start_ticks) / 1000

    timer = game_font.render(
        str(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time < 1:
        running = False

    pg.display.update()

pg.time.delay(1024)

pg.quit()
