'''
Problem 1
Ross Parsons
Z23388473
'''


def line_number(input_file: str = 'p1_Parsons_Ross.py', output_file: str = 'outfile.txt') -> None:
    """ Reads from a file and prepends a line number to each line and writes result to another file """
    while True:
        try:
            in_file = open(input_file, 'r')
            break
        except FileNotFoundError:
            input_file = input('Please enter a valid filename: ')
            raise

    output_file = open(output_file, 'w')
    for i, line in enumerate(in_file):
        i += 1  # add 1 numbers start at 1, not 0
        # prepend number to line. line has been stripped of new line characters
        line = '{}. {}\n'.format(i, line.strip())
        output_file.write(line)
    # close files
    in_file.close()
    output_file.close()


line_number('sample.txt', 'sample_out.txt')
comments = ['"""', '#']

'''
    while !eof:
        keep reading
        if """:
            while !"""
                skipping (continue)
        keeping reading starting at the 1st character right after """
'''


def strip_comments(infile):
    read_from = open(infile, 'r')
    for line in read_from:
        line_list = line.split()
        flip = 0
        for i in line_list:
            if '"""' in i:
                flip = 1
                if flip % 2 != 0:
                    continue
        print(line)

    else:
        print('Nothing left to print')


def parse_functions(infile):
    function_tuple = tuple()
    function_list = []
    read_from = open(infile, 'r')
    for line in read_from:
        line_list = line.split(' ')
        if 'def' in line_list:
            func_list = (line_list[2].split('('))
            # line number
            line_number = line_list[0].split('.')[0]
            # function name
            function_name = func_list[0]
            # signature
            signature = line_list[1] + ' ' + line_list[2] + line_list[3]
            print((line_number, function_name, signature))
    print(function_list)


# parse_functions('sample_out.txt')
strip_comments('sample.txt')
