import logging
from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework import status
# 配置日志
logger = logging.getLogger('django')


def exception_handler(exc, context):
    # 详细错误信息的定义
    error = '%s %s %s' % (context['view'], context['request'].method, exc)

    # 先让DEF处理异常，根据异常的返回值可以判断异常是否被处理
    response = drf_exception_handler(exc, context)
    # 如果返回为None, 代表DRF无法处理此时发生的异常 ，需要自定义处理

    if response is None:
        logger.error(error)
        return Response(
            {'error_msg': '程序内部错误，请稍等'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR, exception=None
        )

    return response