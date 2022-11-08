class Validator:
    def validate_name(self, name):
        if name is None:
            raise ValueError("Введите название продукта.")
        if not name.isalpha():
            raise ValueError("Название не должно содержать цифр.")

    def validate_price(self, price):
        if price is None:
            raise ValueError("Введите цену на продукт продукта.")
        if not price.isnumeric():
            raise ValueError("Цена не должно содержать букв.")