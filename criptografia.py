import bcrypt as bc
from verif_user import senha_ver
import hashlib



salto = bc.gensalt(rounds=12)

def criptografar(c):
    senha_user_str = c
    senha_user_byte = senha_user_str.encode('utf-8')
    hash_user_byte = bc.hashpw(senha_user_byte, salto)
    hash_user_str = hash_user_byte.decode('utf-8')
    return hash_user_str

def verificar_hash(e,h):
    hash_bd = h
    hash_bd_byte = hash_bd.encode('utf-8')
    senha_atual_str = e
    senha_atual_byte = senha_atual_str.encode('utf-8')
    senha_atual_hash = bc.hashpw(senha_atual_byte, salto)
    vericacao = bc.checkpw(senha_atual_byte, hash_bd_byte)
    if vericacao:
        return True
    else:
        return False


