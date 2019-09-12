# ApiProblemResolver by Josimar Andrade

Objective / Problem Descriptions
As seen in the API endpoints section, this homework assignment has two parts. You are expected to write a program that GETs problem input and POSTs a solution to both problems, /problem/part_1 and /problem/part_2. There is an example problem endpoint /problem/test that you can use to build/test the general structure of your solution. Both of the required /problem/* endpoints also accept the query param ?sample=true which enables an "example-mode" for each problem. In "example-mode", the input sent to you is similar in nature to the large randomized data-set you would normally receive, but human-sized and static -- "example-mode" also disables the 5s response time-limit.

* Requirements
- Problem 1:
Given a collection of roundtrip Fares and Legs, determine the total time (in seconds, rounded down) spent in the air for a given Fare.

- Problem 2:
Given a collection of roundtrip Fares and Legs, determine the viable return-leg ids for a given outbound-leg id. A viable combination of Legs is one where both outbound and return Leg are present in the leg-list of a Fare.


## File directory
```
.
├── app.py                    -->   Main application
├── challenge.md              -->   The full challenge
├── config.yml                -->   API configurations
├── part_1_reply.json         -->   Data exemple
├── part_1_response.json      -->    "
├── part_2_reply.json         -->    "
├── part_2_response.json      -->    "
├── README.md                 -->   This file
├── requirements.txt          -->   Application dependencis
├── src                       -->   Others codes files
│   ├── APIcontroller.py      -->   HTTP/ API controler
│   ├── ApiUtil.py            -->   Utilities functions
│   ├── data_model            -->   Class represents there json/ymal models
│   │   ├── Config.py         -->     "
│   │   ├── Part1reply.py     -->     "
│   │   ├── Part1Response.py  -->     "
│   │   ├── Part2reply.py     -->     "
│   │   ├── Part2Response.py  -->     "
│   ├── Problem.py            -->    class that solve the problems
├── test.py                   -->    test file



```

## Installation/run.
```

# Creating virtual environment:
    python3 -m venv env
# Activating virtual environment: 
    source env/bin/activate
# Install dependencies: 
    pip install -r requirements.txt
# Test:
    python -m unittest test.py
# run:
    python app.py
```

## License
Copyright (c) 2019. Josimar Andrade, No Rights Reserved
