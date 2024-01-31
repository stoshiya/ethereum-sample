from web3 import Web3
from eth_account.messages import encode_defunct

# Web3ライブラリを使ってアカウント作成
account = Web3().eth.account.create()

# 作成したアカウントから秘密鍵と公開鍵を取得
private_key = account._private_key
public_key = account.address

# メッセージ(任意)
message = "Hello, world!"

# メッセージをハッシュ化
message_hash = encode_defunct(text=message)

# ハッシュ化したメッセージを署名
w3 = Web3()
signed_message = w3.eth.account.sign_message(message_hash, private_key=private_key)

# ハッシュ化したメッセージを署名で検証
signer = w3.eth.account.recover_message(message_hash, signature=signed_message.signature)

print(f"Private Key: {private_key}")
print(f"Public Key: {public_key}")
print(f"Message: {message}")
print(f"Message Hash: {message_hash}")
print(f"Signed Message: {signed_message}")
print(f"Signer: {signer}")

# 署名者が期待する公開鍵と一致するかを確認
if signer == public_key:
    print("Signature is valid!")
else:
    print("Signature is invalid!")
