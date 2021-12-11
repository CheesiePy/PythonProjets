"""
Student: May lindenberg
ID: 203132949
Assignment no. 5
program: num_sums.py
"""

def num_sums(n, num_parts):
    """
    param: n: positive natural number.
    param:num_part: list with positive natural numbers
    returns: the number of possibal disassembles of n using the elements in num_parts
    """
    counter = 0
    for val in num_parts: # val == 1
        if val < n:
            counter += num_sums(n-val, num_parts)
        if n == val:
               return counter + 1
    return counter

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
    input_file = "input_ex2.txt"
    output_file = "output_ex2.txt"
    with open(input_file, "r") as reader, open(output_file, "w") as writer:
        f = reader.readlines()
        if input_chuck(f) == True:
            n = [int(f[i][0]) for i in range(len(f))] # n == list of the first nun in every line
            num_list = [[int(f[i][j]) for j in range(1, len(f[i])) if f[i][j].isdigit()] for i in range(len(f))] # return a nested list of all the non first nums in every line
            num_list_fix = [sorted(i) for i in num_list]
            for i in range(len(n)): ## this for loop is used for writing the num_sums of the n[i] teamed with num_list[i] for every element in n
                x = num_sums(n[i], num_list_fix[i])
                writer.write(str(x))
                writer.write("\n")
            writer.close()
            print('Done! please check "{0}"'.format(output_file))
            print(num_list_fix)
        else:
            print("Error invalid input in txt file.")
    reader.close()
    writer.close()

main()
