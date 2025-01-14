from rest_framework import serializers
from .models import User, BookInventory, BookTransaction


class SignInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            raise serializers.ValidationError("Both email and password are required.")
        user = User.objects.filter(email=email, password=password)
        if not user:
            raise serializers.ValidationError({'message': 'Invalid credentials'})
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_name', 'email', 'role','password']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class BookInventorySerializer(serializers.ModelSerializer):

    book_name=serializers.SerializerMethodField()

    author=serializers.SerializerMethodField()

    comments=serializers.SerializerMethodField()

    class Meta:
        model = BookInventory
        fields = [
            'id',
            'book_name',
            'isbn',
            'author',
            'book_cost',
            'available_qty',
            'publication_date',
            'rental_days',
            'created_at',
            'updated_at',
            'is_deleted',
            'comments',
        ]


    def get_book_name(self, obj):
        return f"Book is {obj.book_name}"
    
    def get_author(self,obj):
        author=obj.author
        author=author[::-1]
        return author
    
    def get_comments(self,obj):
        return f"The Book {obj.book_name} is written by {obj.author} and is available at a cost of {obj.book_cost} and has {obj.available_qty} copies available"

class BookTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTransaction
        fields = '__all__'

