# Реализуйте класс Time, описывающий время на цифровых часах.
# При создании экземпляра класс должен принимать два аргумента в следующем порядке:
# hours — количество часов; каждые 24 часа должны преобразовываться в 0 часов
# minutes — количество минут; каждые 60 минут должны преобразовываться в 1 час
# Экземпляр класса Time должен иметь следующее неформальное строковое представление:
# <количество часов в формате HH>:<количество минут в формате MM>
# Также экземпляры класса Time должны поддерживать между собой операцию сложения с помощью операторов + и +=

class Time:
    def __init__(self, hours, minutes):
        self.hours, self.minutes = Time.normalize(hours, minutes)
    
    @staticmethod
    def normalize(hours, minutes):
        return (hours + minutes // 60) % 24, minutes % 60
    
    def __str__(self):
        return f'{self.hours:02d}:{self.minutes:02d}'
        
    def __add__(self, other):
        if isinstance(other, Time):
            return Time(*Time.normalize(self.hours + other.hours, self.minutes + other.minutes))
        return NotImplemented
    
    def __iadd__(self, other):
        if isinstance(other, Time):
            self.hours, self.minutes = Time.normalize(self.hours + other.hours, self.minutes + other.minutes)
            return self
        return NotImplemented
    

