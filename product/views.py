from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from product.models import Product
from product.serializers import UserSerializer
from rest_framework.decorators import authentication_classes, permission_classes

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method=='GET':
        product_list = Product.objects.all()
        serializers = UserSerializer(product_list,many=True)
        return Response (serializers.data)

    elif request.method=='POST':
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response (serializers.data,status=status.HTTP_201_CREATED)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@authentication_classes([])
@permission_classes([])
def product_details(request,pk):

    try:
        product_detail = Product.objects.get(pk=pk)
    except product_detail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        product_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method=='GET':
        serializers = UserSerializer(product_detail)
        return Response (serializers.data)

    elif request.method=='PUT':
        serializers = UserSerializer(product_detail,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)