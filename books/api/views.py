from django.http import HttpRequest, JsonResponse


def books(request: HttpRequest) -> JsonResponse:
    return JsonResponse({'is_ok': True})
