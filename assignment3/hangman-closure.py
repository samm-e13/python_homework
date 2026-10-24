def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)
        #compare guesses with secret_word - can just use in
        #compare letters in secret word vs guesses
        #or compare guesses vs. secret word -> if word is not there
        new_word = [] #build as we go, in order via loop:
        for letter in secret_word:
            if letter in guesses:
                new_word.append(letter)
            elif letter not in guesses:
                new_word.append("_")
        current_word = "".join(new_word)
        if "_" in current_word:
            print(f"{current_word}")
            return False
        else:
            print(f"{current_word}")
            return True
    return hangman_closure

secret_input = input("Enter your secret word:")
hangman_game = make_hangman(secret_input)
game_status = False 
while game_status == False:
    game_status = hangman_game(input("Enter your letter guess:"))
    

