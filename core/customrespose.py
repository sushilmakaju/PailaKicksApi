class CustomResponse:
    @classmethod
    def success_response_token(cls, refresh, access, msg, data=None):
        data = data or {}
        return cls._build_response(msg, data)

    def successResponse(self, msg, data=dict()):
        context = {
            "message": msg,
            "detail": data,
            "error": []
        }
        return context

    @classmethod
    def errorResponse(cls, msg, error=None):
        error = error or {}
        return cls._build_response(msg, data={}, error=error)

    @classmethod
    def _build_response(cls, msg, data, error=None):
        return {
            "message": msg,
            "data": data,
            "error": error or [],
        }