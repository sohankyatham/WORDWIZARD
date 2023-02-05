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
player1_guesses = 3
player2_guesses = 3
player1_score = 0
player2_score = 0

# Input box variables
input_box1 = pygame.Rect(50, 175, 140, 32)
input_box2 = pygame.Rect(400, 175, 140, 32)
text1 = ''
text2 = ''
player1_active = False
player2_active = False
player1_text = ''
player2_text = ''

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check if player 1's input box was clicked on
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box1.collidepoint(event.pos):
                player1_active = True
                player2_active = False
            elif input_box2.collidepoint(event.pos):
                player2_active = True
                player1_active = False
            else:
                player2_active = False

        # Check if player 1 is typing in the input box
        if event.type == pygame.KEYDOWN and player1_active:
            if event.key == pygame.K_RETURN:
                if text1.lower() == word.lower():
                    player1_score += 100
                    text1 = ''
                    scrambled_word = ''
                else:
                    player1_guesses -= 1
                    text1 = ''
            elif event.key == pygame.K_BACKSPACE:
                text1 = text1[:-1]
            else:
                text1 += event.unicode

        # Check if player 2 is typing in the input box
        if event.type == pygame.KEYDOWN and player2_active:
            if event.key == pygame.K_RETURN:
                if player2_text.lower() == word.lower():
                    player2_score += 100
                    player2_text = ''
                    scrambled_word = ''
                else:
                    player2_guesses -= 1
                    player2_text = ''
            elif event.key == pygame.K_BACKSPACE:
                player2_text = player2_text[:-1]
            else:
                player2_text += event.unicode

    screen.fill(BLUE)

    # Choose a random word from the list
    if not scrambled_word:
        word = random.choice(word_list)
        scrambled_word = "".join(random.sample(word, len(word)))

    # Draw the scrambled word on the screen
    draw_text("Scrambled Word: " + scrambled_word, WHITE, 50, 50)

    # Draw the number of Player 1's guesses left on the screen
    draw_text("Guesses Left: " + str(player1_guesses), WHITE, 50, 100)

    # Draw player 1's score on the screen
    draw_text("Player 1 Score: " + str(player1_score), WHITE, 50, 150)

    # Draw player 2's score on the screen
    draw_text("Player 2 Score: " + str(player2_score), WHITE, 400, 150)

    # Draw the number of Player 2's guesses left on the screen
    draw_text("Guesses Left: " + str(player2_guesses), WHITE, 400, 100)


    # Draw player 1's input box and the text entered
    pygame.draw.rect(screen, WHITE, input_box1, 2)
    draw_text(text1, WHITE, 55, 180)

    # Draw player 2's input box and the text entered
    pygame.draw.rect(screen, WHITE, input_box2, 2)
    draw_text(player2_text, WHITE, 420, 180)

    # Check if player 1 has no more guesses left
    if player1_guesses == 0:
        draw_text("Player 1 Game Over", WHITE, 250, 250)
        pygame.display.update()
        pygame.time.wait(3000)
        running = False

    # Check if player 1 has 5 words right in a row
    if player1_score == 500:
        draw_text("Player 1 Level Completed", WHITE, 250, 250)
        pygame.display.update()
        pygame.time.wait(3000)
        running = False

    # Check if player 2 has no more guesses left
    if player2_guesses == 0:
        draw_text("Player 2 Game Over", WHITE, 250, 250)
        pygame.display.update()
        pygame.time.wait(3000)
        running = False

    # Check if player 2 has 5 words right in a row
    if player2_score == 500:
        draw_text("Player 2 Level Completed", WHITE, 250, 250)
        pygame.display.update()
        pygame.time.wait(3000)
        running = False

    pygame.display.update()

pygame.quit()
