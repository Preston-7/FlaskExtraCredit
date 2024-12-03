import uuid

class MultipleChoiceQuestion:
    """A class to represent a multiple choice question"""
    def __init__(self, question_id: str, question_text: str,  answer_index: int, choices: list[str]):
        """Constructor for MultipleChoiceQuestion

        Args:
            question_id (str): The unique identifier for the question
            question_text (str): The question to be asked
            answer_index (int): The index of the correct answer in the choices list
            choices (list[str]): the list of choices for the question
        """
        self.question_id = question_id
        self.question_text = question_text
        self.answer_index = answer_index
        self.choices = choices

    def __repr__(self) -> str:
        return f"MultipleChoiceQuestion({self.question_id}, {self.question_text}, {self.answer_index}, {self.choices})"


QUESTIONS = [
    MultipleChoiceQuestion(str(uuid.uuid4()), 
                            "What is the capital of England?",
                           1,
                           ["Paris", "London", "Berlin", "Madrid"]),

    MultipleChoiceQuestion(str(uuid.uuid4()), 
                           "Who invented Git?",
                           0,
                           ["Linus Torvalds", "Bill Gates", "Steve Jobs", "Jeff Bezos"]),

    MultipleChoiceQuestion(str(uuid.uuid4()), 
                            "What is the capital of North Carolina?",
                            2,
                            ["Greensboro", "Wilmington", "Raleigh", "Charlotte"]),

    MultipleChoiceQuestion(str(uuid.uuid4()), 
                            "What is the capital of Texas?", 
                            0, 
                            ["Austin", "Dallas", "Houston", "San Antonio"]),

    MultipleChoiceQuestion(str(uuid.uuid4()), 
                            "Which planet is known as the Red Planet?", 
                            0, 
                            ["Mars", "Venus", "Jupiter", "Saturn"]),

    MultipleChoiceQuestion(str(uuid.uuid4()), 
                            "What is the smallest planet in our solar system?", 
                            1, 
                            ["Earth", "Mercury", "Mars", "Pluto"]),

    MultipleChoiceQuestion(str(uuid.uuid4()), 
                            "Which ocean is the largest?", 
                            0, 
                            ["Pacific", "Atlantic", "Indian", "Arctic"]),
    MultipleChoiceQuestion(str(uuid.uuid4()), 
                            "What is the hardest natural substance on Earth?", 
                            2, 
                            ["Gold", "Iron", "Diamond", "Platinum"]),
    MultipleChoiceQuestion(str(uuid.uuid4()), 
                            "What is the largest mammal?", 
                            1, 
                            ["Elephant", "Blue Whale", "Giraffe", "Shark"]),

    MultipleChoiceQuestion(str(uuid.uuid4()), 
                            "What is the speed of light?", 
                            1, 
                            ["299,792 km/s", "300,000 km/s", "250,000 km/s", "320,000 km/s"]),
    MultipleChoiceQuestion(str(uuid.uuid4()), 
                            "Who was the first man on the Moon?", 
                            0, 
                            ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Michael Collins"]),
    MultipleChoiceQuestion(str(uuid.uuid4()), 
                            "Which country is known as the Land of the Rising Sun?", 
                            0, 
                            ["Japan", "China", "South Korea", "India"]),
]
