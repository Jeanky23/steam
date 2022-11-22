class Profile:
    def __init__(self,id,username,email,password,status="online",level=0):
        self.id=id
        self.username=username
        self.email=email
        self.password=password
        self.status=status
        self.level=level

    def print2(self):
        print("El id es: ",self.id)
        print("El nombre de usuario es: ",self.username)
        print("El email es: ",self.email)
        print("La contraseña es: ",self.password)
        print("Estado: ",self.status)
        print("Nivel: ",self.level)

    def changepass(self,new_password):
        self.username=input("Ingrese su nombre de usuario: ")
        self.password=input("Ingrese su contraseña: ")
        self.new_password=input("Para cambiar contraseña, ingrese nueva contraseña: ")

        if (self.new_password == self.password):
            print("Favor de elejir una contraseña distinta a la anterior.")
            else:
            (self.password = self.new_password)
