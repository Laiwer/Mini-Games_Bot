from environs import Env


env = Env()
env.read_env()
BOT_TOKEN, ADMINS = env.str("BOT_TOKEN"), env.list("ADMINS")