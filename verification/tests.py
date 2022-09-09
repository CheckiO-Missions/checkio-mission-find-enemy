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
            "answer": ['F', 1],
            "explanation": {'A': [1, 1], 'B': [1, 1], 'C': [1, 2],
                'D': [1, 2], 'E': [1, 3], 'F': [1, 3], 'G': [1, 3],
                'H': [1, 3]}
        },
        {
            "input": ['G5', 'N', 'I4'],
            "answer": ['R', 2],
            "explanation": {'H': [4, 5], 'I': [4, 6], 'J': [3, 6]}
        },
        {
            "input": ['G5', 'N', 'J6'],
            "answer": ['R', 3],
            "explanation": {'H': [4, 5], 'I': [4, 6], 'J': [3, 6]}
        },
        {
            "input": ['G5', 'N', 'G9'],
            "answer": ['B', 4],
            "explanation": {'A': [9, 9], 'B': [8, 9], 'C': [8, 9],
                'D': [7, 9], 'E': [7, 9], 'F': [6, 9], 'G': [6, 9],
                'H': [6, 9]}
        },
        {
            "input": ['G5', 'N', 'B7'],
            "answer": ['L', 5],
            "explanation": {'A': [2, 8], 'B': [2, 7], 'C': [3, 7],
                'D': [3, 6], 'E': [4, 6], 'F': [4, 5], 'G': [5, 5]}
        },
        {
            "input": ['G5', 'N', 'A2'],
            "answer": ['L', 6],
            "explanation": {'A': [2, 8], 'B': [2, 7], 'C': [3, 7],
                'D': [3, 6], 'E': [4, 6], 'F': [4, 5], 'G': [5, 5]}
        },
        {
            "input": ['G3', 'NE', 'C5'],
            "answer": ['B', 4],
            "explanation": {'A': [1, 9], 'B': [1, 9], 'C': [2, 9],
                'D': [2, 9], 'E': [3, 9], 'F': [3, 9]}
        },
        {
            "input": ['H3', 'SW', 'E2'],
            "answer": ['R', 3],
            "explanation": {'C': [1, 1], 'D': [1, 1], 'E': [1, 2],
                'F': [1, 2], 'G': [1, 3], 'H': [1, 3]}
        },
        {
            "input": ['A4', 'S', 'M4'],
            "answer": ['L', 12],
            "explanation": {'A': [4, 4], 'B': [3, 4], 'C': [3, 5],
                'D': [2, 5], 'E': [2, 6], 'F': [1, 6], 'G': [1, 7],
                'H': [1, 7], 'I': [1, 8], 'J': [1, 8], 'K': [1, 9],
                'L': [1, 9], 'M': [1, 9], 'N': [1, 9]}
        },
        {
            "input": ['D9', 'NE', 'B9'],
            "answer": ['B', 2],
            "explanation": {'A': [9, 9], 'B': [9, 9]}
        },
        {
            "input": ['B2', 'N', 'C4'],
            "answer": ['B', 2],
            "explanation": {'A': [4, 4], 'B': [3, 4], 'C': [4, 4]}
        } 
    ],

    "Extra": [
        {
	    "input": ['C3', 'SE', 'A1'],
	    "answer": ['B', 3],
            "explanation": {'A': [1, 3], 'B': [1, 2]}
	},
	{
	    "input": ['D3', 'NE', 'A1'],
	    "answer": ['L', 4],
            "explanation": {'A': [1, 2], 'B': [1, 2], 'C': [1, 3],
                'D': [1, 2]}
	},
        {
            "input": ['A1', 'SW', 'Z9'],
            "answer": ['B', 25],
            "explanation": {'A': [1, 1], 'C': [1, 1],
                'D': [1, 1], 'E': [1, 2], 'F': [1, 2], 'G': [1, 3],
                'H': [1, 3], 'I': [1, 4], 'J': [1, 4], 'K': [1, 5],
                'L': [1, 5], 'M': [1, 6], 'N': [1, 6], 'O': [1, 7],
                'P': [1, 7], 'Q': [1, 8], 'R': [1, 8], 'S': [1, 9],
                'T': [1, 9], 'U': [1, 9], 'V': [1, 9], 'W': [1, 9],
                'X': [1, 9], 'Y': [1, 9], 'Z': [1, 9]}
        },
    ],
}
