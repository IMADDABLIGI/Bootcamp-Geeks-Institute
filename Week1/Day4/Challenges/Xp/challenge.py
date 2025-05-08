class Pagination():

    def __init__(self, items, page_size=10):
        if items:
            self.items = items
        else:
            self.items = []
        self.page_siwe = page_size
        self.current_idx = 0