# Tic-Tac-Toe-Game---python
#Python-Essentials course provided by cicco Network acadamy , this course final project is the tic tac toe game python using basic fundamentals of python programming.
"""This code implements a simple command-line Tic-Tac-Toe game where a human player ('O') plays against a computer player ('X'). Here's a step-by-step explanation of the code:

1. Import the `randrange` function from the `random` module.

2. Define a function `display_board(board)` to display the current state of the Tic-Tac-Toe board in the console.

3. Define a function `enter_move(board)` to handle the human player's move. It prompts the user to input a number from 1 to 9 corresponding to the position they want to place their 'O' on the board. It checks whether the input is valid, and if the chosen cell is unoccupied, it updates the board with the 'O' at the selected position.

4. Define a function `list_of_free_cells(board)` that returns a list of tuples representing the coordinates of unoccupied cells on the board.

5. Define a function `check_win(board, sgn)` to check if a player has won. It checks rows, columns, and diagonals for the specified player's symbol ('X' or 'O'). It returns 'you' if the human player wins ('O'), 'me' if the computer player wins ('X'), and `None` if there's no winner yet.

6. Define a function `draw_move(board)` to handle the computer player's move. It chooses a random unoccupied cell and places an 'X' on the board.

7. Create the initial empty Tic-Tac-Toe board, with numbers 1 to 9 representing each cell. The center cell is set to 'X' to ensure the computer starts in the middle.

8. Initialize a list of free fields by calling `list_of_free_cells(board)`.

9. Set `human_turn` to `True` to indicate that the game starts with the human player's turn.

10. Enter the main game loop. While there are free cells left (the `len(free)` is not zero), the game continues:

   - Display the current state of the board.
   - If it's the human player's turn (`human_turn` is `True`), call `enter_move(board)` for the human player, and check if they have won.
   - If it's the computer player's turn, call `draw_move(board)` to make a move for the computer and check if it has won.
   - Toggle `human_turn` to switch to the other player's turn.
   - Update the list of free fields based on the current board state.

11. After the game loop ends, display the final state of the board.

12. Check the value of `victor` to determine the winner or declare a tie. The winner is either 'you' (human player), 'me' (computer player), or `None` if it's a tie.

13. Print the result of the game.

In summary, this code provides a basic console-based Tic-Tac-Toe game where the player ('O') competes against a computer opponent ('X'). The game continues until there is a winner or a tie."""
