from termcolor import colored
from .pokemon import Pokemon

class Menu:
    def __init__(self, pokedex):
        self.pokedex = pokedex

    def mostrar_menu(self):
        while True:
            print(colored("\n=== POKÉDEX ===", "yellow", attrs=["bold"]))
            print(colored("1. Agregar Pokémon", "cyan"))
            print(colored("2. Ver todos los Pokémon", "cyan"))
            print(colored("3. Buscar Pokémon", "cyan"))
            print(colored("4. Actualizar Pokémon", "cyan"))
            print(colored("5. Eliminar Pokémon", "cyan"))
            print(colored("6. Salir", "cyan"))
            
            opcion = input(colored("\nElige una opción: ", "green"))
            
            if opcion == "1":
                self.agregar_pokemon()
            elif opcion == "2":
                self.mostrar_pokemons()
            elif opcion == "3":
                self.buscar_pokemon()
            elif opcion == "4":
                self.actualizar_pokemon()
            elif opcion == "5":
                self.eliminar_pokemon()
            elif opcion == "6":
                print(colored("¡Hasta luego!", "yellow"))
                break
            else:
                print(colored("Opción no válida. Por favor, intenta de nuevo.", "red"))

    def agregar_pokemon(self):
        print(colored("\n=== Agregar Pokémon ===", "yellow"))
        try:
            id = int(input(colored("ID del Pokémon: ", "green")))
            nombre = input(colored("Nombre del Pokémon: ", "green"))
            tipo = input(colored("Tipo del Pokémon: ", "green"))
            nivel = int(input(colored("Nivel del Pokémon: ", "green")))

            pokemon = Pokemon(id, nombre, tipo, nivel)
            self.pokedex.agregar_pokemon(pokemon)
            print(colored("¡Pokémon agregado exitosamente!", "green"))
        except ValueError:
            print(colored("Error: Por favor ingresa valores válidos", "red"))

    def mostrar_pokemons(self):
        print(colored("\n=== Lista de Pokémon ===", "yellow"))
        if not self.pokedex.pokemons:
            print(colored("No hay Pokémon registrados", "red"))
            return
        
        for pokemon in self.pokedex.pokemons:
            print(colored(f"ID: {pokemon.id}", "cyan"))
            print(colored(f"Nombre: {pokemon.nombre}", "cyan"))
            print(colored(f"Tipo: {pokemon.tipo}", "cyan"))
            print(colored(f"Nivel: {pokemon.nivel}", "cyan"))
            print("-" * 20)

    def buscar_pokemon(self):
        print(colored("\n=== Buscar Pokémon ===", "yellow"))
        try:
            id = int(input(colored("Ingresa el ID del Pokémon: ", "green")))
            pokemon = self.pokedex.buscar_pokemon(id)
            if pokemon:
                print(colored(f"ID: {pokemon.id}", "cyan"))
                print(colored(f"Nombre: {pokemon.nombre}", "cyan"))
                print(colored(f"Tipo: {pokemon.tipo}", "cyan"))
                print(colored(f"Nivel: {pokemon.nivel}", "cyan"))
            else:
                print(colored("Pokémon no encontrado", "red"))
        except ValueError:
            print(colored("Error: Por favor ingresa un ID válido", "red"))

    def actualizar_pokemon(self):
        print(colored("\n=== Actualizar Pokémon ===", "yellow"))
        try:
            id = int(input(colored("ID del Pokémon a actualizar: ", "green")))
            pokemon = self.pokedex.buscar_pokemon(id)
            if pokemon:
                nombre = input(colored("Nuevo nombre (Enter para mantener actual): ", "green"))
                tipo = input(colored("Nuevo tipo (Enter para mantener actual): ", "green"))
                nivel_str = input(colored("Nuevo nivel (Enter para mantener actual): ", "green"))

                datos_nuevos = {}
                if nombre: datos_nuevos["nombre"] = nombre
                if tipo: datos_nuevos["tipo"] = tipo
                if nivel_str: datos_nuevos["nivel"] = int(nivel_str)

                if self.pokedex.actualizar_pokemon(id, datos_nuevos):
                    print(colored("¡Pokémon actualizado exitosamente!", "green"))
            else:
                print(colored("Pokémon no encontrado", "red"))
        except ValueError:
            print(colored("Error: Por favor ingresa valores válidos", "red"))

    def eliminar_pokemon(self):
        print(colored("\n=== Eliminar Pokémon ===", "yellow"))
        try:
            id = int(input(colored("ID del Pokémon a eliminar: ", "green")))
            if self.pokedex.eliminar_pokemon(id):
                print(colored("¡Pokémon eliminado exitosamente!", "green"))
            else:
                print(colored("Pokémon no encontrado", "red"))
        except ValueError:
            print(colored("Error: Por favor ingresa un ID válido", "red"))