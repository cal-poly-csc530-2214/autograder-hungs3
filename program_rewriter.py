"""
    The first step for this paper is to convert python programs and an added eml file into
    a "minipy" program.
"""
import re

EML_RULES = [
    "return x-> return [0]",
    "range(x, y)-> range(x+1, y)",
    "x == y-> False"
]
# return [\w|\d\s@#{L}\(\)]+
# range\([\w|\d\s@#{L}\(\)]+, [\w|\d\s@#{L}\(\)]+\)
# [\w|\d\s@#{L}\(\)]+ == [\w|\d\s@#{L}\(\)]+

def convertRules():
    regexRules = {}
    for eml in EML_RULES:
        LHS = eml.split("->")[0]
        regexed = LHS.replace("x", "[\w|\d\s@#{L}\(\)\[\]]+")
        regexed = regexed.replace("y", "[\w|\d\s@#{L}\(\)\[\]]+")
        regexRules[regexed] = eml.split("->")[1] 
    print(regexRules)
    return regexRules

def convertFile(strArr):
    regRules = convertRules()
    for i, line in enumerate(strArr):
        for rule in regRules.keys():
            # print("(" + rule + ")")
            found = re.finditer(rule, line)
            for pattern in found:
                cleaned = pattern.string.strip()
                cleanedArr = cleaned.split(" ")
                pStr = ""
                if pattern.span()[0] != 0:
                    pStr = pattern.string[:pattern.span()[0]]
                aStr = pattern.string[pattern.span()[1]:]
                # print("pStr: ", repr(pStr))
                # print("cleaned: ", cleaned)
                if "==" in cleaned: # equals case
                    newStr = re.sub(rule, pStr + " {" + cleaned + ", " + regRules[rule] + "} ", line)
                    strArr[i] = newStr
                    # print(repr(newStr))
                elif "return" in cleaned:
                    newStr = re.sub(rule, pStr + " {" + cleaned + ", " + regRules[rule] + "} " + "\n", line)
                    # print(repr(newStr))
                    strArr[i] = newStr
                elif "range" in cleaned:
                    newStr = re.sub(rule, " {" + cleaned + ", " + regRules[rule] + "} " , line)
                    # print(repr(newStr))
                    strArr[i] = newStr
    return strArr





def main():
    allLines = []

    # Read file
    fName = "test.py"
    f = open(fName, "r")
    for line in f:
        allLines.append(line)
    f.close()

    strArr = convertFile(allLines)

    # Write to file
    fw = open("test.mpy", "w")
    for a in strArr:
        print(a)
        fw.write(a)
    fw.close()





if __name__ == "__main__":
    main()
