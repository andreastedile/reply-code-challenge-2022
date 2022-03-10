def main(dataset_name: str):
    with open(dataset_name) as f:
        lines = f.readlines()
        lines = [line.removesuffix("\n") for line in lines]
        print(lines)
    with open("output.txt", "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main("datasets/test.txt")
