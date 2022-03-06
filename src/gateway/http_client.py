import httpx
import logging

# import pydantic
from entities.http_client import (
    HttpGateway,
    HttpGatewayResponse,
    HttpGatewayError,
)


class AsyncHttpGateway(HttpGateway):
    async def send_message(self, message: str, url: str) -> HttpGatewayResponse:
        try:
            async with httpx.AsyncClient() as client:
                result = await client.post(url, data=message)
            result.raise_for_status()
        except httpx.HTTPError as err:
            logging.error(f"http error while sending message to {url}")
            if err.response and err.response.status_code == 404:
                logging.error(f"{url} not found")
                raise HttpGatewayError.NotFoundError(str(err))
            else:
                raise HttpGatewayError.ResponseNotValid(str(err))

        return result
