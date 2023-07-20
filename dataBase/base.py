import sqlite3
import pytz
from datetime import datetime
from dateutil.relativedelta import relativedelta


db = sqlite3.connect("dataBase/bot_data_base.db")
cursor = db.cursor()


def existe_in_db(table:str, user_id:int) -> bool:
    cursor.execute(f"SELECT user_id FROM {table}")
    for i in cursor.fetchall():
        if user_id in i:
            return True
    return False



# ?==================================================
# ?|||                   Юзер                     |||
# ?==================================================
def add_user_in_data_base(user_id:int, username:str, full_name:str, referrer_id:str="") -> None:
    t = datetime.now(pytz.timezone('Europe/Moscow'))
    date_time = f"{t.day:02}.{t.month:02}.{t.year:04} {t.hour:02}:{t.minute:02}:{t.second:02}"
    if referrer_id != "":
        cursor.execute("INSERT INTO user (user_id, username, full_name, join_date, last_message, referrer_id) VALUES (?, ?, ?, ?, ?, ?)", (user_id, username, full_name, date_time, date_time, referrer_id))
    else:
        cursor.execute("INSERT INTO user (user_id, username, full_name, join_date, last_message) VALUES (?, ?, ?, ?, ?)", (user_id, username, full_name, date_time, date_time))
    db.commit()

def get_data_from_user(user_id:int) -> list:
    cursor.execute("SELECT * FROM user WHERE user_id = (?)", (user_id,))
    return cursor.fetchone()[1:]

def get_all_user_id() -> list:
    cursor.execute("SELECT user_id FROM user")
    return cursor.fetchall()

def add_last_message(user_id:int) -> None:
    t = datetime.now(pytz.timezone('Europe/Moscow'))
    date_time = f"{t.day:02}.{t.month:02}.{t.year:04} {t.hour:02}:{t.minute:02}:{t.second:02}"
    cursor.execute("UPDATE user SET last_message = (?) WHERE user_id = (?)", (date_time, user_id))
    db.commit()

def count_all_bot_users() -> int:
    cursor.execute("SELECT user_id FROM user")
    return len(cursor.fetchall())

def count_active_bot_users() -> int:
    cursor.execute("SELECT last_message FROM user")
    data = cursor.fetchall()
    t = datetime.now(pytz.timezone('Europe/Moscow'))
    date_time = f"{t.day:02}.{t.month:02}.{t.year:04} {t.hour:02}:{t.minute:02}:{t.second:02}"
    date_now = date_time.split()[0].split(".")[:2]
    time_now = int(date_time.split()[1].split(":")[0])
    count = 0
    for i in data:
        date_last = i[0].split()[0].split(".")[:2]
        time_last = int(i[0].split()[1].split(":")[0])
        if int(date_now[1]) - int(date_last[1]) not in [0, 1]:
            continue
        elif date_now[0] == date_last[0] and date_now[1] == date_last[1]:
            count += 1
        elif (int(date_now[0]) - int(date_last[0])) == 1 and date_now[1] == date_last[1]:
            hour = 24 - time_last
            hour += time_now
            if hour <= 24:
                count += 1
            else:
                continue
    return count

def count_recently_bot_users() -> int:
    cursor.execute("SELECT last_message FROM user")
    data = cursor.fetchall()
    t = datetime.now(pytz.timezone('Europe/Moscow'))
    date_time = f"{t.day:02}.{t.month:02}.{t.year:04} {t.hour:02}:{t.minute:02}:{t.second:02}"
    date_now = int(date_time.split()[0].split(".")[0])
    time_now = int(date_time.split()[1].split(":")[0])
    count = 0
    for i in data:
        date_last = int(i[0].split()[0].split(".")[0])
        time_last = int(i[0].split()[1].split(":")[0])
        if date_now == date_last:
            if time_now - time_last <= 1:
                count += 1
        elif date_now - time_last == 1:
            if time_last == 23 and time_now == 0:
                count += 1
    return count

def count_time_in_bot(user_id:int) -> list:
    cursor.execute("SELECT join_date FROM user WHERE user_id = (?)", (user_id,))
    data = cursor.fetchone()[0]
    t = datetime.now(pytz.timezone('Europe/Moscow'))
    date_last = data.split()[0].split(".")
    time_last = data.split()[1].split(":")
    dt = datetime(int(date_last[2]), int(date_last[1]), int(date_last[0]), int(time_last[0]), int(time_last[1]), int(time_last[2]), tzinfo=pytz.timezone('Europe/Moscow'))
    rel = relativedelta(t, dt)
    return [rel.years*12+rel.months, rel.days, rel.hours, rel.minutes]

