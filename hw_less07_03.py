# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять
# увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

class Cell:
    def __init__(self, param=int):
        self.param = param

    def __add__(self, other):
        return f"Сложение двух ячеек дает новую клетку с {self.param + other.param} ячейками"

    def __sub__(self, other):
        if self.param > other.param:
           return f"При вычитании образуется новая клетка с {self.param - other.param} ячейками"
        else:
            print(f"Операция невозможна")

    def __mul__(self, other):
        return f"При умножении образуется новая клетка с {self.param * other.param} ячейками"

    def __floordiv__(self, other):
        return f"При делении образуется новая клетка с {self.param // other.param} ячейками"

    def make_order(self, in_row):
        result = " "
        for i in range((int(self.param / in_row))):
            result += "*" * in_row + "\n"
            result += "*" * (self.param % in_row) + "\n"
        return result

cell_1 = Cell(16)
cell_2 = Cell(2)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(4))
