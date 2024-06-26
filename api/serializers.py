from rest_framework import serializers
from storeapp.models import Product, Category, Review, Cart, CartItems, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'title', 'slug']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'image']


class ProductSerializer(serializers.ModelSerializer):
    imagesss = ProductImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description',
                  # 'category', 'slug', 'inventory',
                  'price', 'imagesss', 'uploaded_images']

    # category = serializers.StringRelatedField()
    # category = CategorySerializer()

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images')
        product = Product.objects.create(**validated_data)
        for image in uploaded_images:
            newproduct_image = ProductImage.objects.create(product=product, image=image)

        return product


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date_created', 'name', 'description']

    def create(self, validated_data):
        product_id = self.context["product_id"]
        return Review.objects.create(product_id=product_id, **validated_data)


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']


class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    sub_total = serializers.SerializerMethodField(method_name='total')

    class Meta:
        model = CartItems
        fields = ['id', 'cart', 'product', 'quantity', 'sub_total']

    def total(self, cartitem: CartItems):
        return cartitem.quantity * cartitem.product.price


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    itemsss = CartItemSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField(method_name='main_total')

    class Meta:
        model = Cart
        fields = ['id', 'itemsss', 'grand_total']

    def main_total(self, cart: Cart):
        items = cart.itemsss.all()
        total = sum([item.quantity * item.product.price for item in items])
        return total
