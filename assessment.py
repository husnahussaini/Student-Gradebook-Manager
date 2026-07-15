class Assessment:
    def __init__(self, title, max_score):
        self.title = title
        self.max_score = max_score

    def calculate_percentage(self, score):
        return (score / self.max_score) * 100

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)
        if percentage >= 55:
            return "Good job!"
        else:
            return "Needs improvement."

    def display_info(self):
        print(f"{self.title} / max_score: {self.max_score}")

class Quiz(Assessment):
    def display_info(self):
        print(f"Quiz: {self.title} / max_score: {self.max_score}")
