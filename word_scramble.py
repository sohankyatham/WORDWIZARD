import pygame
import random

# Initialize the Pygame library
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((600, 500))

# Set the title of the window
pygame.display.set_caption("Word Scramble Game")

# Load font
font = pygame.font.Font(None, 30)

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (64, 92, 128)


# Function to draw text on the screen
def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


# List of words for the game
with open("5000-words.txt") as f:
    word_list = f.readlines()
word_list = [word.strip() for word in word_list]

# Game variables
word = ""
scrambled_word = ""
guesses = 3
score = 0

# Input box variables
input_box = pygame.Rect(50, 175, 140, 32)
active = False
text = ''

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check if the input box was clicked on
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = True
            else:
                active = False

        # Check if the user is typing in the input box
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    if text.lower() == word.lower():
                        score += 100
                        text = ''
                        scrambled_word = ''
                        guesses = 3
                    else:
                        guesses -= 1
                        text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    screen.fill(BLUE)

    # Choose a random word from the list
    if not scrambled_word:
        word = random.choice(word_list)
        scrambled_word = "".join(random.sample(word, len(word)))

    # Draw the scrambled word on the screen
    draw_text("Scrambled Word: " + scrambled_word, WHITE, 50, 50)

    # Draw the number of guesses left on the screen
    draw_text("Guesses Left: " + str(guesses), WHITE, 50, 100)

    # Draw the score on the screen
    draw_text("Score: " + str(score), WHITE, 450, 50)

    # Draw the input box and the text entered
    pygame.draw.rect(screen, WHITE, input_box, 2)
    draw_text(text, WHITE, 55, 180)

    # Check if the player has no more guesses left
    if guesses == 0:
        draw_text("Game Over", WHITE, 250, 250)
        pygame.display.update()
        pygame.time.wait(3000)
        running = False

    # Check if the player has 5 words right in a row
    if score == 500:
        draw_text("Level Completed", WHITE, 250, 250)
        pygame.display.update()
        pygame.time.wait(3000)
        running = False

    pygame.display.update()
pygame.quit()
