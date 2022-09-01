import os
import pygame
pygame.init()

WIDTH, HEIGHT = 1280, 720
ORANGE_KET_WIDTH, ORANGE_KET_HEIGHT = 95, 80
GREY_KET_WIDTH, GREY_KET_HEIGHT = 95, 80
# double brackets, because we insert a tuple
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("KitTy pOnG")
APP_ICON = pygame.image.load(os.path.join('Assets', 'ket.png'))
pygame.display.set_icon(APP_ICON)


FPS = 60
VEL = 12
MAX_VEL = 15
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
BALL_RADIUS = 20

GREY_HIT = pygame.USEREVENT + 1
ORANGE_HIT = pygame.USEREVENT + 2

WHITE = (255, 255, 255)
CYAN = 'cyan'
BLACK = (0, 0, 0)
FUCHSIA = (217, 2, 125)

ORANGE_KET_IMAGE = pygame.image.load(os.path.join('Assets', 'orange.png'))
ORANGE_KET = pygame.transform.rotate(pygame.transform.scale(
    ORANGE_KET_IMAGE, (ORANGE_KET_WIDTH, ORANGE_KET_HEIGHT)), 0)
GREY_KET_IMAGE = pygame.image.load(os.path.join('Assets', 'grey.png'))
GREY_KET = pygame.transform.flip(pygame.transform.scale(
    GREY_KET_IMAGE, (GREY_KET_WIDTH, GREY_KET_HEIGHT)), 1, 0)
SPACE_BG = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'SPACE_FOOD.png')), (WIDTH, HEIGHT))

ORANGE_MEOW = pygame.mixer.Sound(os.path.join('Assets', 'ORANGE_MEOW.wav'))
GREY_MEOW = pygame.mixer.Sound(os.path.join('Assets', 'GREY_MEOW.wav'))
BG_MUSIC = pygame.mixer.Sound(os.path.join('Assets', 'NYAN_FUNK_REDUX.wav'))
pygame.mixer.Sound.set_volume(BG_MUSIC, 0.5)
pygame.mixer.Sound.set_volume(GREY_MEOW, 0.77)
pygame.mixer.Sound.set_volume(ORANGE_MEOW, 0.77)
WINNERZ = pygame.mixer.Sound(os.path.join('Assets', 'WINNERZ.mp3'))
pygame.mixer.Sound.set_volume(WINNERZ, 0.5)
OBLIVION = pygame.mixer.Sound(os.path.join('Assets', 'BLACK_HOLED.wav'))
pygame.mixer.Sound.set_volume(OBLIVION, 0.5)
OBLIVION_LOW = pygame.mixer.Sound(
    os.path.join('Assets', 'BLACK_HOLED_LOW.wav'))
pygame.mixer.Sound.set_volume(OBLIVION_LOW, 0.5)


SCORE_FONT = pygame.font.SysFont('ibm3270', 50)
TITLE_FONT = pygame.font.SysFont('ibm3270', 70)
LEGEND_FONT = pygame.font.SysFont('ibm3270', 50)
WINNING_SCORE = 5


