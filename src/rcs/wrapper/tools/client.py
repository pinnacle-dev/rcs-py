from typing import Optional

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...tools.client import AsyncToolsClient, ToolsClient
from .file_uploader import AsyncFileUploader, FileUploader


class EnhancedTools(ToolsClient):
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)
        self._file_uploader: Optional[FileUploader] = None

    @property
    def file(self) -> FileUploader:
        if self._file_uploader is None:
            self._file_uploader = FileUploader(client_wrapper=self._client_wrapper)
        return self._file_uploader


class AsyncEnhancedTools(AsyncToolsClient):
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)
        self._file_uploader: Optional[AsyncFileUploader] = None

    @property
    def file(self) -> AsyncFileUploader:
        if self._file_uploader is None:
            self._file_uploader = AsyncFileUploader(client_wrapper=self._client_wrapper)
        return self._file_uploader