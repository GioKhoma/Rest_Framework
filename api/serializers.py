from rest_framework import serializers
from storeapp.models import (Product, Category, Review,
                             Cart, CartItems,
                             ProductImage,
                             Profile, Order, OrderItem)


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


class UpdateCartItemSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    class Meta:
        model = CartItems
        fields = ['quantity']


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


class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.UUIDField()

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError('Product does not exist')

        return value

    def save(self, *args, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        try:
            cartitem = CartItems.objects.get(product_id=product_id, cart_id=cart_id)
            cartitem.quantity += quantity
            cartitem.save()

            self.instance = cartitem


        except:
            self.instance = CartItems.objects.create(cart_id=cart_id, **self.validated_data)

        return self.instance

    class Meta:
        model = CartItems
        fields = ['id', 'product_id', 'quantity']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'bio', 'picture']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'placed_at', 'pending_status', 'owner']
