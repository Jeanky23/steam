class Profile:
    def __init__(self,id,username,email,password,status="online",level=0):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.status = status
        self.level =  level

    def show(self):
        print("El id es: ",self.id)
        print("El nombre de usuario es: ",self.username)
        print("El email es: ",self.email)
        print("La contraseña es: ",self.password)
        print("Estado: ",self.status)
        print("Nivel: ",self.level)

    def change_pass(self):
        self.password = input("Ingrese nueva contraseña: ")
