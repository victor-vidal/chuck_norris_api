from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient


class BasePublicTestCase(TestCase):
    """Base class for public test cases"""
    
    def setUp(self) -> None:
        self.client = APIClient()
        
        
class JokeTestCase(BasePublicTestCase):
    """Jokes app test cases"""
    
    def test_random_joke(self):
        """Tests the random joke view"""
        
        res = self.client.get(
            reverse('jokes:random_joke')
        )
        
        # The view should return a 200 status
        self.assertEqual(
            res.status_code,
            status.HTTP_200_OK
        )
        
    def test_random_category_joke(self):
        """Tests the random category joke view"""
        
        res = self.client.get(
            reverse(
                'jokes:random_category_joke',
                kwargs={ 'category': 'animal' }
            ),
        )
        
        # The view should return a 200 status when a known category is given
        self.assertEqual(
            res.status_code,
            status.HTTP_200_OK
        )
        
        result = res.json()
        
        # The returned joke should belong to the requested category
        self.assertTrue(
            'animal' in result['categories']
        )
        

        res = self.client.get(
            reverse(
                'jokes:random_category_joke',
                kwargs={ 'category': 'test' }
            ),
        )
        
        # The view should return a 400 status when a unknown category is given
        self.assertEqual(
            res.status_code,
            status.HTTP_404_NOT_FOUND
        )
        
    def test_filter(self):
        """Tests the filtered jokes view"""
        
        res = self.client.get(
            '%s?search=%s&limit=%s' %
            (reverse('jokes:filtered_jokes'),
            'animal',
            '10')
        )
        
        # The view should return a 200 status when a valid filter and limit are
        # given
        self.assertEqual(
            res.status_code, 
            status.HTTP_200_OK
        )
        
        result = res.json()
        
        # The resulting list of jokes should not more than 10 items
        self.assertLessEqual(len(result), 10)
        
        res = self.client.get(
            '%s?search=%s&limit=%s' %
            (reverse('jokes:filtered_jokes'),
            'TESTEtesteTESTE',
            '10')
        )
        
        # If there is no joke with the filter used, the view should return a 404 
        # status code
        self.assertEqual(
            res.status_code,
            status.HTTP_404_NOT_FOUND
        )

    def test_subscribe(self):
        """Tests the subscribe view"""
        
        payload = {
            'email': 'victorvidal584@gmail.com',
            'category': 'animal'
        }
        
        res = self.client.post(
            reverse('jokes:subscribe'),
            payload,
            format='json'
        )
        
        # A user should be able to register a subscription
        self.assertEqual(
            res.status_code,
            status.HTTP_201_CREATED
        )
        
        payload = {
            'category': 'animal'
        }
        
        res = self.client.post(
            reverse('jokes:subscribe'),
            payload,
            format='json'
        )
        
        # An invalid payload should be properly responded
        self.assertEqual(
            res.status_code,
            status.HTTP_400_BAD_REQUEST
        )