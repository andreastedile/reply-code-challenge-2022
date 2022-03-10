import os


class Demon:
    def __init__(self, index: int, required_stamina: int, rest_time: int, recovered_stamina: int, fragments: list[int]):
        self.index = index
        self.required_stamina = required_stamina
        self.rest_time = rest_time
        self.recovered_stamina = recovered_stamina
        self.fragments = fragments

    def __str__(self):
        return f"Demon ({self.index}) requires {self.required_stamina}, gives {self.recovered_stamina} after {self.rest_time} turns, has {len(self.fragments)} fragments: {self.fragments}"


class Pandora:
    def __init__(self, stamina: int, max_stamina: int):
        self.stamina = stamina
        self.max_stamina = max_stamina

    def __str__(self):
        return f"Pandora has {self.stamina}/{self.max_stamina} stamina"

    def kill_demon(self, demon: Demon):
        self.stamina -= demon.required_stamina

    def gain_stamina(self, stamina: int):
        self.stamina = min(self.max_stamina, self.stamina + stamina)


class Simulation:
    def __init__(self, n_turns: int, pandora: Pandora, demons: list[Demon]):
        self.current_turn = 0
        self.max_turns = n_turns
        self.pandora = pandora
        self.demons = demons
        self.defeated: list[Demon] = []

        self.stamina_schedule: [int] = [0 for _ in range(n_turns)]  # schedule stamina

    def __str__(self):
        f"current turn: {self.current_turn}/{self.max_turns}"

    def run(self):
        while self.current_turn < self.max_turns:
            print(f"{self.current_turn}")
            self.tick()

    def tick(self):
        self.pandora.gain_stamina(self.stamina_schedule[self.current_turn])

        demon = self.chose_demon()
        if demon:
            self.pandora.kill_demon(demon)
            self.defeated.append(demon)
            self.demons.remove(demon)

            # schedule the stamina to be recovered in the future
            if self.current_turn + demon.rest_time < self.max_turns:
                self.stamina_schedule[self.current_turn + demon.rest_time] += demon.recovered_stamina

        self.current_turn += 1
        pass

    def chose_demon(self) -> Demon | None:
        defeatable = [demon for demon in self.demons if demon.required_stamina <= self.pandora.stamina]
        defeatable.sort(key=lambda demon: (demon.recovered_stamina - demon.required_stamina) / demon.rest_time,
                        reverse=True)

        return defeatable.pop(0) if len(defeatable) > 0 else None

    def write_solution(self, filename: str):
        with open("./results/" + filename + "_OUT.txt", "w") as f:
            for demon in self.defeated:
                f.write(str(demon.index))
                f.write("\n")
            for demon in self.demons:
                f.write(str(demon.index))
                f.write("\n")


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
        simulation.run()

        print("Defeated demons:")
        for demon in simulation.defeated:
            print(demon)
        print("Remaining demons:")
        for demon in simulation.demons:
            print(demon)
        print(f"Pandora: {pandorina}")

        filename: str = dataset_name.replace("./datasets/", "").replace(".txt", "")
        simulation.write_solution(filename)


if __name__ == "__main__":
    content = os.listdir("./datasets/")
    # content = ["00-example.txt"]
    for file in content:
        main("./datasets/" + file)
