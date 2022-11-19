

class ColumnMeta:
    def __init__(self, name: str, nullable: bool, dtype: str, char_max_len: int, is_unique: bool, udt_name: str):
        self.name = name.lower()
        self.nullable = nullable
        self.dtype = dtype.lower()
        self.char_max_len = char_max_len
        self.is_unique = is_unique
        self.udt_name = udt_name.lower()

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"""name={self.name} nullable={self.nullable} dtype={self.dtype} char_max_len={self.char_max_len}""" \
               + f" is_unique={self.is_unique} udt_name={self.udt_name}"
