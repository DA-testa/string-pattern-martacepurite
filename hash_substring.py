# python3


B=13
Q=256


def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    inp=input()

    if(inp.startswith("F")):
        file=open("tests/06","r")
        pat=file.readline().rstrip()
        txt=file.readline().rstrip()
    elif(inp.startswith("I")):
        pat=input().rstrip()
        txt=input().rstrip()

    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pat, txt)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))


def get_hash(pattern: str)->int:
    global B,Q
    m=len(pattern)
    result=0
    for i in range(m):
        result=(B*result+ord(pattern[i]))%Q

    return result

    

def get_occurrences(pattern, txt):
    # this function should find the occurances using Rabin Karp alghoritm 
    
    global B,Q

    occurences=[]

    pattern_len=len(pattern)
    text_len=len(txt)

    pattern_hash=get_hash(pattern)

    text_hash=get_hash(txt[:pattern_len])

    multiplier=1

    for i in range(1,pattern_len):
        multiplier=(multiplier*B)%Q

    # print(text_hash)
    if text_hash==pattern_hash:
            occurences.append(0)


    for j in range(0,text_len-pattern_len):

        # print(text_hash)
        text_hash=(text_hash+B*Q-ord(txt[j])*multiplier)%Q
        text_hash=(text_hash*B+ord(txt[j+pattern_len]))%Q

        if text_hash==pattern_hash:
            if(get_hash(txt[j+1:j+1+pattern_len])==pattern_hash):
                occurences.append(j+1)

    # and return an iterable variable
    return occurences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

