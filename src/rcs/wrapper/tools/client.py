from typing import Optional
from ...tools.client import ToolsClient, AsyncToolsClient
from ...tools.file.client import FileClient, AsyncFileClient
from .file_uploader import FileUploader, AsyncFileUploader
from ...core.client_wrapper import SyncClientWrapper, AsyncClientWrapper


class EnhancedFileClient(FileClient):
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._file_uploader: Optional[FileUploader] = None

    def upload_from_path(self, *args, **kwargs):
        if self._file_uploader is None:
            self._file_uploader = FileUploader(client_wrapper=self._client_wrapper)
        return self._file_uploader.upload_from_path(*args, **kwargs)


class AsyncEnhancedFileClient(AsyncFileClient):
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._file_uploader: Optional[AsyncFileUploader] = None

    async def upload_from_path(self, *args, **kwargs):
        if self._file_uploader is None:
            self._file_uploader = AsyncFileUploader(client_wrapper=self._client_wrapper)
        return await self._file_uploader.upload_from_path(*args, **kwargs)


class EnhancedTools(ToolsClient):
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)
        self._enhanced_file: Optional[EnhancedFileClient] = None

    @property
    def file(self) -> EnhancedFileClient:
        if self._enhanced_file is None:
            self._enhanced_file = EnhancedFileClient(client_wrapper=self._client_wrapper)
        return self._enhanced_file


class AsyncEnhancedTools(AsyncToolsClient):
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)
        self._enhanced_file: Optional[AsyncEnhancedFileClient] = None

    @property
    def file(self) -> AsyncEnhancedFileClient:
        if self._enhanced_file is None:
            self._enhanced_file = AsyncEnhancedFileClient(client_wrapper=self._client_wrapper)
        return self._enhanced_file