#  KNN API
##  Batch 1 - Cinta Negra 
------------

The main goal of this API is to have a Data Set of Apartments, Houses, Departments and/or Buildings where
you can send a list of places and the API determines wich type of building it is.

Example:

Request:

```
[{
    "rooms": 1, 
    "area": 350, 
    "floors":2,
    "type": ""
}]
```

Response:
```
[{
    "rooms": 1, 
    "area": 350, 
    "floors":2,
    "type": "house"
}]
```