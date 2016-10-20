from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.blog import utils
from apps.blog import helper

import logging
logger = logging.getLogger(__name__)


class Blogs(APIView):
    """
    Api for Blogs Operations :  List & Create
    URL : /app/v1/blogs/
    """

    def get(self, request):
        """
        GET             : API for all Blog List $ Details
        """

        status_code, message, data = helper.get_blogs()

        if status_code:
            return Response({"message": message, "data": data}, status=status.HTTP_200_OK)
        else:
            logger.error(message)
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)

    

    def post(self, request):
        """ 
        POST                 : API for Create Blog
        Mandatory Params     : title (string), slug (string), content (string) 
        Non Mandatory Params : author_id (int), category_ids (list of id's)
        """

        title = request.data.get('title', None)
        slug = request.data.get('slug', None)
        author_id = request.data.get('author_id', None)
        content = request.data.get('content', None)
        category_ids = request.data.get('category_ids', None)

        input_param_dict = {'Title': title, 'Slug': slug, 'Content': content}
        status_code, message = utils.validate_params(input_param_dict)

        if not status_code:
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)

        if category_ids:
            status_code, message, categories = helper.validate_categories(
                category_ids)
            if not status_code:
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        else:
            categories = None

        status_code, message, data = helper.create_blog(
            title, slug, content, author_id, categories)

        if status_code:
            return Response({"message": message, "data": data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)



class BlogOperation(APIView):
    """
    Api for Blog Operations : Read, Update and Delete
    URL : /app/v1/blogs/blog/<blog_id>/
    """

    
    def get(self, request, blog_id):
        """ GET             : API for Blog Details
            INPUT_PARAMS    : blog_id 
        """


        input_param_dict = {'Blog_ID': blog_id}
        status_code, message = utils.validate_params(input_param_dict)

        if not status_code:
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)

        status_code, message, data = helper.get_blogs(blog_id)

        if status_code:
            return Response({"message": message, "data": data}, status=status.HTTP_200_OK)
        else:
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, blog_id):
        """ 
        PUT                 : API for Edit Blog
        Mandatory Params     : blog_id (int)
        Non Mandatory Params : title (string), slug (string), content (string) ,
                                author_id (int), category_ids (list of id's)
        """
        title = request.data.get('title', None)
        slug = request.data.get('slug', None)
        author_id = request.data.get('author_id', None)
        content = request.data.get('content', None)
        category_ids = request.data.get('category_ids', None)

        input_param_dict = {'Blog_ID': blog_id}
        status_code, message = utils.validate_params(input_param_dict)

        if not status_code:
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)

        if category_ids is not None:
            status_code, message, categories = helper.validate_categories(
                category_ids)
            if not status_code:
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        else:
            categories = None

        status_code, message, data = helper.update_blog(
            blog_id, title, slug, content, author_id, categories)

        if status_code:
            return Response({"message": message, "data": data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)

    

    def delete(self, request, blog_id):
        """ 
        DELETE  : API for delete Blog
        """
        input_param_dict = {'Blog_ID': blog_id}
        status_code, message = utils.validate_params(input_param_dict)

        if not status_code:
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)

        status_code, message = helper.delete_blog(blog_id)

        if status_code:
            return Response({"message": message}, status=status.HTTP_200_OK)
        else:
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
