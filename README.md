# ethereum-sample 
Ethereumで署名と検証をするサンプルコード

## 動作環境
- Python 3.11.7
- web3.py (<https://github.com/ethereum/web3.py>)

## 使い方
```bash
$ python -m venv venv
$ source venv/bin/activate
(venv)$ pip install web3
(venv)$ python main.py
```

## 実行結果の一例
```
Private Key: b'\x97\x96\xe5fV\xc4~\xd5c\xea(k\xb9+-\xf8\xf4\xff\x1d>\x8cX\x1fWz\xa2;\xb8,\xfc\x98&'
Public Key: 0x9E0864be39228745785B3Ba94e39AfEF18F44b3C
Message: Hello, world!
Message Hash: SignableMessage(version=b'E', header=b'thereum Signed Message:\n13', body=b'Hello, world!')
Signed Message: SignedMessage(messageHash=HexBytes('0xb453bd4e271eed985cbab8231da609c4ce0a9cf1f763b6c1594e76315510e0f1'), r=94864266915549208088084793639014012179935936538649571289765151232373098723814, s=22574175102948307617578598219805865590281406599989614069097106192007956097603, v=27, signature=HexBytes('0xd1bb45b73c6ffcc0ec20078aabdea6325a2730c01d64bc8c38e1567f108ab9e631e887c362b098f91d24078432f638566cae58a473884c55d36ecb3d2c396a431b'))
Signer: 0x9E0864be39228745785B3Ba94e39AfEF18F44b3C
Signature is valid!
```
