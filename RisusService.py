import aiogram
import config
import WordsGeneratorService
import codecs
import re
import RisusHelperService
class RisusLogger:

    def logMessage(self, text):
        with codecs.open("demons.txt", "a", encoding="utf-8") as demonfiles:

            text = RisusHelperService.StringAdapter().delete_emoji(text);


            demonfiles.write(text + u"\n");


logger = RisusLogger();

class RisusFilter(aiogram.dispatcher.filters.Filter):

    def __init__(self ):

        self.target = 971098650
        self.chat = -797011067;
        self.key_words = [
            "risus",
            "Різус",
            "Ризус",
            "ris",
            "риз",
            "різ"
        ]

    async def check(self, message) -> bool:
        print(message.from_user.id )

        status_r = False;
        for i in self.key_words:

            if i.upper() in message.text.upper():
                status_r = True;
        if (status_r==False and message.chat.id == -1001622487064):
            logger.logMessage(message.text);
        return  status_r ;


class RisusResponse(WordsGeneratorService.WordsGenerator):

    def __init__(self, message,bot):
        super().__init__();
        self.id = message.chat.id
        self.message = message
        self.bot = bot

    def getResponseByFilter(self):
        if self.message.from_user.id == 820980192:
            return  self.GenerateText(config.complement_text);
        if self.message.from_user.id == 1341005388:
            return self.bot.send_sticker(chat_id=self.id, sticker=config.go_fuckyourself_piano_cat,
                                         reply_to_message_id=self.message.message_id);
        else:
            return self.GenerateText(config.main_text_ukr);

    def responseToText(self):

        text = self.getResponseByFilter();
        if type(text) is str:
            return self.bot.send_message(text=text,chat_id=self.id, reply_to_message_id = self.message.message_id);
        else:
            return text;
    def responseToSticker(self, sticker):
        if(sticker == "AgADhwEAAixg9Rw"):
            return self.bot.send_sticker(chat_id=self.id, sticker=config.suck_dick_cat,
                                  reply_to_message_id=self.message.message_id);
        else:
            return self.responseToText();