def handle_collision(ball, grey, orange):
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if ball.y >= grey.y and ball.y <= grey.y + grey.height:
            if ball.x - ball.radius <= grey.x + grey.width:

                GREY_MEOW.play()
                ball.x_vel *= -1

                middle_y = grey.y + grey.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (grey.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

    else:
        if ball.y >= orange.y and ball.y <= orange.y + orange.height:
            if ball.x + ball.radius >= orange.x:
                ORANGE_MEOW.play()
                ball.x_vel *= -1

                middle_y = orange.y + orange.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (orange.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel


class Ball:
    MAX_VEL = 5

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = MAX_VEL
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, (217, 2, 125), (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1


def grey_movement_handling(keys_pressed, grey):

    if keys_pressed[pygame.K_w] and grey.y - VEL > 0:  # up
        grey.y -= VEL
    if keys_pressed[pygame.K_s] and grey.y + VEL + grey.height < HEIGHT:  # down
        grey.y += VEL


def orange_movement_handling(keys_pressed, orange):

    if keys_pressed[pygame.K_UP] and orange.y - VEL > 0:  # up
        orange.y -= VEL
    if keys_pressed[pygame.K_DOWN] and orange.y + VEL + orange.height < HEIGHT:  # down
        orange.y += VEL


def reset_o_ket(orange):
    orange.x = 1185
    orange.y = HEIGHT//2


def reset_g_ket(grey):
    grey.x = 0
    grey.y = HEIGHT//2


def draw_intro(win, orange, grey):

    win.blit(SPACE_BG, (0, 0))
    win.blit(ORANGE_KET, (orange.x, orange.y))
    win.blit(GREY_KET, (grey.x, grey.y))


def draw(win, orange, grey, ball, left_score, right_score):

    left_score_text = SCORE_FONT.render(f"{left_score}", 1, 'yellow')
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, 'yellow')

    win.blit(SPACE_BG, (0, 0))
    win.blit(ORANGE_KET, (orange.x, orange.y))
    win.blit(GREY_KET, (grey.x, grey.y))
    win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
    win.blit(right_score_text, (WIDTH * (3/4) -
             right_score_text.get_width()//2, 20))

    # CENTER BORDER
    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, 'grey', (WIDTH // 2 - 5, i, 10, HEIGHT // 50))
    ball.draw(win)
    pygame.display.update()


def main():

    orange = pygame.Rect(1185, HEIGHT//2, ORANGE_KET_WIDTH, ORANGE_KET_HEIGHT)
    grey = pygame.Rect(0, HEIGHT//2, GREY_KET_WIDTH, GREY_KET_HEIGHT)
    ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS)
    left_score = 0
    right_score = 0

    run = True
    clock = pygame.time.Clock()
    draw_intro(WIN, orange, grey)
    intro_text = TITLE_FONT.render('K I T T Y P O N G', 1, CYAN)
    legend_text = LEGEND_FONT.render('', 1, "green")
    guide_left_player = SCORE_FONT.render('LEFT KET:', 1, 'green')
    guide_right_player =  SCORE_FONT.render('      RIGHT KET:', 1, 'green')
    guide_left_player_nl = SCORE_FONT.render('WASD', 1, 'green')
    guide_right_player_nl =  SCORE_FONT.render('            ↑←↓→', 1, 'green')
    WIN.blit(intro_text, (WIDTH//2 - intro_text.get_width() //
                          2, HEIGHT//2 - intro_text.get_height()//2))
    WIN.blit(guide_left_player, (10, 40 - legend_text.get_height()//2))
    WIN.blit(guide_right_player, (847, 40 - legend_text.get_height()//2))
    WIN.blit(guide_left_player_nl, (10, 80 - legend_text.get_height()//2))
    WIN.blit(guide_right_player_nl, (844, 80 - legend_text.get_height()//2))
    pygame.display.update()

    WINNERZ.play()
    pygame.time.delay(3200)
    BG_MUSIC.play()

    while run:
        clock.tick(FPS)
        draw(WIN, orange, grey, ball, left_score, right_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys_pressed = pygame.key.get_pressed()
        orange_movement_handling(keys_pressed, orange)
        grey_movement_handling(keys_pressed, grey)
        ball.move()
        handle_collision(ball, grey, orange)

        if ball.x < 0:
            right_score += 1
            OBLIVION.play()
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            OBLIVION_LOW.play()
            ball.reset()

        won = False
        if left_score >= WINNING_SCORE:
            won = True
            win_text = "LEFT KET WON!"
        elif right_score >= WINNING_SCORE:
            won = True
            win_text = "ORANGE KET WON!"

        if won:
            BG_MUSIC.stop()
            pygame.time.delay(500)
            text = TITLE_FONT.render(win_text, 1, 'green')
            WINNERZ.play()
            WIN.blit(text, (WIDTH//2 - text.get_width() //
                            2, HEIGHT//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(3200)
            ball.reset()
            reset_o_ket(orange)
            reset_g_ket(grey)
            left_score = 0
            right_score = 0
            BG_MUSIC.play()

    pygame.quit()


if __name__ == "__main__":
    main()
