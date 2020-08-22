import csv
import os

def append_range(range):
    



def prefix_2_range(ip):
    int_ip = int(ip[-2:])
    exponent = 32-int_ip
    range = (2**exponent)-1
    print(range)

def file_reader(file):
    with open(file,'r') as csv_file:
        userFileReader = csv.reader(csv_file)
        for row in userFileReader:
            for ip in row:
                prefix_2_range(ip)

if __name__ == "__main__":
    working_dir = 'D:\Python_Pojects\Small_Projects'
    os.chdir(working_dir)
    file = 'csv_prefix.csv'
    file_reader(file)

