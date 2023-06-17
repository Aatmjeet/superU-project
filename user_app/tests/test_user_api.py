from django.test import TestCase
from django.test.client import MULTIPART_CONTENT, encode_multipart, BOUNDARY
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from user_app.tests.user_factory import UserFactory
from django.core.files.uploadedfile import SimpleUploadedFile


class UserAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.sample_object = UserFactory.create()

    def test_user_create_endpoint(self):
        # Path to local image file
        image_path = "user_app/tests/dummyAdhar.jpeg"

        # Open the image file and create a SimpleUploadedFile object
        with open(image_path, 'rb') as file:
            image_content = file.read()
            profile_picture = SimpleUploadedFile('image.jpg', image_content, content_type='image/jpeg')

        data = dict(
                        first_name=self.sample_object.first_name,
                        last_name=self.sample_object.last_name,
                        username="dummyUser",
                        email="test@test.com",
                        profile_picture=profile_picture,
                        password=self.sample_object.password
                    )

        # encoding data to be sent in a multipart request
        # https://gist.github.com/nghiaht/682c2d8d40272c52dbf7adf214f1c0f1
        encoded_data = encode_multipart(data=data, boundary=BOUNDARY)

        # Make a request to your API endpoint using the client
        url = 'http://localhost:8000/user/'
        response = self.client.post(path=url, data=encoded_data, content_type=MULTIPART_CONTENT)

        # # Add your assertions to verify the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)

