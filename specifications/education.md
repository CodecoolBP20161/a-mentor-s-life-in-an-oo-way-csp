# Education

## Description
This class represents the education part of the school life

## Parent class
None

## Attributes

* ```lessons```
  * data type: string
  * description: contains the name of the lessons
* ```knowledge_delta```
  * data type: integer
  * description: contains a number, that change the value of the knowledge_level of the students
* ```happiness_delta```
  * data type: integer
  * description: contains a number, that change the value of the happiness_level of the students

## Instance methods

### ```__init__```
The constructor of the object.


#### Arguments

All of the arguments of the class itself.

#### Return value
None
## Static methods

### ```peer_mentoring```
Picks two students for a peer-mentoring session.

#### Arguments

```school ```
  * Type: Codecool Class object
  * Description: An instance of Codecool Class.

#### Return value
None

### ```private_mentoring```
Picks a mentor and a student for a private-mentoring session.

#### Arguments

```school ```
  * Type: Codecool Class object
  * Description: An instance of Codecool Class.

#### Return value
None

### ```not_exam```
Picks a student and a mentor for the 'not exam'.

#### Arguments

```school ```
  * Type: Codecool Class object
  * Description: An instance of Codecool Class.

#### Return value
None

## Class methods

### ```create_by_csv```

#### Arguments
A csv file name

#### Return value
A list of education objects
