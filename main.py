import config
import logging
import aiogram



logging.basicConfig(level=logging.INFO);

bot = aiogram.Bot(config.TOKEN);

eventHandler = aiogram.Dispatcher(bot);

@eventHandler.message_handler(content_types=['sticker','text'])
async def ds( message ):
    id = message.chat.id;


    await bot.send_sticker(chat_id=id, sticker='CAACAgIAAxkBAAN6Yc8PDm4Vq6MQasoMsTesgaFoWMsAAncBAAIsYPUcWWKFR1r1NF0jBA',reply_to_message_id=message.message_id);

if __name__ == "__main__":
    aiogram.executor.start_polling(eventHandler,skip_updates=True);
