"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ['G5', 'N', 'G4'],
            "answer": ['F', 1]
        },
       {
            "input": ['G5', 'N', 'I4'],
            "answer": ['R', 2]
        },
        {
            "input": ['G5', 'N', 'J6'],
            "answer": ['R', 3]
        },
        {
            "input": ['G5', 'N', 'G9'],
            "answer": ['B', 4]
        },
        {
            "input": ['G5', 'N', 'B7'],
            "answer": ['L', 5]
        },
        {
            "input": ['G5', 'N', 'A2'],
            "answer": ['L', 6]
        },
        {
            "input": ['G3', 'NE', 'C5'],
            "answer": ['B', 4]
        },
        {
            "input": ['H3', 'SW', 'E2'],
            "answer": ['R', 3]
        },
        {
            "input": ['A4', 'S', 'M4'],
            "answer": ['L', 12]
        },

    ],

	"Extra": [
		{
			"input": ['C3', 'SE', 'A1'],
			"answer": ['B', 3]
		},
		{
			"input": ['D3', 'NE', 'A1'],
			"answer": ['L', 4]
		},
        {
            "input": ['A1', 'SW', 'Z9'],
            "answer": ['B', 25]
        },
	],
}
