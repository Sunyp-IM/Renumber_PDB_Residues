'''
This script is used for changing residue number by adding or subtracting an assigned value to each residue in a pdb file
Usage:
   python renumber_residue pdbfile +/- value
'''


import sys
import os.path
import operator

def check_argument(arguments):
    """
    Check if filename passed as argument exists.

    Parameters
    ----------
    arguments : list
        list of arguments passed to the script

    Returns
    -------
    string
        file name
    """
    if len(arguments) == 4:
        file_name_list = arguments[1:]
    else:
        message = """
        ERROR: missing pdb filename as argument
        usage: %s input.pdb +/- value output.pdb""" %(arguments[0])
        sys.exit(message)



def renumber(input_pdb, op, value):
    ops = {"+": operator.add, "-": operator.sub}
    output_pdb = input_pdb.replace('.pdb','_renumbered.pdb')
    with open(output_pdb, 'w') as f:
       with open(input_pdb, 'r') as pdb_file:
          for line in pdb_file:
              if line.startswith("ATOM"):
                  frag = line[23:27]
                  newValue = ops[op](int(frag), int(value))
                  if newValue < 10:
                      newStr = '   ' + str(newValue)
                  elif newValue > 9 and newValue < 100:
                      newStr = '  ' + str(newValue)
                  elif newValue > 99 and newValue < 1000:
                      newStr = ' ' + str(newValue)
                  else:
                      newStr = str(newValue)
              line = line[:23] + newStr + line[27:]
              f.write(line)


if __name__ == '__main__':
    projectPath = '/home/sunyp/Documents/projects/pA104R'
    dataPath = projectPath + '/pA104R-DNA/qijx_191116/StructureRefined/'
    check_argument(sys.argv)
    input_pdb = dataPath + sys.argv[1]
    op = sys.argv[2]
    value = sys.argv[3]
    renumber(input_pdb, op, value)
