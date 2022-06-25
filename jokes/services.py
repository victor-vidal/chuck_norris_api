import os
import requests

from jokes.models import Subscription


class JokeHandler():
    """Class responsible for handling joke acquisition from the Chuck Norris API"""
    
    def __init__(self) -> None:
        """Creates a JokeHandler"""
        
        self._url = os.environ.get('CHUCK_NORRIS_API_URL')
        
    def _handle_response(self, response: requests.Response) -> dict:
        """Assembles the result object based on the given response status"""
        
        if response.ok:
            return { 'success': True, 'data': response.json() }
        return { 'success': False, 'status': response.status_code }
    
    def get_random_joke(self) -> dict:
        """Gets a random joke from the API and returns a result object"""
        
        response = requests.get(f'{self._url}/jokes/random')
        return self._handle_response(response)
    
    def get_random_category_joke(self, category: str) -> dict:
        """Gets a joke belonging from a given category and returns a result object"""
        
        response = requests.get(f'{self._url}/jokes/random?category={category}')
        return self._handle_response(response)
    
    def search_joke(self, query: str, limit: int) -> dict:
        """Searches and returns a list of jokes based on the given query and 
        limit. If no limit is given, returns all query resulting jokes"""
        
        response = requests.get(f'{self._url}/jokes/search?query={query}')
        
        if response.ok:
            result = response.json()

            if not result['result']:
                return { 'success': False, 'status': 404 }
            return { 'success': True, 'data': result['result'][0:limit]  }
        return { 'success': False, 'status': response.status_code }
    
    
class SubscriptionDeliveryService():
    """Class responsible for deliverying random jokes from a category to the 
    subscribed emails"""
    
    def execute(self) -> dict:
        """Delives the jokes"""
        
        joke_handler = JokeHandler()
        
        for subscription in Subscription.objects.all():
            result = joke_handler.get_random_category_joke(
                subscription.category
            )
            
            if result['success']:
                joke = result['data']['value']
                
                print(f'Joke \"{joke}\" belongs to category \"{subscription.category}\" and was send to \"{subscription.email}\".')
   