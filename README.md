# TimeLambda

This is an AWS lambda function which will take in arguments
name
and produce a unique name as the output: time21032118320000.txt
the file will contain the following output
Good Morning, (if before 12 AM), Good Afternoon, (if after 12 and before 6 PM) and Good Evening, (if after 6 PM) {name}; he current date and time is {datetime}. Thank you for visiting, please come again! 

Sample input JSON:

{
"name" : "John"
} 

