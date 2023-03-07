from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from product.models import *
from product.views import CategoryAPIView, ProductModelViewset
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()

class CategoryTest(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()

        category = [
            Category(title='c1'),
            Category(title='c2'),
            Category(title='c3')
        ]
        Category.objects.bulk_create(category)

        self.setup_user()

    def setup_user(self):
        self.user = User.objects.create_user(
            email = 'test@test.com',
            password = 'test123',
            is_active = True
        )   


    def test_get_category(self):
        request = self.factory.get('api/v1/product/category/') 
        view = CategoryAPIView.as_view({'get': 'list'})  
        response = view(request)
        print(response.data)
        assert response.status_code == 200
        assert len(response.data) == 3
        assert response.data[0]['title'] == 'c1'


    def test_post_category(self):
        data = {
            'title': 'c4'
        }
        request = self.factory.post('api/v1/product/category/', data)
        force_authenticate(request, self.user)
        view = CategoryAPIView.as_view({'post': 'create'})
        response = view(request)

        assert response.status_code == 201
        assert Category.objects.filter(title='c4').exists()
        # print(response.status_code)


class ProductTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.setup_category()
        self.setup_user()
        self.access_token = self.setup_user_token()


    def setup_user_token(self):
        data = {
            'email': 'test@test.com',
            'password': 'test123',
            
        }     
        request = self.factory.post('api/v1/account/login/', data)
        view = TokenObtainPairView.as_view()
        response = view(request)
        
        return response.data['access']

        
    @staticmethod
    def setup_category():
         
         category = [
            Category(title='c1'),
            Category(title='c2'),
            Category(title='c3')
        ]
         Category.objects.bulk_create(category)


    def setup_user(self):
        self.user = User.objects.create_user(
            email = 'test@test.com',
            password = 'test123',
            is_active = True
        )   
    

    def test_post_product(self):
        image = open('media/products/test.jpeg', 'rb')
        data = {
            'category': Category.objects.first(),
            'title': 'test_product',
            'amount': 20,
            'price': 20, 
            'image': image
        }
        request = self.factory.post('api/v1/modelviewset_crud/', data, HTTP_AUTHORIZATION='Bearer'+ self.access_token)
        view = ProductModelViewset.as_view({'post':'create'})
        response = view(request)

        assert response.status_code == 201
        assert Product.objects.filter(title='test_product').exists()

    




