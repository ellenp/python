class expense:

    def __init__(self, amount=0.00 :float, category="OTHERS" : str, description = "" : str):
        self.category = category
        self.amount = amount
        self.description = description

    def set_category(self, category:str):
        self.category = category

    def get_category(self):
    	return self.category

    def set_amount(self, amount:float):
        self.amount = amount

    def get_amount(self):
    	self.amount

    def set_description(self, description:str):
        self.description = description

    def get_description(self):
    	return self.description