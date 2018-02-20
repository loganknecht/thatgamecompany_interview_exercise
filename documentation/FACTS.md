- Languages
    - Python
    - JavaScript

- Technology
    - Git
    - Pip
    - Postman
    - Sqlite

- Libraries
    - Python
        - Django
        - Django Rest Framework
        - Gunicorn
        - Locust
        - Pdb PP
            - Debuging
        - Pytest
        - Pytest Django
        - VirtualEnv
    - JavaScript
        - React
        - React Router

- Branching Strategy
    - master
        - Gold copy, only feature complete with tests allowed
    - development
        - Feature complete allowed here
    - spike/
        - Branch prefix for determining how features might work
    - feature/
        - Branch prefix for implementing well understood functions


- Codebase Code Information
```
(venv) ╭─Hugbot@Hugbots-MacBook-Pro  ~/Repositories/thatgamecompany_interview_exercise  ‹master*› 
╰─$ cloc .
      65 text files.
      65 unique files.                              
      10 files ignored.

github.com/AlDanial/cloc v 1.76  T=1.07 s (55.0 files/s, 5214.3 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Markdown                         8            782              0           1849
JSON                             6              0              0            980
Python                          29            243            361            779
JavaScript                       7             25             46            242
CSS                              5             17              5            181
make                             1              1              0             32
HTML                             1              3             20             17
INI                              1              0              0              3
Bourne Shell                     1              1              2              1
-------------------------------------------------------------------------------
SUM:                            59           1072            434           4084
-------------------------------------------------------------------------------
```