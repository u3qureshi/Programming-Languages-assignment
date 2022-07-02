# Lexical Analyzer for a hypothetical imperative programming language

Assignment instructions:

Given the grammar for a hypothetical imperative programming language, write a program that analyzes the syntax of input programs for the language. Your program should read an input test program from a file and then determine whether or not it contains any syntax errors. The program does not have to show where the syntax error occurred or what kind of error it was. You can use any programming language you prefer to write the program.

In your program:

    1) Implement a lexical analyzer as a subprogram of your program. Each time the lexical analyzer is called, it should return the next lexeme and its token code.
    2) Implement a parser based on the following EBNF rules. Create a subprogram for each nonterminal symbol which should parse only sentences that can be generated by the nonterminal.
    
          <program> -> program begin <statement_list> end
          <statement_list> -> <statement> {;<statement>}
          <statement> -> <assignment_statement> | <if_statement> | <loop_statement>
          <assignment_statement> -> <variable> = <expression>
          <variable> -> identifier (An identifier is a string that begins with a letter followed by 0 or more letters and/or digits)
          <expression> -> <term> { (+|-) <term>}
          <term> -> <factor> {(* | /) <factor> }
          <factor> -> identifier | int_constant | (<expr>)
          <if_statement> -> if (<logic_expression>) then <statement>
          <logic_expression> -> <variable> (< | >) <variable> (Assume that logic expressions have only less than or greater than operators)
          <loop_statement> -> loop (<logic_expression>) <statement>

Sample output of a program without syntax errors:
----------------------------------------
Next token is: 15 Next lexeme is program
Next token is: 15 Next lexeme is begin
Next token is: 11 Next lexeme is sum1
Next token is: 20 Next lexeme is =
Next token is: 11 Next lexeme is var1
Next token is: 21 Next lexeme is +
Next token is: 11 Next lexeme is var2
Next token is: -1 Next lexeme is ;
Next token is: 11 Next lexeme is sum2
Next token is: 20 Next lexeme is =
Next token is: 11 Next lexeme is var3
Next token is: 21 Next lexeme is +
Next token is: 11 Next lexeme is var2
Next token is: 23 Next lexeme is *
Next token is: 10 Next lexeme is 90
Next token is: -1 Next lexeme is ;
Next token is: 11 Next lexeme is sum3
Next token is: 20 Next lexeme is =
Next token is: 25 Next lexeme is (
Next token is: 11 Next lexeme is var2
Next token is: 21 Next lexeme is +
Next token is: 11 Next lexeme is var1
Next token is: 26 Next lexeme is )
Next token is: 23 Next lexeme is *
Next token is: 11 Next lexeme is var3
Next token is: -1 Next lexeme is ;
Next token is: 15 Next lexeme is if
Next token is: 25 Next lexeme is (
Next token is: 11 Next lexeme is sum1
Next token is: -1 Next lexeme is <
Next token is: 11 Next lexeme is sum2
Next token is: 26 Next lexeme is )
Next token is: 15 Next lexeme is then
Next token is: 15 Next lexeme is if
Next token is: 25 Next lexeme is (
Next token is: 11 Next lexeme is var1
Next token is: -1 Next lexeme is >
Next token is: 11 Next lexeme is var2
Next token is: 26 Next lexeme is )
Next token is: 15 Next lexeme is then
Next token is: 11 Next lexeme is var4
Next token is: 20 Next lexeme is =
Next token is: 11 Next lexeme is sum2
Next token is: 22 Next lexeme is -
Next token is: 11 Next lexeme is sum1
Next token is: -1 Next lexeme is ;
Next token is: 15 Next lexeme is loop
Next token is: 25 Next lexeme is (
Next token is: 11 Next lexeme is var1
Next token is: -1 Next lexeme is <
Next token is: 11 Next lexeme is var2
Next token is: 26 Next lexeme is )
Next token is: 11 Next lexeme is var5
Next token is: 20 Next lexeme is =
Next token is: 11 Next lexeme is var4
Next token is: 24 Next lexeme is /
Next token is: 10 Next lexeme is 45
Next token is: 15 Next lexeme is end
----------------------------------------
