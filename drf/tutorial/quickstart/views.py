from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions

from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Handles user-related actions via a RESTful API.

    Provides a viewset for managing User objects, allowing standard CRUD operations
    while ensuring only authenticated users can perform actions.

    :ivar queryset: Queryset of User objects ordered by their date of joining in
        descending order.
    :type queryset: QuerySet[User]

    :ivar serializer_class: Serializer class used for serializing and deserializing
        User objects.
    :type serializer_class: type

    :ivar permission_classes: List of permission classes that define the required
        permissions for accessing this viewset.
    :type permission_classes: list
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    Manages and interacts with groups in the application.

    This class provides a view set for managing group-related data. It allows for
    standard CRUD functionalities while ensuring the actions are performed securely
    using permissions. It operates on a queryset of all available `Group` objects,
    ordered by the date they were joined in descending order. Each group is serialized
    using the specified serializer class.

    :ivar queryset: A queryset containing all `Group` objects sorted by
        the date joined, in descending order.
    :type queryset: QuerySet
    :ivar serializer_class: The serializer class used for serializing and deserializing
        group data.
    :type serializer_class: type
    :ivar permission_classes: A list of permission classes that restrict and
        manage access to this view set.
    :type permission_classes: list
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
