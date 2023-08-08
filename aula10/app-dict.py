meses = {
    "jan" : "Janeiro",
    "fev" : "Fevereiro",
    "marc" : "Marco",
    "abri" : "Abriu",
    "mai" : "Maio",
    "jun" : "Junho",
    "jul" : "Julho",
    "ago" : "Agosto",
    "set" : "Setembro",
    "out" : "Outubro",
    "nov" : "Novembro",
    "dez" : "Dezembro",
}

print(len(meses))
print(meses["mai"])
print(meses.get("maio"))
print(meses.get("maio","padrao"))