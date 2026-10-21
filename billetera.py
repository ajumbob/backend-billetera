class BilleteraMensual:
    def __init__(self, saldo_inicial=0.0):
        # Atributos de la clase
        self.saldo = saldo_inicial
        self.movimientos = [] # Lista para guardar el historial
        
    def registrar_transaccion(self, monto, tipo, descripcion):
        # Validamos y convertimos el monto a decimal
        monto_float = float(monto)
        
        # Lanzamos excepciones para que el controlador web las atrape
        if monto_float <= 0:
            raise ValueError("El monto debe ser mayor a cero.")
            
        if tipo == "gasto" and monto_float > self.saldo:
            raise ValueError("Fondos insuficientes para este gasto.")
            
        # Aplicamos la lógica
        if tipo == "ingreso":
            self.saldo += monto_float
        elif tipo == "gasto":
            self.saldo -= monto_float
            
        # Guardamos la transacción
        self.movimientos.append({
            "tipo": tipo, 
            "monto": monto_float, 
            "desc": descripcion
        })

    def mostrar_resumen(self):
        print("\n--- Resumen Mensual ---")
        print(f"Saldo Actual: ${self.saldo:.2f}")
        print(f"Total de movimientos: {len(self.movimientos)}")

# --- Bloque de Prueba ---
if __name__ == "__main__":
    # Instanciamos el objeto con 150 dólares de saldo inicial
    mi_billetera = BilleteraMensual(150.0)
    
    # Pruebas exitosas protegidas para pruebas locales en terminal
    try:
        mi_billetera.registrar_transaccion(50.0, "ingreso", "Pago freelance")
        mi_billetera.registrar_transaccion(20.5, "gasto", "Comida")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Imprimimos el estado final
    mi_billetera.mostrar_resumen()