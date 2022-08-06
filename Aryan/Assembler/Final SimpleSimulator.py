import os
import sys
import site
#import matplotlib.pyplot as plt

lines=[]
temp=[]
temp=sys.stdin.read().splitlines()

for i in range(len(temp)):
    if temp[i]=='' or temp[i].isspace()==True:
        #lines.append("Empty line")
        continue
    else:
        lines.append(temp[i])

text='\n'.join(lines)
input_list=text.split("\n")


#input_list=["1001000100001010","1001001001100100","1011000011001010","1010101100000101","0101000000000000"]
output_list=[]
varmem_value={}
reg_code={'000':'R0','001':'R1','010':'R2','011':'R3','100':'R4','101':'R5','110':'R6','111':'FLAGS'}
reg_value={'R0':0,'R1':0,'R2':0,'R3':0,'R4':0,'R5':0,'R6':0,'FLAGS':0} #all initial values are 0

reg_code_value={'000':0,'001':0,'010':0,'011':0,'100':0,'101':0,'110':0,'111':0}

cycle_list=[]
memory_access_list=[]
cycle_counter=0


def binary(n):
    """Takes int returns string"""
    out=""
    temp = n
    i=0
    while i<16: #check
        out+=str(temp%2)
        temp=temp//2
        i+=1
    return out[::-1]

def binary8(n):
    """Takes int returns string"""
    out=""
    temp = n
    i=0
    while i<8: #check
        out+=str(temp%2)
        temp=temp//2
        i+=1
    return out[::-1]
def binary_extension(n,length):
    """Takes string and extends it to the length required and returns new string"""
    new_str=""
    current_length=len(n)
    for i in range(0,length-current_length):
        new_str+="0"
    for i in n:
        new_str+=i
    return new_str


def bin_to_float(al):
    exp = 0
    a = str(al)
    for i in range(3):
        exp+=(2**i)*int(a[2-i])
    if exp<=5:
        temp = "1"+a[3:]
    elif exp==6:
        temp = "1"+a[3:]+"0"
    elif exp==7:
        temp = "1"+a[3:]+"00"
    whole = temp[:exp+1]
    frac = temp[exp+1:]
    out = 0
    outf = 0.0
    for i in range(len(whole)):
        out+=(2**i)*int(whole[len(whole)-i-1])
    for i in range(len(frac)):
        outf+=(2**(-(i+1)))*int(frac[i])
    return out+outf

out = []
tempp=["0", "1"]
cases = []
temp2=["000", "001", "010", "011", "100", "101", "110", "111"]
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                for m in range(2):
                    cases.append(tempp[i]+tempp[j]+tempp[k]+tempp[l]+tempp[m])
for i in range(len(cases)):
    for j in range(len(temp2)):
        out.append(temp2[j]+cases[i])
outlist=[]
for i in range(len(out)):
    outlist.append(bin_to_float(out[i]))

float_list = outlist
float_list_bin = out

rep_dic = {}
for i in range(len(out)):
    rep_dic[out[i]]=outlist[i]
#print(rep_dic)

ref_dic = {}
for i in range(len(out)):
    ref_dic[outlist[i]]=out[i]
#print(ref_dic)

PC=0
var_count=0
flag_check=1
prev_flags=0

if len(input_list)>256:
    flag_check=0
    print("Number of lines exceeds 256.")

if input_list[len(input_list)-1][0:5]!="01010":
    flag_check=0
    print("Halt instruction not at end.")

while(PC<len(input_list) and flag_check==1):

  cycle_list.append(cycle_counter)
  memory_access_list.append(PC)
 
  #if input_list[PC-1][0:5]!='11110':
  #    reg_code_value['111']=0
     
  #reg_code_value['111']=0 #setting FLAGS to 0 at the beginning of the instruction
  instruction_output=[]
  jump=0
  instrn=input_list[PC] #storing the instruction as per the value of the PC
  #now we will check for the opcodes and register values and perform the operations accordingly

#type A instructions: add, sub, multiply, xor, or, and
#type B instructions: mov, left shift, right shift
#type C instructions: mov imm, divide, invert, compare
#type D instructions: load, store
#type E instructions: unconditional jump, jump if less than, jump if greater than, jump if equal
#type F instructions: hlt

 


