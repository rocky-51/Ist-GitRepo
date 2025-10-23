from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import CustomUser, TransactionCategory, Transaction
from .serializers import UserSerializer, CategorySerializer, TransactionSerializer


# ---------- USER VIEWSET ----------
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # open for registration

    # Optional custom action for user registration
    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "User registered successfully", "user": serializer.data})


# ---------- CATEGORY VIEWSET ----------
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = TransactionCategory.objects.all().order_by('-category_id')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


# ---------- EXPENSE VIEWSET ----------
class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Each user sees only their own expenses
        return Transaction.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        # Automatically assign logged-in user to expense
        serializer.save(user=self.request.user)
