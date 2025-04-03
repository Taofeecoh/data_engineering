### Task 1
Create a function that return the first name of anyone
Create another function that return the last name of anyone
Then Create a function that will concatenate the first name and the last name that will be returned from those 2 functions above.
Please use F string interpolation to return a readable message. 
It can be something like, My full name is x y. 
Hint: The first 2 functions will be used inside the third function.

### Task 2
Create a list of the below attributes
first name
last_name
date of birth
Transform the name of the attributes to follow the naming convention we have in the last_name
Meaning, at the end, the final list should be first_name, last_name, date_of_birth
Please make sure the newly transformed attributes are put inside another list.

### Task 3
Create a list with the following names
Mayowa
chizoba
Chigozie
Write a code that will extract names that begin with a capital letter and end with letter a
But If there is any name that begin with a capital letter but doesn’t end with letter a like Chigozie, convert its last letter to letter a, at the end it will turn it to Chigozia
Hint: The final list should contain just Mayowa and Chigozia 

### Task 4
Let’s assume we usually receive some data from the marketing team every monday inside a list. Elements expected inside that list are the names of the customers.
Let’s assume what they sent contains  Wofai, Zainab, A4atullah
Write a function that will intentionally make your code fail if what they have inside that list doesn’t look like a valid name, this will allow us to quickly get in touch with the marketing team that they have a bad entry.
In the values above, you can see A4atullah is a bad entry.
So it should fail when it gets to A4atullah.
Please when you are writing that function , make sure it gives the exact entry that is bad with a meaningful message, so that we can be sure of the specific entry and relay back to the marketing team.

### Task 5
Write a geenric function to filter out bad entries in a list using the "yield" keyword.
