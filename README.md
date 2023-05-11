# DjangoSchoolApp
This app is a simple rest API to maganage students in school.

## Models
__Schools__ have a name (_name_) and a maximum number of students (_max_numb_). It isn't possible to add students to an already full school.
```json
{
  "id": 1,
  "name": "Hogwarts",
  "max_numb": 750
}
```

__Students__ have a name (_name_), a last name (_last_name_), a birthday (_birthday_), an automatically unique string identifier (_str_id_) and an automatically filled creation date (_creation_date_).
```json
{
  "id": 1,
  "name": "Harry",
  "last_name": "Potter",
  "str_id": "\u0001",
  "creation_date": "2019-09-12",
  "birthday": "1989-09-12",
  "school": 1
}
```

## What you can do
The API allows a set of actions depending on the route:
* /schools/ allows to list the schools (_GET_) or create a new school (_POST_)
* /schools/X allows to retrieve the school _X_ (_GET_), modify this school (_PUT_ or _PATCH_) or delete it (_DELETE_)
* /students/ allows to list the students (_GET_) or create a new student (_POST_)
* /students/X allows to retrieve the student _X_ (_GET_), modify this student (_PUT_ or _PATCH_) or delete it (_DELETE_)
* the same actions are possible at the route /schools/Y/students but result will be filtered for the specified school
* student request can be filtered with _?name=Michel_ or _?year=1989_ or _?order=birthday_
