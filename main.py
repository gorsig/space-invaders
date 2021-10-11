import pygame

HEIGHT = 600
WIDTH = 800


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Invaders")
    icon = pygame.image.load('spaceship.png')
    pygame.display.set_icon(icon)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
