from environs import Env


env = Env()
env.read_env()
BOT_TOKEN, ADMINS, IP = env.str("BOT_TOKEN"), env.list("ADMINS"), env.str("ip")