%option noyywrap

%{
#include<bits/stdc++.h>
using namespace std;

ofstream yyoutlog; //output filestream for log file

string loglist = ""; //list of tokens along with line numbers

// define necessary c++ variables and functions here (if any)
int lines = 1;

%}

/* Regular Definitions */

delim	 [ \t\v\r]

/* write regular expressions for whitespace and newline */
ws [ ]		 

newline [\n]  

letter	 [A-Za-z]
digit	 [0-9]

/* write regular expressions for id, float and integers */

integers [0-9]+
id [a-zA-Z_][a-zA-Z0-9_]*		 
float {digit}*"."{digit}+(e[+-]?{digit}+)?

%%

{ws} { /* ignore whitespace */ }

{newline} {

        /* do necessary bookkeeping (line number tracking etc.) */
		lines += 1;		
    }


if     {
			loglist="Line no "+to_string(lines)+": Token <IF> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}


else   {
			loglist="Line no "+to_string(lines)+": Token <ELSE> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}


for     {
			loglist="Line no "+to_string(lines)+": Token <FOR> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}


while  {
			loglist="Line no "+to_string(lines)+": Token <WHILE> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}
		

 do    {
			loglist="Line no "+to_string(lines)+": Token <DO> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}

break  {
			loglist="Line no "+to_string(lines)+": Token <BREAK> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}

int    {
			loglist="Line no "+to_string(lines)+": Token <INT> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}


char    {
			loglist="Line no "+to_string(lines)+": Token <CHAR> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}


float    {
			loglist="Line no "+to_string(lines)+": Token <FLOAT> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}


double    {
			loglist="Line no "+to_string(lines)+": Token <DOUBLE> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}


void    {
			loglist="Line no "+to_string(lines)+": Token <VOID> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}


return    {
			loglist="Line no "+to_string(lines)+": Token <RETURN> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}


switch    {
			loglist="Line no "+to_string(lines)+": Token <SWITCH> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}


case    {
			loglist="Line no "+to_string(lines)+": Token <CASE> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}


default    {
			loglist="Line no "+to_string(lines)+": Token <DEFAULT> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}


continue   {
			loglist="Line no "+to_string(lines)+": Token <CONTINUE> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}


goto    {
			loglist="Line no "+to_string(lines)+": Token <GOTO> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}


printf    {
			loglist="Line no "+to_string(lines)+": Token <PRINTF> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}


{integers} {
			loglist="Line no "+to_string(lines)+": Token <CONST_INT> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		   }


{id} {
			loglist="Line no "+to_string(lines)+": Token <ID> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}

{float}    {
			loglist="Line no "+to_string(lines)+": Token <CONST_FLOAT> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		   }


"+"|"-" { /* to match two same operators use | */
			loglist="Line no "+to_string(lines)+": Token <ADDOP> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}


"*"|"/"|"%" { 
			loglist="Line no "+to_string(lines)+": Token <MULOP> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}

"++"|"--" { 
			loglist="Line no "+to_string(lines)+": Token <INCOP> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		  }

"<"|">"|"=="|"<="|">="|"!=" { 
			loglist="Line no "+to_string(lines)+": Token <RELOP> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}


"="     { 
			loglist="Line no "+to_string(lines)+": Token <ASSIGNOP> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}


"&&"|"||" {
			loglist="Line no "+to_string(lines)+": Token <LOGICOP> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		 }

"!"     { 
			loglist="Line no "+to_string(lines)+": Token <NOT> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}

"("     { 
			loglist="Line no "+to_string(lines)+": Token <LPAREN> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}

")"     { 
			loglist="Line no "+to_string(lines)+": Token <RPAREN> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}

"{"     { 
			loglist="Line no "+to_string(lines)+": Token <LCURL> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}

"}"     { 
			loglist="Line no "+to_string(lines)+": Token <RCURL> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}

"["     { 
			loglist="Line no "+to_string(lines)+": Token <LTHIRD> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}

"]"     { 
			loglist="Line no "+to_string(lines)+": Token <RTHIRD> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}

","     { 
			loglist="Line no "+to_string(lines)+": Token <COMMA> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}

":"     { 
			loglist="Line no "+to_string(lines)+": Token <COLON> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}


";"     { 
			loglist="Line no "+to_string(lines)+": Token <SEMICOLON> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}



%%

int main(int argc, char *argv[])
{

	if(argc != 2) //check if file name is given
	{
		cout<<"Please input file name"<<endl;
		return 0;
	}

	yyin = fopen(argv[1], "r"); //the file to be read must be assigned to yyin

	yyoutlog.open("22341082_log.txt", ios::trunc); // remember to rename the log file as mentioned in the spec
	
	if(yyin == NULL) // file does not exist
	{
		// print error message and exit
		cout << "Can not find the input file\n";
	}
	
	yylex(); // start reading the input file in a loop
	
	//print total number of lines found in the input file
	
	loglist = "Total lines: " + to_string(lines);
	yyoutlog<<loglist;
	
	yyoutlog.close();  // close the log file
	
	fclose(yyin); // close the input file
}
