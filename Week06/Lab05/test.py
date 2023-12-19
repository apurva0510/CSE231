file = input("Input a file: ")

while True:
    try:
        fp = open(file)
        break
    except FileNotFoundError:
        print("\nFile does not exist.")
        file = input("Input a file: ")

name = ()
exam1 = ()
exam2 = ()
exam3 = ()
exam4 = ()
mean = ()

exam1_mean = 0
exam2_mean = 0
exam3_mean = 0
exam4_mean = 0

for line in fp:
    line_list = line.split()

    name_str = line_list[0] + ' ' + line_list[1]
    
    name = name + (name_str,)

    exam1 = exam1 + (line_list[2],)
    exam1_int = int(line_list[2])

    exam2 = exam2 + (line_list[3],)
    exam2_int = int(line_list[3])

    exam3 = exam3 + (line_list[4],)
    exam3_int = int(line_list[4])

    exam4 = exam4 + (line_list[5],)
    exam4_int = int(line_list[5])

    mean_float = (exam1_int + exam2_int + exam3_int + exam4_int) / 4
    mean = mean + (mean_float,)

    exam1_mean += exam1_int
    exam2_mean += exam2_int
    exam3_mean += exam3_int
    exam4_mean += exam4_int

exam1_mean /= len(exam1)
exam2_mean /= len(exam2)
exam3_mean /= len(exam3)
exam4_mean /= len(exam4)

fp.close()

print("\n{:20s}{:>6s}{:>6s}{:>6s}{:>6s}{:>10s}".format("Name", "Exam1", "Exam2", "Exam3", "Exam4", "Mean"))
for i in range(len(name)):
    print("{:20s}{:>6s}{:>6s}{:>6s}{:>6s}{:>10.2f}".format(name[i], exam1[i], exam2[i], exam3[i], exam4[i], mean[i]))
print("{:20s}{:>6.1f}{:>6.1f}{:>6.1f}{:>6.1f}".format("Exam Mean", exam1_mean, exam2_mean, exam3_mean, exam4_mean))