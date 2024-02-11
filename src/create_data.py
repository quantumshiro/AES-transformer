from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import pandas as pd

def generate_data_modified(num_plain_texts=1000, num_encryptions_per_key=100):
    data = []
    for _ in range(num_plain_texts):
        plain_text = get_random_bytes(16)  # 16 bytes = 128 bits
        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC)
        for _ in range(num_encryptions_per_key):
            encrypted_text = cipher.encrypt(plain_text)
            # Convert bytes to hex string for easier handling
            data.append({
                'plain_text': plain_text.hex(), 
                'encrypted_text': encrypted_text.hex(), 
                'key': key.hex()
            })
    return data

# Generate the data
data = generate_data_modified()

# Create a DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('data/data.csv', index=False)
