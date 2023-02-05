import pygame
import random
import webbrowser


# Initialize pygame
pygame.font.init()
pygame.init()
# Color variables

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (64, 92, 128)

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
active = True
text = ''

player1_guesses = 3
player2_guesses = 3
player1_score = 0
player2_score = 0
# Input box variables
input_box1 = pygame.Rect(50, 190, 140, 32)
input_box2 = pygame.Rect(400, 190, 140, 32)
player1_active = False
player2_active = True
player1_text = ''
player2_text = ''


class Screen:
    def __init__(self, title, width, height, color, initial_surface=None):
        self.title = title
        pygame.display.set_caption(title)
        self.surface = pygame.display.set_mode((width, height))
        self.surface.fill(color)  # Set the background color of the screen
        if initial_surface:
            self.blit(initial_surface, (0, 0))

    def blit(self, source_surface, dest_pos):
        self.surface.blit(source_surface, dest_pos)


# Create a surface for the main menu
width, height = 800, 600
main_menu_surface = pygame.Surface((width, height))

# Create a surface for the level screen
width, height = 800, 600
level_screen_surface = pygame.Surface((width, height))

# Create a surface for the instructions
width, height = 800, 600
instructions_screen_surface = pygame.Surface((width, height))

# Create a surface for level 1
width, height = 800, 600
level1_surface = pygame.Surface((width, height))

# Create a surface for level 2
width, height = 800, 600
level2_surface = pygame.Surface((width, height))

# Create a surface for level 3
width, height = 800, 600
level3_surface = pygame.Surface((width, height))

# Pause Surface
width, height = 800, 600
pause_surface = pygame.Surface((width, height))

# Level Completed Surface
width, height = 800, 600
level_completed_surface = pygame.Surface((width, height))

# Game Over surface
width, height = 800, 600
game_over_surface = pygame.Surface((width, height))

# Game select
width, height = 800, 600
game_select_surface = pygame.Surface((width, height))

# Hang Man
width, height = 800, 600
hangman_surface = pygame.Surface((width, height))

# Multiplayer
multiplayer_surface = pygame.Surface((width, height))

# Making game window
screen = Screen("Word Wizard", 800, 600, (255, 255, 255), main_menu_surface)
font = pygame.font.Font('./DeterminationSansWeb.ttf', 40)
font_big = pygame.font.Font('./DeterminationSansWeb.ttf', 70)
font_small = pygame.font.Font('./DeterminationSansWeb.ttf', 15)
main_menu_surface.fill(BLUE)
level_screen_surface.fill(BLUE)
instructions_screen_surface.fill(BLUE)
level1_surface.fill(BLUE)
level2_surface.fill(BLUE)
level3_surface.fill(BLUE)
pause_surface.fill(BLUE)
level_completed_surface.fill(BLUE)
game_over_surface.fill(BLUE)
game_select_surface.fill(BLUE)
multiplayer_surface.fill(BLUE)
hangman_surface.fill(BLUE)


# Drawing text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# Creating buttons

# Play Button

play_button = pygame.Rect(250, 250, 200, 50)
pygame.draw.rect(main_menu_surface, BLUE, play_button)

# Quit Button

quit_button = pygame.Rect(150, 300, 200, 50)
pygame.draw.rect(main_menu_surface, BLUE, quit_button)



# Instructions

instructions_button = pygame.Rect(360, 300, 200, 50)
pygame.draw.rect(main_menu_surface, BLUE, instructions_button)

# Back

back_button = pygame.Rect(300, 500, 200, 50)
pygame.draw.rect(instructions_screen_surface, BLUE, back_button)
pygame.draw.rect(level_screen_surface, BLUE, back_button)
pygame.draw.rect(game_select_surface, BLUE, back_button)
pygame.draw.rect(game_over_surface, BLUE, back_button)
pygame.draw.rect(level_completed_surface, BLUE, back_button)

