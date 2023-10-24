class SymbolEntry:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class SymbolTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.table = [[] for _ in range(table_size)]

    def hash(self, key):
        hash_val = sum(ord(c) for c in key)
        return hash_val % self.table_size

    def insert(self, name, value):
        index = self.hash(name)
        entry = SymbolEntry(name, value)
        self.table[index].append(entry)

    def lookup(self, name):
        index = self.hash(name)
        for entry in self.table[index]:
            if entry.name == name:
                return entry.value
        return -1  # Return -1 to indicate that the variable is not found


if __name__ == "__main__":
    symbol_table = SymbolTable(10)

    symbol_table.insert("x", 5)
    symbol_table.insert("y", 10)

    print("Value of x:", symbol_table.lookup("x"))
    print("Value of y:", symbol_table.lookup("y"))
    print("Value of z:", symbol_table.lookup("z"))
