from django_filters import rest_framework as filters

class PaymentFilter(filters.FilterSet):
    payment_date = filters.DateFilter(field_name='payment_date', lookup_expr='date')

    class Meta:
        model = Payment
        fields = ['course_or_lesson', 'payment_method']

class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filterset_class = PaymentFilter

from rest_framework import filters

class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['payment_date']
