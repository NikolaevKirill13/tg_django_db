from aiogram import executor, exceptions
from dispatcher import dispatcher
import handlers


if __name__ == '__main__':
	executor.start_polling(dispatcher, skip_updates = True)