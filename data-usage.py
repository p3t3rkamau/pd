import subprocess
import csv
import time

def generate_data():
    # Run the `adb shell dumpsys netstats detail full` command
    result = subprocess.run(["adb", "shell", "dumpsys", "netstats", "detail", "full"], stdout=subprocess.PIPE)

    # Split the output into lines
    lines = result.stdout.decode().strip().split("\n")

    # Initialize an empty list to store the processed data
    data = []
    for line in lines:
        if "ident=[" in line:
            network_type_parts = line.split("type=")
            if len(network_type_parts) > 1:
                network_type = network_type_parts[1].split(",")[0].strip()
            else:
                network_type = "Unknown"

            network_id_parts = line.split("networkId=")
            if len(network_id_parts) > 1:
                network_id = network_id_parts[1].split(",")[0].strip('"') 
            else:
                network_id = "unknown"   
                

        elif "st=" in line:
            parts = line.split(" ")
            print(parts)
            if not parts:
                continue
            st = parts[7].split("=")[1]
            rb = parts[8].split("=")[1]
            rp = parts[9].split("=")[1]
            tb = parts[10].split("=")[1]
            tp = parts[11].split("=")[1]
           
            
            data.append([network_type, network_id, st, rb, rp, tb, tp])
        else:
            continue
    # Write the data to a CSV file
    with open("network_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        if file.tell() == 0:  # Check if file is empty
            writer.writerow(["Network Type", "Network ID", "st", "rb", "rp", "tb", "tp", "op"])
        writer.writerows(data)
if __name__ == "__main__":
    generate_data()



# import subprocess
# import csv
# import time

# def generate_data():
#     # Run the `adb shell dumpsys netstats detail full` command
#     result = subprocess.run(["adb", "shell", "dumpsys", "netstats", "detail", "full"], stdout=subprocess.PIPE)

#     # Split the output into lines
#     lines = result.stdout.decode().strip().split("\n")

#     # Initialize an empty list to store the processed data
#     data = []
#     for line in lines:
#         if "ident=[" in line:
#             network_type_parts = line.split("type=")
#             if len(network_type_parts) > 1:
#                 network_type = network_type_parts[1].split(",")[0].strip()
#             else:
#                 network_type = "Unknown"

#             network_id_parts = line.split("networkId=")
#             if len(network_id_parts) > 1:
#                 network_id = network_id_parts[1].split(",")[0].strip('"') 
#             else:
#                 network_id = "unknown"   
                
#         elif "uid=" in line:
#             uid = line.split("uid=")[1].split(" ")[0].strip()
#             print(uid)
#             data.append([uid, network_type, network_id])
#             print(data)
#         else:
#             continue

# import subprocess
# import csv
# import time

# def generate_data():
#     # Run the `adb shell dumpsys netstats detail full` command
#     result = subprocess.run(["adb", "shell", "dumpsys", "netstats", "detail", "full"], stdout=subprocess.PIPE)

#     # Split the output into lines
#     lines = result.stdout.decode().strip().split("\n")

#     # Initialize an empty list to store the processed data
#     data = []
#     for line in lines:
#         if "ident=[" in line:
#             network_type_parts = line.split("type=")
#             if len(network_type_parts) > 1:
#                 network_type = network_type_parts[1].split(",")[0].strip()
#             else:
#                 network_type = "Unknown"

#             network_id_parts = line.split("networkId=")
#             if len(network_id_parts) > 1:
#                 network_id = network_id_parts[1].split(",")[0].strip('"') 
#             else:
#                 network_id = "unknown"   
                
#         elif "uid=" in line:
#             uid = line.split("uid=")[1].split(" ")[0].strip()
#             print(uid)
#             data.append([uid, network_type, network_id])
#             print(data)
#     else:
#         continue    

         

        # if "st=" in line:
        #     parts = line.split(" ")
        #     if parts:
        #         st = parts[0].split("=")[1]
        #         rb = parts[1].split("=")[1]
        #         rp = parts[2].split("=")[1]
        #         tb = parts[3].split("=")[1]
        #         tp = parts[4].split("=")[1]
        #         op = parts[5].rstrip()
        #         print(st)
        #         print(rb) 
             
              
           
        #     data.append([network_type, network_id, uid, st, rb, rp, tb, tp, op])

            # # Add the data to the list
            # data.append([network_type, network_id, uid, st, rb, rp, tb, tp, op])



# Write the processed data to a CSV file
# with open("network_stats.csv", "a", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Type", "Network ID", "UID", "ST", "RB", "RP", "TB", "TP", "OP"])
#     data = generate_data()
#     print(data)

    # while True:
    
    #     print(data)
    #     writer.writerows(data)
    #     time.sleep(4)

# import csv
# import subprocess

# output = subprocess.check_output("adb shell dumpsys netstats detail full", shell=True)
# output = output.decode("utf-8")
# output = output.split("\r\n")

# with open("data-usage.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["type", "network_id", "uid", "st", "rp", "tb", "op"])

#     for line in output:
#         if "ident=[" in line:
#             network_id_parts = line.split("ident=[")
#             network_id = network_id_parts[1].split("networkId=")[1].split(",")[0].strip('"')
#             uid = line.split("uid=")[1].split(" ")[0]

#         if "st=" in line:
#             parts = line.split(" ")
#             if parts:
#                 st = parts[0].split("=")[1]
#                 rp = parts[2].split("=")[1]
#                 tb = parts[4].split("=")[1]
#                 op = parts[6].rstrip()
#             else:
#                 continue

# #             writer.writerow(["MOBILE", network_id, uid, st, rp, tb, op])
# import subprocess
# import csv

# # Run the `adb shell dumpsys netstats detail full` command
# result = subprocess.run(["adb", "shell", "dumpsys", "netstats", "detail", "full"], stdout=subprocess.PIPE)

# # Split the output into lines
# lines = result.stdout.decode().strip().split("\n")


# # Initialize an empty list to store the processed data

# for line in lines:
#     if "ident=[" in line:
#         # Extract the network type
#         network_type_parts = line.split("]")
#         if len(network_type_parts) > 1:
#             network_type = network_type_parts[0].split("[")[1].strip()
#         else:
#             network_type = "Unknown"

#         # Extract the network ID
#         network_id_parts = line.split("networkId=")
#         if len(network_id_parts) > 1:
#             network_id = network_id_parts[1].split(",")[0].strip('"')
# Iterate over the lines
# for line in lines:
#     if "ident=[" in line:
#         # Extract the network type
#         network_type_parts = line.split("]")
#         if len(network_type_parts) > 1:
#             network_type = network_type_parts[0].split("[")[1].strip()
#         else:
#             network_type = "Unknown"

#         # Extract the network ID
#         network_id_parts = line.split("networkId=")
#         if len(network_id_parts) > 1:
#             network_id = network_id_parts[1].split(",")[0].strip('"')
#         elif "uid=" in line:
#         # Extract the user ID
#          uid = line.split("uid=")[1].split(" ")[0]
        
#         if "st=" in line:
#             parts = line.split(" ")
#             if parts:
#                 st = parts[0].split("=")[1]
#                 print(st)
#                 rb = parts[1].split("=")[1]
#                 rp = parts[2].split("=")[1]
#                 tb = parts[3].split("=")[1]
#                 tp = parts[4].split("=")[1]
#                 op = parts[5].rstrip()
#             else:
#                 continue

            # Add the data to the list
           
            # data.append([network_type, network_id, uid, st, rb, rp, tb, tp, op])

# Write the processed data to a CSV file
# with open("network_stats.csv", "a", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Type", "Network ID", "UID", "ST", "RB", "RP", "TB", "TP", "OP"])
#     print(data)
#     writer.writerows(data)




# Open a CSV file for writing
# with open("data-usage.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Timestamp", "Data Usage"])
#     for line in output.splitlines():
#         if len(line.split(' ')) >= 3:
#             data_usage = line.split(' ')[2].split('=')[1]
#         else:
#             data_usage = None
#         writer.writerow([time.time(), data_usage])


#     # Loop through the lines of the output
   

# import re
# import csv
# import os
# import subprocess
# import time
# import datetime

# # Retrieve data usage statistics using ADB
# result = subprocess.run(['adb', 'shell', 'dumpsys', 'netstats', '--uid', '-t'], stdout=subprocess.PIPE)
# output = result.stdout.decode('utf-8')

# import re
# import csv

# # Get the adb output
# output = "uid=10140 set=DEFAULT tag=0x0\n    NetworkStatsHistory: bucketDuration=7200\n      st=1675454400 rb=6433 rp=12 tb=2230 tp=13 op=0"

# # Split the output into separate lines
# lines = output.split('\n')



# # Define a list to store the formatted data
# data = []

# # Loop over the lines and extract the relevant information
# for line in lines:
    
#     if 'uid=' in line:
#         uid = line.split(' ')[0].split('=')[1]
#     if 'rb=' in line:
#         data_usage = line.split(' ')[2].split('=')[1]
#         timestamp = line.split(' ')[1].split('=')[1]
#         data.append([uid, timestamp, data_usage])

# # Write the data to a csv file
# with open('data_usage.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['UID', 'Timestamp', 'Data Usage'])
#     for row in data:
#         writer.writerow(row)

# with open('data_usage.csv', 'a', newline='') as csvfile:
#     writer = csv.writer(csvfile)

#     # write the header row
   
#     data_usage = re.search(r'rb=(\d+)', output).group(1)
   

#     current_time = int(time.time())
#     readable_time = datetime.datetime.fromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S')

#     with open("data_usage.csv", "a") as f:
#         f.write("{},{}\n".format(readable_time, data_usage))
  
# open the file for writing

# import csv
# from datetime import datetime

# header = ['Timestamp', 'Data Usage']
# rows = []

# # Populate the rows list with data usage and timestamps
# for i in range(5):
#     rows.append({'Timestamp': datetime.now(), 'Data Usage': i})

# # Write the data to a csv file
# with open('data_usage.csv', 'w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=header)
#     writer.writeheader()
#     for row in rows:
#         writer.writerow(row)


    # loop over the outputs
    # for outputs in output:
        # extract the data usage from each output
       
        
 

# import os
# import subprocess
# import csv
# import re

# # Retrieve data usage statistics using ADB
# result = subprocess.run(['adb', 'shell', 'dumpsys', 'netstats', '--uid', '-t'], stdout=subprocess.PIPE)
# output = result.stdout.decode('utf-8')


# # Extract the data usage and time from the output
# data_usage = re.search(r'rb=(\d+)', output).group(1)
# time = re.search(r'st=(\d+)', output).group(1)

# # Write the data to a csv file
# with open('data_usage.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['time', 'data_usage'])
#     writer.writerow([time, data_usage])
# # Split the output into separate lines
# lines = output.splitlines()

# # Extract the data usage and time information
# data = []
# for line in lines:
#     if "Data usage" in line:
#         # Split the line into separate fields
#         fields = line.split()

#         # Extract the data usage and time information
#         usage = fields[2]
#         time = fields[-1]
     

#         # Store the information in a list
#         data.append([usage, time])
       

# # Write the data to a CSV file
# with open('data_usage_stats.csv', 'w', newline='') as file:
   
#     writer = csv.writer(file)
#     writer.writerows(data)

# # Read the data from the CSV file
# with open('data_usage_stats.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# import os
# import subprocess
# import time
# import csv

# def process_data_usage(data_usage_stats):
#     data_usage_per_second = []
#     for line in data_usage_stats:
#         parts = line.split()
#         # assuming the data usage is stored in the last part of each line
#         data_usage = int(parts[-1])
#         data_usage_per_second.append(data_usage)
#     return data_usage_per_second


# filename = "data_usage_stats.csv"
# fieldnames = ['time', 'data_usage']

# with open(filename, 'w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     while True:
#         result = subprocess.run(['adb', 'shell', 'dumpsys', 'netstats', '--uid', '-t'], stdout=subprocess.PIPE)
#         output = result.stdout.decode('utf-8')
#         data_usage = process_data_usage(output)
#         current_time = time.time()
#         writer.writerow({'time': current_time, 'data_usage': data_usage})
#         time.sleep(1) # wait for 1 second before getting data usage again

# import os
# import subprocess
# import csv

# import os
# import subprocess
# import csv
# import time

# # Define the interval for data retrieval (in minutes)
# interval = 1

# while True:
#   # Retrieve data usage statistics using ADB
#   result = subprocess.run(['adb', 'shell', 'dumpsys', 'netstats', '--uid', '-t'], stdout=subprocess.PIPE)
#   output = result.stdout.decode('utf-8')

#   # Store the data in a CSV file
#   with open('data_usage_stats.csv', 'a', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow([output])

#   # Sleep for the defined interval
#   time.sleep(interval * 60)

# # Retrieve data usage statistics using ADB
# result = subprocess.run(['adb', 'shell', 'dumpsys', 'netstats', '--uid', '-t'], stdout=subprocess.PIPE)
# output = result.stdout.decode('utf-8')

# # Parse the output to extract data usage per day
# lines = output.split("\n")
# data_usage = []
# for line in lines:
#     if "DataUsage per day" in line:
#         parts = line.split()
#         date = parts[0]
#         usage = parts[1]
#         data_usage.append([date, usage])

# # Write the data usage per day to a CSV file
# with open('data_usage_stats.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Date", "Data Usage"])
#     for row in data_usage:
#         writer.writerow(row)

# import os
# import subprocess
# import csv

# # Retrieve data usage statistics using ADB
# result = subprocess.run(['adb', 'shell', 'dumpsys', 'netstats', '--uid', '-t'], stdout=subprocess.PIPE)
# output = result.stdout.decode('utf-8')

# # Parse the output to extract data usage per day
# lines = output.split("\n")
# data_usage = []
# for line in lines:
#     if "DataUsage per day" in line:
#         parts = line.split()
#         date = parts[0]
#         usage = parts[1]
#         data_usage.append([date, usage])

# # Write the data usage per day to a CSV file
# with open('data_usage_stats.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Date", "Data Usage"])
#     for row in data_usage:
#         writer.writerow(row)

# # Read the data from the CSV file
# with open('data_usage_stats.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
