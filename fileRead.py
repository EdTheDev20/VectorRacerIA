from dataStructures import Track

pista = Track()
pista.setEnv(pista.readTrack)

for i in range(len(pista.env)):
    for j in range(len(pista.env[0])):
        print(pista.env[i][j],end="")
    print()