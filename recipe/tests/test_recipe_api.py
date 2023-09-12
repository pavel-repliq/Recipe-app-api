from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from recipe.models import RecipeModel
from recipe.serializers import RecipeSerializer, RecipeDetailSerializer

RECIPE_URL = reverse("recipe:recipe_list")


def get_detail_id(recipe_id):
    return f"/api/recipe/recipe_list/{recipe_id}/"


def create_recipe(user, **perams):
    #  create and return a sample recipe

    defults = {
        "title": "sample title",
        "description": "sample descr",
        "time_minutes": 30,
        "price": 240,
    }

    defults.update(**perams)

    recipe = RecipeModel.objects.create(user=user, **defults)
    return recipe


class RecipeAPITest(TestCase):
    #  testing for recipe api

    def setUp(self):
        self.client = APIClient()

        self.user = get_user_model().objects.create_user(
            email="user@example.com", password="pass1234"
        )
        self.client.force_authenticate(self.user)

    def test_retrive_recipe(self):
        #  test for retive recipe by api
        create_recipe(user=self.user)
        create_recipe(user=self.user)

        res = self.client.get(RECIPE_URL)

        recipes = RecipeModel.objects.filter().order_by("id")
        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        print(serializer.data)
        self.assertEqual(res.data, serializer.data)

    def test_recipe_list_limited_to_user(self):
        #   test recipe list limited to creator user or not
        other_user = get_user_model().objects.create_user(
            email="other_user@example.com", password="other_user12345"
        )
        create_recipe(user=other_user)
        create_recipe(user=self.user)

        res = self.client.get(RECIPE_URL)

        recipes = RecipeModel.objects.filter()
        serializer = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_recipe_details(self):
        #   test for recipe details

        recipe = create_recipe(user=self.user)
        url = get_detail_id(recipe.id)
        res = self.client.get(url)

        serializer = RecipeDetailSerializer(recipe)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_recipe_update(self):
        # test for recipe update

        payload = {"time_minutes": 45, "price": 15}

        recipe = create_recipe(user=self.user)
        url = get_detail_id(recipe.id)
        res = self.client.patch(url, payload, format="json")

        self.assertEqual(res.status_code, status.HTTP_200_OK)
