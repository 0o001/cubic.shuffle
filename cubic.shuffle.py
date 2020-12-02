class CubicShuffle:

    @staticmethod
    def __reshape(lst, n):
        return [lst[i * n: (i + 1) * n] for i in range(len(lst) // n)]

    @staticmethod
    def __createCube(text, shape = 5):
        cube = [char for char in text]

        if len(cube) % shape != 0:
            cube.extend([' '] * (len(cube) % shape))

        cube = CubicShuffle.__reshape(cube, shape)

        return cube

    @staticmethod
    def __shiftCubeRight(cube, turnCount, position):
        for shift in cube:
            for loop in range(turnCount):
                shift.insert(position, shift.pop())

        return cube

    @staticmethod
    def __shiftCubeLeft(cube, turnCount, position):
        for shift in cube:
            for loop in range(turnCount):
                shift.append(shift.pop(position))

        return cube

    @staticmethod
    def __shiftCubeDown(cube, turnCount, position):
        for shift in range(turnCount):
            cube.insert(position, cube.pop())

        return cube

    @staticmethod
    def __shiftCubeUp(cube, turnCount, position):
        for shift in range(turnCount):
            cube.append(cube.pop(position))

        return cube

    @staticmethod
    def __cubeToFlatList(cube):
        flat_list = []
        for sublist in cube:
            for item in sublist:
                flat_list.append(item)

        return flat_list

    @staticmethod
    def shuffle(text, keyString):
        [shape, keys] = keyString.split("-")

        cube = CubicShuffle.__createCube(text, int(shape))
        keys = keys.split(",")

        for key in keys:
            [direction, turnCount, position] = key.split(":")

            turnCount = int(turnCount)
            position = abs(int(position))

            if direction == "r":
                cube = CubicShuffle.__shiftCubeRight(cube, turnCount, position)

            if direction == "l":
                cube = CubicShuffle.__shiftCubeLeft(cube, turnCount, position)

            if direction == "d":
                cube = CubicShuffle.__shiftCubeDown(cube, turnCount, position)

            if direction == "u":
                cube = CubicShuffle.__shiftCubeUp(cube, turnCount, position)

        cube = CubicShuffle.__cubeToFlatList(cube)

        return "".join(cube)

    @staticmethod
    def deshuffle(suffledText, keyString):
        [shape, keys] = keyString.split("-")

        keys = keys.split(",")
        keys = keys[::-1]

        keyString = shape + "-" + ",".join(keys)

        [shape, keys] = keyString.split("-")

        cube = CubicShuffle.__createCube(suffledText, int(shape))
        keys = keys.split(",")

        for key in keys:
            [direction, turnCount, position] = key.split(":")

            turnCount = int(turnCount)
            position = abs(int(position))

            if direction == "r":
                cube = CubicShuffle.__shiftCubeLeft(cube, turnCount, position)

            if direction == "l":
                cube = CubicShuffle.__shiftCubeRight(cube, turnCount, position)

            if direction == "d":
                cube = CubicShuffle.__shiftCubeUp(cube, turnCount, position)

            if direction == "u":
                cube = CubicShuffle.__shiftCubeDown(cube, turnCount, position)

        cube = CubicShuffle.__cubeToFlatList(cube)
        
        return "".join(cube)