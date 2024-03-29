import django
import render
import django.http
import HttpResponse
import random

def index(request):
    if 'word_to_guess' not in request.session:
        request.session['word_to_guess'] = choose_word()
        request.session['guessed_letters'] = []
        request.session['attempts'] = 0

    word_to_guess = request.session['word_to_guess']
    guessed_letters = request.session['guessed_letters']
    attempts = request.session['attempts']

    if request.method == 'POST':
        guess = request.POST.get('guess', '').lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                message = "You already guessed that letter. Try again."
            elif guess in word_to_guess:
                guessed_letters.append(guess)
                if "_" not in display_word(word_to_guess, guessed_letters):
                    message = "Congratulations! You guessed the word."
                else:
                    message = display_word(word_to_guess, guessed_letters)
            else:
                attempts += 1
                message = f"Incorrect guess! Attempts left: {6 - attempts}"
        else:
            message = "Please enter a valid single letter."

        request.session['guessed_letters'] = guessed_letters
        request.session['attempts'] = attempts

    else:
        message = display_word(word_to_guess, guessed_letters)

    return render(request, 'hangman_app/index.html', {'message': message})

def choose_word():
    words = ["Shantanu", "Sanket", "Vicky", "pritam", "vaishnami"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display