# Levels
level1_button = pygame.Rect(50, 100, 200, 100)
level2_button = pygame.Rect(300, 100, 200, 100)
level3_button = pygame.Rect(550, 100, 200, 100)
pygame.draw.rect(level_screen_surface, BLUE, level1_button)
pygame.draw.rect(level_screen_surface, BLUE, level2_button)
pygame.draw.rect(level_screen_surface, BLUE, level3_button)
# Documentation
documentation_button = pygame.Rect(250, 320, 200, 100)
pygame.draw.rect(main_menu_surface, BLUE, documentation_button)
# Multiplayer
multiplayer_button = pygame.Rect(270, 400, 200, 100)
pygame.draw.rect(level_screen_surface, BLUE, multiplayer_button)
# Word Scramble
word_scramble_button = pygame.Rect(150, 200, 200, 100)
pygame.draw.rect(game_select_surface, BLUE, word_scramble_button)

# Hangman
hangman_button = pygame.Rect(500, 200, 200, 100)
pygame.draw.rect(game_select_surface, BLUE, hangman_button)
# Render text for the buttons

# Play Button
play_text = font.render("Play", True, (255, 255, 255))
play_text_rect = play_text.get_rect()
play_text_rect.center = play_button.center
main_menu_surface.blit(play_text, play_text_rect)

# Quit Button
quit_text = font.render("Quit", True, (255, 255, 255))
quit_text_rect = quit_text.get_rect()
quit_text_rect.center = quit_button.center
main_menu_surface.blit(quit_text, quit_text_rect)

# Instructions Button
instructions_text = font.render("Instructions", True, (255, 255, 255))
instructions_text_rect = instructions_text.get_rect()
instructions_text_rect.center = instructions_button.center
main_menu_surface.blit(instructions_text, instructions_text_rect)

# Back Button
back_text = font.render("Back", True, (255, 255, 255))
back_text_rect = back_text.get_rect()
back_text_rect.center = back_button.center
instructions_screen_surface.blit(back_text, back_text_rect)
level_screen_surface.blit(back_text, back_text_rect)
game_select_surface.blit(back_text, back_text_rect)
level_completed_surface.blit(back_text, back_text_rect)
game_over_surface.blit(back_text, back_text_rect)

# Level 1 Button
level1_text = font_big.render("Level 1", True, (255, 255, 255))
level1_text_rect = level1_text.get_rect()
level1_text_rect.center = level1_button.center
level_screen_surface.blit(level1_text, level1_text_rect)

# Level 2 Button
level2_text = font_big.render("Level 2", True, (255, 255, 255))
level2_text_rect = level2_text.get_rect()
level2_text_rect.center = level2_button.center
level_screen_surface.blit(level2_text, level2_text_rect)

# Level 3 Button
level3_text = font_big.render("Level 3", True, (255, 255, 255))
level3_text_rect = level3_text.get_rect()
level3_text_rect.center = level3_button.center
level_screen_surface.blit(level3_text, level3_text_rect)

# Documentation Button
documentation_text = font.render("Documentation", True, (255, 255, 255))
documentation_text_rect = documentation_text.get_rect()
documentation_text_rect.center = documentation_button.center
main_menu_surface.blit(documentation_text, documentation_text_rect)

# Multiplayer button
multiplayer_text = font_big.render("Multiplayer", True, (255, 255, 255))
multiplayer_text_rect = multiplayer_text.get_rect()
multiplayer_text_rect.center = multiplayer_button.center
level_screen_surface.blit(multiplayer_text, multiplayer_text_rect)

# Word Scramble
word_scramble_text = font_big.render("Word Scramble", True, (255, 255, 255))
word_scramble_text_rect = word_scramble_text.get_rect()
word_scramble_text_rect.center = word_scramble_button.center
game_select_surface.blit(word_scramble_text, word_scramble_text_rect)

# Hangman
hangman_text = font_big.render("Hangman", True, (255, 255, 255))
hangman_text_rect = hangman_text.get_rect()
hangman_text_rect.center = hangman_button.center
game_select_surface.blit(hangman_text, hangman_text_rect)

# Drawing Text on screen
draw_text("Word Wizard", font_big, (255, 255, 255), main_menu_surface, 225, 100)

draw_text("Game Select: ", font_big, WHITE, game_select_surface, 225, 100)
draw_text("GAME OVER", font_big, WHITE, game_over_surface, 225, 100)
draw_text("LEVEL COMPLETED", font_big, WHITE, level_completed_surface, 225, 100)
draw_text("Instructions", font_big, (255, 255, 255), instructions_screen_surface, 225, 50)
draw_text("Word Scramble: ", font, (255, 255, 255), instructions_screen_surface, 10, 150)
draw_text("A scrambled word will appear on the screen.", font_small, (255, 255, 255), instructions_screen_surface, 10,
          200)
