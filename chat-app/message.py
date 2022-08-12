# https://medium.com/swlh/applying-oop-in-real-world-applications-495c8ee4d946

# Encapsulated Message class contains all message related variables / functions
class Message:
    MSG_TYPE_TEXT = 1
    MSG_TYPE_VOICE = 2
    MSG_TYPE_IMAGE = 3

    # Private variables will be like "__var" or "_var"
    def __init__(self, sender = None, receiver = None):
        self.__message_id: None
        self.__sender: None
        self.__receiver: None
        self. __message_content = None

        # fields can be extended
        self.__delivery_status = None
        self.__return_receipt_required = None

    def set_sender(self, sender):
        self.__sender = sender

    def set_receiver(self, receiver):
        self.__receiver = receiver
    
    def set_message_content(self, message_content):
        self.__message_content = message_content

    def get_sender(self):
        return self.__sender

    def get_receiver(self):
        return self.__receiver

    def get_message_content(self, message_content):
        return self.__message_content

# TextMessage is inherited from Message class
class TextMessage(Message):

    def __init__(self, sender = None, receiver = None):
        super().__init__(sender, receiver)
        # Fields related to text message
        self.__text_message_content = None
        self.__message_type = Message.MSG_TYPE_TEXT

    def set_text_message_conten(self, text_message_content: str):
        self.__text_message_content = text_message_content

    def get_text_message_content(self):
        return self.__text_message_content

    def get_text_message_size(self):
        return len(self.__text_message_content)


class ImageMessage(Message):

    def __init__(self):
        # Fields related to image message
        self.__image_message_content = None
        self.__image_resolution = None
        self.__image_metadata = None
        self.__message_type = Message.MSG_TYPE_IMAGE

    def set_image_message_content(self, image_message_content: bytes, image_resolution, image_metadata):
        self.__image_message_content = image_message_content
        self.__image_resolution = image_resolution
        self.__image_metadata = image_metadata

    def get_image_message_content(self):
        return self.__image_message_content

    

