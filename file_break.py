import os

fileR = open("doge.jpg", "rb")

chunk = 0

byte = fileR.read(1024)

while byte:
    if chunk == 0: print(byte)

    fileN = 'chunk'+ str(chunk) + ".txt"
    fileT = open(fileN, "wb")
    fileT.write(byte)
    fileT.close()

    byte = fileR.read(1024)
    chunk += 1

