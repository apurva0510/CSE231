import string


def add_name(name_map, name_list):
    if name_list[0] not in name_map:
        name_map[name_list[0]] = int(name_list[1])
    else:
        name_map[name_list[0]] += int(name_list[1])


def build_map(in_file, name_map):
    for line in in_file:
    
        if line.startswith("Name"):
            continue
        else:
            name_list = line.split()
        
        add_name(name_map, name_list)


def display_map(name_map):
    name_list = list(name_map.items())
    name_list.sort(key=lambda x: x[0])

    print("{:10s}{:10s}".format("Name", "Total"))
    for item in name_list:
        print("{:10s}{:<10d}".format(item[0], item[1]))


def open_file(file):
    in_file = open(file, "r")

    return in_file


def main():
    name_map = {}

    in_file = open_file("data1.txt")
    build_map(in_file, name_map)

    in_file = open_file("data2.txt")
    build_map(in_file, name_map)

    display_map(name_map)
    in_file.close()


if __name__ == "__main__":
    main()