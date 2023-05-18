from django.db import models


class Quiz(models.Model):
    chapter = models.OneToOneField('chapters.Chapter', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return self.chapter.name

class Question(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    question_content = models.TextField()

    def __str__(self):
        return self.question_content

class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer_content = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def check_correctness(self, user_answer) -> bool:
        return self.is_correct == user_answer

