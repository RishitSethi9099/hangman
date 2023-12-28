from word import choose_word
from rich import print
from rich.prompt import Prompt
def hangman():
        s= Prompt.ask("[italic bold underline green]Do you want to play hangman? (yes/no): [/italic bold underline green]" )
        if s == "yes":
            print("[blue]Let's play![/blue]")
            word = choose_word()
            word_list = list(word)
            word_length = len(word)
            display = []
            for i in range(word_length):
                display.append("_")
            print(display)

            end_of_game = False
            lives = 10

            while not end_of_game:
                guess = Prompt.ask("[yellow]Guess a letter: [/yellow]").lower()
                if guess in display:
                    print(f"You've already guessed {guess}")
                for i in range(word_length):
                    letter = word[i]
                    if letter == guess:
                        display[i] = letter
                print(f'[bold cyan]{display}[/bold cyan]')
                if guess not in word:
                    print(f"[pink]You guessed {guess}, that's not in the word. You lose a life.[/pink]")
                    lives -= 1
                    print(f"[bold red]You have {lives} lives left.[/bold red]")
                    if lives == 0:
                        end_of_game = True
                        print("[bold red]You lose. the word was [/bold red]" + word)
                if not "_" in display:
                    end_of_game = True
                    print("[bold italic green]You win.[/bold italic green]")
                    

if __name__ == '__main__':
    hangman()
    
