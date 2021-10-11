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

    def player():
        screen.blit(player_img, (player_x, player_y))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        player()
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
