from rest_framework.permissions import BasePermission, SAFE_METHODS


class ISAuthorOrReadOnly(BasePermission):
    message = 'Нельзя менять чужие записи.'

    def has_permission(self, request, obj=None):
        return request.method in SAFE_METHODS or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or obj.author == request.user
# не совсем понял. Если я убираю не используемый аргумент, то тесты не проходят
# ожидают 3 или 4 аргумента а я передаю 2 или 3.
