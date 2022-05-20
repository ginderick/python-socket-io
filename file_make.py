fileM = open("copy.jpg", "wb")

chunk = 0
chunks = 173

while chunk <= chunks:
    fileName = "chunk" + str(chunk) + ".txt"
    fileTemp = open(fileName, "rb")

    byte = fileTemp.read(1024)
    fileM.write(byte)

    chunk += 1

fileM.close()