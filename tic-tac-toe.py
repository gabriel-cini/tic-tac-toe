def main():
# The main function
    introduction = intro()
    board = create_grid()
    pretty = printPretty(board)
    symbol_1, symbol_2 = sym()
    full = isFull(board, symbol_1, symbol_2) # La fonction qui commence le jeu.
    

    


def intro():
# Cette fonction introduit les règles du jeu Tic Tac Toe
    print("Bonjour ! Bienvenue au jeu Tic Tac Toe ")
    print("\n")
    print("Règles : Joueur 1 et joueur 2, représentés par X et O, à tour de rôle "
          "marquer les espaces dans une grille 3*3. Le joueur qui réussit à placer "
          "trois de leurs marques dans une rangée horizontale, verticale ou diagonale gagne.")
    print("\n")
    input("Appuyez sur Entrée pour continuer.")
    print("\n")



def create_grid():
# Cette fonction crée un tableau de bord vierge
    print("Voici le tableau de bord: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board



def sym():
# Cette fonction détermine les symboles des joueurs
    symbol_1 = input("Joueur 1, tu veux être X ou O ? ")
    if symbol_1 == "X":
        symbol_2 = "O"
        print("Joueur 2, vous êtes O. ")
    else:
        symbol_2 = "X"
        print("Joueur 2, vous êtes X. ")
    input("Appuyez sur Entrée pour continuer.")
    print("\n")
    return (symbol_1, symbol_2)



def startGamming(board, symbol_1, symbol_2, count):
# Cette fonction démarre le jeu.

   # Décide du tour
    if count % 2 == 0:
        player = symbol_1
    elif count % 2 == 1:
        player = symbol_2
    print("Player "+ player + ", c'est votre tour. ")
    row = int(input("Choisir une rangée:"
                    "[Choisir une rangée]:"))
    column = int(input("Choisir une colonne:"
                       "[colonne de gauche : entrer 0, colonne du milieu : entrer 1, colonne de droite : entrer 2]"))


    
    while (row > 2 or row < 0) or (column > 2 or column < 0):
        outOfBoard(row, column)
        row = int(input("Choisir une rangée[rangée supérieure:"
                        "[entrer 0, ligne du milieu: entrer 1, ligne du bas: entrer 2]:"))
        column = int(input("Choisir une colonne:"
                           "[colonne de gauche: entrer 0, colonne du milieu: entrer 1, colonne de droite: entrer 2]"))

        # Check if the square is already filled
    while (board[row][column] == symbol_1)or (board[row][column] == symbol_2):
        filled = illegal(board, symbol_1, symbol_2, row, column)
        row = int(input("choisir une rangée[rangée supérieure:"
                        "[entrer 0, ligne du milieu: entrer 1, ligne du bas: entrer 2]:"))
        column = int(input("Chosir une colonne:"
                            "[colonne de gauche: entrer 0, colonne du milieu: entrer 1, colonne de droite: entrer 2]"))    
        
    # Repère le symbole du joueur sur le tableau
    if player == symbol_1:
        board[row][column] = symbol_1
            
    else:
        board[row][column] = symbol_2
    
    return (board)



def isFull(board, symbol_1, symbol_2):
    count = 1
    winner = True
# Cette fonction vérifie si la grille est pleine
    while count < 10 and winner == True:
        gaming = startGamming(board, symbol_1, symbol_2, count)
        pretty = printPretty(board)
        
        if count == 9:
            print("Le plateau est plein. Game over.")
            if winner == True:
                print("il y a égalité. ")

        # Vérifiez s’il y a un gagnant
        winner = isWinner(board, symbol_1, symbol_2, count)
        count += 1
    if winner == False:
        print("Game over.")
        
    # This is function gives a report 
    report(count, winner, symbol_1, symbol_2)



def outOfBoard(row, column):
# Cette fonction indique aux joueurs que leur sélection est hors de portée
    print("Hors de la limite. Choisissez un autre. ")
    
    

def printPretty(board):

    rows = len(board)
    cols = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board



def isWinner(board, symbol_1, symbol_2, count):
# Cette fonction vérifie si y a un gagant
    winner = True
    # Vérifier les lignes
    for row in range (0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
            winner = False
            print("Player " + symbol_1 + ", you won!")
   
        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", you won!")
            
            
    # Vérifier les colonnes
    for col in range (0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
            winner = False
            print("Player " + symbol_1 + ", you won!")
        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", you won!")

    # Vérifier les diagnostics
    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        winner = False 
        print("Player " + symbol_1 + ", you won!")

    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        winner = False
        print("Player " + symbol_2 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        winner = False
        print("Player " + symbol_1 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = False
        print("Player " + symbol_2 + ", you won!")

    return winner
    


def illegal(board, symbol_1, symbol_2, row, column):
    print("Le carré que vous avez choisi est déjà rempli. Choisissez un autre.")

    
def report(count, winner, symbol_1, symbol_2):
    print("\n")
    input("Appuyez sur Entrée pour voir le résumé du jeu. ")
    if (winner == False) and (count % 2 == 1 ):
        print("Winner : Player " + symbol_1 + ".")
    elif (winner == False) and (count % 2 == 0 ):
        print("Winner : Player " + symbol_2 + ".")
    else:
        print("il y a égalité. ")


main()
