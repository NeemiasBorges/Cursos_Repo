from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_senha(senha: str, senha_hash: str) -> bool:
    return CRIPTO.verify(senha, senha_hash)

def criar_senha(senha: str) -> str:
    return CRIPTO.hash(senha)