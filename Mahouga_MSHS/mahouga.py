

class MahougaSolver():
    def __init__(self):
        self.rows = 3
        self.values = {
            "row": [],
            "column": [],
            "diagonal": []
        }
        self.magic_square = {
            "row": [],
            "column": [],
            "diagonal": [],
        }
    
    def build_magic_square(self, row1: list[int], row2: list[int], row3: list[int]):
        self.magic_square["row"].append(row1)
        self.magic_square["row"].append(row2)
        self.magic_square["row"].append(row3)
        self.magic_square["column"].append([row1[0], row2[0], row3[0]])
        self.magic_square["column"].append([row1[1], row2[1], row3[1]])
        self.magic_square["column"].append([row1[2], row2[2], row3[2]])
        self.magic_square["diagonal"].append([row1[0], row2[1], row3[2]])     
        self.magic_square["diagonal"].append([row1[2], row2[1], row3[0]])
    
    def calculate_horizontals(self):
        for row in self.magic_square["row"]:
            self.values["row"].append(row[0] + row[1] + row[2])
        return 0

    def calculate_verticals(self):
        for column in self.magic_square["column"]:
            self.values["column"].append(column[0] + column[1] + column[2])
        return 0

    def calculate_diagonals(self):
        for diagonal in self.magic_square["diagonal"]:
            self.values["diagonal"].append(diagonal[0] + diagonal[1] + diagonal[2])
        return 0
    
    def calculate_magic_square(self):
        occurance = []
        print(self.values)
        for key, value in self.values.items():
            for num in value:
                if num in occurance:
                    pass
                else:
                    occurance.append(num)

        print(occurance)
        if len(occurance) != 1:
            return False
        else:
            return True