def existe_referrer_id(user_id:int) -> bool:
    if user_id is not None:
        cursor.execute("SELECT referrer_id FROM user")
        for i in cursor.fetchall():
            if user_id in i:
                return True
        return False
    else:
        return False

def count_referal(user_id:int):
    cursor.execute("SELECT user_id FROM user WHERE referrer_id = (?)", (user_id,))
    return len(cursor.fetchall())

def get_all_count_referal_from_player():
    cursor.execute("""SELECT user_id FROM user""")
    top = {}
    for i in cursor.fetchall():
        top[i[0]] = len(cursor.execute("SELECT user_id FROM user WHERE referrer_id = (?)", (i[0],)).fetchall())
    return top




# ?==================================================
# ?|||                   Игрок                    |||
# ?==================================================
def add_player_in_data_base(user_id:int, name_player:str, emoji_player:str) -> None:
    cursor.execute("INSERT INTO player (user_id, name_player, emoji_player, trophies) VALUES (?, ?, ?, ?)", (user_id, name_player, emoji_player, 0))
    db.commit()

def existe_name_player(name_player:str) -> bool:
    cursor.execute("SELECT name_player FROM player")
    for i in cursor.fetchall():
        if name_player in i:
            return True
    return False

def update_emoji_player(user_id:int, emoji_player:str) -> None:
    cursor.execute("UPDATE player SET emoji_player = (?) WHERE user_id = (?)", (emoji_player, user_id))
    db.commit()

def get_data_from_player(user_id:int) -> list:
    cursor.execute("SELECT * FROM player WHERE user_id = (?)", (user_id,))
    return cursor.fetchone()[1:]

def get_player_from_user_id(user_id:int) -> str:
    cursor.execute("SELECT emoji_player, name_player FROM player WHERE user_id = (?)", (user_id,))
    data = cursor.fetchone()
    return f"{data[0]} {data[1]}"

def get_all_trophies_from_player() -> dict:
    cursor.execute("""SELECT trophies, user_id FROM player""")
    top = {}
    for i in cursor.fetchall():
        top[i[1]] = i[0]
    return top

def increase_played_mini_games(user_id:int):
    all = get_data_from_player(user_id)[3]
    cursor.execute("UPDATE player SET played_mini_games = (?) WHERE user_id = (?)", (all + 1, user_id))
    db.commit()



# ?==================================================
# ?|||           Найди эмодзи на поле             |||
# ?==================================================
def add_mini_game_search_emoji_on_field_in_data_base(user_id:int) -> None:
    cursor.execute("INSERT INTO mini_game_search_emoji_on_field (user_id) VALUES (?)", (user_id,))
    db.commit()

def get_search_emoji_on_field(user_id:int) -> list:
    cursor.execute("SELECT * FROM mini_game_search_emoji_on_field WHERE user_id = (?)", (user_id,))
    return cursor.fetchone()[1:]

def update_is_win_search_emoji(user_id:int, is_win:int) -> None:
    cursor.execute("UPDATE mini_game_search_emoji_on_field SET is_win = (?) WHERE user_id = (?)", (int(is_win), user_id))
    db.commit()

def update_difficulty_search_emoji(user_id:int, difficulty:int) -> None:
    cursor.execute("UPDATE mini_game_search_emoji_on_field SET difficulty = (?) WHERE user_id = (?)", (difficulty, user_id))
    db.commit()

def update_stage_search_emoji(user_id:int, stage:int=0) -> None:
    if stage != 0:
        cursor.execute("UPDATE mini_game_search_emoji_on_field SET stage = (?) WHERE user_id = (?)", (stage, user_id))
    else:
        cursor.execute("SELECT stage FROM mini_game_search_emoji_on_field WHERE user_id = (?)", (user_id,))
        data = cursor.fetchone()[0]
        cursor.execute("UPDATE mini_game_search_emoji_on_field SET stage = (?) WHERE user_id = (?)", (data + 1, user_id))
    db.commit()

def profit_by_search_emoji_on_field(user_id:int, profit:int, simbol:str):
    cursor.execute("SELECT trophies FROM player WHERE user_id = (?)", (user_id,))
    data = cursor.fetchone()
    trophies = data[0]
    if simbol == "-" and data[0] - profit < 0:
        trophies = 0
    else:
        trophies = data[0] + profit if simbol == "+" else data[0] - profit
    cursor.execute("UPDATE player SET trophies = (?) WHERE user_id = (?)", (trophies, user_id))
    db.commit()

