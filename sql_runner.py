import sys
import subprocess

tmp_file_name = "./tmp.sql"


def create_sql_file(sql_file_absolute_path):
    with open(tmp_file_name, 'w') as f_w:
        with open(sql_file_absolute_path, 'r') as f_r:
            arr = []
            for line in f_r.readlines():
                line = line.lstrip()
                if line.lstrip().startswith("--"):
                    continue
                line = line.rstrip()
                if len(line) == 0:
                    continue
                arr.append(line)
                if line[-1] == ';':
                    sql = ' '.join(arr)
                    if len(sql) > 0:
                        f_w.write(f"{sql[0:-1]}\n")
                    arr = []
    print(f"created file : {tmp_file_name}")


def run_sql(data_source_name):
    command = f"isql -v {data_source_name} -w < {tmp_file_name}"
    print(command)
    run_command(command)
    run_command(f"rm {tmp_file_name}")


def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    while True:
        output = process.stdout.readline()
        if process.poll() is not None:
            break
        if output:
            print(str(output, 'utf-8').rstrip())
    rc = process.poll()
    return rc


if __name__ == '__main__':
    data_source_name = sys.argv[1]
    sql_file_absolute_path = sys.argv[2]
    create_sql_file(sql_file_absolute_path)
    run_sql(data_source_name)
