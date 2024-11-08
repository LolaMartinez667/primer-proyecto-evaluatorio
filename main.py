from src.pokedex import Pokedex
from src.menu import Menu

def main():
    pokedex = Pokedex()
    menu = Menu(pokedex)
    menu.mostrar_menu()

if __name__ == "__main__":
    main() 