# FoosballMatch

## Description
this class contains details about a soccer match

## Parent class
None

## Attribute
* ```result```
    * type: list
    * description: the result of the match


## Instance method

### ```soccer_match```

two players game with each other

#### Arguments
* ```person_1```
* ```person_2```

#### Return value
return a match result

### ```turn_result```
generate a random result of a turn

#### Argument
None

#### Return value
a turn result which is generated randomly (0-1, 1-0)

### ```crawl_under_table```

#### Arguments
* ```result```
    * type: int
    * description: result of the match
* ```person```
    type: person object
    description: who lose the match have to crawl under the table

#### Return value
None

### ```match_with_miki```
Miki plays a game with someone, and as usual, Miki loses. Also, he will crawl under the table. As usual.

#### Arguments
* ```person_1```
* ```miki```

#### Return value
None

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None
