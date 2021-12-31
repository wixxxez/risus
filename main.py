import config
import logging
import aiogram



logging.basicConfig(level=logging.INFO);

bot = aiogram.Bot(config.TOKEN);

eventHandler = aiogram.Dispatcher(bot);

@eventHandler.message_handler()
async def echo( message ):
    await message.answer(message["from"].first_name);

if __name__ == "__main__":
    aiogram.executor.start_polling(eventHandler,skip_updates=True);
