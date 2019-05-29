"""
Runs all the tests in the /good/ directory and checks whether
the tools run without error
"""
import sys
import getopt
import subprocess
import os
import tempfile

def run_good(tool: str, verbose=False, output_file="failed_good.txt") -> None:
    correct = 0
    total = 0
    out_file = open(output_file, "a")

    out_file.write("**************************" + tool + "**************************\n\n")

    temp1 = tempfile.NamedTemporaryFile()
    temp2 = tempfile.NamedTemporaryFile()

    for directory in os.listdir("./good/"):
        for file in os.listdir("./good/" + directory):
            if file.endswith(".bed"):
                filepath = "./good/" + directory + "/" + file
                execute_line = tool.replace("FILE", filepath).replace("TEMP1", temp1.name).replace("TEMP2", temp2.name) + " 2>&1"
                process = subprocess.run(execute_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                if process.returncode == 0:
                    if verbose:
                        print(filepath + ' passed correctly')
                        print(process.stdout)
                        print()
                    correct += 1
                else:
                    print(filepath + ' failed incorrectly')
                    if verbose:
                        print(process.stdout)
                        print()
                    out_file.write("%===========================%\n" + filepath + "\n\n")
                    out_file.write(process.stdout)
                    out_file.write("%===========================%\n\n")
                total += 1

    out_file.write("\n\nTests completed.\n" + str(correct) + " correct out of " + str(total) +
        "\n\n**************************" + tool + "**************************\n")
    out_file.close()


def usage():
    print("""Runs all the good test files against a tool and records the failing cases.
Usage: run_good.py tool [-h] [-V] [-v] [--output-file]
    options:
      tool  The full command line to call the tool being tested. However, replace the input with "FILE" and if
        there are any temporary files needed to be created such as a sorted file, use TEMP1 or TEMP2. The
        command line must be all in one line. If multiple lines are needed, use ; to separate them.
      -h, --help    Help
      -v, --verbose=    If True, it prints the results and outputs from all tests. Default is False
      -V, --version The version number
      --output-file The output file that logs cases where the tool ran with error. Default is failing_good.txt
    """)


if __name__ == "__main__":
    try:
        optlist, args = getopt.getopt(sys.argv[1:], "hVv", ["help", "verbose=", "version", "output-file="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        exit(2)
    
    verbose = False
    output_file = "failed_good.txt"

    for o, a in optlist:
        if o in ("-V", "--version"):
            print("0.1")
            exit(0)
        elif o in ("-h", "--help"):
            usage()
            exit(0)
        elif o in ("-v", "--verbose"):
            if a.lower() not in ('true', 'false'):
                usage()
                exit(2)
            verbose = True if a.lower() == 'true' else False
        elif o == "--output-file":
            output_file = a
        else:
            assert False, "unhandled option"
    
    if len(args) != 1:
        usage()
        exit(2)

    run_good(args[1], verbose, output_file)