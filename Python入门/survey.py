class AnonymousSurvey:
    """AnonymousSurvey"""
    def __init__(self, question):
        """存储一个问题，并存储调查答案"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问题"""
        print(self.question)

    def store_response(self, new_response):
        """存储一个调查答案"""
        self.responses.append(new_response)

    def show_results(self):
        """显示所有的答案"""
        print("Survey Result:")
        for response in self.responses:
            print(f"- {response.title()}")