#reg_code_value

  """Type A Instructions"""

  #for add instruction
  if(instrn[0:5]=="10000"):
    #assigning the values to the registers depending on the code (instrn[x:y])
    reg_code_value[instrn[13:16]]=reg_code_value[instrn[7:10]]+reg_code_value[instrn[10:13]]
    #register_1=reg_code[instrn[7:10]]
    #register_2=reg_code[instrn[10:13]]
    #register_3=reg_code[instrn[13:16]]
    #reg_value[register_3]=reg_value[register_2]+reg_value[register_1]
    check_value=reg_code_value[instrn[13:16]]
    if(check_value>=65536):
      reg_code_value[instrn[13:16]]=reg_code_value[instrn[13:16]]%65536
      reg_code_value['111']+=8 #setting the value of FLAGS register


  #for addf instruction
  if(instrn[0:5]=="00000"):
    #assigning the values to the registers depending on the code (instrn[x:y])
    reg_code_value[instrn[13:16]]=reg_code_value[instrn[7:10]]+reg_code_value[instrn[10:13]]
    #register_1=reg_code[instrn[7:10]]
    #register_2=reg_code[instrn[10:13]]
    #register_3=reg_code[instrn[13:16]]
    #reg_value[register_3]=reg_value[register_2]+reg_value[register_1]
    check_value=reg_code_value[instrn[13:16]]
    if(check_value>=65536):
      reg_code_value[instrn[13:16]]=reg_code_value[instrn[13:16]]%65536
      reg_code_value['111']+=8 #setting the value of FLAGS register


  #for subtract instruction
  if(instrn[0:5]=="10001"):
    #assigning the values to the registers depending on the code (instrn[x:y])
    reg_code_value[instrn[13:16]]=reg_code_value[instrn[7:10]]-reg_code_value[instrn[10:13]]
    check_value=reg_code_value[instrn[13:16]]
    if(check_value<0):
      reg_code_value[instrn[13:16]]=0
      reg_code_value['111']+=8 #setting the value of FLAGS register

  #for subf instruction
  if(instrn[0:5]=="00001"):
    #assigning the values to the registers depending on the code (instrn[x:y])
    reg_code_value[instrn[13:16]]=reg_code_value[instrn[7:10]]-reg_code_value[instrn[10:13]]
    #register_1=reg_code[instrn[7:10]]
    #register_2=reg_code[instrn[10:13]]
    #register_3=reg_code[instrn[13:16]]
    #reg_value[register_3]=reg_value[register_2]+reg_value[register_1]
    check_value=reg_code_value[instrn[13:16]]
    if(check_value>=65536):
      reg_code_value[instrn[13:16]]=reg_code_value[instrn[13:16]]%65536
      reg_code_value['111']+=8 #setting the value of FLAGS register


  #for multiply instruction
  if(instrn[0:5]=="10110"):
    #assigning the values to the registers depending on the code (instrn[x:y])
    reg_code_value[instrn[13:16]]=reg_code_value[instrn[7:10]]*reg_code_value[instrn[10:13]]
    check_value=reg_code_value[instrn[13:16]]
    if(check_value>=65536):
      reg_code_value[instrn[13:16]]=reg_code_value[instrn[13:16]]%65536
      reg_code_value['111']+=8 #setting the value of FLAGS register




  #for xor instruction
  if(instrn[0:5]=="11010"):
    #assigning the values to the registers depending on the code (instrn[x:y])
    reg_code_value[instrn[13:16]]=reg_code_value[instrn[7:10]]^reg_code_value[instrn[10:13]]

    #reg_value[register_3]=(reg_value[register_1])^(reg_value[register_2]) #storing result in R3


  #for or instruction
  if(instrn[0:5]=="11011"):
    reg_code_value[instrn[13:16]]=reg_code_value[instrn[7:10]]|reg_code_value[instrn[10:13]]
   

  #for and instruction
  if(instrn[0:5]=="11100"):
    reg_code_value[instrn[13:16]]=reg_code_value[instrn[7:10]]&reg_code_value[instrn[10:13]]
   


  """Type B Instructions"""

       
  #for right shift instruction
  if(instrn[0:5]=="11000"):
    reg_code_value[instrn[5:8]]=int(reg_code_value[instrn[5:8]])>>(int(instrn[8:16]))
    """Note: No overflow/underflow is possible in case of right shift"""



  #for left shift instruction
  if(instrn[0:5]=="11001"):
    reg_code_value[instrn[5:8]]=int(reg_code_value[instrn[5:8]])<<(int(instrn[8:16]))



   
  #for mov register instruction
  if(instrn[0:5]=="10011"):
    reg_code_value[instrn[13:16]]=reg_code_value[instrn[10:13]]
                                                                   
    """The flags if-else part is not really required
    if register_1=="FLAGS": #if first register is FLAGS register
        reg_value[register_2]=reg_value["FLAGS"] #put contents of FLAGS into the second register
    else:
        reg_value[register_2]=reg_value[register_1] #otherwise
    """


  """Type C Instructions"""


  #for mov imm instruction
  if(instrn[0:5]=="10010"):
    #assigning the values to the registers depending on the code (instrn[x:y])
    reg_code_value[instrn[5:8]]=int(instrn[8:16],2)
    check_val=reg_code_value[instrn[5:8]]
    if check_val>=65536:
        reg_code_value[instrn[5:8]]=reg_code_value[instrn[5:8]]%65536
        reg_code_value["111"]+=8

  #for mov float imm instruction
  if(instrn[0:5]=="00010"):
    #assigning the values to the registers depending on the code (instrn[x:y])
    reg_code_value[instrn[5:8]]=rep_dic[instrn[8:16]]
    #register_1=reg_code[instrn[5:8]]
    #imm_val=int(instrn[8:16],2)
    #reg_value[register_1]=imm_val
    check_val=reg_code_value[instrn[5:8]]
    if check_val>=65536:
        reg_code_value[instrn[5:8]]=reg_code_value[instrn[5:8]]%65536
        reg_code_value["111"]+=8

  #for divide instruction
  if(instrn[0:5]=="10111"):
    #assigning the values to the registers depending on the code (instrn[x:y])

    reg_code_value['000']=int(reg_code_value[instrn[10:13]]/reg_code_value[instrn[13:16]])                                                            
    reg_code_value['001']=reg_code_value[instrn[10:13]]%reg_code_value[instrn[13:16]]                                                        
   

  #for invert instruction
  if(instrn[0:5]=="11101"):
    value_to_invert_int=binary(reg_code_value[instrn[10:13]])#converting register 1 value to 16 bit binary format
    value_to_invert=binary_extension(value_to_invert_int,16)
    inverted_val=""
    for i in value_to_invert:
        if i=='1':
            inverted_val+='0'
        else:
            inverted_val+='1'
    inverted_val=int(inverted_val,2) #converting back to decimal
    reg_code_value[instrn[13:16]]=inverted_val #storing final value in register 2
   


  #for compare instruction
  if(instrn[0:5]=="11110"):
    re_val1=reg_code_value[instrn[10:13]]
    re_val2=reg_code_value[instrn[13:16]]
    """Setting values of flags depending on the values of Register 1 and Register 2"""
    if(re_val1>re_val2):
       
      if reg_code_value['111']>=8: #if overflow bit is set or overflow and some other bit are set
          reg_code_value['111']=10
      else:
          reg_code_value['111']=2 #whenever we are comparing, we are resetting the flags

    elif(re_val1==re_val2):
       
      if reg_code_value['111']>=8:#if overflow bit is set or overflow and some other bit are set
          reg_code_value['111']=9
      else:
          reg_code_value['111']=1

    elif re_val1<re_val2:
        if reg_code_value['111']>=8: #if overflow bit is set or overflow and some other bit are set
            reg_code_value['111']=12
        else:
            reg_code_value['111']=4
     
    else:
      reg_code_value['111']=0


  """Type D Instructions"""

  #for load instruction
  if(instrn[0:5]=="10100"):
    mem_addr=instrn[8:16]
    if mem_addr in varmem_value:
        mem_addr_value=varmem_value[mem_addr]
        reg_code_value[instrn[5:8]]=mem_addr_value
        #memory_access_list.append(int(mem_addr_value,2))
    else:
        varmem_value[mem_addr]=0
        mem_addr_value=varmem_value[mem_addr]
        reg_code_value[instrn[5:8]]=mem_addr_value
        #memory_access_list.append(0)
   
    cycle_list.append(cycle_counter)
   



  #for store instruction
  if(instrn[0:5]=="10101"):

    mem_addr=instrn[8:16]
    varmem_value[mem_addr]=reg_code_value[instrn[5:8]]
    #memory_access_list.append(int(mem_addr_value,2))
    cycle_list.append(cycle_counter)

  """Type E Instructions"""

  #for jmp instruction
  if(instrn[0:5]=="11111"):
      jump=1 #unconditional jump
     
  #for jlt instruction
  if(instrn[0:5]=="01100"):
      reg_FLAGS_binary=binary_extension(binary(reg_code_value['111']),16)
      if reg_FLAGS_binary[-3]=='1': #if less than
          jump=1
      else:
        jump=0

  #for jgt instruction
  if(instrn[0:5]=="01101"):
      reg_FLAGS_binary=binary_extension(binary(reg_code_value['111']),16)
      if reg_FLAGS_binary[-2]=='1': #if greater than
          jump=1
      else:
        jump=0
       
  #for je instruction
  if(instrn[0:5]=="01111"):
      reg_FLAGS_binary=binary_extension(binary(reg_code_value['111']),16)
      if reg_FLAGS_binary[-1]=='1': #if equal to
          jump=1
      else:
        jump=0


  #converting all the values to 8 bit and 16 bit binary format
  pc_str=binary8(PC)
  R0_str=(binary(reg_code_value['000']) if type(reg_code_value['000'])==int else "00000000"+ref_dic[reg_code_value['000']])
  R1_str=(binary(reg_code_value['001']) if type(reg_code_value['001'])==int else "00000000"+ref_dic[reg_code_value['001']])
  R2_str=(binary(reg_code_value['010']) if type(reg_code_value['010'])==int else "00000000"+ref_dic[reg_code_value['010']])
  R3_str=(binary(reg_code_value['011']) if type(reg_code_value['011'])==int else "00000000"+ref_dic[reg_code_value['011']])
  R4_str=(binary(reg_code_value['100']) if type(reg_code_value['100'])==int else "00000000"+ref_dic[reg_code_value['100']])
  R5_str=(binary(reg_code_value['101']) if type(reg_code_value['101'])==int else "00000000"+ref_dic[reg_code_value['101']])
  R6_str=(binary(reg_code_value['110']) if type(reg_code_value['110'])==int else "00000000"+ref_dic[reg_code_value['110']])
  RFLAGS_str=binary(reg_code_value['111'])

  instruction_output.append(pc_str)
  instruction_output.append(R0_str)
  instruction_output.append(R1_str)
  instruction_output.append(R2_str)
  instruction_output.append(R3_str)
  instruction_output.append(R4_str)
  instruction_output.append(R5_str)
  instruction_output.append(R6_str)
 
  #PC+=1 #adding 1 to the program counter
  if jump==True:
    PC=int(instrn[8:16],2) #converting it into decimal format
  else:
    PC=PC+1

  if reg_code_value['111']==prev_flags:
      reg_code_value['111']=0
     
  prev_flags=reg_code_value['111']

  RFLAGS_str=binary(reg_code_value['111'])
  instruction_output.append(RFLAGS_str)
  output_list.append(instruction_output) #adding that list to a final output list
         
  #if instrn[0:5] not in ["11111","01100","01101","01111"]:
  print(pc_str,R0_str,R1_str,R2_str,R3_str,R4_str,R5_str,R6_str,RFLAGS_str)
  cycle_counter+=1 #adding 1 to the cycle counter at the end of every cycle
 
  #print(pc_str_final,R0_str_final,R1_str_final,R2_str_final,R3_str_final,R4_str_final,R5_str_final,R6_str_final,RFLAGS_str_final)

"""
#printing the output list
for i in output_list:
    for j in i:
        print(j,end=" ") #printing PC and register values of each instruction
    print()
"""

var_count=len(varmem_value)
total_memory_locations=PC+var_count



if flag_check==1:

    #for memory dump
    #print()
    #print("Memory Dump: ")
    #print()
   
    for i in input_list:
      print(i)

    for i in sorted(varmem_value):
      #print(i,end=" ") #uncomment this to see the memory location of the variable
      print(binary(varmem_value[i]))

    #for memory locations
    #print("Total memory locations: ",total_memory_locations)
   
    for i in range(total_memory_locations,256):
      print("0"*16)
print("\n")
#Uncomment this part to see the graph
"""
plt.scatter(cycle_list,memory_access_list)
plt.xlabel("Cycle Number")
plt.ylabel("Memory Location (in Decimal)")
plt.show()

"""
