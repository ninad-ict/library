from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
from .models import User, BookInventory, BookTransaction

from .Serializers import UserSerializer, BookInventorySerializer, BookTransactionSerializer,SignInSerializer



class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'],url_path='signin')
    def sign_in(self, request):
        serializer= SignInSerializer(data=request.data)
        print("Login->",serializer)
        if serializer.is_valid():
            return Response({'message': 'Login successful'},status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    

class BookInventoryViewSet(ModelViewSet):
    queryset = BookInventory.objects.all()
    serializer_class = BookInventorySerializer

    @action(detail=True,methods=['patch'],url_path='increment')
    def update_book_quantity(self,request,pk=None):
        try:
            book=BookInventory.objects.get(id=pk)
            increment_by=request.data.get('increment_by')


            try:
                increment_by=int(increment_by)
            except:
                return Response({'message':'Invalid increment value'},status=status.HTTP_400_BAD_REQUEST)

            book.available_qty+=increment_by
            book.save()
            serializer=BookInventorySerializer(book)

            return Response(serializer.data,status=status.HTTP_200_OK)
        except BookInventory.DoesNotExist:
            return Response({'message':'Book not found'},status=status.HTTP_404_NOT_FOUND)
        



class BookTransactionViewSet(ModelViewSet):
    queryset = BookTransaction.objects.all()
    serializer_class = BookTransactionSerializer


    @action(detail=False,methods=['post'],url_path='rent')
    def book_transaction(self,request):
        try:
            user_id=request.data.get('user')
            book_id=request.data.get('book')
            state=request.data.get('status')
        except:
            return Response({'message':'Invalid request'},status=status.HTTP_400_BAD_REQUEST)
        try:
            user=User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'message':'User not found'},status=status.HTTP_404_NOT_FOUND)
        
        try:
            book=BookInventory.objects.get(id=book_id)
        except BookInventory.DoesNotExist:
            return Response({'message':'Book not found'},status=status.HTTP_404_NOT_FOUND)
        
        if book.available_qty<=0 and state=='taken':
            return Response({'message':'Book not available'},status=status.HTTP_400_BAD_REQUEST)
        
        quantity=-1 if state=='taken' else 1
        transaction=BookTransaction.objects.create(
            user=user,
            book=book,
            amount_paid=book.book_cost,
            date_of_transaction=book.publication_date,
            status=state
            )
        
        serializer=BookTransactionSerializer(transaction)
        print("quantity->",quantity)
        book.available_qty+=quantity
        book.save()

        return Response(serializer.data,status=status.HTTP_200_OK)
        


