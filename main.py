import os


class Demon:
    def __init__(self, index: int, stamina: int, resttime: int, recovery: int, fragments: list[int]):
        self.index = index
        self.stamina = stamina
        self.rest_time = resttime
        self.recovery = recovery
        self.fragments = fragments

    def __str__(self):
        return f"Demon ({self.index}) requires {self.stamina} (gives {self.recovery} after {self.rest_time} turns) and has {len(self.fragments)} fragments ({self.fragments})"


class Pandora:
    def __init__(self, stamina: int, max_stamina: int, turns: int):
        self.stamina = stamina
        self.max_stamina = max_stamina
        self.turns = turns

    def __str__(self):
        return f"Pandora has {self.stamina} stamina (out of {self.max_stamina}) and {self.turns} turns"


def main(dataset_name: str):
    print(f"working on {dataset_name}")

    with open(dataset_name) as f:
        firstline = f.readline().split()
        pandorina = Pandora(int(firstline[0]), int(firstline[1]), int(firstline[2]))
        demons: list[Demon] = []
        for i in range(int(firstline[3])):
            line = f.readline().split()
            stamina = int(line[0])
            resttime = int(line[1])
            recovery = int(line[2])
            fragments = []
            if line[3] != 0:
                fragments: list[int] = [int(x) for x in line[4:-1] + [line[-1]]]
            demons.append(Demon(i, stamina, resttime, recovery, fragments))

    print(pandorina)
    for demon in demons:
        print(demon)

    filename: str = dataset_name.replace("./datasets/", "").replace("txt", "")
    # with open("./results/" + filename + "_OUT.txt", "w") as f:


if __name__ == "__main__":
    content = os.listdir("./datasets/")
    content = ["00-example.txt"]
    for file in content:
        main("./datasets/" + file)
