class Pokemon:
    def __init__(self, id, nombre, tipo, nivel=1):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
    
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tipo": self.tipo,
            "nivel": self.nivel
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["nombre"],
            data["tipo"],
            data.get("nivel", 1)
        ) 