class Diamond:
    def __init__(self, diamond_id, carat, cut, color, clarity, depth, table, price, x, y, z):
        self.id = int(diamond_id)
        self.carat = float(carat)
        self.cut = cut  
        self.color = color
        self.clarity = clarity
        self.depth = float(depth)
        self.table = float(table)
        self.price = float(price)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
        return f"Id: {self.id}, Carat: {self.carat}, Cut: {self.cut}, Color: {self.color}, Clarity: {self.clarity}, " \
               f"Depth: {self.depth}, Table: {self.table}, Price: {self.price}, " \
               f"X: {self.x}, Y: {self.y}, Z: {self.z}"
