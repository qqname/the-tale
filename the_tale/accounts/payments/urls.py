# coding: utf-8

from dext.views import resource_patterns

from accounts.payments.views import PaymentsResource

urlpatterns = resource_patterns(PaymentsResource)
