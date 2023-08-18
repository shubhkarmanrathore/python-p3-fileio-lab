def write_file(file_name="lib/logfile", file_content="log 1: 5 bananas added"):
    with open(f"{file_name}.txt", mode="w", encoding="utf-8") as logfile:
        logfile.write(f"{file_content}")


def append_file(file_name="lib/logfile", append_content="log 2: 3 bananas subtracted"):
    with open(f"{file_name}.txt", mode="a", encoding="utf-8") as logfile:
        logfile.write(f"{append_content}")


def read_file(file_name="lib/logfile"):
    with open(f"{file_name}.txt", encoding="utf-8") as logfile:
        return logfile.read()


write_file(file_name="logfile", file_content="Log 1: 5 bananas added")
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

read_file(file_name="logfile")