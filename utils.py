import pyqrcode
import base64
from io import BytesIO

# Создание URI для TOTP (для сканирования через Authenticator)
def generate_totp_uri(username: str, secret: str, issuer: str = "MyApp") -> str:
    return f"otpauth://totp/{issuer}:{username}?secret={secret}&issuer={issuer}&algorithm=SHA1&digits=6&period=30"

# Генерация QR-кода в base64
def generate_qr_code(uri: str) -> str:
    qr = pyqrcode.create(uri)
    buffer = BytesIO()
    qr.png(buffer, scale=5)
    qr_base64 = base64.b64encode(buffer.getvalue()).decode()
    return f"data:image/png;base64,{qr_base64}"

