import random  #installing the random module
#setup
word_bank = ['component', 'service', 'house', 'garden', 'tree','smile', 'laugh','innovation' ,'design','security','collaboration','cookie', 'pizza','plane','moon', 'star','school' ]  #all possible words that can be the answer

word = random.choice (word_bank) #choosing a random word from the bank  and assign it to the variable word

guessed_word = ["_"]*len(word) #placeholders for the word

lives = 15 #number of attempts the player has at guessing the word

#game loop

while lives>0:
    print("\n Current Word:" + "".join(guessed_word))#The statement is printed on a new line via \n, and joins the strings in guessedWord together with spaces.
    guess = input('Guess a letter: ')
#determine whether or not the guessed letter is in the correct word

    if guess in word:
     for i in range(len(word)):
        if word[i] == guess:   #checks if the guessed letter is correct
          guessed_word[i] = guess #replaces the placeholder with the correct letter
     print("Great Guess!")
    else:
     lives -= 1
     print("Wrong Guess! Attempts Left: " + str(lives))

    if "_" not in guessed_word:
      print("\nCongratulations! You guessed the word" + word)
      break
   # If the player runs out of lives
    else:
      if lives == 0:
            print("\nYou've run out of attempts! The word was: " + word)