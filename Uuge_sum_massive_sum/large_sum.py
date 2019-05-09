def get_data():
    num_list = []
    input_file = open('/home/gtimm/Documents/Projects/ProjectEuler/Uuge_sum_massive_sum/data.txt')

    for line in input_file:
        num_list.append(str.strip(line))

    return num_list

def git_sum(num_list):
    accumulator = 0

    for i in range(len(num_list)):
        accumulator += int(num_list[i])

    print(accumulator)
    return(accumulator)

if __name__ == "__main__":
    num_list = get_data()
    git_sum(num_list)
