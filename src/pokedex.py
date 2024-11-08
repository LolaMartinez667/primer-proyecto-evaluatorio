import json
import os
from .pokemon import Pokemon

class Pokedex:
    def __init__(self, archivo_json="data/pokemon.json"):
        self.archivo_json = archivo_json
        self.pokemons = self.cargar_pokemons()

    def cargar_pokemons(self):
        if os.path.exists(self.archivo_json):
            with open(self.archivo_json, 'r') as f:
                data = json.load(f)
                return [Pokemon.from_dict(p) for p in data]
        return []

    def guardar_pokemons(self):
        with open(self.archivo_json, 'w') as f:
            json.dump([p.to_dict() for p in self.pokemons], f, indent=4)

    def agregar_pokemon(self, pokemon):
        self.pokemons.append(pokemon)
        self.guardar_pokemons()

    def buscar_pokemon(self, id):
        return next((p for p in self.pokemons if p.id == id), None)

    def actualizar_pokemon(self, id, datos_nuevos):
        pokemon = self.buscar_pokemon(id)
        if pokemon:
            for key, value in datos_nuevos.items():
                setattr(pokemon, key, value)
            self.guardar_pokemons()
            return True
        return False

    def eliminar_pokemon(self, id):
        pokemon = self.buscar_pokemon(id)
        if pokemon:
            self.pokemons.remove(pokemon)
            self.guardar_pokemons()
            return True
        return False 