draw_text("Unscramble the word in three guesses or fewer.", font_small, (255, 255, 255), instructions_screen_surface,
          10,
          210)
draw_text("To make a guess, type it in the box", font_small, (255, 255, 255), instructions_screen_surface, 10, 220)
draw_text("Correct Guesses will give you new words.", font_small, (255, 255, 255), instructions_screen_surface, 10, 230)
draw_text("Incorrect Guesses will drop your guess counter.", font_small, (255, 255, 255), instructions_screen_surface,
          10, 240)
draw_text("Try your best at word scramble.", font_small, (255, 255, 255), instructions_screen_surface, 10, 250)
draw_text("Hangman: ", font, (255, 255, 255), instructions_screen_surface, 360, 150)
draw_text("A blank word will appear on the screen with spaces.", font_small, (255, 255, 255),
          instructions_screen_surface, 360, 200)
draw_text("To guess a letter, click on the letter you want to try.", font_small, (255, 255, 255),
          instructions_screen_surface, 360, 210)
draw_text("If its right it will appear in the spaces.", font_small, (255, 255, 255), instructions_screen_surface, 360,
          220)
draw_text("If its wrong a part of hangman will be drawn", font_small, (255, 255, 255), instructions_screen_surface, 360,
          230)
draw_text("Try your best to get it right before hangman is drawn.", font_small, (255, 255, 255),
          instructions_screen_surface, 360, 240)

