class calculator:
    """Calculator for vector operations"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result = sum(v1 * v2 for v1, v2 in zip(V1, V2))
        print(result)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        result = [v1 + v2 for v1, v2 in zip(V1, V2)]
        print(result)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        result = [v1 - v2 for v1, v2 in zip(V1, V2)]
        print(result)
