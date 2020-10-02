from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import ToDoList


class TodoTestCase(TestCase):
    def test_add_todo_success(self):
        data = {"text": "laundry"}
        url = reverse("add-todo")
        response = self.client.post(path=url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("text", response.json())
        self.assertEqual(response.json().get("text"), "homework")
        self.assertIn("url", response.json())
        self.assertTrue(response.json()["url" > 0])
    
    def test_add_todo_success(self):
        data = {"todo": "laundry"}
        url = reverse("add-todo")
        response = self.client.post(path=url, data=data, format="json")
        self.assertEqual(response.status_code, 400)

class AddToDoToListTestCase(TestCase):
    # def setUp(self):
    #     todo_list = ToDoLists.objects.last()
    #     url = todo_list.url
        # self.data = {"text": "gym"}
        # self.url = reverse("add-todo-to-list", kwargs={"url": url})
        # self.response = self.client.post(
        #     path=self.url,
        #     data=self.data,
        #     format="json"
        # )
    def test_add_todo_to_list_success(self):
        data = {"text": "clean windows"}
        url = reverse("add-todo")
        response = self.client.post(path=url, data=data, format="json")
        todo_list_url = response.json()["url"]

        self.data = {"text": "gym"}
        self.url = reverse("add-todo-to-list", kwargs={"url": todo_list_url})
        self.response = self.client.post(
            path=self.url,
            data=self.data,
            format="json"
        )
        self.assertEqual(self.response.status_code, 201)
        self.assertEqual(self.response.json()["text"], "gym")