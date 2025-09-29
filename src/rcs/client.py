import typing
from .base_client import PinnacleBase, AsyncPinnacleBase

if typing.TYPE_CHECKING:
    from .wrapper.tools.file_uploader import FileUploader, AsyncFileUploader
    from .wrapper.messages.client import EnhancedMessages, AsyncEnhancedMessages


class Pinnacle(PinnacleBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._file_uploader: typing.Optional[FileUploader] = None
        self._enhanced_messages: typing.Optional[EnhancedMessages] = None

    @property
    def file_uploader(self):
        if self._file_uploader is None:
            from .wrapper.tools.file_uploader import FileUploader  # noqa: E402

            self._file_uploader = FileUploader(client_wrapper=self._client_wrapper)
        return self._file_uploader

    @property
    def enhanced_messages(self):
        if self._enhanced_messages is None:
            from .wrapper.messages.client import EnhancedMessages  # noqa: E402

            self._enhanced_messages = EnhancedMessages(client_wrapper=self._client_wrapper)
        return self._enhanced_messages


class AsyncPinnacle(AsyncPinnacleBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._file_uploader: typing.Optional[AsyncFileUploader] = None
        self._enhanced_messages: typing.Optional[AsyncEnhancedMessages] = None

    @property
    def file_uploader(self):
        if self._file_uploader is None:
            from .wrapper.tools.file_uploader import AsyncFileUploader  # noqa: E402

            self._file_uploader = AsyncFileUploader(client_wrapper=self._client_wrapper)
        return self._file_uploader

    @property
    def enhanced_messages(self):
        if self._enhanced_messages is None:
            from .wrapper.messages.client import AsyncEnhancedMessages  # noqa: E402

            self._enhanced_messages = AsyncEnhancedMessages(client_wrapper=self._client_wrapper)
        return self._enhanced_messages
