from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        return self.get_response(request)

    def process_response(self, request, response):
        # 判断请求头  如果非浏览器则返回非法操作
        ua = request.headers.get("User-Agent")
        # print("当前访问工具为",ua)
        if ua.__contains__("python"):
            return HttpResponse("非法请求")
        else:
            return response