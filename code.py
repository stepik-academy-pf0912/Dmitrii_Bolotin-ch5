from flask import Flask

app = Flask(__name__)
# app.config['DEBUG'] = True

# routes --------------------------------
ROUTE_MAIN = '/'
ROUTE_ABOUT = '/about'
ROUTE_VIDEOS = '/videos'
ROUTE_VIDEO = ROUTE_VIDEOS + '/<int:id>'
ROUTE_PLAYLISTS = '/playlists'
ROUTE_PLAYLIST = ROUTE_PLAYLISTS + '/<int:id>'
ROUTE_TAGS = '/tags'
ROUTE_TAG = ROUTE_TAGS + '/<tag>'

# messages-------------------------------
MESSAGE_PAGE_NOT_FOUND = 'Такой страницы нет'
MESSAGE_ABOUT_APP = '<h1>"Stepik VideoGames", портал видео про видеоигры.</h1>'

# data----------------------------------
playlists = [{'id': 1, 'title': 'ИгроСториз', 'videos': [0, 4, 7]}, {'id': 2, 'title': 'Репортажи', 'videos': [8, 9]},
             {'id': 3, 'title': 'Обзоры', 'videos': [1, 2]}, {'id': 4, 'title': 'Летсплеи', 'videos': [3]},
             {'id': 5, 'title': 'Новости', 'videos': [5, 6, 10, 11, 12, 13]},
             ]

tags = [{'title': 'opinion', 'id': 1}, {'title': 'fan', 'id': 2}, {'title': 'overview', 'id': 3},
        {'title': 'game-analytics', 'id': 4}, {'title': 'insiders', 'id': 5}, {'title': 'races', 'id': 6},
        {'title': 'PC', 'id': 7}]

videos = [
    {'id': 0, 'title': 'ИгроСториз: Mafia 4, GTA 6 и BioShock Online – Take-Two дает бой конкурентам на '
                       'PS5 и Xbox Series X', 'videoid': 'https://youtu.be/05GPNjBtF48', 'tags': [1, 4, 5, 7]},
    {'id': 1, 'title': 'Поиграли в Sekiro: Shadows Die Twice. Свежо, но знакомо',
     'videoid': 'https://youtu.be/nwPs5f4WLN8', 'tags': [2, 3, 6, 7]},
    {'id': 2, 'title': 'Gothic Remake - Актуально ли в 2021 году ? [Мнение после Демки]',
     'videoid': 'https://youtu.be/eVtx5Y6lFjk', 'tags': [1, 4]},
    {'id': 3, 'title': 'Начало прохождения - Anno 1800 #01', 'videoid': 'https://youtu.be/J3Wk2CecrUg',
     'tags': [3, 6, 7]},
    {'id': 4, 'title': 'ИгроСториз: Итоги 2019 года. ПК победит PS5 и Xbox, сюжетные игры оживают, '
                       'крупные студии вымрут?', 'videoid': 'https://youtu.be/pxsJsFjCcgU', 'tags': [1, 4, 5, 7]},
    {'id': 5, 'title': 'Подробности игры по «Властелину колец», глобальный мод для Mafia II, '
                       'падение популярности Dota 2...', 'videoid': 'https://youtu.be/UdsrgZk5lVA', 'tags': [4, 5, 7]},
    {'id': 6, 'title': 'ИГРОВЫЕ НОВОСТИ STALKER 2, про The Elder Scrolls 6, Medal of Honor, '
                       'PlayStation 5, Final Fantasy 7', 'videoid': 'https://youtu.be/VYAk05t6Q', 'tags': [1, 4, 5, 7]},
    {'id': 7, 'title': 'Эпидерсия: Невероятный случай на Кикстартер. Игра о драконах собрала кучу денег '
                       'из-за Гарри Поттера', 'videoid': 'https://youtu.be/fvTZTx6tlAU', 'tags': [1, 5]},
    {'id': 8, 'title': 'Поиграли в Borderlands 3. Вооружённая жертва Epic Games Store',
     'videoid': 'https://youtu.be/NXlosGTO3', 'tags': [1, 3, 7]},
    {'id': 9, 'title': '10 лучших хорроров десятилетия. От Amnesia: The Dark Descent до Resident Evil 2 Remake',
     'videoid': 'https://youtu.be/83r7CffMmS8', 'tags': [1, 3]},
    {'id': 10, 'title': 'АААА-новости #135. Новогодний эфир. Вопросы, ответы, рефлексия',
     'videoid': 'https://youtu.be/ksWZfVsxTN4', 'tags': [1, 2, 4, 5]},
    {'id': 11, 'title': 'Экранизация GTA, новинки Star Citizen, мультиплеер Cyberpunk 2077, боссы '
                        'Final Fantasy VII Remake...', 'videoid': 'https://youtu.be/TkVUnyEAk0M', 'tags': [1, 4, 5, 7]},
    {'id': 12, 'title': 'АААА-новости #135. Новогодний эфир. Вопросы, ответы, рефлексия',
     'videoid': 'https://youtu.be/ksWZfVsxTN4', 'tags': [1, 4, 5, 7]},
    {'id': 13, 'title': 'Игромания! ИГРОВЫЕ НОВОСТИ, 16 декабря (The Game Awards 2019, '
                        'Resident Evil 3, Half-Life: Alyx)', 'videoid': 'https://youtu.be/xn6URedv4LQ',
     'tags': [1, 4, 5, 7]},
]

