class Calcular_Edades:

    @staticmethod
    def calcular_edadalbert(edjuan):
        return (2 * edjuan) / 3

    @staticmethod
    def calcular_edadana(edjuan):
        return(4 * edjuan) / 3

    @staticmethod
    def calcular_edadmama(edjuan,edadalbert,edadana):
        return edjuan + edadalbert + edadana
    
edjuan = int(input("Ingrese la edad de Juan\n"))
edadalbert = Calcular_Edades .calcular_edadalbert(edjuan)
edadana = Calcular_Edades .calcular_edadana(edjuan)
edadmama = Calcular_Edades.calcular_edadmama(edjuan, edadalbert, edadana)
print(f"La edad de Juan es:{edjuan}\n"+f"La edad de Alberto es:{edadalbert}\n" +
    f"La edad de Ana es: {edadana}\n" + f"La edad de la Madre es: {edadmama}")