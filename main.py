import re

class Program:

    def readFile(self, fileName):

        lineList = []

        # Read file and append each line to lineList if it has content and is not an empty line
        with open(fileName, 'r') as f:
            for line in f:
                if line not in ['\n', '\r\n']:
                    lineList.append(line.strip())
        
        # Pass the lineList to the program function
        self.program(lineList)

    # <program> -> program begin <statement_list> end
    def program(self, list):

        # Check if program begins with 'program', and 'begin' and ends with 'end'
        if (list[0] == 'program' and list[1]=='begin' and list[len(list) - 1]=='end'):
            # The statement before the 'END' keyword must NOT have a semicolon, so if it does, then raise an error
            if (";" in list[len(list) - 2]):
                raise SyntaxError('The program contains syntax errors.')
            del list[-1]
            del list[0:2]

            # Pass the <statement_list> portion of the code to statement_list func
            self.statement_list(list)
            return True
        else:
            # Raise exception of syntax error if <program> statement is invalid
            raise SyntaxError('The program contains syntax errors.')

    # <statement_list> -> <statement> {;<statement>}
    def statement_list(self, list):

        # Get each individual <statement> which is separated by a ';'
        listString = ' '.join(list)
        list = listString.split(';')
        # Remove any blank spaces in the list
        try:
            while True:
                list.remove('')
        except ValueError:
            pass
        # Pass each individual statement separated by a semicolon to the statement func
        for i in list:
            i = i.strip()
            self.statement(i)
    
    # <statement> -> <assignment_statement> | <if_statement> | <loop_statement>
    def statement(self, listString):
        list = listString.split(' ')
        # Remove any blank spaces in the list
        try:
            while True:
                list.remove('')
        except ValueError:
            pass


        list[:] = (value for value in list if value != '')
        list[:] = (value for value in list if value != ' ')
        
        # If the <statement> is an <if_statement>
        if (list[0] == 'if'):

            ifList = listString.split('if', 1)
            ifList[:] = (value for value in ifList if value != ' ')
            ifList[:] = (value for value in ifList if value != '')

            for i in ifList:
                if (i != ''):
                    i = i.strip()
                    self.if_statement(i)

        # If the <statement> is a <loop_statement>
        elif (list[0] == 'loop'):
            # del the 'loop' keyword
            del list[0]
            self.loop_statement(list)
        # If the <statement> is an <assignment_statement>
        else:
            self.assignment_statement(list)
        
    # <if_statement> -> if (<logic_expression>) then <statement>
    def if_statement(self, listString):

        if ('then' in listString):
            # Remove and split with the 'then' keyword, then remove any /n elements
            list = listString.split('then', 1)
            list[:] = (value for value in list if value != ' ')
            list[:] = (value for value in list if value != '')


            # list[0] is the (<logic_expression>) and list[1] is the <statement>
            # Check if parentheses are balanced
            if(self.parenthesesCheck(list[0])):
                # Get the content inside the parentheses and pass it to logic_expression func
                insideParentheses = list[0][list[0].find('(')+1:list[0].find(')')]
                self.logic_expression(insideParentheses)
            # Raise exception if parentheses not balanced
            else:
                raise SyntaxError('The program contains syntax errors.')

            # Get the statement content and pass it to the statement func
            self.statement(list[1])

        # Raise an exception if the 'then' keyword is absent in the <if_statement>
        else:
            raise SyntaxError('The program contains syntax errors.')
        
    # <loop_statement> -> loop (<logic_expression>) <statement>
    def loop_statement(self, list):
        listString = ' '.join(list)

        # Ensure parentheses are present
        if not ('(' and ')' in listString):
            raise SyntaxError('The program contains syntax errors.')

        d = ")"
        list =  [i + d for i in listString.split(d) if i]
        list[1] = list[1].replace(')','')

        # list[0] is the (<logic_expression>) and list[1] is the <statement>
        # Check if parentheses are balanced
        if(self.parenthesesCheck(list[0])):
            # Get the content inside the parentheses and pass it to logic_expression func
            insideParentheses = list[0][list[0].find('(')+1:list[0].find(')')]
            self.logic_expression(insideParentheses)
        # Raise exception if parentheses not balanced
        else:
            raise SyntaxError('The program contains syntax errors.')

        # Get the statement content and pass it to the statement func
        self.statement(list[1])


    # <assignment_statement> -> <variable> = <expression>
    def assignment_statement(self,list):
        listString = ' '.join(list)
        print(listString)
        # The statement must NOT contain ANY keywords like 'if' and 'then', because if it does then that means there was a missing semicolon for one of the statements
        if('if' in listString or 'then' in listString):
            raise SyntaxError('The program contains syntax errors.')

        if ('=' in listString):
            list = listString.split('=')
            # list[0] is the <variable> and list[1] is the <expression>
            # Send to variable func
            self.variable(list[0].strip())
            # Send to expression func
            self.expression(list[1].strip())

    # <logic_expression> -> <variable> (< | >) <variable>
    def logic_expression(self, insideParentheses):
        if('>' or '<' in insideParentheses):
            insideParentheses = insideParentheses.replace('<','>')
            list = insideParentheses.split('>')

            # Ensure there is only one occurrence of (< | >)
            if (insideParentheses.count('>') > 1):
                raise SyntaxError('The program contains syntax errors.')

            # Send the two variables to the variable func
            for i in list:
                i = i.strip()
                self.variable(i)

        else:
            raise SyntaxError('The program contains syntax errors.')

    # <expression> -> <term> { (+|-) <term>}
    def expression(self, listString):
        # We cannot include anything in brackets, example, (var2 + var1) * var3, this is only one <term> with no optional second part
        # If the expression contains brackets, AND the parentheses are valid, do NOT evaluate anything inside the brackets
        # If there are brackets, then it MUST be a single term and we can simply send the ENTIRE TERM to the term function
        if ("(" in listString or ")" in listString):
            if(self.parenthesesCheck(listString)):
                self.term(listString)
            else:
                raise SyntaxError('The program contains syntax errors.')
        # if there are no parentheses, and there is a positive or negative sign present
        elif ("-" in listString):
            list = listString.split("-")
            for i in list:
                i=i.strip()
                self.term(i)
        elif ("+" in listString):
            list = listString.split("+")
            
            for i in list:
                i=i.strip()
                self.term(i)
        # If there are no brackets, we can send the entire term to the term function
        else:
            self.term(listString)

    # <variable> -> identifier (An identifier is a string that begins with a letter followed by 0 or more letters and/or digits)
    def variable(self, identifier):
        # Check if the identifier is valid:
        # An identifier is a string that begins with a letter followed by 0 or more letters and/or digits
        identifierList = list(identifier)

        # Check if the first character in the text is a letter
        if (identifierList[0].isalpha()):
            for i in identifierList:
                if not (i.isalpha() or i.isdigit()):
                    raise SyntaxError('The program contains syntax errors.')
                else:
                    return True
        else:
            raise SyntaxError('The program contains syntax errors.')

    # <term> -> <factor> {(* | /) <factor> }
    def term(self, listString):
        
        # If the term contains a * or /
        if ("*" in listString):
            list = listString.split('*')
            for i in list:
                i=i.strip()
                self.factor(i)
        elif ("/" in listString):
            list = listString.split('/')
            for i in list:
                i=i.strip()
                self.factor(i)
        #else it is simply a <factor> so we send to factor func
        else:
            self.factor(listString)
  
    # <factor> -> identifier | int_constant | (<expr>)
    def factor(self, listString):
        # We have to determine if it is either an identifier, int constant or expression.
        # If the factor contains parentheses which are valid, send the content inside the parentheses to the expression func
        if ("(" in listString or ")" in listString):
            if(self.parenthesesCheck(listString)):
                insideParentheses = listString[listString.find('(')+1:listString.find(')')]
                insideParentheses=insideParentheses.strip()
                self.expression(insideParentheses)
            else:
                raise SyntaxError('The program contains syntax errors.')
        # if the factor is an int constant
        elif (listString.isdigit()):
            return
        # If the factor is not a int or expression inside parentheses, then we send to the variable function to check if it is a valid identifier.
        else:
            self.variable(listString)
  
    # Function returns true if parentheses are balanced, and false otherwise
    def parenthesesCheck(self, string):
        stack = []
        for i in string:
            if (i == '('):
                stack.append(i)
            elif (i ==')'):
                if ((len(stack) > 0) and ('(' == stack[len(stack)-1])):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
    

