import random
import subprocess
import time
import sys
import random

random.seed(int(sys.argv[2]))
port = str(5201+int(sys.argv[1]))
varying = bool(sys.argv[2])
# List of random Linux commands
def format_output(output):
    if not output:
        return "No output"
    
    # Split the output into lines and add indentation
    lines = output.strip().split("\n")
    formatted_output = "\n".join(f"{line}" for line in lines)
    return formatted_output

commands = [
    
    "iperf3 -s -p {}".format(port),
    "wget https://speed.hetzner.de/1GB.bin 2>&1 | tee -a wget_log",
    "mpv https://www.dailymotion.com/video/x7xtdoc -vo=null -v",
    "python gen.py"
    "scp d1GB.bin 192.168.1.10:."
]

def run_random_command():
    # Pick a random command from the list
    command = random.choice(commands)
    print(f"Running command: {command}")

    try:
        # Run the command in a subprocess for 10 seconds
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf8')
        if(command == "mpv https://www.dailymotion.com/video/x7xtdoc -vo=null -v"):
            time.sleep(10)
        if varying:    
            sleep_time = random.uniform(8,15)
            time.sleep(sleep_time)
        else:
            time.sleep(600)
        process.terminate()
        print(format_output(process.stdout.read()))
        print(format_output(process.stderr.read()))
        print(f"Command '{command}' completed.")
    except Exception as e:
        print(f"Error while running the command: {e}")

def main():
    if varying:
        for _ in range(50):
            run_random_command()
            # Sleep for random time between 3 to 8 seconds
            sleep_time = random.uniform(3, 8)
            time.sleep(sleep_time)
    else:
        run_random_command()
if __name__ == "__main__":
    main()
