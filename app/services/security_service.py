from werkzeug.security import check_password_hash

class SecurityService:
    """
    En este servicio van todas las funciones referidas a la seguridad.
    Generar un hash de una contraseña, comparar una contraseña con un hash.
    """
    
    @staticmethod
    def check_password(pwhash: str, password: str) -> bool:
        """Compara el hash de la contraseña con la contraseña ingresada."""
        return check_password_hash(pwhash, password)