"""
Python-версия GetContact API
Для работы нужны TOKEN и AES_KEY из приложения GetContact.
Получить: /data/data/app.source.getcontact/shared_prefs/GetContactSettingsPref.xml
"""
import json
import time
import base64
import hashlib
import hmac
from Crypto.Cipher import AES
import aiohttp

# Ключ шифрования из Data.Key (статический, из C# кода)
STATIC_KEY = "2Wq7)qkX~cp7)H|n_tc&o+:G_USN3/-uIi~>M+c ;Oq]E{t9)RC_5|lhAA_Qq%_4"


class GetContactAPI:
    def __init__(self, token: str, aes_key: str):
        """
        token: токен из GetContact (строка между <string name="TOKEN">)
        aes_key: AES ключ 64 символа (из <string name="FINAL_KEY">)
        """
        if len(aes_key) != 64:
            raise ValueError("AES key must be 64 characters long")
        self.token = token
        self.aes_key = aes_key
        self.device_id = "14130e29cebe9c39"

    def _sha256_hmac(self, data: str) -> str:
        """SHA256 HMAC signature"""
        h = hmac.new(
            STATIC_KEY.encode(),
            data.encode(),
            hashlib.sha256
        )
        return base64.b64encode(h.digest()).decode()

    def _aes256_ecb_encrypt(self, data: str) -> str:
        """AES-256-ECB encrypt"""
        key = bytes.fromhex(self.aes_key)
        cipher = AES.new(key, AES.MODE_ECB)
        # PKCS7 padding
        pad_len = 16 - (len(data) % 16)
        data += chr(pad_len) * pad_len
        encrypted = cipher.encrypt(data.encode())
        return base64.b64encode(encrypted).decode()

    def _aes256_ecb_decrypt(self, data: str) -> str:
        """AES-256-ECB decrypt"""
        key = bytes.fromhex(self.aes_key)
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted = cipher.decrypt(base64.b64decode(data)).decode()
        # Remove PKCS7 padding
        pad_len = ord(decrypted[-1])
        return decrypted[:-pad_len]

    async def search(self, phone: str, country_code: str = "RU") -> dict:
        """
        Поиск информации по номеру
        phone: номер без + (например 79123456789)
        """
        timestamp = str(int(time.time()))
        
        req_obj = {
            "countryCode": country_code,
            "source": "search",
            "token": self.token,
            "phoneNumber": phone,
        }
        
        req_json = json.dumps(req_obj, separators=(',', ':'))
        
        # Формируем подпись
        sign_data = timestamp + "-" + req_json
        signature = self._sha256_hmac(sign_data)
        
        # Шифруем тело запроса
        crypt = self._aes256_ecb_encrypt(req_json)
        body = '{"data":"' + crypt + '"}'
        
        # Отправляем
        headers = {
            "X-App-Version": "4.9.1",
            "X-Token": self.token,
            "X-Os": "android 5.0",
            "X-Client-Device-Id": self.device_id,
            "Accept-Encoding": "deflate",
            "X-Req-Timestamp": timestamp,
            "X-Req-Signature": signature,
            "X-Encrypted": "1",
            "Content-Type": "application/json",
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://pbssrv-centralevents.com/v2.5/search",
                data=body,
                headers=headers,
                timeout=aiohttp.ClientTimeout(total=15),
            ) as resp:
                if resp.status != 200:
                    return {"error": f"HTTP {resp.status}"}
                
                raw = await resp.json()
                if "data" not in raw:
                    return {"error": "No data in response"}
                
                try:
                    decrypted = self._aes256_ecb_decrypt(raw["data"])
                    result = json.loads(decrypted)
                    return result
                except Exception as e:
                    return {"error": f"Decrypt error: {e}"}

    async def get_tags(self, phone: str, country_code: str = "RU") -> dict:
        """
        Получить теги (имена из телефонной книги)
        """
        timestamp = str(int(time.time()))
        
        req_obj = {
            "countryCode": country_code,
            "source": "details",
            "token": self.token,
            "phoneNumber": phone,
        }
        
        req_json = json.dumps(req_obj, separators=(',', ':'))
        sign_data = timestamp + "-" + req_json
        signature = self._sha256_hmac(sign_data)
        crypt = self._aes256_ecb_encrypt(req_json)
        body = '{"data":"' + crypt + '"}'
        
        headers = {
            "X-App-Version": "4.9.1",
            "X-Token": self.token,
            "X-Os": "android 5.0",
            "X-Client-Device-Id": self.device_id,
            "Accept-Encoding": "deflate",
            "X-Req-Timestamp": timestamp,
            "X-Req-Signature": signature,
            "X-Encrypted": "1",
            "Content-Type": "application/json",
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://pbssrv-centralevents.com/v2.5/number-detail",
                data=body,
                headers=headers,
                timeout=aiohttp.ClientTimeout(total=15),
            ) as resp:
                if resp.status != 200:
                    return {"error": f"HTTP {resp.status}"}
                
                raw = await resp.json()
                if "data" not in raw:
                    return {"error": "No data in response"}
                
                try:
                    decrypted = self._aes256_ecb_decrypt(raw["data"])
                    result = json.loads(decrypted)
                    return result
                except Exception as e:
                    return {"error": f"Decrypt error: {e}"}