current_surface = main_menu_surface

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if play_button.collidepoint(pos):
                current_surface = game_select_surface
            elif quit_button.collidepoint(pos):
                running = False
            elif instructions_button.collidepoint(pos):
                current_surface = instructions_screen_surface
            elif back_button.collidepoint(pos):
                current_surface = main_menu_surface
            elif level1_button.collidepoint(pos):
                current_surface = level1_surface
            elif level2_button.collidepoint(pos):
                current_surface = level2_surface
            elif level3_button.collidepoint(pos):
                current_surface = level3_surface
            elif documentation_button.collidepoint(pos):
                webbrowser.open(
                    r"https://docs.google.com/document/d/1jn4zOt7qwukGf7bq7IPNrxrMMzPeT55Kqnf7PX_qGOM/edit?usp=sharing")
            elif multiplayer_button.collidepoint(pos):
                current_surface = multiplayer_surface
            elif word_scramble_button.collidepoint(pos):
                current_surface = level_screen_surface
            elif hangman_button.collidepoint(pos):
                current_surface = hangman_surface
            elif input_box1.collidepoint(event.pos):
                player1_active = True
                player2_active = False
            elif input_box2.collidepoint(event.pos):
                player2_active = True
                player1_active = False
            else:
                player2_active = False
                player1_active = False
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
                elif event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    text += event.unicode
        if event.type == pygame.KEYDOWN and player1_active:
            if event.key == pygame.K_RETURN:
                if player1_text.lower() == word.lower():
                    player1_score += 100
                    player1_text = ''
                    scrambled_word = ''
                else:
                    player1_guesses -= 1
                    player1_text = ''
            elif event.key == pygame.K_BACKSPACE:
                player1_text = player1_text[:-1]
            else:
                player1_text += event.unicode

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
        level1_surface.fill(BLUE)
        level2_surface.fill(BLUE)
        level3_surface.fill(BLUE)
        multiplayer_surface.fill(BLUE)
    if current_surface == level1_surface:

        if not scrambled_word:
            word = random.choice(word_list)
            scrambled_word = "".join(random.sample(word, len(word)))

        # Draw the scrambled word on the screen
        draw_text("Scrambled Word: " + scrambled_word, font, WHITE, level1_surface, 50, 50)

        # Draw the number of guesses left on the screen
        draw_text("Guesses Left: " + str(guesses), font, WHITE, level1_surface, 50, 100)

        # Draw the score on the screen
        draw_text("Score: " + str(score), font, WHITE, level1_surface, 550, 50)

        # Draw the input box and the text entered
        pygame.draw.rect(level1_surface, WHITE, input_box, 2)
        draw_text(text, font, WHITE, level1_surface, 55, 170)

        # Check if the player has no more guesses left
        if guesses == 0:
            current_surface = game_over_surface

        # Check if the player has 5 words right in a row
        if score == 500:
            current_surface = level_completed_surface
    elif current_surface == level2_surface:

        if not scrambled_word:
            word = random.choice(word_list)
            scrambled_word = "".join(random.sample(word, len(word)))

        # Draw the scrambled word on the screen
        draw_text("Scrambled Word: " + scrambled_word, font, WHITE, level2_surface, 50, 50)

        # Draw the number of guesses left on the screen
        draw_text("Guesses Left: " + str(guesses), font, WHITE, level2_surface, 50, 100)

        # Draw the score on the screen
        draw_text("Score: " + str(score), font, WHITE, level2_surface, 550, 50)

        # Draw the input box and the text entered
        pygame.draw.rect(level2_surface, WHITE, input_box, 2)
        draw_text(text, font, WHITE, level2_surface, 55, 170)

        # Check if the player has no more guesses left
        if guesses == 0:
            current_surface = game_over_surface

        # Check if the player has 5 words right in a row
        if score == 1000:
            current_surface = level_completed_surface
    elif current_surface == level3_surface:

        if not scrambled_word:
            word = random.choice(word_list)
            scrambled_word = "".join(random.sample(word, len(word)))

        # Draw the scrambled word on the screen
        draw_text("Scrambled Word: " + scrambled_word, font, WHITE, level3_surface, 50, 50)

        # Draw the number of guesses left on the screen
        draw_text("Guesses Left: " + str(guesses), font, WHITE, level3_surface, 50, 100)

        # Draw the score on the screen
        draw_text("Score: " + str(score), font, WHITE, level3_surface, 550, 50)

        # Draw the input box and the text entered
        pygame.draw.rect(level3_surface, WHITE, input_box, 2)
        draw_text(text, font, WHITE, level3_surface, 55, 170)

        # Check if the player has no more guesses left
        if guesses == 0:
            current_surface = game_over_surface

        # Check if the player has 5 words right in a row
        if score == 1500:
            current_surface = level_completed_surface
    elif current_surface == multiplayer_surface:
        # Choose a random word from the list
        if not scrambled_word:
            word = random.choice(word_list)
            scrambled_word = "".join(random.sample(word, len(word)))

        # Draw the scrambled word on the screen
        draw_text("Scrambled Word: " + scrambled_word, font, WHITE, multiplayer_surface, 50, 50)

        # Draw the number of Player 1's guesses left on the screen
        draw_text("Guesses Left: " + str(player1_guesses), font, WHITE, multiplayer_surface, 50, 100)

        # Draw player 1's score on the screen
        draw_text("Player 1 Score: " + str(player1_score), font, WHITE, multiplayer_surface, 50, 150)

        # Draw player 2's score on the screen
        draw_text("Player 2 Score: " + str(player2_score), font, WHITE, multiplayer_surface, 400, 150)

        # Draw the number of Player 2's guesses left on the screen
        draw_text("Guesses Left: " + str(player2_guesses), font, WHITE, multiplayer_surface, 400, 100)

        # Draw player 1's input box and the text entered
        pygame.draw.rect(multiplayer_surface, WHITE, input_box1, 2)
        draw_text(player1_text, font, WHITE, multiplayer_surface, 55, 180)

        # Draw player 2's input box and the text entered
        pygame.draw.rect(multiplayer_surface, WHITE, input_box2, 2)
        draw_text(player2_text, font, WHITE, multiplayer_surface, 420, 180)

        # Check if player 1 has no more guesses left
        if player1_guesses == 0:
            current_surface = game_over_surface

        # Check if player 1 has 5 words right in a row
        if player1_score == 500:
            current_surface = level_completed_surface

        # Check if player 2 has no more guesses left
        if player2_guesses == 0:
            current_surface = game_over_surface

        # Check if player 2 has 5 words right in a row
        if player2_score == 500:
            current_surface = level_completed_surface

    pygame.display.update()
    screen.blit(current_surface, (0, 0))
    pygame.display.update()
pygame.quit()
