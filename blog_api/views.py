from django.db import connection
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from blog_api.models import Blog


# Create your views here.
@api_view(['GET', 'POST'])
def check(request):

    response_data = {
        'status': True,
        'message': 'Blog Api Server Connected Successfully...!',
        'data': None
    }

    if request.method == 'GET':
        return Response(response_data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        return Response(response_data, status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def create(request):
    if request.method == 'GET':
        response_data = {
            'status': True,
            'message': 'Blog Create Function executed without any data...!',
            'data': None
        }
        return Response(response_data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        try :
            user = request.user
            title = request.data['title']
            description = request.data['description']
            
            blog = Blog(title=title, description=description, created_by=user)
            blog.save()

            response_data = {
                'status': True,
                'message': 'Blog Created Successfully...!',
                'data': blog.toJson()
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
    
        except Exception as e:
            response_data = {
                'status': False,
                'message': 'Error: ' + str(e),
                'data': None
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# sample request data
# {
#     "title": "Blog Title",
#     "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500."
# }


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def posts(request):
    if request.method == 'GET':
        try :
            per_page = int(request.query_params.get('per-page', 10))
            page_number = int(request.query_params.get('page', 1))
            search_query = request.query_params.get('search', '')
            
            # Create a paginator object with the desired page size
            paginator = PageNumberPagination()
            paginator.page_size = per_page
            paginator.page_query_param = 'page'


            blogs = Blog.objects.order_by('-created_at')

            if search_query:
                print(search_query)
                blogs = blogs.filter(title__icontains=search_query)

            # Get the paginated result from the paginator
            paginated_blogs = paginator.paginate_queryset(blogs, request)

            if page_number < 1 or page_number > paginator.page.paginator.num_pages:
                raise ValueError('Invalid page.')

            response_data = {
                'status': True,
                'message': 'Blogs Fetched Successfully...!',
                'data': [blog.toJson() for blog in paginated_blogs]
            }
            return Response(response_data, status=status.HTTP_200_OK)
    
        except Exception as e:
            response_data = {
                'status': False,
                'message': 'Error: ' + str(e),
                'data': None
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)