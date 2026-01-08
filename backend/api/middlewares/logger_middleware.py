from collections.abc import Callable
from typing import Any
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import time
from datetime import datetime
from backend.utils import logging

logger = logging.logger_setup()

class LoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Any]
    ) -> Response:
        """
        Logs all incoming and outgoing request, response pairs. This method logs the request params,
        datetime of request, duration of execution. Logs should be printed using the custom logging module provided.
        Logs should be printed so that they are easily readable and understandable.

        :param request: Request received to this middleware from client (it is supplied by FastAPI)
        :param call_next: Endpoint or next middleware to be called (if any, this is the next middleware in the chain of middlewares, it is supplied by FastAPI)
        :return: Response from endpoint
        """
        # TODO:(Member) Finish implementing this method
        start = time.time()
        timsp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

        logger.info(f"""Incoming request:
            Time: {timsp}
            Query Params: {dict(request.query_params)}
        """)
        response = await call_next(request)
        time_dur = time.time()-start

        logger.info(f"""Outgoing Response:
                    Status: {response.status},
                    Duration: {time_dur}""")
        response = await call_next(request)
        return response
