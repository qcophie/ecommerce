from random import randrange
from django.http import Http404
from .models import SEUser


def random_code():
    CHARSET = '0123456789abcdefghijklmnopqrstuvwxyz'
    LENGTH = 7
    new_code = ''
    for i in range(LENGTH):
        new_code += CHARSET[randrange(0, len(CHARSET))]
    return new_code


def log_user_activity(module, description, user_id, device, ip_address, merchant_id):
    user = SEUser.objects.get(id=int(user_id))
    myactivity = UserActivity.objects.create(module=module,
                                             description=description,
                                             user=user,
                                             merchant=user.merchant,
                                             device=device,
                                             ip_address=ip_address
                                             )
    if merchant_id:
        mymerchant = Merchant.objects.get(id=int(merchant_id))
        myactivity.merchant = mymerchant
        myactivity.save()


def create_activity(request, module, description):
    try:
        log_user_activity(module, description, request.user.id, request.META['HTTP_USER_AGENT'],
                          request.META['HTTP_X_FORWARDED_FOR'], '')
    except KeyError:
        log_user_activity(module, description, request.user.id, request.META['HTTP_USER_AGENT'], 'LOCALHOST', '')


def validate(request, mykey):
    if request.user.is_authenticated:
        if request.user.is_active:
            if mykey == 'edit_profile' or mykey == 'change_password':
                if request.user.permission == '0' or request.user.permission == '1' or request.user.permission == '2' or request.user.permission == '3' or request.user.permission == '4':
                    return True
                else:
                    print('not validated!!!')
                    raise Http404
            if mykey == 'general_report' or mykey == 'report_by_merchant' or mykey == 'full_report':
                if request.user.permission == '0' or request.user.permission == '1' or request.user.permission == '2':
                    return True
                else:
                    print('not validated!!!')
                    raise Http404
            if mykey == 'user_activity' or mykey == 'overview' or mykey == 'report_detail' or mykey == 'merchant_report':
                if request.user.permission == '0' or request.user.permission == '1' or request.user.permission == '2' or request.user.permission == '3' or request.user.permission == '4':
                    if request.user.permission == '0' or request.user.permission == '1' or request.user.permission == '2':
                        return '0'
                    else:
                        return '1'
                else:
                    print('not validated!!!')
                    raise Http404
            if mykey == 'user_detail' or mykey == 'users':
                if request.user.permission == '0':
                    return '0'
                elif request.user.permission == '3':
                    return '1'
                else:
                    print('not validated!!!')
                    raise Http404
            if mykey == 'disable_merchant' or mykey == 'enable_merchant':
                if request.user.permission == '0':
                    return True
                else:
                    print('not validated!!!')
                    raise Http404
            if mykey == 'merchants' or mykey == 'merchant_detail' or mykey == 'merchant_activity':
                if request.user.permission == '0' or request.user.permission == '1' or request.user.permission == '2':
                    if request.user.permission == '1':
                        return '1'
                    return True
                else:
                    print('not validated!!!')
                    raise Http404
            if mykey == 'new_merchant_setup' or mykey == 'existing_merchant_setup' or mykey == 'wallet_credit' or mykey == 'wallet_debit' or mykey == 'returned_wallet_credit' or mykey == 'returned_wallet_debit':
                if request.user.permission == '1':
                    return True
                else:
                    print('not validated!!!')
                    raise Http404
            if mykey == 'pending':
                if request.user.permission == '0' or request.user.permission == '1' or request.user.permission == '2':
                    if request.user.permission == '2':
                        return '2'
                    return True
                else:
                    print('not validated!!!')
                    raise Http404
            if mykey == 'returned':
                if request.user.permission == '0' or request.user.permission == '1' or request.user.permission == '2':
                    if request.user.permission == '1':
                        return '1'
                    return True
                else:
                    print('not validated!!!')
                    raise Http404
            if mykey == 'new_merchant_return' or mykey == 'existing_merchant_return' or mykey == 'pending_payout' or mykey == 'pending_wallet_credit' or mykey == 'pending_wallet_debit' or mykey == 'wallet_credit_return' or mykey == 'wallet_debit_return':
                if request.user.permission == '2':
                    return True
                else:
                    print('not validated!!!')
                    raise Http404
            if mykey == 'merchant_credentials':
                if request.user.permission == '3' or request.user.permission == '4':
                    return True
                else:
                    print('not validated!!!')
                    raise Http404
            if mykey == 'payout':
                if request.user.permission == '3':
                    return True
                else:
                    print('not validated!!!')
                    raise Http404
            else:
                print('not validated!!!')
                raise Http404
        else:
            print('not validated!!!')
            raise Http404
    else:
        print('definitely not!!!')
        raise Http404
