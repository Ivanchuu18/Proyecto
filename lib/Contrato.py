class Contrato:
    def __int__(self, fecha_entrega, fecha_devolucion, estado):
        self._fecha_entrega = fecha_entrega
        self._fecha_devolucion = fecha_devolucion
        self._estado = estado

    def __str__(self):
        return f"Fecha de entrega: {self._fecha_entrega}, Fecha de devolucion: {self._fecha_devolucion}, Estado: {self._estado}"


    def validar_estado(self):
        # Verificar si el estado es uno de los valores permitidos
        estados_permitidos = ["P", "D"]
        if self._estado in estados_permitidos:
            if self._estado == "P":
                return "Prestado"
            else:
                return "Devuelto"
        else:
            raise ValueError("Estado no válido. Debe ser 'P' para prestado o 'D' para devuelto.")
