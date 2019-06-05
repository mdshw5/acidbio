"""
Runs all the tests in the /good/ directory and checks whether
the tools run without error
"""
import sys
import getopt
import subprocess
import os
import tempfile

def run_good(tool: str, tool_name=None, verbose=False, output_file="failed_good.txt") -> None:
    correct = 0
    total = 0
    out_file = open(output_file, "a")

    title = tool_name if tool_name is not None else tool

    out_file.write(f"************************** {title} **************************\n\n")
    
    temps = tool.count("TEMP")
    temp_file_list = [tempfile.NamedTemporaryFile() for _ in range(temps)]

    for directory in os.listdir("./good/"):
        for file in os.listdir("./good/" + directory):
            if file.endswith(".bed"):
                filepath = "./good/" + directory + "/" + file
                execute_line = tool.replace("FILE", filepath) + " 2>&1"
                for i in range(temps):
                    execute_line = execute_line.replace("TEMP" + str(i), temp_file_list[i].name)
                process = subprocess.run(execute_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                if process.returncode == 0:
                    if verbose:
                        print(f'{filepath} passed correctly')
                        print(process.stdout)
                        print()
                    correct += 1
                else:
                    print(f'{filepath} failed incorrectly')
                    if verbose:
                        print(process.stdout)
                        print()
                    out_file.write(f"%===========================%\n {filepath}\n\n")
                    out_file.write(process.stdout)
                    out_file.write("%===========================%\n\n")
                total += 1

    out_file.write(f"\n\nTests completed.\n{correct} correct out of {str(total)}" +
        f"\n\n************************** {title} **************************\n")
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
    tool_name = None

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
    
    if len(args) == 2:
        tool_name = args[2]
    
    if len(args) > 2 or len(args) == 0:
        usage()
        exit(2)

    run_good(args[1], tool_name, verbose, output_file)