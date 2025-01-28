class OperasBas:
    #declarion de propiedades
    num1=0 #public
    _um2=0 #private
    __res=0 #protected
    #declaracon del constructor
    def __init__(self,num1,um2):
        self.num1=num1
        self.um2=um2
    #declaracion de metodos de clase
    def suma(self):
        self.res=self.num1+self.um2
        print("La suma es: {}".format(self.res))

    def resta(self):
            self.res=self.num1-self
            print("La resta es: {}".format(self.res))

    def main():
         obj=OperasBas(3,4)
         obj.suma()
    if __name__ == "__main__":
         main()