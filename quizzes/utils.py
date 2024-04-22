import ast

from .models import Answer, QuizResult


class QuizUtils:
    @staticmethod
    def save_quiz_score(post_data, quiz, user):
        score, responses = QuizUtils.count_quiz_score(post_data, quiz)
        result = QuizResult(quiz=quiz, user=user, score=score, answers=responses)
        result.save()

    @staticmethod
    def count_quiz_score(
        post_data,
        quiz,
    ):
        score = 0
        responses = []
        for question in quiz.question_set.all():
            answers = question.answer_set.all()
            for answer in answers:
                if answer.id == int(post_data[str(question.id)]):
                    responses.append({question.id: answer.id})
                    if answer.is_correct:
                        score += 1
        return score, responses

    @staticmethod
    def get_incorrect_responses_dict(answers, quiz):
        answers_dict = QuizUtils.answer_array_to_dict(answers)
        incorrect_responses = {}, {}
        for question in quiz.question_set.all():
            question_answers = question.answer_set.all()
            for answer in question_answers:
                user_response_id = answers_dict.get(question.id)
                if answer.id == user_response_id and not answer.is_correct:
                    answer_content = Answer.objects.get(
                        id=user_response_id
                    ).answer_content
                    incorrect_responses.update({question.id: answer_content})

        return UserResponses(incorrect_responses)

    @staticmethod
    def answer_array_to_dict(answers_array):
        answer_dict = {}
        for answer in answers_array:
            answer_dict.update(ast.literal_eval(answer))
        return answer_dict


class UserResponses:
    def __init__(self, incorrect_answers):
        self.incorrect_answers = incorrect_answers

    def get_incorrect_answers_dict(self):
        return self.incorrect_answers
