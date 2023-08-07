tenho_sede = True
tenho_fome = False
esta_frio = True
estou_em_dieta = False

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
