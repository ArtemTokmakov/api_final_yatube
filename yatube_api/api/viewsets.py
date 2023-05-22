from rest_framework import mixins, viewsets


class ModelViewSetMixin(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass
