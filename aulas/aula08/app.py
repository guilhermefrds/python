tenho_sede = False
tenho_fome = False
esta_frio = True
estou_em_dieta = True


if tenho_sede:
    print("beber agua")

print("Vida que segue")

print("--------------------------------------------")


if esta_frio:
    print("Vista um casaco")
else:
    print("vestir camiseta")

print("--------------------------------------------")

if tenho_sede or tenho_fome:
    print("ir na cozinha")
else:
    print("ficar vendo netflix")

print("--------------------------------------------")

#if tenho_sede and tenho_fome:
#    print("fazer sanduiche e uma coquinha")
#else:
#    print("nao tenho fome ou nao tenho sede")

print("--------------------------------------------")

if tenho_sede and tenho_fome:
    print("fazer sanduiche e uma coquinha")
elif tenho_sede and not(tenho_fome):
    if estou_em_dieta:
        print("tomar agua")
    else:
        print("tomar uma coquinha apenas")
elif not(tenho_sede) and tenho_fome:
    print("fazer um sandubas apenas")
else:
    print("ficar vendo netflix")

