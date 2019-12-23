# - Определите класс с именем Lamp. 

# - Он будет иметь строковый атрибут для цвета и логический атрибут on, который будет указывать, 
# включена лампа или нет. 

# - Определите конструктор вашего класса с параметром для цвета и присвойте ему значение false при 
# инициализации.

# - Дайте лампе метод экземпляра toggle_switch, который переключит значение атрибута on.

# - Определите другой экземплярный метод с именем state, который будет возвращать «Лампа включена». 
# Если он включен и "Лампа выключена". в противном случае.

# implement the Lamp class
class Lamp:
	on_true = True
	on_false = False
	def __init__(self, color: str):
		self.color = color
		self.on = False
    
	def toggle_switch(self):
		self.on = True if self.on == False else False 
        
	def state(self):
		if self.on == True:
			return "The lamp is on."
		else:
			return "The lamp is off."

