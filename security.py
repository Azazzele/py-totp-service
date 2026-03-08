# Генерация секретов, base32, HMAC

import base64 			# декодирует секрет
import hmac				# делает HMAC
import hashlib			# алгоритм хеша
import time				# алгоритм хеша
import struct			# перевод числа в байты


class HOTPGenerator:
    def __init__(self, secret,algorithm="sha1", digits=6, counter=0):
        self.secret = base64.b32decode(secret)  
        self.algorithm = algorithm
        self.digits = digits
        self.counter = counter

    def generate_otp(self):
        self.counter += 1
        return self.generate_hotp(self.counter)

    def generate_hotp(self, counter):
        msg = struct.pack(">Q", counter)
        h = hmac.new(self.secret, msg, hashlib.sha1).digest()
        offset = h[-1] & 0x0F
        binary = (
            ((h[offset] & 0x7F) << 24) |
            ((h[offset+1] & 0xFF) << 16) |
            ((h[offset+2] & 0xFF) << 8) |
            (h[offset+3] & 0xFF)
        )
        otp = binary % (10 ** self.digits)
        return str(otp).zfill(self.digits)
    
    def get_time_step(self, time_step=30):
        return int(time.time()) // time_step
    
    def generate_totp(self, time_step=30):
        counter = self.get_time_step(time_step)
        return self.generate_hotp(counter)
        
# -----------------------------
# Вспомогательная функция для проверки кода
def verify_totp(secret, code, window=1):
    """
    Проверяет, совпадает ли code с TOTP для данного секрета
    с допуском ±window шагов времени
    """
    otp_gen = HOTPGenerator(secret)
    counter = otp_gen.get_time_step()
    for i in range(-window, window+1):
        otp = otp_gen.generate_hotp(counter + i)
        if otp == code:
            return True
    return False		

