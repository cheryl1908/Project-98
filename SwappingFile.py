def SwappingFile():
    
    input_1=input("Enter file 1 name: ")
    input_2=input("Enter file 2 name: ")

    with open(input_1,'r') as a:
        data_a=a.read()

    with open(input_2,'r') as b:
        data_b=b.read()

    with open(input_1,'w') as write1:
        write1.write(data_b)

    with open(input_2,'w') as write2:
        write2.write(data_a)

SwappingFile()