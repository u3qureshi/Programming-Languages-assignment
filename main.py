
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

        # Pass each individual statement separated by a semicolon to the statement func
        for i in list:
            i = i.strip()
            self.statement(i)
    
    # <statement> -> <assignment_statement> | <if_statement> | <loop_statement>
    def statement(self, listString):
        list = listString.split(' ')
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
        print(listString)

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
            raise SyntaxError('The program contains syntax errors.')

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


Program().readFile('test-program-1.txt')
