class SmartDevice:
    def __init__(self, nom):
        self.nom = nom
        self.__holat = False

    def turn_on(self):
        self.__holat = True
        print(f"{self.nom} yoqildi.")

    def turn_off(self):
        self.__holat = False
        print(f"{self.nom} o'chirildi.")

    def get_status(self):
        return "on" if self.__holat else "off"


class SmartHome:
    def __init__(self):
        self.devices = {}

    def add_device(self, device):
        self.devices[device.nom] = device

    def control_device(self, nom, action):
        if nom in self.devices:
            device = self.devices[nom]
            if action == "on":
                device.turn_on()
            elif action == "off":
                device.turn_off()
        else:
            print(f"{nom} topilmadi.")

    def show_all(self):
        for d in self.devices.values():
            print(f"{d.nom}: {d.get_status()}")


class Guest:
    def __init__(self, smart_home):
        self.smart_home = smart_home

        self.restricted = ["Xavfsizlik kamerasi"]

    def control_device(self, nom, action):
        if nom in self.restricted:
            print(f"⚠️ Sizga '{nom}' qurilmasini boshqarish taqiqlangan!")
        else:
            self.smart_home.control_device(nom, action)



light = SmartDevice("Chiroq")
camera = SmartDevice("Xavfsizlik kamerasi")


home = SmartHome()
home.add_device(light)
home.add_device(camera)


print(">>> Asosiy foydalanuvchi:")
home.control_device("Chiroq", "on")
home.control_device("Xavfsizlik kamerasi", "on")
home.show_all()

print("\n>>> Guest foydalanuvchi:")
guest = Guest(home)
guest.control_device("Chiroq", "off")
guest.control_device("Xavfsizlik kamerasi", "off")
home.show_all()
