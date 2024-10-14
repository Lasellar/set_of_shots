# Models' Fields
## Tag
- **id**(required) - Primary Key
- **title** - String 
- **is_published** - Bool
- **background_color** - String
## Category
- **id** - Primary Key
- **title** - String
- **slug** - SlugField|String
- **is_published** - Bool
## Underground
- **id** - Primary Key
- **title** - String
- **image** - ImageField|String(url)
- **is_published** - Bool
## AttachmentImage
- **id** - Primary Key
- **image** - ImageField|String(url)
- **bar** - ForeignKey[Bar]
- **is_published** - Bool
## Event
- **id** - Primary Key
- **title** - String
- **description** - String
- **slug** - SlugField|String
- **start** - DateTimeField
- **duration** - IntegerField
- **place** - ForeignKey[Bar]
- **is_published** - Bool
- **image** - ImageField|String(url)
## Post
- **id** - Primary Key
- **title** - String
- **slug** - SlugField|String
- **text**- String
- **bar** - ForeignKey[Bar]
- **is_published** - Bool
- **pub_datetime** - DateTimeField
- **image** - ImageField|String(url)
## Dish
- **id** - Primary Key
- **title** - String
- **slug** - SlugField|String
- **category** - ForeignKey[Category]
- **description** - String
- **tags** - ManyToManyField[Tag]
- **price** - Integer
- **promille** - Integer
- **bar** - ForeignKey[Bar]
- **image** - ImageField|String(url)
- **is_published** - Bool
## Bar
- **id** - Primary Key
- **title** - String
- **slug** - SlugField|String
- **description** - String
- **address** - String
- **work_time_monday** - String
- **work_time_tuesday** - String
- **work_time_wednesday** - String
- **work_time_thursday** - String
- **work_time_friday** - String
- **work_time_saturday** - String
- **work_time_sunday** - String
- **telegram_link** - String
- **instagram_link** - String
- **yandex_maps_link** - String
- **image** - ImageField|String(url)
- **underground** - ManyToManyField[Underground]
- **is_published** - Bool


