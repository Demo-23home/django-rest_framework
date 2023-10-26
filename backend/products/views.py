#Rest_framework
from rest_framework import generics, mixins, permissions, authentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
#internal imports
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffEditorPermission
from api.authintecation import TokenAuthentication
#djagno imports
from django.shortcuts import get_object_or_404
# Create your views here.



class ProductMixinView( mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        generics.GenericAPIView):
    
    queryset = Product.objects.all()
    serializer_class =ProductSerializer


    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
product_mixn_view = ProductMixinView.as_view()





class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #lookup_filed = 'pk'

product_detail_view = ProductDetailAPIView.as_view()



class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        
        if content is None :
            content = title
        serializer.save(content=content)

proudct_list_create_view = ProductListCreateAPIView.as_view()

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




##

@api_view(['GET','POST'])
def product_alt_view(request,pk=None,*args,**kwargs):
    # method = request.mehtod

    if request.method == "GET": 
        if pk is not None:
        #detail
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)

        #list
        queryset = Product.objects.all()
        data = ProductSerializer(queryset,many=True).data
        return Response(data)
        #create
    if request.method == "POST":
        serializer = ProductSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None

            if content == None :
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"Invalid":"Not good data"}, status=404)
    


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    lookup_field = 'pk'


    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title 
         



class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


    def perform_destroy(self, instance):
        super().perform_destroy(instance)