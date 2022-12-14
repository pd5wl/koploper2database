# Example Config File
#
# MySQL serrings
mysql = {
    'host': '[host]',
    'user': '[user]',
    'password': '[pass]',
    'database': '[database]]',
    'raise_on_warnings': True
}

# socket info

# Make shure that in koploper poort 5700 is enabled
sckthost = "[koploperip]"
scktport = 5700

# Output options
op_select = 0  # 1 for database. 0 for file

# File options
op_fileadd = 0  # 1 for append to file. 0 create a new file every time you start
save_path = 'output'  # Save where (relative)
file_name = "test.txt"  # Save name
kl_tijd = 1  # 1 for model time and 0 for realtime

# Add-Ons
trace_train = 1  # 1 to see the prevous blok of the train (Works only for the database storage)

# Debug options
dbg_print = 1  # 1 to print debug data
dbg_svr = 1 # 1 to use local test server to debug data