# Student

## Description
This class represents the students @ Codecool.

## Parent class
Person

## Attributes

* ```knowledge_level```
  * data type: integer
  * description: stores the knowledge levels of the students
* ```retrospective_objects```
  * data type: string
  * description: stores the thoughts of the students

## Class Methods

### ```creat_by_csv```
Read the students from a file

#### Arguments
* file_name


#### Return value
Return a list which containing the students.

## Instance Methods

### ```__init__```
The constructor of the object

#### Arguments
All of the arguments of the class itself with knowledge and retro

### ```knowledge_level_changer```
increase ```knowledge_level``` depend on the different events

#### Arguments
Delta: amount of changing

#### Return value
The new knowledge level
