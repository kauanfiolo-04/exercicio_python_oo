from cliente import Cliente

class Conta(Cliente):
    def __init__(self, nome, cpf, idade,saldo,limite):
        Cliente.__init__(self,nome, cpf, idade)
        self.saldo=saldo
        self.limite=limite
    def depositar(self,deposito):
        self.saldo += deposito
        print(self.saldo)
    def sacar(self,saque):
        if self.saldo - saque < self.saldo:
            print("Seu limite é de:",self.limite,"R$")
            resp=input("Você n tem saldo suficiente, deseja utilizar seu limite?")
            if resp == 'sim':
                self.limite += saque
                print("Você sacou:",saque,"R$\n Seu saldo agr é de:",self.saldo,"\n Seu limite agr é de:",self.limite)
            else:
                print("Você não pode sacar, pois o saldo é menor q a quantia do saque")
        else:
            self.saldo -= saque
            print("Você sacou:",saque,"R$\n Seu saldo agr é de:",self.saldo)
    def consulta(self):
        print("Seu saldo é de:",self.saldo,"R$")
        
    