from django.test import TestCase
from django.contrib.auth import get_user_model
from models import Question, Comment


User = get_user_model()

class QuestionModelTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Create a user for the foreign key requirement
        test_user = User.objects.create_user(username='testuser', password='testpass')
        test_user.save()

        # Create a Question instance to use in tests
        Question.objects.create(
            user=test_user,
            title='Test Question Title',
            body='This is a Test body for a Question'
        )

    def test_question_creation(self):
        question = Question.objects.get(id=1)
        self.assertEqual(str(question), 'Test Question Title')

    def test_get_absolute_url(self):
        question = Question.objects.get(id=1)
        # Make sure to include the namespace if your URLconf is namespaced
        self.assertEquals(question.get_absolute_url(), '/questions/1/')


class CommentModelTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Reuse the setup for QuestionModelTests to create a user and question
        test_user = User.objects.create_user(username='testuser', password='testpass')
        test_user.save()
        test_question = Question.objects.create(
            user=test_user,
            title='Test Question Title',
            body='This is a Test body for a Question'
        )

        # Create a Comment instance to use in tests
        Comment.objects.create(
            question=test_question,
            author=test_user,
            text='Test comment text'
        )

    def test_comment_creation(self):
        comment = Comment.objects.get(id=1)
        self.assertTrue(isinstance(comment, Comment))
        self.assertEqual(str(comment), 'Test comment text')