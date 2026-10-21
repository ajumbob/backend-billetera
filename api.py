from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from billetera import BilleteraMensual

# Inicializamos la aplicación web
app = FastAPI(title="API Billetera de Álvaro")

# Instanciamos nuestra clase principal (simulando una base de datos temporal)
mi_billetera = BilleteraMensual(150.0)

# Definimos la estructura de los datos que esperamos recibir desde internet
class TransaccionWeb(BaseModel):
    monto: float
    tipo: str
    descripcion: str

# Ruta GET: Para consultar información
@app.get("/resumen")
def obtener_resumen():
    return {
        "saldo_actual": mi_billetera.saldo,
        "total_movimientos": len(mi_billetera.movimientos),
        "historial": mi_billetera.movimientos
    }

# Ruta POST: Para enviar nueva información
@app.post("/transaccion")
def registrar(datos: TransaccionWeb):
    try:
        # Llamamos al método que ya programaste en billetera.py
        mi_billetera.registrar_transaccion(datos.monto, datos.tipo, datos.descripcion)
        return {
            "mensaje": f"Éxito: {datos.tipo} registrado", 
            "saldo_actual": mi_billetera.saldo
        }
    except ValueError as e:
        # Si la lógica de negocio falla (ej. sin fondos), devolvemos un error HTTP 400
        raise HTTPException(status_code=400, detail=str(e))