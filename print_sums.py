"""
Student: May lindenberg
ID: 203132949
Assignment no. 5
program: print_sums.py
"""
def print_sums(n, num_parts, file_path):
    """
    param: n -->  natural possitive number
    param: num_parts --> list of natural possitive numbers
    param: file_path --> the file diratory you would like to write in
    return: write the first line and call _print_sums_helper
    """
    w = file_path
    opener = "{0} as sum of {1}:".format(n,num_parts)
    w.writelines(opener)
    w.write("\n")
    _print_sums_helper(n, num_parts, file_path)


def _print_sums_helper(n, num_parts, file_path, lst=[]):
    """
    param: n -->  natural possitive number
    param: num_parts --> list of natural possitive numbers
    param: file_path --> the file diratory you would like to write in
    param: lst --> leave empty!  for collation the information inside the recurtion
    return: calls it self, coletcts the numbers from num_parts until n reaches zero zero the calls _print_values
    """
    for val in num_parts:
        if val < n:
            _print_sums_helper(n - int(val), num_parts,file_path, lst = lst + [val])
        if n == val:
            _print_values(file_path, lst + [val])

def _print_values(file_path, lst):
    """
    # this funtion writes the values _print_sums_helper gather to the file_path requsted in print_sums
    param: lst --> the lst created by _print_sums_helper
    param: file_path --> the file diratory you would like to write in
    return: writes the values in file path
    """
    w = file_path
    opener = "{0} = {1}".format(sum(lst), lst[0])
    w.write(opener)
    for i in range(1, len(lst)):
        digit = " + {0}".format(lst[i])
        w.write(digit)

    w.write("\n")


def input_chuck(list):
    """
    param: any list
    return: True if the list is legal to use
    """
    t_flag = True
    for j in range(len(list)):
        for i in list[j]:
            if i.isdigit() or i == " " or i == "," or i == "\n":
                continue
            else:
                t_flag = False

    return t_flag


def main():
    input_file = "input_ex3.txt" ## enter coustom file path to get difrent resoult
    output_file = "output_ex3.txt"
    with open(input_file, "r") as reader, open(output_file, "w") as writer:
        f = reader.readlines()
        if input_chuck(f) == True:
            n = [int(f[i][0]) for i in range(len(f))] # n == list of the first nun in every line
            num_list = [[int(f[i][j]) for j in range(1, len(f[i])) if f[i][j].isdigit()] for i in range(len(f))] # return a nested list of all the non first nums in every line
            num_list_fix = [sorted(i) for i in num_list]
            for i in range(len(n)):
                writer.write("-------------------------->\n")
                print_sums(n[i], num_list_fix[i], writer)
                writer.write("\n")
            print('Done! please check: "{0}"'.format(output_file))
            writer.write("<-------------------------->\n")

        else:
            print("Error invalid input in txt file.")
    reader.close()
    writer.close()
main()
