import math

class Pagination():

    def __init__(self, items=None, page_size=10):
        if items is None:
            self.items = []
        else:
            self.items = items
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)


    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        if page_num > self.total_pages or page_num < 1:
            raise ValueError("Page number out of range")
        self.current_idx = page_num - 1
    
    def first_page(self):
        self.current_idx = 0

    def last_page(self):
        self.current_idx = self.total_pages - 1

    def next_page(self):
        if self.current_idx != self.total_pages - 1:
            self.current_idx += 1
        else:
            print("This is the last page")
    
    def previous_page(self):
        if self.current_idx != 0:
            self.current_idx -= 1
        else:
            print("This is the first page")
    
    def __str__(self):
        str = ""
        items = self.items
        start = self.current_idx * self.page_size
        end = start + self.page_size
        # print("start", start)
        # print("end", end)
        while start < end and start < len(items):
            str += (f"{items[start]}\n")
            start += 1
        return str


if __name__ == "__main__":
    try:
        # p = Pagination(["a", "b", "c", "d", "e", "f"], page_size=2)
        # print(p.get_visible_items())
        # p.go_to_page(1)
        # print(p.get_visible_items())
        # p.go_to_page(3)
        # # p.go_to_page(30)
        # p.last_page()
        # p.next_page()
        # print(p.get_visible_items())
        # p.first_page()
        # p.previous_page()
        # print(p.get_visible_items())
        # print(p.__str__())
        
        alphabetList = list("abcdefghijklmnopqrstuvwxyz")
        p = Pagination(alphabetList, 4)

        print(p.get_visible_items())
        # ['a', 'b', 'c', 'd']

        p.next_page()
        print(p.get_visible_items())
        # ['e', 'f', 'g', 'h']

        p.last_page()
        print(p.get_visible_items())
        # ['y', 'z']

        # p.go_to_page(10)
        print(p.current_idx + 1)
        # Output: 7

        p.go_to_page(0)
        # Raises ValueError
        

    except Exception as e:
        print(f"Error: {e}")
