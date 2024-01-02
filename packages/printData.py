###############################################################################################################
# script:       readCollection.py
# description:  This script can display different information from the given collection
# version:      1.0
# creation:     December 10, 2023
# update:       December 10, 2023
###############################################################################################################
# Function(s)

# print_table. It display the information from a given table
def print_table(data):
    # Find the maximum width of each column
    column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]

    # Print the header
    for i, header in enumerate(data[0]):
        print(f"{header:<{column_widths[i]}}", end=" | ")
    print()

    # Print a separator line
    print("-" * (sum(column_widths) + len(column_widths) * 3 - 1))

    # Print the rows
    for row in data[1:]:
        for i, item in enumerate(row):
            print(f"{item:<{column_widths[i]}}", end=" | ")
        print()
    '''
    Example:
    Column 1 | ... | Column n |
    --------------------------|
    raw 1    | ... | raw 1    |
    ...      | ... | ...      |
    raw n    | ... | raw n    |
    '''