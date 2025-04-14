def encode_instruction(instruction):
    leftinstruction=instruction[0:13]
    rightinstruction=instruction[15:28]
    ocl=leftinstruction[0:10]
    ocr=rightinstruction[0:10]
    full=''
    if(ocl=='LOAD    M['):
        address=bin(int(leftinstruction[10:13]))
        full+=f"00000001 {address[2:].zfill(12)} "
    elif(ocl=='COMP    M['):
        address=bin(int(leftinstruction[10:13]))
        full+=f"01010000 {address[2:].zfill(12)} "
    elif(ocl=='JP+M[0:19,'):
        address=bin(int(leftinstruction[10:13]))
        full+=f"00001111 {address[2:].zfill(12)} "
    elif(ocl=='DIVI    M['):
        address=bin(int(leftinstruction[10:13]))
        full+=f"00001100 {address[2:].zfill(12)} "
    elif(ocl=='STOR    M['):
        address=bin(int(leftinstruction[10:13]))
        full+=f"00100001 {address[2:].zfill(12)} "
    elif(ocl=='LOAD  (MQ)'):
        
        full+=f"00001010 000000000000 "
    elif(ocl=='LOADMQMXM['):
        address=bin(int(leftinstruction[10:13]))
        full+=f"00001001 {address[2:].zfill(12)} "
    elif(ocl=='MUL     M['):
        address=bin(int(leftinstruction[10:13]))
        full+=f"00001011 {address[2:].zfill(12)} "
    elif(ocl=='ADD     M['):
        address=bin(int(leftinstruction[10:13]))
        full+=f"00000101 {address[2:].zfill(12)} "
    elif(ocl=='LOA(AC-MQ)'):
        address=bin(int(leftinstruction[10:13]))
        full+=f"00101000 {address[2:].zfill(12)} "
    elif(ocl=='SUB     M['):
        address=bin(int(leftinstruction[10:13]))
        full+=F"00000110 {address[2:].zfill(12)} "
    elif(ocl=='STOR[0:19,'):
        address=bin(int(leftinstruction[10:13]))
        full+=F"00010010 {address[2:].zfill(12)} "
    elif(ocl=='NO       P'):
        full+=f"11111111 111111111111 "
    elif(ocl=='JUMP    M['):
        address=bin(int(leftinstruction[10:13]))
        full+=F"00001101 {address[2:].zfill(12)} "    
    elif(ocl=='NO      P['):
        full+=F"11001100 111111111100 " 


    if(ocr=='LOAD    M['):
        address=bin(int(rightinstruction[10:13]))
        full+=f"00000001 {address[2:].zfill(12)} "
    elif(ocr=='COMP    M['):
        address=bin(int(rightinstruction[10:13]))
        full+=f"01010000 {address[2:].zfill(12)} "
    elif(ocr=='JP+M[0:19,'):
        address=bin(int(rightinstruction[10:13]))
        full+=f"00001111 {address[2:].zfill(12)} "
    elif(ocr=='DIVI    M['):
        address=bin(int(rightinstruction[10:13]))
        full+=f"00001100 {address[2:].zfill(12)} "
    elif(ocr=='STOR    M['):
        address=bin(int(rightinstruction[10:13]))
        full+=f"00100001 {address[2:].zfill(12)} "
    elif(ocr=='LOAD  (MQ)'):    
        full+=f"00001010 000000000000 "
    elif(ocr=='LOADMQMXM['):
        address=bin(int(rightinstruction[10:13]))
        full+=f"00001001 {address[2:].zfill(12)} "
    elif(ocr=='MUL     M['):
        address=bin(int(rightinstruction[10:13]))
        full+=f"00001011 {address[2:].zfill(12)} "
    elif(ocr=='ADD     M['):
        address=bin(int(rightinstruction[10:13]))
        full+=f"00000101 {address[2:].zfill(12)} "
    elif(ocr=='LOA(AC-MQ)'):
        full+=f"00101000 111111111110 "
    elif(ocr=='NO       P'):
        full+=f"11111111 111111111111 "
    elif(ocr=='SUB     M['):
        address=bin(int(rightinstruction[10:13]))
        full+=f"00000110 {address[2:].zfill(12)} "
    elif(ocr=='STOR[0:19,'):
        address=bin(int(rightinstruction[10:13]))
        full+=f"00010010 {address[2:].zfill(12)} "
    elif(ocr=='JUMP    M['):
        address=bin(int(rightinstruction[10:13]))
        full+=f"00001101 {address[2:].zfill(12)} " 
    elif(ocr=='NO      P['):
        full+=f"11001100 111111111100 " 
    return full
    




file_path='ASSEMBLY.txt'
with open(file_path, 'r') as file:
        instructions = file.readlines()
machine_code=[0]*1000
for i in range(len(instructions)):
    machine_code[i]=(encode_instruction(instructions[i]))
    
