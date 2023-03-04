from typing import List, Union

from aiogram import types
from aiogram.dispatcher.filters import ContentTypeFilter
from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.manager.protocols import ManagedDialogProto
from aiogram_dialog.widgets.input import MessageHandlerFunc, BaseInput
from aiogram_dialog.widgets.widget_event import WidgetEventProcessor, ensure_event_processor


class Contents(ContentTypeFilter):
    photo = types.ContentTypes.PHOTO
    document = types.ContentTypes.DOCUMENT
    contact = types.ContentTypes.CONTACT
    audio = types.ContentTypes.AUDIO
    video = types.ContentTypes.VIDEO
    any = types.ContentTypes.ANY


class AudioInput(BaseInput):
    def __init__(self, func: Union[MessageHandlerFunc, WidgetEventProcessor, None],
                 content_types: List[str] = Contents.audio):
        super().__init__()
        self.func = ensure_event_processor(func)
        self.filter = ContentTypeFilter(content_types)

    async def process_message(self, message: Message, dialog: ManagedDialogProto, manager: DialogManager) -> bool:
        if not await self.filter.check(message):
            return False
        await self.func.process_event(message, manager.dialog(), manager)
        return True


class ContactInput(BaseInput):
    def __init__(self, func: Union[MessageHandlerFunc, WidgetEventProcessor, None],
                 content_types: List[str] = Contents.contact):
        super().__init__()
        self.func = ensure_event_processor(func)
        self.filter = ContentTypeFilter(content_types)

    async def process_message(self, message: Message, dialog: ManagedDialogProto, manager: DialogManager) -> bool:
        if not await self.filter.check(message):
            return False
        await self.func.process_event(message, manager.dialog(), manager)
        return True


class DocumentInput(BaseInput):
    def __init__(self, func: Union[MessageHandlerFunc, WidgetEventProcessor, None],
                 content_types: List[str] = Contents.document):
        super().__init__()
        self.func = ensure_event_processor(func)
        self.filter = ContentTypeFilter(content_types)

    async def process_message(self, message: Message, dialog: ManagedDialogProto, manager: DialogManager) -> bool:
        if not await self.filter.check(message):
            return False
        await self.func.process_event(message, manager.dialog(), manager)
        return True


class VideoInput(BaseInput):
    def __init__(self, func: Union[MessageHandlerFunc, WidgetEventProcessor, None],
                 content_types: List[str] = Contents.video):
        super().__init__()
        self.func = ensure_event_processor(func)
        self.filter = ContentTypeFilter(content_types)

    async def process_message(self, message: Message, dialog: ManagedDialogProto, manager: DialogManager) -> bool:
        if not await self.filter.check(message):
            return False
        await self.func.process_event(message, manager.dialog(), manager)
        return True


class PhotoInput(BaseInput):
    def __init__(self, func: Union[MessageHandlerFunc, WidgetEventProcessor, None],
                 content_types: List[str] = Contents.photo):
        super().__init__()
        self.func = ensure_event_processor(func)
        self.filter = ContentTypeFilter(content_types)

    async def process_message(self, message: Message, dialog: ManagedDialogProto, manager: DialogManager) -> bool:
        if not await self.filter.check(message):
            return False
        await self.func.process_event(message, manager.dialog(), manager)
        return True


class AnyInput(BaseInput):
    def __init__(self, func: Union[MessageHandlerFunc, WidgetEventProcessor, None],
                 content_types: List[str] = Contents.any):
        super().__init__()
        self.func = ensure_event_processor(func)
        self.filter = ContentTypeFilter(content_types)

    async def process_message(self, message: Message, dialog: ManagedDialogProto, manager: DialogManager) -> bool:
        if not await self.filter.check(message):
            return False
        await self.func.process_event(message, manager.dialog(), manager)
        return True
