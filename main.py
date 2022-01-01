import config
import logging
import aiogram
import RisusService


logging.basicConfig(level=logging.INFO);

bot = aiogram.Bot(config.TOKEN);

eventHandler = aiogram.Dispatcher(bot);

@eventHandler.message_handler( content_types=['text'])
async def message_handler_text( message ):


    risus = RisusService.RisusResponse(message,bot);
    RisusService.Risus(True,message);
    #await risus.responseToText();
@eventHandler.message_handler( content_types=['sticker'])
async def message_handler_sticker( message ):
    print( message );
    risus = RisusService.RisusResponse(message,bot)
    RisusService.Risus(True,message);

    #await risus.responseToSticker(message.sticker.file_unique_id);
if __name__ == "__main__":
    eventHandler.filters_factory.bind(RisusService.RisusFilter  );


    aiogram.executor.start_polling(eventHandler,skip_updates=True);
