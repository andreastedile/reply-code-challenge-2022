import os


class Demon:
    def __init__(self, index: int, required_stamina: int, rest_time: int, recovered_stamina: int, fragments: list[int]):
        self.index = index
        self.stamina = required_stamina
        self.rest_time = rest_time
        self.recovery = recovered_stamina
        self.fragments = fragments

    def __str__(self):
        return f"Demon ({self.index}) requires {self.stamina}, gives {self.recovery} after {self.rest_time} turns, has {len(self.fragments)} fragments: {self.fragments}"


class Pandora:
    def __init__(self, stamina: int, max_stamina: int):
        self.stamina = stamina
        self.max_stamina = max_stamina

    def __str__(self):
        return f"Pandora has {self.stamina}/{self.max_stamina} stamina"


class Simulation:
    def __init__(self, n_turns: int, pandora: Pandora, demons: list[Demon]):
        self.current_turn = 0
        self.max_turns = n_turns
        self.pandora = pandora
        self.demons = demons
        self.defeated = []

    def __str__(self):
        f"current turn: {self.current_turn}/{self.max_turns}"

    def run(self):
        while self.current_turn < self.max_turns:
            self.tick()

    def tick(self):
        self.current_turn += 1
        pass


def main(dataset_name: str):
    print(f"working on {dataset_name}")

    with open(dataset_name) as f:
        firstline = f.readline().split()
        stamina_pandora = int(firstline[0])
        max_stamina = int(firstline[1])
        turns = int(firstline[2])

        pandorina = Pandora(stamina_pandora, max_stamina)
        print(f"Pandora: {pandorina}")

        n_demons = int(firstline[3])
        demons: list[Demon] = []
        for i in range(n_demons):
            line = f.readline().split()
            required_stamina = int(line[0])
            rest_time = int(line[1])
            recovery = int(line[2])
            fragments = []
            if line[3] != 0:
                fragments: list[int] = [int(x) for x in line[4:-1] + [line[-1]]]
            demons.append(Demon(i, required_stamina, rest_time, recovery, fragments))

        simulation = Simulation(turns, pandorina, demons)

        for demon in demons:
            print(demon)

        filename: str = dataset_name.replace("./datasets/", "").replace(".txt", "")
        with open("./results/" + filename + "_OUT.txt", "w") as f:
            for demon in simulation.defeated:
                f.write(demon.index)
                f.write("\n")


if __name__ == "__main__":
    content = os.listdir("./datasets/")
    content = ["00-example.txt"]
    for file in content:
        main("./datasets/" + file)
