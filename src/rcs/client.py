from .base_client import PinnacleBase, AsyncPinnacleBase

from .utils import parse_inbound


class Pinnacle(PinnacleBase):

    @staticmethod
    def parse_inbound_message(
        data: dict,
    ):
        """
        Parse the inbound message data.

        Parameters
        ----------
        data : dict
            The inbound message data to be parsed.

        Returns
        -------
        inbound_message : Union[
            InboundActionMessage,
            InboundTextMessage,
            InboundLocationMessage,
            InboundMediaMessage,
        ]
            The parsed inbound message data.


        Examples
        --------
        from rcs import Pinnacle

        data = {
            "message_type": "text",
            "text": "Hello, World!",
            "from": "+12345678901",
            "to": "+10987654321",
            "metadata": None
        }
        parsed_data = Pinnacle.parse_inbound_message(data)
        """

        return parse_inbound(data)


class AsyncPinnacle(AsyncPinnacleBase):

    @staticmethod
    def parse_inbound_message(
        data: dict,
    ):
        """
        Parse the inbound message data.

        Parameters
        ----------
        data : dict
            The inbound message data to be parsed.

        Returns
        -------
        inbound_message : Union[
            InboundActionMessage,
            InboundTextMessage,
            InboundLocationMessage,
            InboundMediaMessage,
        ]
            The parsed inbound message data.


        Examples
        --------
        from rcs import Pinnacle

        data = {
            "message_type": "text",
            "text": "Hello, World!",
            "from": "+12345678901",
            "to": "+10987654321",
            "metadata": None
        }
        parsed_data = Pinnacle.parse_inbound_message(data)
        """
        return parse_inbound(data)
