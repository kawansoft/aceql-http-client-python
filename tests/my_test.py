import os

print("1")
try:
    os.remove("filename")
except Exception as e:
    pass
print("2")
