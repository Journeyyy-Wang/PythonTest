from survey import AnonymousSurvey

question = "What language did you first learn?"
language_survey = AnonymousSurvey(question)

language_survey.show_question()
print("Enter 'q' any time to quit.")
while True:
    response = input("Language: ")
    if response == "q":
        break
    language_survey.store_response(response)

# 显示调查结果
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()