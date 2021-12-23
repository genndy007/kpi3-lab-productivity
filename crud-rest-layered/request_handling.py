from __future__ import annotations
from abc import ABC, abstractmethod
from apartment_facade import ApartmentFacade

# chain of responsibility


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request):
        pass


class AbstractHandler(Handler):
    _next_handler = None
    apartment_facade = ApartmentFacade()

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class GETHandler(AbstractHandler):
    def handle(self, request):
        if request.method == 'GET':
            return {
                "apartments": self.apartment_facade.get_apartments(request)
            }
        return super().handle(request)


class POSTHandler(AbstractHandler):
    def handle(self, request):
        if request.method == "POST":
            return {
                "apartment_id": self.apartment_facade.add_apartment(request)
            }
        return super().handle(request)


class PATCHHandler(AbstractHandler):
    def handle(self, request):
        if request.method == "PATCH":
            return {
                "apartment_id": self.apartment_facade.update_apartment(request)
            }
        return super().handle(request)


class DELETEHandler(AbstractHandler):
    def handle(self, request):
        if request.method == "DELETE":
            return {
                "apartment_id": self.apartment_facade.remove_apartment(request)
            }
        return super().handle(request)
