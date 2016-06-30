# CodecoolClass

## Description
This class represents a real class @ Codecool, containing mentors and students working at the class.

## Parent class
None

## Attributes

* ```location```
  * data type: string
  * description: stores the city where the the class started
* ```year```
  * data type: integer
  * description: stores the year when the class started
* ```mentors```
   * data type: list (containing Mentor objects)
   * description: stores the mentors of the class
* ```students```
  * data type: list (containing Student objects)
  * description: stores the students of the class
* ```retorospectives```
  * data type: list (retro objects)
* ```events```
  * data type: list (event objects)
* ```education```
  * data type: list (education objects)
## Class methods

### ```generate_local```

Creates a ```CodecoolClass``` object having some real-life data from the implementer students' real class.

#### Arguments
None

#### Return value

```CodecoolClass``` object

## Instance methods

### ```do_event```
Picks two students for a peer-mentoring session.

#### Arguments
```integer ```
  * Type: integer
  * Description: we call the desired event from the list, according to this number.

#### Return value
None

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None

### ```count_students```
Counts the students.

#### Arguments
None

#### Return value
None
### ```count_mentors```
Counts the mentors.


#### Arguments
None

#### Return value
None


### ```check_energy```
Checks the energy level.

#### Arguments
None

#### Return value
```energy_level``` method



### ```class_do_gym```
Checks the energy level.

#### Arguments
```energy_level_counter ```
  * data_type: integer
  * description: shows the student's energy level


#### Return value
None



### ```do_project```
The students do a project given by the mentor.

#### Arguments
None

#### Return value
None

### ```find_student_by_full_name```

Gives back a student with the same full name as the argument from ```students```
#### Arguments
* ```full_name```
  * data_type: string
  * description: holds the full name of the student to be found

#### Return value
```Student``` object

### ```find_mentor_by_full_name```

#### Arguments
* ```full_name```
  * data_type: string
  * description: holds the full name of the mentor to be found

#### Return value
```Mentor``` object
