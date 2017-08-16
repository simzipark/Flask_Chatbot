from app import db, session
from .message import BaseMessage, HomeMessage, SuccessMessage, FailMessage, FindMessage, ConvenienceMessage
from .model import User
from .keyboard import Keyboard


class Singleton(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance


class APIManager(metaclass=Singleton):
    def process(self, mode, *args):
        try:
            options = {
                'home': self.return_home_keyboard,
                'message': self.handle_message,
                'add': self.add_friend,
                'block': self.block_friend,
                'exit': self.exit_chatroom,
            }

            message = options.get(mode)(*args)
            response_code = 200
        except:
            message = self.handle_fail()
            response_code = 400
        finally:
            return message, response_code

    def return_home_keyboard(self):
        '''
        [GET] your_server_url/keyboard 일 때 사용되는 함수입니다.
        '''
        message = MessageHandler.get_home_message()
        return message

    def handle_message(self, data):
        '''
        [POST] your_server_url/message 일 때 사용되며
        사용자가 전달한 data에 따라 처리 과정을 거쳐 메시지를 반환하는 메인 함수입니다.
        '''
        user_key = data['user_key']
        request_type = data['type']
        content = data['content']

        step1 = Keyboard.home_buttons
        conv_step2 = Keyboard.conv_buttons
        
        if content == '이전으로 돌아가기':
            message = MessageHandler.get_base_message()
            return message


        elif UserSessionAdmin.checkExist(user_key):
            UserSessionAdmin.addHistory(user_key, content)
            message = MessageHandler.get_conv_message(content, #유저세션 히스토리의 크기만큼을 step으로)
        
        else:
            UserSessionAdmin.init(user_key, content)
            if content == step[2]
                message = MessageHandler.get_conv_message(content, 1)

        return message

    def add_friend(self, data):
        '''
        [POST] your_server_url/friend 일 때 사용되는 함수입니다.
        기본 동작으로 수집된 user_key를 DB에 추가합니다.
        '''
        user_key = data['user_key']
        DBHandler.add_user(user_key)
        message = MessageHandler.get_success_message()
        return message

    def block_friend(self, user_key):
        '''
        [DELETE] your_server_url/friend/{user_key} 일 때 사용되는 함수입니다.
        기본 동작으로 수집된 user_key를 DB에서 제거합니다.
        '''
        DBHandler.delete_user(user_key)
        message = MessageHandler.get_success_message()
        return message

    def exit_chatroom(self, user_key):
        '''
        [DELETE] your_server_url/chat_room/{user_key} 일 때 사용되는 함수입니다.
        '''
        message = MessageHandler.get_success_message()
        return message

    def handle_fail(self):
        '''
        처리 중 예외가 발생했을 때 사용되는 함수입니다.
        '''
        message = MessageHandler.get_fail_message()
        return message


class MessageManager(metaclass=Singleton):
    def get_find_message(self, message, step):
        find_message = FindMessage(message, step).get_message()
        return find_message
	
    def get_conv_message(self, message, step):
        conv_message = ConvenienceMessage(message, step).get_message()
        return conv_message

    def get_base_message(self):
        base_message = BaseMessage().get_message()
        return base_message

    def get_home_message(self):
        home_message = HomeMessage().get_message()
        return home_message

    def get_fail_message(self):
        fail_message = FailMessage().get_message()
        return fail_message

    def get_success_message(self):
        success_message = SuccessMessage().get_message()
        return success_message


class UserSessionManager(metaclass=Singleton):
    def checkExist(self, user_key):
        return True if user_key in session else False

    def init(self, user_key, content):
        session[user_key] = {
            'history': [content]
        }

    def delete(self, user_key):
        if self.checkExist(user_key):
            del session[user_key]

    def addHistory(self, user_key, action):
        if self.checkExist(user_key):
            session[user_key]['history'].append(action)

    def getHistory(self, user_key):
        if self.checkExist(user_key):
            return session[user_key]['history'][:]
        else:
            return ['택배 조회']


class DBManager(metaclass=Singleton):
    def query(self, model, **kwargs):
        return model.query.filter_by(**kwargs).first()

    def delete(self, obj):
        db.session.delete(obj)
        self.commit()

    def delete_user(self, user_key):
        user = self.query(User, user_key=user_key)
        if user:
            self.delete(user)

    def add(self, obj):
        db.session.add(obj)
        self.commit()

    def add_user(self, user_key):
        user = self.query(User, user_key=user_key)
        if not user:
            user = User(user_key)
            self.add(user)

    def commit(self):
        db.session.commit()


APIHandler = APIManager()
MessageHandler = MessageManager()
UserSessionAdmin = UserSessionManager()
DBHandler = DBManager()
