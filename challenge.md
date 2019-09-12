Lola Backend Homework https://backend-candidate-homework.lola.co/
What we are looking for
This project helps us to evaluate your coding style, and how easy your code will be to work with in the future. With that in mind, we're looking for the following (in order of importance):

High quality, readable code
Well defined functions/modules/classes, documentation, reproducible build instructions
Test coverage
Completeness + correctness
Getting started
You should have been provided an api access token which must be sent with every request in an X-Lola-Homework-Access-Token: <your-token> header.

You can confirm your token is registered by sending a request to /token/test

$ curl https://backend-candidate-homework.lola.co/token/test -H 'X-Lola-Homework-Access-Token: <your-access-token>'
{"email": "you@me.com"}
API endpoints
You can hit these endpoints as many times as you need to!

[GET] /token/test: confirm you have a valid token

[GET, POST] /problem/test: An example problem you can use to build the general structure of your solutions. GET a simple test problem, POST back a response

$ curl https://backend-candidate-homework.lola.co/problem/test -H 'X-Lola-Homework-Access-Token: <your-access-token>'
# ... you should see a bunch of json information about the problem come back
# ... you will need to grab the `token` value to send back in your response
# ... note: this endpoint has a 5s time-limit (requires your response to come back within 5s)
# ...       to mimic the non-sample versions of part-1 and part-2
$ curl -X POST https://backend-candidate-homework.lola.co/problem/test -H 'X-Lola-Homework-Access-Token: <your-access-token>' -d '{"header": {"token": "<token-from-prev-request"}, "data": {"multiplication_result": 10}}'
[GET, POST] /problem/part_1: GET randomly generated problem-1 input, POST back your solution within 5s. Follows the same structure as /problem/test. Supports ?sample=true param to send static, simplified, example problem input with no time-limit.

$ curl https://backend-candidate-homework.lola.co/problem/part_1?sample=true -H 'X-Lola-Homework-Access-Token: <your-access-token>'
# ... you should see a bunch of json information about the problem come back
# ... you will need to grab the `token` value to send back in your response
$ curl -X POST https://backend-candidate-homework.lola.co/problem/part_1?sample=true -H 'X-Lola-Homework-Access-Token: <your-access-token>' -d '{"header": {"token": "<token-from-prev-request>"}, "data": {"total_seconds": 48600}}'
[GET, POST] /problem/part_2: GET randomly generated problem-2 input, POST back your solution within 5s. Follows the same structure as /problem/test Supports ?sample=true param to send static, simplified, example problem input with no time-limit.

