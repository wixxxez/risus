import aiogram
import config
import WordsGeneratorService




class RisusFilter(aiogram.dispatcher.filters.Filter):

    def __init__(self ):

        self.target = 971098650
        self.chat = -797011067;
        self.key_words = [
            "risus",
            "Різус",
            "Ризус"
        ]

    async def check(self, message) -> bool:
        print(message.chat.id )
        status_r = False;
        for i in self.key_words:

            if i.upper() in message.text.upper():
                status_r = True;

        return  status_r ;

class RisusResponse(WordsGeneratorService.WordsGenerator):

    def __init__(self, message,bot):
        super().__init__();
        self.id = message.chat.id
        self.message = message
        self.bot = bot

    def responseToText(self):

        text = self.GenerateText();
        return self.bot.send_message(text=text,chat_id=self.id, reply_to_message_id = self.message.message_id);

    def responseToSticker(self, sticker):
        if(sticker == "AgADhwEAAixg9Rw"):
            return self.bot.send_sticker(chat_id=self.id, sticker=config.suck_dick_cat,
                                  reply_to_message_id=self.message.message_id);
        else:
            return self.responseToText();
