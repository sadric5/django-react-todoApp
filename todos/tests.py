from django.test import TestCase
from .models import Todo
from django.contrib.auth.models import User
# Create your tests here.

class TodoTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Dave', password='John34')
        self.user.save()
        self.todo = Todo.objects.create(author=self.user, title='Lerning Python', description='Learning to make good testing in Python is really important', completed = True)
        self.todo.save()

    def test_todo_tilte(self):
        self.assertEqual(self.todo.title, 'Lerning Python')
    
    def test_todo_description(self):
        self.assertEqual(self.todo.description, 'Learning to make good testing in Python is really important')

    def test_todo_completed(self):
        self.assertEqual(self.todo.completed, True)