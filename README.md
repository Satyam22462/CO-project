# CO-project
firstly dictionary of opcode is made having instruction as its key and its corresponding opcode as its value. similarly dictionary of register is made having register names as its key and its corresponding address as its values and then file is going to read from input.txt and empty lines are removed and a list of instructions carrying each line as a string is made.
similarly a list of list holding all types var instructions is made and then we have dict of labels and dict of instructions is made.
dict of instruction carry's each line as its values and an address of each line as its key this like von neumann architecture , firstly their is program memory and then data memory.
now the functions are called according to the instructions.
function one is for to convert the instructions of add, subtract, multiply, xor, or, and.
then their is load and store function that converts the instruction of load and store to its binary by checking all possible errors.
move finally take's care of two types of move instructions.
funtion 4 is for left ship and right shift instruction.
function 5 is used for instruction like compare , division and note.
now function 6 is for jlt , jmp, jjt, je types of instructions.
function 7 is for the halt instruction and it is the last instruction that have to be in our input file otherwise it shows syntax error.
all this function take care of all the possible errors like checking the immediate value is a whole number and it is between 0 to 127, checking of illegal use of flag register, checking of use of undefine register and similarly all the error.
at last we are checking if the halt instruction is present or not, if not then it's going to show error in output.txt file.
we are also taking care that halt must be used as the last instruction.
finally if their are no errors our assembly code is successfully converted into it's binary code and saved in the output.txt file.