def isIdentifier(identifier):
    # Check if the identifier is valid:
    # An identifier is a string that begins with a letter followed by 0 or more letters and/or digits
    identifierList = list(identifier)

    # Check if the first character in the text is a letter
    if (identifierList[0].isalpha()):
        for i in identifierList:
            if not (i.isalpha() or i.isdigit()):
                return False
        # Return true if the identifier is able to exit the for loop
        return True
    else: #If the identifier does not begin with a letter or char
        return False

#Function checks if string is a keyword of the language, such as 'if' or 'loop'
def isKeyword(operator):
    if(operator=='if' or operator=='loop' or operator=='program' or operator=='begin' or operator=='end' or operator=='then'):
        return True
    else:
        return False

# Function for tokens which returns the token value
def tokenLookup(string):

    if string.isdigit(): #Int constant
        return 10
    elif isKeyword(string): #Reserved keyword
        return 15
    elif string=='=':
        return 20
    elif string=='+':
        return 21
    elif string=='-':
        return 22
    elif string=='*':
        return 23
    elif string=='/':
        return 24
    elif string=='(':
        return 25
    elif string==')':
        return 26
    elif isIdentifier(string): #Valid variable/identifier
        return 11
    else: #-1 is returned if the string matches none of the tokens
        return -1

def lexicalAnalyzer(fileName):
    
    list = []

    # Read file and append each line to lineList if it has content and is not an empty line
    with open(fileName, 'r') as f:
        for line in f:
            if line not in ['\n', '\r\n']:
                list.append(line.strip())
   
    newList=[]          
    newList = [word for line in list for word in line.split()]
    
    for i in newList:
        if not i.isalnum(): # If string contains non-alphanumeric chars
            li = re.split("(\W)", i)
            # Strip spaces and blanks from the list
            try:
                while True:
                    li.remove('')
            except ValueError:
                pass
                
            for j in li:
                str = f"Next token is: {tokenLookup(j)} Next lexeme is {j}"
                print(str)
        else:
            str = f"Next token is: {tokenLookup(i)} Next lexeme is {i}"
            print(str)


# MAIN SECTION ---------------

### FOR THE TA OR INSTRUCTOR ## If you would like to change the file name, please just alter this variable with the new file name
currentFile = 'test-program-6.txt'
### ------------------------------------------


Program().readFile(currentFile)
lexicalAnalyzer(currentFile)
