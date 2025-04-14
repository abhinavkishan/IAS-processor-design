from assembler import machine_code
MEMORY=machine_code
AC=0
MQ=0
PC=0
MBR=0
MAR=0
IR=0
IBR=0
class IAS:
    def __init__(self,AC,MQ,PC,MBR,MAR,IR,IBR,MEMORY):
        self.MEMORY=MEMORY
        self.AC=AC
        self.MQ=MQ                          #initialising registers
        self.PC=PC
        self.MAR=MAR
        self.MBR=MBR
        self.IR=IR
        self.IBR=IBR
    def LOADAC(self,address):
        self.MAR=self.PC
        self.MBR=self.MEMORY[address]       #loads AC with the value in the address through MBR
        self.AC=self.MBR
        
        print(f'PC is {self.PC}, MBR is {self.MBR}, AC is {self.AC}')
    def LOAD_MQ(self):
        self.AC=self.MQ                     #loads MQ with the value in the address through MBR
        print(f'AC is {self.AC}')
    def LOAD_MQ_MX(self,address):
        self.MBR=self.MQ
        self.MEMORY[address]=self.MBR       #loads address with the value in MQ through MBR
        print(f'MBR is {self.MBR}, memory[{address}] is {self.MEMORY[address]}')
    def LOAD_AC_MQ(self):
        self.MBR=self.AC
        self.MQ=self.MBR                    #loads MQ with the value in AC through MBR
        print(f'MBR is {self.MBR},MQ is {self.MQ}')
    def STOR(self,address):
        self.MBR=self.AC
        self.MEMORY[address]=self.MBR       #stores the value in AC in the address through MBR
        print(f'memory[{address}] is {self.AC}')       
    def ADD(self,address):
        self.MBR=self.MEMORY[address]
        self.AC+=self.MBR                   #adds the value in address to AC and stores back in it

        print(f'AC is {self.AC}')
    def SUB(self,address):
        self.MBR=self.MEMORY[address]
        self.AC-=self.MBR                # subtracts the value from address to AC and stores back in it
        print(f'AC is {self.AC}')
    def DIV(self,address):
        self.MBR=self.MEMORY[address]
        self.MQ=(self.AC)//self.MBR      #quotient is stored in MQ
        self.AC=self.AC%self.MBR         # remainder is stored in AC
        print(f'AC is {self.AC}, MQ is {self.MQ}')
    def COMP(self,address):
        self.MBR=self.MEMORY[address]
        if(self.AC>self.MBR):      #if the value in address is less than value in AC then AC is kept 1
            self.AC=1            
        else:
            self.AC=-1             #else AC is set as -1 which we will later use in JUMP condition
        print(f'AC is {self.AC}')
    def JUMP_conditional(self,address):
        check=0
        if(self.AC>0):
            check=1
            self.PC=address
        self.MAR=self.PC
        print(f'PC is {self.PC}, MAR is {self.MAR}')
        if(check):
            return address
        else:
            return self.PC
    def JUMP_unconditional(self,address):
        self.PC=address
        self.MAR=self.PC
        print(f'PC is {self.PC}, MAR is {self.MAR}')
        return address    
    def MUL(self,address):
        self.AC*=(self.MEMORY[address])
    def STORLEINC(self,address):
        newaddress=(bin(self.AC))[2:].zfill(12)
        self.MEMORY[address]=self.MEMORY[address][0:9]+newaddress+self.MEMORY[address][21:]
        print(f'newaddress is {newaddress}, memory[{self.PC+1}] is {self.MEMORY[self.PC+1][9:21]}')
    def NOP(self):
        pass
ias=IAS(AC,MQ,PC,MBR,MAR,IR,IBR,MEMORY)
MEMORY[101]=2
MEMORY[100]=6 #INPUT
MEMORY[102]=0
MEMORY[103]=0
MEMORY[104]=1
MEMORY[105]=-2
MEMORY[106]=0 #result
MEMORY[107]=10
MEMORY[120]=500
print("Decimal Number",MEMORY[100])
inst=0
while(inst<1000):
    if(inst<50 and isinstance(MEMORY[inst],str)):
        ocl=MEMORY[ias.PC][0:8]
        
        ocr=MEMORY[ias.PC][22:30]
        
        adl=int(MEMORY[ias.PC][8:21],2)
        adr=int(MEMORY[ias.PC][31:43],2)

        ias.IR=ocl
        ias.MAR=MEMORY[ias.PC][8:21]
        ias.IBR=ocr+MEMORY[ias.PC][31:43]
        print("IR is",ias.IR)
        print("MAR is",ias.MAR)
        print("IBR is",ias.IBR)
        print("MBR is",ocl+bin(adl)[2:]+ocr+bin(adr)[2:])
        if(MEMORY[inst]==0):
            inst+=1
            continue
        else:
            if(ocl=="00000001"):
                ias.LOADAC(adl)
            if(ocl=="00001010"):
                ias.LOAD_MQ()
            if(ocl=="00001001"):
                ias.LOAD_MQ_MX(adl)
            if(ocl=="00101000"):
                ias.LOAD_AC_MQ()
            if(ocl=="01010000"):
                ias.COMP(adl)
            if(ocl=="00001101"):
                inst=ias.JUMP_unconditional(adl)
                continue
            if(ocl=="00001111"):
                inst=ias.JUMP_conditional(adl)
                if(adl==ias.PC):
                    continue
            if(ocl=="00000101"):
                ias.ADD(adl)
            if(ocl=="00001100"):
                ias.DIV(adl)
            if(ocl=="00010010"):
                ias.STORLEINC(adl)
            if(ocl=="00100001"):
                ias.STOR(adl)
            if(ocl=="00000110"):
                ias.SUB(adl)
            if(ocl=="11111111"):
                ias.NOP()
            if(ocl=="00001011"):
                ias.MUL(adl)

            ias.IR=ocr
            ias.MAR=adr
            ias.IBR=''
            print("IR is",ias.IR)
            print("MAR is",ias.MAR)
            if(ias.IBR==''):
                print("IBR is Empty",ias.IBR)
            else:
                print("IBR is",ias.IBR)

            if(ocr=="00000001"):
                ias.LOADAC(adr)
            if(ocr=="00001010"):
                ias.LOAD_MQ()
            if(ocr=="00001001"):
                ias.LOAD_MQ_MX(adr)
            if(ocr=="00101000"):
                ias.LOAD_AC_MQ()
            if(ocr=="01010000"):
                ias.COMP(adr)
            if(ocr=="00001101"):
                inst=ias.JUMP_unconditional(adr)
                continue
            if(ocr=="00001111"):
                inst=ias.JUMP_conditional(adr)
                if(adr==ias.PC):
                    continue
            if(ocr=="00000101"):
                ias.ADD(adr)
            if(ocr=="00001100"):
                ias.DIV(adr)
            if(ocr=="00010010"):
                ias.STORLEINC(adr)
            if(ocr=="00100001"):
                ias.STOR(adr)
            if(ocr=="00000110"):
                ias.SUB(adr)
            if(ocr=="11111111"):
                ias.NOP()
            if(ocr=="00001011"):
                ias.MUL(adr)
            if(ocr=='11001100'):
                break
            inst=inst+1
            ias.PC+=1
            print("PC is",ias.PC)
print(f'result is {MEMORY[106]}')
