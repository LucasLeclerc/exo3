import sys
import csv

def OperationSigne(operation:str):
    if operation == '+':
        return 'addition'
    if operation == '-':
        return 'soustraction'
    if operation == '*':
        return 'multiplication'
    if operation == '/':
        return 'division'
def calcule(val1:int, val2:int, operation:str):
    if operation == '+':
        return val1 + val2
    if operation == '-':
        return val1 - val2
    if operation == '*':
        return val1 * val2
    if operation == '/':
        if val2==0:
            return 'error'
        return val1 / val2
def operation(listValue:list[int],signe:str):
    result=[]
    result.append(listValue[0])
    for i in range(len(listValue)-1):
        result.append(calcule(result[-1],listValue[i+1],signe))
        if(result[-1]=='error'):
            return 'error'
    return result

def printResult(listInput:list[int],listResult:list[int],signe:str):
    print('\t' + str(listResult[0]))
    for i in range(len(listResult) - 1):
        print('\t+' + str(listInput[i + 1]) + ' (=' + str(listResult[i+1]) + ')')
    print('\t-------')
    print('total = ' + str(listResult[-1]) + '(' + OperationSigne(signe) + ')')
def convertListToInt(strlist:list[str]):
    return list(map(lambda x: int(x), strlist))

if __name__ == '__main__':
    filename=sys.argv[1]
    signe=sys.argv[2]

    value=[]

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            value.append(row[0])

    value=convertListToInt(value)

    listResult=operation(value,signe)
    if(listResult=='error'):
        print("erreur lors du calcule")
    printResult(value,listResult,signe)