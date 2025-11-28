from src.product import Product


class Category:
    category_count = 0
    product_count = 0
    all_products_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """Для класса Category определите следующие свойства:
        название (name),
        описание (description),
        список товаров категории (products)."""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.all_products_count += len(products) if products else 0

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @property
    def product_in_list(self):
        return self.__products

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    # @products.setter
    # def products(self, product: Product):
    #     self.__products.append(product)
    #     Category.all_products_count += 1
