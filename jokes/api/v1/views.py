from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from jokes.services import JokeHandler


class BaseJokeView(APIView):
    """Base Joke view"""
    
    permission_classes = [AllowAny]
    _joke_handler = JokeHandler()
    
    def _handle_result(self, result: dict) -> Response:
        
        if result['success']:
            return Response(
                status=status.HTTP_200_OK,
                data=result['data']
            )
        return Response(status=result['status'])


class RandomJokeView(BaseJokeView):
    """View to get a random joke from the Chuck Norris API"""
    
    def get(self, request):
        """Returns a random joke"""
        
        result = self._joke_handler.get_random_joke()
        return self._handle_result(result)
            
            
class RandomCategoryJokeView(BaseJokeView):
    """View to get a joke from a given category from the Chuck Norris API"""
    
    def get(self, request, category: str):
        """Returns a joke from a given category"""
        
        result = self._joke_handler.get_random_category_joke(category)
        return self._handle_result(result)
    

class FilteredJokesView(BaseJokeView):
    """View to get jokes filtered by a given query"""
    
    def get(self, request):
        """Returns some filtered jokes"""
        
        query = self.request.query_params.get('search', '')
        limit = self.request.query_params.get('limit')
        
        try:
            if limit:
                limit = int(limit)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
        result = self._joke_handler.search_joke(query, limit)
        return self._handle_result(result)