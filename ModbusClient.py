from pymodbus.client.sync import ModbusTcpClient
n=0

# Welcome message
print "Welcome to the UR5 data reading example"
print "Press Ctrl-C to stop."

UR5ip = raw_input ("Please enter the IP address of UR5: ")
       

client = ModbusTcpClient(UR5ip)

while True:
    FunctionCode = raw_input ("Please enter the Function Code (01 for Reading Coils and 03 for Reading Holding Registers): ")
    if FunctionCode == "01":
        StartingAddress = input ("Please enter the Starting Address: ")
        NumberOfCoils = input ("Please enter the Number of Coils: ")
        result = client.read_coils(StartingAddress,NumberOfCoils)
        print result
    elif FunctionCode == "03":
        StartingAddress = input ("Please enter the Starting Address: ")
        NumberOfRegisters = input ("Please enter the Number of Registers: ")
        result = client.read_holding_registers(StartingAddress,NumberOfRegisters)
        print result.registers
    else:
        break

client.close()