def update_record_stage_and_all_stage_search_emoji(user_id:int, size:int, stage:int):
    if size == 3:
        cursor.execute("SELECT record_stage_small, all_stage_small FROM mini_game_search_emoji_on_field WHERE user_id = (?)", (user_id,))
        data = cursor.fetchone()
        record = stage if stage > data[0] else data[0]
        cursor.execute("UPDATE mini_game_search_emoji_on_field SET record_stage_small = (?), all_stage_small = (?) WHERE user_id = (?)", (record, data[1] + stage, user_id))
        db.commit()
    elif size == 5:
        cursor.execute("SELECT record_stage_medium, all_stage_medium FROM mini_game_search_emoji_on_field WHERE user_id = (?)", (user_id,))
        data = cursor.fetchone()
        record = stage if stage > data[0] else data[0]
        cursor.execute("UPDATE mini_game_search_emoji_on_field SET record_stage_medium = (?), all_stage_medium = (?) WHERE user_id = (?)", (record, data[1] + stage, user_id))
        db.commit()
    elif size == 7:
        cursor.execute("SELECT record_stage_hard, all_stage_hard FROM mini_game_search_emoji_on_field WHERE user_id = (?)", (user_id,))
        data = cursor.fetchone()
        record = stage if stage > data[0] else data[0]
        cursor.execute("UPDATE mini_game_search_emoji_on_field SET record_stage_hard = (?), all_stage_hard = (?) WHERE user_id = (?)", (record, data[1] + stage, user_id))
        db.commit()

def get_all_record_search_emoji_small_from_player():
    cursor.execute("""SELECT record_stage_small, user_id FROM mini_game_search_emoji_on_field""")
    top = {}
    for i in cursor.fetchall():
        top[i[1]] = i[0]
    return top

def get_all_record_search_emoji_medium_from_player():
    cursor.execute("""SELECT record_stage_medium, user_id FROM mini_game_search_emoji_on_field""")
    top = {}
    for i in cursor.fetchall():
        top[i[1]] = i[0]
    return top

def get_all_record_search_emoji_hard_from_player():
    cursor.execute("""SELECT record_stage_hard, user_id FROM mini_game_search_emoji_on_field""")
    top = {}
    for i in cursor.fetchall():
        top[i[1]] = i[0]
    return top

def get_all_all_stage_search_emoji_small_from_player():
    cursor.execute("""SELECT all_stage_small, user_id FROM mini_game_search_emoji_on_field""")
    top = {}
    for i in cursor.fetchall():
        top[i[1]] = i[0]
    return top

def get_all_all_stage_search_emoji_medium_from_player():
    cursor.execute("""SELECT all_stage_medium, user_id FROM mini_game_search_emoji_on_field""")
    top = {}
    for i in cursor.fetchall():
        top[i[1]] = i[0]
    return top

def get_all_all_stage_search_emoji_hard_from_player():
    cursor.execute("""SELECT all_stage_hard, user_id FROM mini_game_search_emoji_on_field""")
    top = {}
    for i in cursor.fetchall():
        top[i[1]] = i[0]
    return top



# ?==================================================
# ?|||           Соединить по порядку             |||
# ?==================================================
def add_mini_game_connect_in_order_in_data_base(user_id:int):
    cursor.execute("INSERT INTO mg_connect_in_order (user_id) VALUES (?)", (user_id,))
    db.commit()

def get_connect_in_order(user_id:int) -> list:
    cursor.execute("SELECT * FROM mg_connect_in_order WHERE user_id = (?)", (user_id,))
    return cursor.fetchone()[1:]

def update_now_number_connect_in_order(user_id:int, now_num:int):
    cursor.execute("UPDATE mg_connect_in_order SET now_number = (?) WHERE user_id = (?)", (now_num, user_id))
    db.commit()

def update_win_connect_in_order(user_id:int, win:int):
    cursor.execute("UPDATE mg_connect_in_order SET win = (?) WHERE user_id = (?)", (win, user_id))
    db.commit()

def increase_all_complite_game_connect_in_order(user_id:int):
    all_game = get_connect_in_order(user_id)[2]
    cursor.execute("UPDATE mg_connect_in_order SET all_complite_game = (?) WHERE user_id = (?)", (all_game + 1, user_id))
    db.commit()

def get_all_record_connect_in_order_from_player():
    cursor.execute("""SELECT all_complite_game, user_id FROM mg_connect_in_order""")
    top = {}
    for i in cursor.fetchall():
        top[i[1]] = i[0]
    return top

def get_game_field_connect_in_order(user_id:int) -> list:
    cursor.execute("SELECT game_field FROM mg_connect_in_order WHERE user_id = (?)", (user_id,))
    arr = [int(i) for i in cursor.fetchone()[0].split(",")]
    return arr


def update_game_field_connect_in_order(user_id:int, field:list):
    if field != [0]:
        str_field = ",".join(str(i) for i in field)
    else:
        str_field = "0"
    cursor.execute("UPDATE mg_connect_in_order SET game_field = (?) WHERE user_id = (?)", (str_field, user_id))
    db.commit()