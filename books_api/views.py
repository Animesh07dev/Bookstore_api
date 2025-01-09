from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse,HttpResponse
from .models import Book,Author
import io
from .serializers import bookSerializer,AuthorSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

def home_view(request):
    return HttpResponse("Hello there! this is the home page of BookStore api")

class BookDetailView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Book, pk=pk)

    def get(self, request, pk=None):
        if pk:
            book = get_object_or_404(Book, pk=pk)
            serializer = bookSerializer(book)
        else:
            books = Book.objects.all()
            serializer = bookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request):
        json_data=request.body
        stream= io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=bookSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Data saved successfully'}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        book = self.get_object(pk)
        data = JSONParser().parse(request)
        serializer = bookSerializer(book, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Data updated successfully'})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return JsonResponse({'msg': 'Data deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class AuthorDetailView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Author, pk=pk)
    
    def get(self,request,pk=None):
        if pk:
            author = get_object_or_404(Author, pk=pk)
            serializer = AuthorSerializer(author)
        else:
            authors = Author.objects.all()
            serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request):
        json_data=request.body
        stream= io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=AuthorSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Data saved successfully'}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        author = self.get_object(pk)
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(author, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Data updated successfully'})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return JsonResponse({'msg': 'Data deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    
    
    







    












# def show_all(request):
#     if request.method == "GET":
#         books=Book.objects.all()
#         serializer=bookSerializer(books,many=True)
#         return JsonResponse(serializer.data,safe=False)
    
# @csrf_exempt  
# def show(request,pk):
#     if request.method=="GET":
#         books=Book.objects.get(id=pk)
#         serializer=bookSerializer(books)
#         return JsonResponse(serializer.data)

# @csrf_exempt
# def create_book(request):
#     if request.method == 'POST':
#         json_data=request.body
#         stream= io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         serializer=bookSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({'msg': 'Data saved successfully'})
#         else:
#             return JsonResponse(serializer.errors,status=400)
#     return JsonResponse({'error': 'Invalid request method'}, status=405)

# @csrf_exempt   
# def update_book(request):
#     if request.method == 'PUT':
#         json_data=request.body
#         stream= io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get('id')
#         todo_list=Book.objects.get(id=id)
#         serializer=bookSerializer(todo_list,data=pythondata,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({'msg': 'Data updated successfully'})
#         else:
#             return JsonResponse(serializer.errors,status=400)
        
# @csrf_exempt
# def delete_book(request):
#     if request.method == "DELETE":
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id= pythondata.get('id')
#         del_data=Book.objects.get(id=id)
#         del_data.delete()
#         return JsonResponse({'msg': 'Data deleted successfully'})
#     else:
#         return JsonResponse({'msg': 'There is some error in deleting data'})
    