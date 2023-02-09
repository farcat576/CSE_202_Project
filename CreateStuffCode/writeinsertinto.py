
file_name = "TryCSV_Sheet1.csv"
string_indices = [1,2] # indices of the columns that are strings

with open(file_name, "r+") as f:

    # read the file line by line and append "insert into table values(" to  start of each line and ")\n" to the end of each line

    #read the file line by line into a list
    lines = f.readlines()
    # split the list into a list of lists
    lines = [line.split(',') for line in lines]

    for i in lines:
        for j in range(len(i)):
            if j in string_indices:
                i[j] = "'" + i[j] + "'"

    # reconstruct the list into a list of strings
    lines = [','.join(line) for line in lines]

    # add the "insert into table values(" to  start of each line and ")\n" to the end of each line
    lines = ["insert into table values(" + line.strip() + ");\n" for line in lines]




    with open("new_file.txt", "w") as f2:
        f2.writelines(lines)

print(lines)
