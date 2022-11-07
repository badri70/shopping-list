class Operations:
    def __init__(self, file_name, operation):
        self.file_name = file_name
        self.operation = operation

    def _read_lines(self):
        with open(self.file_name, 'r') as f:
            result = f.readlines()
            return result

    def add_products(self):
        products = input("Enter product: ")
        price = input("Enter its price: ")

        result = products.title() + "-" + price

        with open(self.file_name, 'a') as f:
            f.write("\n" + result)

    def total(self):
            lines = self._read_lines()
            sum = 0
            for el in lines:
                el = el.split("-")
                sum += int(el[1])
            print(sum)

    def delete(self):
        product = input("Enter product: ")
        product = product.title()
        lines = self._read_lines()

        with open(self.file_name, 'w') as f:
            for line in lines:
                if product not in line:
                    f.write(line)

    def update(self):
        product = input("Enter product: ")
        price = input("Enter its price: ")
        product = product.title()
        lines = self._read_lines()

        with open(self.file_name, 'w') as f:
            for line in lines:
                if product not in line:
                    f.write(line)
                else:
                    f.write(product+"-"+price)