All /problem/* endpoints support GETing problem data and POSTing back solutions.

The json data returned to GETs includes:

{
  token: string,                   # the request token expected to be sent back in the response
  description: string,             # a description of the problem, input, and expected response
  input: object,                   # problem input data to be processed
  arguments: object,               # values relevant to solving the problem
  expected_return_shape: object,   # the shape of the json expected to be POSTed back
  millisecond_time_limit: number,  # the number of milliseconds within which a response must be POSTed
}
The json data expected to be POSTed back follows the general shape (with specifics provided in expected_return_shape):

{
  header: {token: string},  # data identifying this submission, this is the problem-specific
                            # token sent with the problem input
  data: object,             # submission data to be validated
}
Objective / Problem Descriptions
As seen in the API endpoints section, this homework assignment has two parts. You are expected to write a program that GETs problem input and POSTs a solution to both problems, /problem/part_1 and /problem/part_2. There is an example problem endpoint /problem/test that you can use to build/test the general structure of your solution. Both of the required /problem/* endpoints also accept the query param ?sample=true which enables an "example-mode" for each problem. In "example-mode", the input sent to you is similar in nature to the large randomized data-set you would normally receive, but human-sized and static -- "example-mode" also disables the 5s response time-limit.

You are only required to GET input and POST a solution from/to /problem/part_1 and /problem/part_2, both without the ?sample=true param

If you have any questions, you can reach out to backend-homework@lola.com.

Once you're happy with your program, you should upload your solution to /upload/solution. There is a 1mb size limit on uploads. You can upload your solution as many times as you need to, but only your most recent upload will be retained.

$ curl https://backend-candidate-homework.lola.co/upload/solution -X POST -H 'X-Lola-Homework-Access-Token: <your-access-token>' -H 'X-Lola-Upload-Filename: <name-of-file-or-archive-being-uploaded>' -H Expect: --data-binary @<your-file-or-archive>
# -> {"upload_size_bytes": <size-of-your-upload>}
# double check your local file size
$ ls -l <file> | awk '{print $2 " bytes"}'

# e.x. assuming you made a tarball of your project and you're in the directory where the tarball is saved:
$ curl https://backend-candidate-homework.lola.co/upload/solution -X POST -H 'X-Lola-Homework-Access-Token: <your-access-token>' -H 'X-Lola-Upload-Filename: homework.tar.gz' -H Expect: --data-binary @homework.tar.gz
* You can GET problems and POST solutions as many times as you need!

* See the appendix for more information on the shape of the input data

- Problem 1:
Given a collection of roundtrip Fares and Legs, determine the total time (in seconds, rounded down) spent in the air for a given Fare.

- Problem 2:
Given a collection of roundtrip Fares and Legs, determine the viable return-leg ids for a given outbound-leg id. A viable combination of Legs is one where both outbound and return Leg are present in the leg-list of a Fare.

Appendix
* What are Fares and Legs?
Leg:
In the context of this assignment, a Leg is a complete flight.
Fare:
A Fare is a collection of Legs describing a complete trip. In the context of this assignment, all Fares are roundtrip - meaning they each have 2 legs, an outbound and return.
* Example request data:
Response from /problem/part_1?sample=true:
{
    "token": "f32af4ef400e457f9a9046e05939030d",
    "description": "You are provided a collection of flattened fares, where the legs of each fare are specified as a list of ids. Your problem argument is a Fare id. You are expected to return the total amount of time, in seconds - rounded down, spent in the air for this Fare.",
    "arguments": {
        "fare_id": "fare:0"
    },
    "expected_return_shape": {
        "header": {
            "token": "str"
        },
        "data": {
            "total_seconds": "int"
        }
    },
    "millisecond_time_limit": null,
    "input": {
        "fares": [
            {
                "id": "fare:0",
                "legs": [
                    "leg:0",
                    "leg:1"
                ]
            }
        ],
        "legs": [
            {
                "id": "leg:0",
                "airline": {
                    "code": "AA",
                    "name": "American Airlines",
                    "short_name": "American"
                },
                "flight_number": "123",
                "departure_airport": {
                    "state": "Massachusetts",
                    "state_code": "MA",
                    "name": "Boston, Logan International Airport",
                    "code": "BOS"
                },
                "arrival_airport": {
                    "state": "California",
                    "state_code": "CA",
                    "name": "San Francisco International Airport",
                    "code": "SFO"
                },
                "departure_utc": {
                    "iso": "2018-11-29T07:00:00+00:00"
                },
                "arrival_utc": {
                    "iso": "2018-11-29T13:30:00+00:00"
                }
            },
            {
                "id": "leg:1",
                "airline": {
                    "code": "AA",
                    "name": "American Airlines",
                    "short_name": "American"
                },
                "flight_number": "123",
                "departure_airport": {
                    "state": "California",
                    "state_code": "CA",
                    "name": "San Francisco International Airport",
                    "code": "SFO"
                },
                "arrival_airport": {
                    "state": "Massachusetts",
                    "state_code": "MA",
                    "name": "Boston, Logan International Airport",
                    "code": "BOS"
                },
                "departure_utc": {
                    "iso": "2018-12-01T05:00:00+00:00"
                },
                "arrival_utc": {
                    "iso": "2018-12-01T12:00:00+00:00"
                }
            }
        ]
    }
}
Expected response to /problem/part_1?sample=true:
{
    "header": {"token": "f32af4ef400e457f9a9046e05939030d"},
    "data": {"total_seconds": 48600}
}
Response from /problem/part_2?sample=true:
{
    "token": "de9dc37632c84f70bb08ef49a5cf0de0",
    "description": "You are provided a collection of flatten fares. Your input argument is an outbound leg id. You are expected to return all viable return-leg leg ids. A viable combination of outbound and return legs is one where both are present in the leg-list of a fare.",
    "arguments": {
        "outbound_leg_id": "leg:00"
    },
    "expected_return_shape": {
        "header": {
            "token": "str"
        },
        "data": {
            "return_leg_ids": "List[str]"
        }
    },
    "millisecond_time_limit": null,
    "input": {
        "fares": [
            {
                "id": "fare:0",
                "legs": [
                    "leg:00",
                    "leg:10"
                ]
            },
            {
                "id": "fare:1",
                "legs": [
                    "leg:00",
                    "leg:11"
                ]
            },
            {
                "id": "fare:2",
                "legs": [
                    "leg:01",
                    "leg:12"
                ]
            }
        ],
        "legs": [
            {
                "id": "leg:00",
                "airline": {
                    "code": "AA",
                    "name": "American Airlines",
                    "short_name": "American"
                },
                "flight_number": "123",
                "departure_airport": {
                    "state": "Massachusetts",
                    "state_code": "MA",
                    "name": "Boston, Logan International Airport",
                    "code": "BOS"
                },
                "arrival_airport": {
                    "state": "California",
                    "state_code": "CA",
                    "name": "San Francisco International Airport",
                    "code": "SFO"
                },
                "departure_utc": {
                    "iso": "2018-12-08T07:00:00+00:00"
                },
                "arrival_utc": {
                    "iso": "2018-12-08T13:30:00+00:00"
                }
            },
            {
                "id": "leg:01",
                "airline": {
                    "code": "AA",
                    "name": "American Airlines",
                    "short_name": "American"
                },
                "flight_number": "123",
                "departure_airport": {
                    "state": "Massachusetts",
                    "state_code": "MA",
                    "name": "Boston, Logan International Airport",
                    "code": "BOS"
                },
                "arrival_airport": {
                    "state": "California",
                    "state_code": "CA",
                    "name": "San Francisco International Airport",
                    "code": "SFO"
                },
                "departure_utc": {
                    "iso": "2018-12-08T07:00:00+00:00"
                },
                "arrival_utc": {
                    "iso": "2018-12-08T13:30:00+00:00"
                }
            },
            {
                "id": "leg:10",
                "airline": {
                    "code": "AA",
                    "name": "American Airlines",
                    "short_name": "American"
                },
                "flight_number": "123",
                "departure_airport": {
                    "state": "California",
                    "state_code": "CA",
                    "name": "San Francisco International Airport",
                    "code": "SFO"
                },
                "arrival_airport": {
                    "state": "Massachusetts",
                    "state_code": "MA",
                    "name": "Boston, Logan International Airport",
                    "code": "BOS"
                },
                "departure_utc": {
                    "iso": "2018-12-10T05:00:00+00:00"
                },
                "arrival_utc": {
                    "iso": "2018-12-10T12:00:00+00:00"
                }
            },
            {
                "id": "leg:11",
                "airline": {
                    "code": "AA",
                    "name": "American Airlines",
                    "short_name": "American"
                },
                "flight_number": "123",
                "departure_airport": {
                    "state": "California",
                    "state_code": "CA",
                    "name": "San Francisco International Airport",
                    "code": "SFO"
                },
                "arrival_airport": {
                    "state": "Massachusetts",
                    "state_code": "MA",
                    "name": "Boston, Logan International Airport",
                    "code": "BOS"
                },
                "departure_utc": {
                    "iso": "2018-12-10T05:00:00+00:00"
                },
                "arrival_utc": {
                    "iso": "2018-12-10T12:00:00+00:00"
                }
            },
            {
                "id": "leg:12",
                "airline": {
                    "code": "AA",
                    "name": "American Airlines",
                    "short_name": "American"
                },
                "flight_number": "123",
                "departure_airport": {
                    "state": "California",
                    "state_code": "CA",
                    "name": "San Francisco International Airport",
                    "code": "SFO"
                },
                "arrival_airport": {
                    "state": "Massachusetts",
                    "state_code": "MA",
                    "name": "Boston, Logan International Airport",
                    "code": "BOS"
                },
                "departure_utc": {
                    "iso": "2018-12-10T05:00:00+00:00"
                },
                "arrival_utc": {
                    "iso": "2018-12-10T12:00:00+00:00"
                }
            }
        ]
    }
}
Expected response to /problem/part_2?sample=true:
{
    "header": {"token": "de9dc37632c84f70bb08ef49a5cf0de0"},
    "data": {"return_leg_ids": ["leg:10", "leg:11"]}
}