back_link = f'<a href={ROUTE_MAIN}>Вернуться на главную страницу</a><br><br>'


# helpers-------------------------------
def get_item_by_key_and_value(entity_list, value, key='id'):
    item = {}

    for entity in entity_list:
        if entity[key] == value:
            item = entity
            break

    return item


def get_playlist_link_text(item):
    return f'''{item['title']} ({len(item['videos'])} видео)'''


def list_to_str(entity_list, route, link_key='id', get_link_text=None):
    result_str = ''

    for item in entity_list:
        href = f'{route}/{item[link_key]}'
        link_text = get_link_text(item) if get_link_text else item['title']

        result_str += f'''<a href="{href}">{link_text}</a>, '''

    return result_str.rstrip(', ')


def create_order_list_by(entity, route, link_key='id', get_link_text=None):
    items = ''

    for item in entity:
        href = f'{route}/{item[link_key]}'
        link_text = get_link_text(item) if get_link_text else item['title']

        items += f'''<li><a href="{href}">{link_text}</a></li>'''

    return f'''<ol>{items}</ol>'''


def render_main_page():
    tags_str = list_to_str(tags, ROUTE_TAGS, link_key='title')
    playlists_str = list_to_str(playlists, ROUTE_PLAYLISTS, get_link_text=get_playlist_link_text)

    return '''<h1>Привет, это: {message_about}</h1>
    <p>Перейдите на <a href={route_about}>"О приложении"</a> чтобы посмотреть информацию о приложении.</p>
    <p>Перейдите на <a href={route_playlists}>"Плейлисты"</a> чтобы посмотреть плейлисты.</p> 
    <p>Перейдите на <a href={route_videos}>"Видео"</a> чтобы посмотреть список видео.</p>

    <b>Теги</b>: {tags}<br>
    <b>Плейлисты</b>: {playlists}
    '''.format(message_about=MESSAGE_ABOUT_APP, route_about=ROUTE_ABOUT, route_playlists=ROUTE_PLAYLISTS,
               route_videos=ROUTE_VIDEOS,
               tags=tags_str, playlists=playlists_str)


def render_video_page(id):
    video_item = get_item_by_key_and_value(videos, id)
    tag_ids = video_item['tags']
    tag_list = []

    for tag_id in tag_ids:
        tag_list.append(get_item_by_key_and_value(tags, tag_id))

    return f'''<h3>Ваше видео:</h3>
<b>Название:</b> {video_item['title']}<br>
<b>Теги:</b> {list_to_str(tag_list, ROUTE_TAGS, link_key='title')}<br>
<b>Видео:</b> <a href="{video_item['videoid']}" target=”_blank”>{video_item['videoid']}</a>
'''


def render_playlist_page(id):
    playlist = get_item_by_key_and_value(playlists, id)
    playlist_str = f'''<h3>Плейлист "{playlist['title']}":</h3>'''
    videos_by_playlists = []
    items = ''

    for video_id in playlist['videos']:
        video_by_id = get_item_by_key_and_value(videos, video_id)
        videos_by_playlists.append(video_by_id)

    for video in videos_by_playlists:
        items += f'''<li>{video['title']}<br><a href="{video['videoid']}" target=”_blank”>{video['videoid']}</a></li>'''

    return playlist_str + f'<ol>{items}</ol><br>Приятного просмотра!'


def render_tag_page(tag):
    tag_item = get_item_by_key_and_value(tags, tag, key='title')
    tag_id = tag_item['id']
    videos_by_tag = []
    items = ''

    for video in videos:
        video_tags = video['tags']
        if tag_id in video_tags:
            videos_by_tag.append(video)

    for v_item in videos_by_tag:
        items += f'''<li>{v_item['title']}<br><a href="{v_item['videoid']}" target=”_blank”>
{v_item['videoid']}</a></li>'''

    return f'<h3>У нас есть {len(videos_by_tag)} видео по тэгу "{tag}":</h3><ol>{items}</ol><br>Приятного просмотра!'


# pages---------------------------------
@app.route(ROUTE_MAIN)
def main_page():
    return render_main_page()

@app.route(ROUTE_ABOUT)
def about_page():
    return back_link + MESSAGE_ABOUT_APP


@app.route(ROUTE_VIDEOS)
def videos_page():
    return back_link + f'<h3>У нас есть следующие видео:</h3>{create_order_list_by(videos, ROUTE_VIDEOS)}'


@app.route(ROUTE_VIDEO)
def video_page(id):
    return back_link + render_video_page(id)


@app.route(ROUTE_PLAYLISTS)
def playlists_page():
    return back_link + f'<h3>Выберите что-нибудь среди плейлистов:</h3>' \
                       f'{create_order_list_by(playlists, ROUTE_PLAYLISTS, get_link_text=get_playlist_link_text)}'


@app.route(ROUTE_PLAYLIST)
def playlist_page(id):
    return back_link + render_playlist_page(id)


@app.route(ROUTE_TAGS)
def tags_page():
    return back_link + f'''<h3>Мы собрали видео по тэгам:</h3>
{create_order_list_by(tags, ROUTE_TAGS, link_key='title')}'''


@app.route(ROUTE_TAG)
def tag_page(tag):
    return back_link + render_tag_page(tag)


@app.errorhandler(404)
def page_not_found(error):
    return MESSAGE_PAGE_NOT_FOUND


app.run('', 8000)