from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import CustomUser, TransactionCategory, Transaction
from .serializers import UserSerializer, CategorySerializer, TransactionSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view, permission_classes

class UserAccountViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    @api_view(['DELETE'])
    def delete_own_profile(request):
        request.user.delete()
        return Response({"message": "Account deleted successfully"}, status=204)

    
    @action(detail=False, methods=["post"], url_path="change-password")
    def change_password(self, request, pk=None):
        user = request.user

        current_password = request.data.get("current_password")
        new_password = request.data.get("new_password")

        if not current_password or not new_password:
            return Response({"error": "Both fields required"}, status=400)

        # verify old password
        if not check_password(current_password, user.password):
            return Response({"error": "Old password is incorrect"}, status=400)

        # save new password
        user.set_password(new_password)
        user.save()

        return Response({"message": "Password changed successfully"}, status=200)

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
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


# ---------- EXPENSE VIEWSET ----------
class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Each user sees only their own expenses
        return Transaction.objects.filter(user_id=self.request.user).order_by('-transaction_date')

    def perform_create(self, serializer):
        # Automatically assign logged-in user to expense
        serializer.save(user_id=self.request.user)
