from braces.views import LoginRequiredMixin, UserPassesTestMixin
from allauth.account.models import EmailAddress
from .functions import confirmation_required_redirect


class LoginAndVerificationRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    # 로그인 여부 + 이메일 인증 필요
    redirect_unauthenticated_users = True
    raise_exception = confirmation_required_redirect
    def test_func(self, user):
        return EmailAddress.objects.filter(user=user, verified=True).exists()
    

class LoginAndOwnershipRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    # 로그인 여부 + 오브젝트 소유 필요
    redirect_unauthenticated_users = False
    raise_exception = True

    def test_func(self, user):
        obj = self.get_object()
        return obj.author == user