import pygame

HEIGHT = 600
WIDTH = 800


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Invaders")
    icon = pygame.image.load('img/spaceship.png')
    pygame.display.set_icon(icon)
    player_img = pygame.image.load('img/battleship.png')
    player_x = 370
    player_y = 480
    player_x_change = 0

    def player(x, y):
        screen.blit(player_img, (x, y))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -0.3
                if event.key == pygame.K_RIGHT:
                    player_x_change = 0.3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_change = 0

        screen.fill((0, 0, 0))

        player_x += player_x_change
        player(player_x, player_y)
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
