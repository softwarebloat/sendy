import abc

from pydantic import BaseModel
from typing import Optional


__all__ = [
    'HttpGateway',
    'HttpGatewayResponse',
    'HttpGatewayError',
]

class HttpGatewayResponse(BaseModel):
    status_code: int
    message: Optional[str]


class HttpGatewayError:
    class BaseError(Exception):
        pass

    class NotFoundError(BaseError):
        pass

    class ResponseNotValid(BaseError):
        pass

class HttpGateway(BaseModel, abc.ABC):

    async def send_message(self, message: str, url: str) -> HttpGatewayResponse:
        """Send message to desired url

        :param message: the name of the pokemon to retrieve
        :type url: str
        :return: http status code and a message if provided (e.g.: error message)
        :rtype: HttpGatewayResponse
        """
        raise NotImplementedError('PokeapiGateway.get_pokemon_species')