# Endpoints
### GET  '/', feeds
**Response:** list of Post objects
```
[
	{
	"id":  2,
	"bar":  {
		"id":  3,
		"title":  "Лампопо",
		"underground":  [],
		"attachment_images":  [],
		"slug":  "lampopo",
		"description":  "Кино и видеигры в уютном подвале, как сходить в компы, только еще и выпить можно!",
		"address":  "Рождественский бул., 22/23",
		"work_time_monday":  null,
		"work_time_tuesday":  null,
		"work_time_wednesday":  null,
		"work_time_thursday":  null,
		"work_time_friday":  null,
		"work_time_saturday":  null,
		"work_time_sunday":  null,
		"telegram_link":  null,
		"instagram_link":  null,
		"yandex_maps_link":  null,
		"image":  "/media/bars_images/%D0%BB%D0%B0%D0%BC%D0%BF%D0%BE%D0%BF%D0%BE.png",
		"is_published":  true
	},
	"pub_datetime":  "2024-10-08T02:27:05+03:00",
	"title":  "→ курилка Рюмочной.",
	"slug":  "kurilka-ryumochnoj",
	"text":  "В Лампопо нагрянет группа с тёмн",
	"is_published":  true,
	"image":  "/media/posts_images/1.jpg"
	}
]
```
### GET  'feeds/<post_slug>/', feed
**Response:** Post object
```
{
	"id":  2,
	"bar":  {
		"id":  3,
		"title":  "Лампопо",
		"underground":  [],
		"attachment_images":  [],
		"slug":  "lampopo",
		"description":  "Кино и видеигры в уютном подвале, как сходить в компы, только еще и выпить можно!",
		"address":  "Рождественский бул., 22/23",
		"work_time_monday":  null,
		"work_time_tuesday":  null,
		"work_time_wednesday":  null,
		"work_time_thursday":  null,
		"work_time_friday":  null,
		"work_time_saturday":  null,
		"work_time_sunday":  null,
		"telegram_link":  null,
		"instagram_link":  null,
		"yandex_maps_link":  null,
		"image":  "/media/bars_images/%D0%BB%D0%B0%D0%BC%D0%BF%D0%BE%D0%BF%D0%BE.png",
		"is_published":  true
	},
	"pub_datetime":  "2024-10-08T02:27:05+03:00",
	"title":  "→ курилка Рюмочной.",
	"slug":  "kurilka-ryumochnoj",
	"text":  "В Лампопо нагрянет группа с тёмным прошлым Deli kate. (https://www.instagram.com/p/DAXxI67iVRz/?igsh=YnZucWprZXB4NHFu) Песни о существах, живущих среди нас и внутри нас, в акустическом формате с 20:00. В Южной уже гудит вечериночная Zero Disco (https://www.instagram.com/p/DAYYMDlCin6/?igsh=MXIyd2JhcHc3NjExdQ==) машина. Хлёсткая электроника и старый добрый хаус в 21:00. В Клубе дружеское новообразование в лице трёх коллективов представит шумную, нестабильную и местами дискомфортную программу. Deep Fried Frenz (https://www.instagram.com/p/DATnp6_CxXx/?igsh=bXRyMHBpdXFhb3po) в 19:00, а в 22:30 намечается внеочередной пятничный шоукейс от команды Track ID pls! (https://www.instagram.com/p/DATnp6_CxXx/?igsh=bXRyMHBpdXFhb3po)",
	"is_published":  true,
	"image":  "/media/posts_images/1.jpg"
}
```
### GET  'events/', events
**Response:** List of Event objects
```
[
	{
		"id":  2,
		"place":  {
			"title":  "Клуб \"Клуб\"",
			"slug":  "klub-klub"
		},
		"formatted_start":  "28.09.2024 00:00",
		"status":  "Закончилось",
		"title":  "«Я исповедуюсь» — история зла, ставшая историей жизни.",
		"description":  "Вишнёвый сад (https://www.instagram.com/p/DAWJL7KiY4A/?igsh=MXJ4emdpcngxNXpwdw==) вместе с Книжным Кубом уже во второй раз зовёт всех желающих на литературный вечер, где мы обсудим, похвалим, а, быть может, даже поругаем произведение ещё одного выдающегося писателя. На этот раз будем разбирать интеллектуальный роман Жауме Кабре, выяснять, кто такой автор и нарратор, говорить об особенностях нелинейной прозы и поднимать ряд философских вопросов. Для участия тыкайте сюда (http://knizhnykub.tilda.ws/reg) 29.09 16:00 18+",
		"slug":  "ya-ispoveduyus-istoriya-zla-stavshaya-istoriej-zhizni",
		"start":  "2024-09-28T03:00:00+03:00",
		"duration":  null,
		"is_published":  true,
		"image":  null
	},
	{
		"id":  3,
		"place":  {
			"title":  "Клуб \"Клуб\"",
			"slug":  "klub-klub"
		},
		"formatted_start":  "28.09.2024 00:00",
		"status":  "Закончилось",
		"title":  "28 сентября отмечается день пивопития. Комментарии, сами понимаете, излишни:",
		"description":  "В Лампопо параллельно в разных залах произойдут сразу два обытия: акустический <a href=\"https://www.instagram.com/p/DAbH8k5iZet/?igsh=MTgzNHVvd2NxMGVzaA==\">концерт авлы ылвоа</a> и турнир по кикеру. (https://t.me/setrumochnyh/5362) В 20:00! В Южной нагрянут до неприличного концептуальные ребятки из объединения Concept 9 (https://www.instagram.com/p/DAYYMDlCin6/?igsh=ZG03ZHRlZnRscWlw) в 21:00. В Клубе состоится презентация эксплейнера по современной философии от Максимилиана Неаполитанского. В чём истина? (https://www.instagram.com/p/DATnp6_CxXx/?igsh=bXRyMHBpdXFhb3po) в 16:00, а сразу после (в 20:00) сцену оккупируют Ублюдки (https://www.instagram.com/p/DATnp6_CxXx/?igsh=bXRyMHBpdXFhb3po) и Псарня. (https://www.instagram.com/p/DATnp6_CxXx/?igsh=bXRyMHBpdXFhb3po) В Барку ближе к вечеру завезут караоке. (https://www.instagram.com/p/DATdvXbioTf/?igsh=MW5qYWY0bWRhOXduNw==) Заходите, если не успели в августе (или если было мало), в 20:00.",
		"slug":  "2-sentyabrya-otmechaetsya-den-pivopitiya-kommentarii-sami-ponimaete-izlishni",
		"start":  "2024-09-28T03:00:00+03:00",
		"duration":  null,
		"is_published":  true,
		"image":  "/media/events_images/4.jpg"
	}
]
```
### GET  'events/<event_slug>/', events
**Response:** List of Event objects
```
{
	"id":  2,
	"place":  {
		"title":  "Клуб \"Клуб\"",
		"slug":  "klub-klub"
	},
	"formatted_start":  "28.09.2024 00:00",
	"status":  "Закончилось",
	"title":  "«Я исповедуюсь» — история зла, ставшая историей жизни.",
	"description":  "Вишнёвый сад (http",
	"slug":  "ya-ispoveduyus-istoriya-zla-stavshaya-istoriej-zhizni",
	"start":  "2024-09-28T03:00:00+03:00",
	"duration":  null,
	"is_published":  true,
	"image":  null
}
```
### GET  'bars/', bars
**Response:** List of Bar objects
```
[
	{
	"id":  2,
	"title":  "Зинзивер",
	"underground":  [
		{
			"title":  "Новокузнецкая"
		},
		{
			"title":  "Китай-город"
		},
		{
			"title":  "Чистые пруды"
		}
	],
	"attachment_images":  [
		{
			"image":  "/media/attachment_images/297000_screenshots_2015-10-31_00001_L47tv90.jpg"
		}
	],
	"slug":  "zinziver",
	"description":  "Бар «Зинзивер» — это место, где можно встретить за одним столиком коммуниста, краснодипломника истфака МГУ, девушку с «Онлифанс» и представителя бомонда. Здесь часто играет приятная андерграундная музыка, которую мало кто знает.\r\nБар «Зинзивер» — это место, где можно встретить за одним столиком коммуниста, краснодипломника истфака МГУ, девушку с «Онлифанс» и представителя бомонда. Здесь часто играет приятная андерграундная музыка, которую мало кто знает.\r\nБар «Зинзивер» — это место, где можно встретить за одним столиком коммуниста, краснодипломника истфака МГУ, девушку с «Онлифанс» и представителя бомонда. Здесь часто играет приятная андерграундная музыка, которую мало кто знает.\r\nБар «Зинзивер» — это место, где можно встретить за одним столиком коммуниста, краснодипломника истфака МГУ, девушку с «Онлифанс» и представителя бомонда. Здесь часто играет приятная андерграундная музыка, которую мало кто знает.",
	"address":  "покровский бульвар 2/14",
	"work_time_monday":  "16:00–04:30",
	"work_time_tuesday":  "16:00–04:30",
	"work_time_wednesday":  "16:00–04:30",
	"work_time_thursday":  "16:00–04:30",
	"work_time_friday":  "16:00–04:30",
	"work_time_saturday":  "14:00–04:30",
	"work_time_sunday":  "14:00–04:30",
	"telegram_link":  "https://t.me/zinzimem",
	"instagram_link":  null,
	"yandex_maps_link":  "<div style=\"position:relative;overflow:hidden;\"><a href=\"https://yandex.ru/maps/org/zinziver/27339938644/?utm_medium=mapframe&utm_source=maps\" style=\"color:#eee;font-size:12px;position:absolute;top:0px;\">Зинзивер</a><a href=\"https://yandex.ru/maps/213/moscow/category/bar_pub/184106384/?utm_medium=mapframe&utm_source=maps\" style=\"color:#eee;font-size:12px;position:absolute;top:14px;\">Бар, паб в Москве</a><a href=\"https://yandex.ru/maps/213/moscow/category/soft_drinks_bar/87599323630/?utm_medium=mapframe&utm_source=maps\" style=\"color:#eee;font-size:12px;position:absolute;top:28px;\">Безалкогольный бар в Москве</a><iframe src=\"https://yandex.ru/map-widget/v1/?ll=37.645529%2C55.758817&mode=search&oid=27339938644&ol=biz&z=16.34\" width=\"560\" height=\"400\" frameborder=\"1\" allowfullscreen=\"true\" style=\"position:relative;\"></iframe></div>",
	"image":  "/media/bars_images/zin.jpg",
	"is_published":  true
	},
	{
		"id":  4,
		"title":  "Ладья",
		"underground":  [],
		"attachment_images":  [],
		"slug":  "ladya",
		"description":  "Бар «Ладья» — это место, где каждый найдет что-то свое. Здесь можно поиграть в шахматы, послушать молодежную музыку, почитать стихи или спеть песни собственного сочинения.",
		"address":  "Столешников пер., 6, стр. 1",
		"work_time_monday":  null,
		"work_time_tuesday":  null,
		"work_time_wednesday":  null,
		"work_time_thursday":  null,
		"work_time_friday":  null,
		"work_time_saturday":  null,
		"work_time_sunday":  null,
		"telegram_link":  null,
		"instagram_link":  null,
		"yandex_maps_link":  null,
		"image":  "/media/bars_images/%D0%9B%D0%B0%D0%B4%D1%8C%D1%8F.png",
		"is_published":  true
	}
]
```
### GET  'bars/<bar_slug>/', bar
**Response:** Bar object
```
{
	"id":  3,
	"title":  "Лампопо",
	"underground":  [],
	"attachment_images":  [],
	"slug":  "lampopo",
	"description":  "Кино и видеигры в уютном подвале, как сходить в компы, только еще и выпить можно!",
	"address":  "Рождественский бул., 22/23",
	"work_time_monday":  null,
	"work_time_tuesday":  null,
	"work_time_wednesday":  null,
	"work_time_thursday":  null,
	"work_time_friday":  null,
	"work_time_saturday":  null,
	"work_time_sunday":  null,
	"telegram_link":  null,
	"instagram_link":  null,
	"yandex_maps_link":  null,
	"image":  "/media/bars_images/%D0%BB%D0%B0%D0%BC%D0%BF%D0%BE%D0%BF%D0%BE.png",
	"is_published":  true
}
```
### GET  'menu/<bar_slug>/', menu
**Response:** Bar object
```
[
    {
	    "id":  1,
	    "category":  {
		    "title":  "Крепкий алкоголь"
		},
		"bar":  {
		    "title":  "Зинзивер",
			"slug":  "zinziver"
		},
		"tags":  [
			{
				"id":  1,
				"title":  "Крепко!",
				"background_color":  null
			},
			{
				"id":  2,
				"title":  "50 мл",
				"background_color":  null
			}
		],
		"title":  "Водка",
		"slug":  "vodka",
		"description":  "описание водкиописание водкиописание водкиописание водкиописание водкиописание водкиописание водки",
		"price":  150,
		"promille":  40,
		"image":  "/media/dishes_images/vodka.jpg",
		"is_published":  false
	},
	{
		"id":  2,
		"category":  {
			"title":  "Еда"
		},
		"bar":  {
			"title":  "Зинзивер",
			"slug":  "zinziver"
		},
		"tags":  [],
		"title":  "Бутерброд с куриным паштетом",
		"slug":  "buterbrod-s-kurinym-pashtetom",
		"description":  "Описание бутера Описание бутера Описание бутера Описание бутера Описание бутера",
		"price":  150,
		"promille":  null,
		"image":  "/media/dishes_images/%D0%91%D1%83%D1%82%D0%B5%D1%80_%D1%81_%D0%BF%D0%B0%D1%88%D1%82%D0%B5%D1%82%D0%BE%D0%BC.jpg",
		"is_published":  true
	},
]
```