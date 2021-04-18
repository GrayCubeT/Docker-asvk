startup = (
'To show a help message, type "help"\n' +
'To run the program, type "run" or "r"\n')
helpmessage = (
'This program is used to calculate the worst mobile network towers to lose\n' +
'in a preset network\n\n' + 
'To run a program you must have python installed\n' +
"If your python interpreter's absolte path is /usr/bin/python3,\n" +
'source.py is a runnable file. Otherwise, use "python source.py"\n' +
'\nThis program can use command line arguments:\n' +
'\t-f: specify a file with input after this flag' + 
'\n\t-h: show this message' + 
'\n\t-d: run in debug mode' +
'\n\t-o: specify an output file (this will print out a full answer)')
filemessage = (
'To input from a file, type in a file name\n' +
'To input from keyboard, leave filename empty\n')
inputmessage = (
'Input structure:\n' +
'\t{ [ [vertex, vertex], ... ], {vertex: value, ...} }\n' +
'First element is a list of edges between vertices\n' + 
'The second element is a dictionary that maps vertices to values\n')