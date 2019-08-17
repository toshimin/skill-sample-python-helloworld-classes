from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.skill_builder import SkillBuilder


class LaunchRequetHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "ようこそ、アレクサスキルキットへ、こんにちは、と言ってみてください。"

        handler_input.response_builder.speak(speech_text).ask(speech_text).set_card(
            SimpleCard("ハローパイソン", speech_text)).set_should_end_session(False)

        return handler_input.response_builder.response


class HelloWorldIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = "こんにちは"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("ハローパイソン", speech_text)).set_should_end_session(True)

        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = "こんにちは、と言ってみてください。"

        handler_input.response_builder.speak(speech_text).ask(speech_text).set_card(
            SimpleCard("ハローパイソン", speech_text)).set_should_end_session(False)

        return handler_input.response_builder.response


class CancelAndStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.CancelIntent")(handler_input) or is_intent_name("AMAZON.StopIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = "さようなら"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("ハローパイソン", speech_text)).set_should_end_session(False)

        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):

        # Nothing to do

        return handler_input.response_builder.response


class AllExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):

        return True

    def handle(self, handler_input, exception):
        # CloudWatch Logsに例外を書き出す
        print(exception)

        speech_text = "すみません。もう一度言ってください"
        handler_input.response_builder.speek(speech_text).ask(speech_text)
        return handler_input.response_builder.response


# Lambda Handlers
sb = SkillBuilder()
sb.add_request_handler(LaunchRequetHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelAndStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_exception_handler(AllExceptionHandler())

handler = sb.lambda_handler()
