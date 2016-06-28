# Education

## Description
This class represents the education part of the school life

## Parent class
None

## Attributes

* ```project```
  * data type: string
  * description: contains the name of the project
* ```knowledge_delta```
  * data type: integer
  * description: contains a number, that change the value of the knowledge_level of the students
* ```happyness_delta```
  * data type: integer
  * description: contains a number, that change the value of the happyness_level of the students

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None

## Class methods

### ```not_exam```

#### Arguments
A person object and a mentor object

#### Return value
None

### ```private_mentoring```

#### Arguments
A person object and a mentor object

#### Return value
None

### ```peer_mentoring```

#### Arguments
2 person object

#### Return value
None

### ```create_by_csv```

#### Arguments
A csv file name

#### Return value
A list of education objects
