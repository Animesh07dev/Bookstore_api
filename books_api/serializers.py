from rest_framework import serializers
from .models import Book,Author

class bookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'title','author','published_date', 'isbn', 'price', 'description']

    def create(self,validate_data):
        return Book.objects.create(**validate_data)
    
    def update(self,instance,validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.author=validated_data.get('author',instance.author)
        instance.published_date=validated_data.get('published_date',instance.published_date)
        instance.isbn=validated_data.get('isbn',instance.isbn)
        instance.price=validated_data.get('price',instance.price)
        instance.description=validated_data.get('description',instance.description)
        instance.save()
        return instance

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'dob', 'bio']
  
    def create(self,validate_data):
        return Author.objects.create(**validate_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.dob=validated_data.get('dob',instance.dob)
        instance.bio=validated_data.get('bio',instance.bio)
        instance.save()
        return instance
    
class newbookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    class Meta:
        model = Book
        fields = ['id', 'title', 'author','description']

