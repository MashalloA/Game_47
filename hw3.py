class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return 
    
    @cpu.setter
    def cpu(self, value):
        self.__cpu = value
    
    @property
    def memory(self):
        return 
    
    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return f"через + :{self.__cpu + self.__memory},через * :{self.__cpu * self.__memory}"

    def __str__(self):
        return f"Computer: CPU: {self.__cpu}, MEMORY: {self.__memory}GB"

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list
    @property
    def sim_cards_list(self):
        return

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}")
        else:
            print("Неверный номер сим-карты")

    def __str__(self):
        return f"Phone info:\n sim cards: {self.__sim_cards_list}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Построение маршрута до локации {location}")

    def __str__(self):
        return (f"SmartPhone:\n "
                f"CPU: {self.cpu}, memory: {self.memory}, sim cards: {self.sim_cards_list}")

computer = Computer(16.0, 512)

phone = Phone(["Beeline", "Megacom"])

smartphone1 = SmartPhone(8, 128, ["Beeline", "O!"])
smartphone2 = SmartPhone(6, 64, ["Megacom", "Beeline"])

method1 = smartphone1.make_computations()
print(f"метод make_computations через smartphone1: {method1}")

smartphone1.use_gps("Парк Победы")
smartphone2.use_gps("Ошский рынок")

phone.call(2, "0999050888")

print(computer > smartphone2)
print(smartphone2 == smartphone1)
print(computer != smartphone1)