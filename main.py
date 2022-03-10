import os


def main(dataset_name: str):
    with open(dataset_name) as f:
        lines = f.readlines()
        lines = [line.removesuffix("\n") for line in lines]

    filename: str = dataset_name.replace("./datasets/", "").replace("txt", "")
    print(filename)
    with open("./results/" + filename + "_OUT.txt", "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    content = os.listdir("./datasets/")
    for file in content:
        main("./datasets/" + file)
