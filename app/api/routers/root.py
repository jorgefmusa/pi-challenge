from fastapi import APIRouter

# Crear una nueva instancia de APIRouter
router = APIRouter()

# Ruta raíz para verificar que la API está funcionando
@router.get("/")
def root():
    return {"message": "Welcome to the Character API. Desarrollado por Jorge Fernández"}