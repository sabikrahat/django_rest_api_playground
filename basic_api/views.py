from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET', 'POST'])
def check(request):
    response_data = {'status': True, 'message': 'Basic Api Connected Successfully...!', 'data': None, }
    if request.method == 'GET':
        return Response(response_data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        return Response(response_data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def addition(request):
    if request.method == 'GET':
        response_data = {'status': True, 'message': 'Addition Function executed without any data...!', 'data': None, }
        return Response(response_data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        try:
            num1 = request.data['num1']
            num2 = request.data['num2']

            res = int(num1) + int(num2)

            response_data = {"success": True,
                            "message": "Successfully solved the equation",
                            "data": res,}

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            response_data = {"success": False,
                            "message": "Error: " + str(e),
                            "data": None}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def addition_list(request):
    if request.method == 'GET':
        response_data = {'status': True, 'message': 'Addition Function executed without any data...!', 'data': None, }
        return Response(response_data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        try:
            list = request.data['num']

            res = 0
            for i in list:
                res += int(i)

            response_data = {"success": True,
                            "message": "Successfully solved the equation",
                            "data": res,}

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            response_data = {"success": False,
                            "message": "Error: " + str(e),
                            "data": None}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)