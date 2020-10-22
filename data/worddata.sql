--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

--
-- Data for Name: adjectives; Type: TABLE DATA; Schema: public; Owner: machinetrans
--

COPY adjectives (name, runame, variety, gender, declension, wordcase, animate) FROM stdin;
green	зелёный	descriptive	feminine	зелёной	genitive	animate
good	хороший	short adjective	nueter	хорошо	nominative	inanimate
green	зелёный	descriptive	plural	зелёные	nominative	animate
good	хороший	descriptive	plural	хороших	prepositional	inanimate
green	зелёный	descriptive	plural	зелёных	prepositional	inanimate
green	зелёный	short adjective	plural	зелёны	nominative	inanimate
green	зелёный	descriptive	plural	зелёные	nominative	inanimate
good	хороший	descriptive	plural	хороших	prepositional	animate
green	зелёный	descriptive	plural	зелёных	prepositional	animate
green	зелёный	descriptive	feminine	зелёной	dative	animate
good	хороший	descriptive	feminine	хорошей	prepositional	animate
green	зелёный	descriptive	nueter	зелёном	prepositional	inanimate
good	хороший	descriptive	masculine	хорошему	dative	inanimate
good	хороший	descriptive	plural	хороших	accusative	animate
green	зелёный	descriptive	plural	зелёных	accusative	animate
good	хороший	descriptive	plural	хорошими	instrumental	inanimate
good	хороший	short adjective	plural	хороши	nominative	inanimate
good	хороший	descriptive	masculine	хорошего	genitive	animate
good	хороший	descriptive	masculine	хороший	nominative	inanimate
good	хороший	descriptive	plural	хорошие	nominative	inanimate
green	зелёный	descriptive	masculine	зелёный	accusative	inanimate
good	хороший	descriptive	masculine	хорошему	dative	animate
good	хороший	descriptive	masculine	хорошем	prepositional	inanimate
good	хороший	descriptive	feminine	хорошюю	accusative	animate
good	хороший	descriptive	nueter	хорошим	instrumental	inanimate
good	хороший	descriptive	masculine	хороший	nominative	animate
good	хороший	descriptive	plural	хорошие	nominative	animate
good	хороший	descriptive	feminine	хорошей	instrumental	animate
good	хороший	descriptive	plural	хорошими	instrumental	animate
good	хороший	descriptive	masculine	хорошего	genitive	inanimate
good	хороший	descriptive	feminine	хорошей	dative	animate
green	зелёный	descriptive	nueter	зелёному	dative	inanimate
green	зелёный	descriptive	masculine	зелёного	genitive	animate
green	зелёный	descriptive	plural	зелёным	dative	inanimate
greener	зелёный	comparative	masculine	зелёнее	nominative	inanimate
green	зелёный	descriptive	masculine	зелёным	instrumental	inanimate
good	хороший	short adjective	feminine	хороша	nominative	inanimate
green	зелёный	descriptive	masculine	зелёный	nominative	inanimate
good	хороший	descriptive	masculine	хороший	accusative	inanimate
green	зелёный	descriptive	masculine	зелёным	instrumental	animate
good	хороший	descriptive	plural	хорошие	accusative	inanimate
green	зелёный	descriptive	feminine	зелёную	accusative	animate
green	зелёный	short adjective	nueter	зелёно	nominative	inanimate
green	зелёный	descriptive	masculine	зелёного	genitive	inanimate
green	зелёный	descriptive	plural	зелёным	dative	animate
green	зелёный	descriptive	masculine	зелёный	nominative	animate
good	хороший	descriptive	nueter	хорошее	nominative	inanimate
green	зелёный	descriptive	plural	зелёными	instrumental	inanimate
green	зелёный	descriptive	masculine	зелёному	dative	animate
green	зелёный	descriptive	plural	зелёные	accusative	inanimate
green	зелёный	descriptive	feminine	зелёная	nominative	animate
good	хороший	descriptive	masculine	хорошим	instrumental	animate
good	хороший	descriptive	feminine	хорошяя	nominative	animate
good	хороший	descriptive	plural	хорошим	dative	animate
green	зелёный	descriptive	masculine	зелёном	prepositional	inanimate
good	хороший	descriptive	nueter	хорошему	dative	inanimate
green	зелёный	descriptive	nueter	зелёное	nominative	inanimate
green	зелёный	descriptive	plural	зелёными	instrumental	animate
good	хороший	descriptive	nueter	хорошего	genitive	inanimate
green	зелёный	descriptive	masculine	зелёному	dative	inanimate
good	хороший	descriptive	plural	хорошим	dative	inanimate
green	зелёный	descriptive	masculine	зелёном	prepositional	animate
good	хороший	descriptive	nueter	хорошем	prepositional	inanimate
good	хороший	descriptive	masculine	хорошим	instrumental	inanimate
green	зелёный	descriptive	masculine	зелёного	accusative	animate
green	зелёный	descriptive	feminine	зелёной	prepositional	animate
good	хороший	short adjective	masculine	хорош	nominative	inanimate
green	зелёный	descriptive	nueter	зелёным	instrumental	inanimate
good	хороший	descriptive	plural	хороших	genitive	inanimate
green	зелёный	descriptive	nueter	зелёное	accusative	inanimate
green	зелёный	descriptive	plural	зелёных	genitive	inanimate
better	хороший	comparative	masculine	лучше	nominative	inanimate
good	хороший	descriptive	masculine	хорошего	accusative	animate
green	зелёный	short adjective	feminine	зелёна	nominative	inanimate
good	хороший	descriptive	plural	хороших	genitive	animate
green	зелёный	descriptive	plural	зелёных	genitive	animate
green	зелёный	descriptive	feminine	зелёной	instrumental	animate
green	зелёный	descriptive	nueter	зелёного	genitive	inanimate
good	хороший	descriptive	masculine	хорошем	prepositional	animate
good	хороший	descriptive	nueter	хорошее	accusative	inanimate
good	хороший	descriptive	feminine	хорошей	genitive	animate
green	зелёный	short adjective	masculine	зелён	nominative	inanimate
\.


--
-- Data for Name: adverbs; Type: TABLE DATA; Schema: public; Owner: machinetrans
--

COPY adverbs (name, runame, variety) FROM stdin;
to the right	направо	place
in Russian	по-русски	manner
badly	плохо	manner
interesting	интересно	manner
a little	немного	degree
need	надо	manner
incorrect	неправильно	manner
yet	ещё	degree
seldom	редко	manner
in Spanish	по-испански	manner
in the middle	посередине	place
no	нет	other
to the left	налево	place
here	тут	place
not bad	неплохо	manner
there	вон	place
in Italian	по-итальянски	manner
in English	по-английски	manner
completely	совсем	degree
directly	прямо	manner
correct	правильно	manner
at home	дома	place
possibly	можно	manner
bad	плохо	manner
pleasantly	приятно	manner
of course	конечно	other
understood	понятно	manner
in French	по-французски	manner
well	хорошо	manner
now	сейчас	time
in German	по-немецки	manner
in Japanese	по-японски	manner
sure	как же	other
\.


--
-- Data for Name: conjunctions; Type: TABLE DATA; Schema: public; Owner: machinetrans
--

COPY conjunctions (name, runame, variety) FROM stdin;
and	а	coordinating
also	тоже	coordinating
while	пока	subordinating
but	но	subordinating
yet	ещё	subordinating
and	и	coordinating
by the way	между прочим	coordinating
so	так	coordinating
then	потом	coordinating
therefore	поэтому	subordinating
only	только	subordinating
\.


--
-- Data for Name: interjections; Type: TABLE DATA; Schema: public; Owner: machinetrans
--

COPY interjections (name, runame) FROM stdin;
well	ну
please	пожалуйста
of course	конечно
there	вот
yes	да
let's go	пойдёмте
oh	ах
hello	привет
thank you	спасибо
\.


--
-- Data for Name: interrogatives; Type: TABLE DATA; Schema: public; Owner: machinetrans
--

COPY interrogatives (name, runame, variety) FROM stdin;
why	почему	method
where	где	place
where	куда	place
\.


--
-- Data for Name: invariants; Type: TABLE DATA; Schema: public; Owner: machinetrans
--

COPY invariants (name, runame, wordcase, variety) FROM stdin;
movie theater	кино	none	foreign
office	бюро	none	foreign
Tokyo	Токио	none	foreign
MF	МФ	none	acronym
Helsinki	Хельсинки	none	foreign
San Francisco	Сан-Франциско	none	foreign
Tbilisi	Тбилиси	none	foreign
Baku	Баку	none	foreign
NEP	НЕП	none	acronym
RSFSR	РСФСР	none	acronym
should	бы	none	subjunctive
USA	США	none	acronym
\.


--
-- Data for Name: nouns; Type: TABLE DATA; Schema: public; Owner: machinetrans
--

COPY nouns (name, runame, variety, gender, type, declension, wordcase, animate) FROM stdin;
door	дверь	concrete	masculine	thing	дверём	instrumental	inanimate
trip	поездка	abstract	feminine	thing	поездку	accusative	inanimate
engineers	инженер	concrete	plural	thing	инженеров	genitive	animate
Los Angeles	Лос-Анжелес	proper	masculine	location	Лос-Анжелесе	prepositional	inanimate
letter	письмо	concrete	nueter	thing	письмо	accusative	inanimate
professor	профессор	concrete	masculine	thing	профессор	nominative	animate
Chitas	Чита	proper	plural	location	Читами	instrumental	inanimate
Volgas	Волга	proper	plural	location	Волги	nominative	inanimate
Dnepropetrovsk	Днепропетровск	proper	masculine	location	Днепропетровск	nominative	inanimate
answer	ответ	abstract	masculine	thing	ответу	dative	inanimate
students	студент	concrete	plural	thing	студентах	prepositional	animate
meeting	собрание	abstract	nueter	thing	собранию	dative	inanimate
notebook	блокнот	concrete	masculine	thing	блокнот	nominative	inanimate
glasses	очки	concrete	plural	thing	очкей	genitive	inanimate
professions	профессия	abstract	plural	thing	профессиях	prepositional	inanimate
notebooks	блокнот	concrete	plural	thing	блокнотам	dative	inanimate
descent	съезд	concrete	masculine	location	съездом	instrumental	inanimate
money	деньги	collective	plural	thing	деньгах	prepositional	inanimate
Irtyshes	Иртыш	proper	plural	location	Иртышами	instrumental	inanimate
America	Америка	proper	feminine	location	Америке	dative	inanimate
notebook	блокнот	concrete	masculine	thing	блокнот	accusative	inanimate
guests	гость	concrete	plural	thing	гостям	dative	animate
Dnepropetrovsk	Днепропетровск	proper	masculine	location	Днепропетровск	accusative	inanimate
Volgas	Волга	proper	plural	location	Волги	accusative	inanimate
America	Америка	proper	feminine	location	Америки	genitive	inanimate
letter	письмо	concrete	nueter	thing	письмо	nominative	inanimate
Los Angeles	Лос-Анжелес	proper	masculine	location	Лос-Анжелесу	dative	inanimate
New Yorks	Нью-Йорк	proper	plural	location	Нью-Йоркей	genitive	inanimate
student	студент	concrete	masculine	thing	студента	genitive	animate
Zagorsk	Загорск	proper	masculine	location	Загорском	instrumental	inanimate
old man	серый	proper	masculine	thing	серого	accusative	animate
pupils	ученик	concrete	plural	thing	ученикей	accusative	animate
lessons	урок	concrete	plural	thing	уроки	nominative	inanimate
zero	нуль	abstract	masculine	thing	нулём	instrumental	inanimate
Rigas	Рига	proper	plural	location	Риги	accusative	inanimate
teas	чай	collective	plural	thing	чаи	accusative	inanimate
Tanya	Таня	proper	feminine	thing	Таной	instrumental	animate
Stockholms	Стокгольм	proper	plural	location	Стокгольмами	instrumental	inanimate
dictation	диктант	concrete	masculine	thing	диктанте	prepositional	inanimate
Dnepropetrovsks	Днепропетровск	proper	plural	location	Днепропетровскам	dative	inanimate
teacher	преподавательница	concrete	feminine	thing	преподавательницу	accusative	animate
Philadelphias	Филадельфия	proper	plural	location	Филадельфиям	dative	inanimate
teas	чай	collective	plural	thing	чаями	instrumental	inanimate
artist	артист	concrete	masculine	thing	артистом	instrumental	animate
mother	мать	concrete	feminine	thing	матери	dative	animate
letter	письмо	concrete	nueter	thing	письма	genitive	inanimate
Elbrus	Эльбрус	proper	plural	location	Эльбрусами	instrumental	inanimate
paper	бумага	concrete	feminine	thing	бумаге	prepositional	inanimate
papers	бумага	concrete	plural	thing	бумаг	genitive	inanimate
teas	чай	collective	plural	thing	чаи	nominative	inanimate
work	работа	abstract	feminine	thing	работу	accusative	inanimate
teachers	преподавательница	concrete	plural	thing	преподавательницах	prepositional	animate
Rigas	Рига	proper	plural	location	Риги	nominative	inanimate
city	города	concrete	feminine	location	городы	genitive	inanimate
papers	бумага	concrete	plural	thing	бумагами	instrumental	inanimate
blackboard	доска	concrete	feminine	thing	доску	accusative	inanimate
lessons	урок	concrete	plural	thing	уроки	accusative	inanimate
teacher	преподаватель	concrete	masculine	thing	преподавателя	genitive	animate
nine	девять	abstract	plural	thing	девяти	dative	inanimate
pupil	ученик	concrete	masculine	thing	ученике	prepositional	animate
building	здание	concrete	nueter	thing	здание	nominative	inanimate
people	человек	concrete	plural	thing	человеках	prepositional	animate
foreigner	иностранка	concrete	feminine	location	иностранки	genitive	animate
American	американец	concrete	masculine	thing	американца	genitive	animate
professor	профессор	concrete	masculine	thing	профессора	accusative	animate
pens	перо	concrete	plural	thing	пера	accusative	inanimate
question	вопрос	concrete	masculine	thing	вопросу	dative	inanimate
Ural	Урал	proper	masculine	location	Урал	nominative	inanimate
Moscows	Москва	proper	plural	location	Москвы	accusative	inanimate
countryside	деревня	concrete	feminine	location	деревню	accusative	inanimate
Los Angeles	Лос-Анжелес	proper	plural	location	Лос-Анжелесам	dative	inanimate
field	поле	concrete	nueter	location	поле	nominative	inanimate
Caucuses	Кавказ	proper	masculine	location	Кавказу	dative	inanimate
engineer	инженер	concrete	masculine	thing	инженер	nominative	animate
artists	артист	concrete	plural	thing	артистами	instrumental	animate
professor	профессор	concrete	masculine	thing	профессором	instrumental	animate
work	занятие	concrete	nueter	thing	занятием	instrumental	inanimate
joys	рад	abstract	plural	thing	радах	prepositional	inanimate
Russian	русский	proper	masculine	thing	русскому	dative	animate
Volga	Волга	proper	feminine	location	Волге	dative	inanimate
field	поле	concrete	nueter	location	поле	accusative	inanimate
Altai	Алтай	proper	masculine	location	Алтаем	instrumental	inanimate
pockets	карман	concrete	plural	location	карманам	dative	inanimate
Ulyanovsks	Уляновск	proper	plural	location	Уляновскам	dative	inanimate
school desk	парта	concrete	feminine	thing	парте	prepositional	inanimate
Moscows	Москва	proper	plural	location	Москвы	nominative	inanimate
Minneapolis	Миннеаполис	proper	masculine	location	Миннеаполиса	genitive	inanimate
Ural	Урал	proper	masculine	location	Урал	accusative	inanimate
pens	перо	concrete	plural	thing	пера	nominative	inanimate
book	книга	concrete	feminine	thing	книге	prepositional	inanimate
Moscows	Москва	proper	plural	location	Москв	genitive	inanimate
lessons	урок	concrete	plural	thing	уроках	prepositional	inanimate
work	работа	abstract	feminine	thing	работы	genitive	inanimate
foreigners	иностранец	concrete	plural	thing	иностранцов	genitive	animate
Magnitogorsk	Магнитогорск	proper	masculine	location	Магнитогорску	dative	inanimate
building	здание	concrete	nueter	thing	здание	accusative	inanimate
Yakutsks	Якутск	proper	plural	location	Якутскей	genitive	inanimate
rags	тряпка	concrete	plural	thing	тряпками	instrumental	inanimate
Russian	русская	proper	feminine	thing	русской	prepositional	animate
nationalities	национальность	abstract	plural	thing	национальности	accusative	inanimate
windows	окно	concrete	plural	thing	окнам	dative	inanimate
works	работа	abstract	plural	thing	работами	instrumental	inanimate
equators	экватор	concrete	plural	thing	экваторы	nominative	inanimate
answers	ответ	abstract	plural	thing	ответах	prepositional	inanimate
chalks	мел	concrete	plural	thing	мелы	accusative	inanimate
museum	музей	concrete	masculine	location	музею	dative	inanimate
one	одна	abstract	feminine	thing	одна	nominative	animate
Gvardyesk	Гвардейск	proper	masculine	location	Гвардейску	dative	inanimate
Kharkhovs	Харьков	proper	plural	location	Харьковам	dative	inanimate
visits	свидание	abstract	plural	thing	свидания	accusative	inanimate
ones	один	abstract	plural	thing	одними	instrumental	inanimate
cities	города	concrete	plural	location	городам	dative	inanimate
Irtyshes	Иртыш	proper	plural	location	Иртышей	genitive	inanimate
laboratories	лаборатория	concrete	plural	location	лабораториям	dative	inanimate
Vladivostoks	Владивосток	proper	plural	location	Владивостоки	nominative	inanimate
accent	акцент	concrete	masculine	thing	акценте	prepositional	inanimate
lesson	урок	concrete	masculine	thing	уроке	prepositional	inanimate
zero	нуль	abstract	masculine	thing	нуля	genitive	inanimate
father	отец	concrete	masculine	thing	отца	accusative	animate
briefcase	портфель	concrete	masculine	thing	портфелём	instrumental	inanimate
train station	вокзал	concrete	masculine	location	вокзалу	dative	inanimate
Vladivostoks	Владивосток	proper	plural	location	Владивостоки	accusative	inanimate
mistake	ошибка	abstract	feminine	thing	ошибкой	instrumental	inanimate
Vladivostoks	Владивосток	proper	plural	location	Владивостокам	dative	inanimate
Ulyanovsks	Уляновск	proper	plural	location	Уляновсках	prepositional	inanimate
school	школа	concrete	feminine	thing	школы	genitive	inanimate
America	Америка	proper	feminine	location	Америке	prepositional	inanimate
Urals	Урал	proper	plural	location	Уралах	prepositional	inanimate
evenings	вечер	abstract	plural	thing	вечерами	instrumental	inanimate
continuations	продолжение	abstract	plural	thing	продолжений	genitive	inanimate
visits	свидание	abstract	plural	thing	свидания	nominative	inanimate
rooms	комната	concrete	plural	thing	комнатам	dative	inanimate
ones	одно	abstract	plural	thing	одних	prepositional	inanimate
dining hall	столовая	concrete	feminine	location	столовая	nominative	inanimate
earths	земля	concrete	plural	thing	землях	prepositional	inanimate
accents	акцент	concrete	plural	thing	акценты	accusative	inanimate
equators	экватор	concrete	plural	thing	экваторы	accusative	inanimate
day	день	concrete	masculine	thing	дня	genitive	inanimate
chalks	мел	concrete	plural	thing	мелы	nominative	inanimate
Baikals	Байкал	proper	plural	location	Байкалами	instrumental	inanimate
Dnepropetrovsks	Днепропетровск	proper	plural	location	Днепропетровски	nominative	inanimate
number	номер	concrete	masculine	thing	номером	instrumental	inanimate
teacher	преподаватель	concrete	masculine	thing	преподавателе	prepositional	animate
Gvardyesks	Гвардейск	proper	plural	location	Гвардейски	nominative	inanimate
meat	мясо	collective	nueter	thing	мясо	accusative	inanimate
Paris	Париж	proper	masculine	location	Париж	accusative	inanimate
nationalities	национальность	abstract	plural	thing	национальности	nominative	inanimate
tardiness	опоздание	abstract	nueter	thing	опоздании	prepositional	inanimate
evenings	вечер	abstract	plural	thing	вечеры	nominative	inanimate
nationalities	национальность	abstract	plural	thing	национальностями	instrumental	inanimate
atom	атом	concrete	masculine	thing	атому	dative	inanimate
work	работа	abstract	feminine	thing	работой	instrumental	inanimate
father	отец	concrete	masculine	thing	отца	genitive	animate
Caucuses	Кавказ	proper	plural	location	Кавказах	prepositional	inanimate
equators	экватор	concrete	plural	thing	экваторов	genitive	inanimate
assignment	задание	abstract	nueter	thing	заданиии	prepositional	inanimate
Elbrus	Эльбрус	proper	plural	location	Эльбрусам	dative	inanimate
Urals	Урал	proper	plural	location	Уралы	accusative	inanimate
Caucuses	Кавказ	proper	masculine	location	Кавказе	prepositional	inanimate
Tanyas	Таня	proper	plural	thing	Таней	genitive	animate
Yakutsks	Якутск	proper	plural	location	Якутсках	prepositional	inanimate
nonsense	ерунда	abstract	feminine	thing	ерунде	prepositional	inanimate
equator	экватор	concrete	masculine	thing	экватора	genitive	inanimate
Russian	русская	proper	feminine	thing	русской	genitive	animate
dictionary	словарь	concrete	masculine	thing	словарём	instrumental	inanimate
dining hall	столовая	concrete	feminine	location	столовой	instrumental	inanimate
cities	города	concrete	plural	location	городы	nominative	inanimate
lecture	лекция	abstract	feminine	thing	лекцией	instrumental	inanimate
Pavlovs	Павлов	proper	plural	thing	Павловам	dative	inanimate
ones	один	abstract	plural	thing	одних	accusative	animate
mister	господин	concrete	masculine	thing	господину	dative	animate
friends	друг	concrete	plural	thing	друзей	accusative	animate
artists	артист	concrete	plural	thing	артистах	prepositional	animate
Watsonvilles	Ватсонвиль	proper	plural	location	Ватсонвили	nominative	inanimate
number	номер	concrete	masculine	thing	номеру	dative	inanimate
train station	вокзал	concrete	masculine	location	вокзал	nominative	inanimate
notebook	блокнот	concrete	masculine	thing	блокноте	prepositional	inanimate
exam	экзамен	concrete	masculine	thing	экзамена	genitive	inanimate
one	один	abstract	masculine	thing	одним	instrumental	inanimate
dining halls	столовая	concrete	plural	location	столовые	accusative	inanimate
friends	друг	concrete	plural	thing	друзей	genitive	animate
teacher	преподаватель	concrete	masculine	thing	преподавателю	dative	animate
Dneprs	Днепр	proper	plural	location	Днепров	genitive	inanimate
Moscow	Москва	proper	feminine	location	Москве	dative	inanimate
Russians	русский	proper	plural	thing	русские	nominative	animate
Leningrads	Ленинград	proper	plural	location	Ленинграды	nominative	inanimate
Magnitogorsks	Магнитогорск	proper	plural	location	Магнитогорсках	prepositional	inanimate
Russians	русские	concrete	plural	thing	русскими	instrumental	animate
sponges	губка	concrete	plural	thing	губки	nominative	inanimate
Tanyas	Таня	proper	plural	thing	Таней	accusative	animate
time	раз	abstract	masculine	thing	разу	dative	inanimate
Romes	Рим	proper	plural	location	Римах	prepositional	inanimate
lectures	лекция	abstract	plural	thing	лекциями	instrumental	inanimate
ones	одна	abstract	plural	thing	одним	dative	inanimate
materials	материал	concrete	plural	thing	материалов	genitive	inanimate
Yaltas	Ялта	proper	plural	location	Ялтам	dative	inanimate
answers	ответ	abstract	plural	thing	ответов	genitive	inanimate
sponges	губка	concrete	plural	thing	губки	accusative	inanimate
lessons	урок	concrete	plural	thing	урокам	dative	inanimate
affairs	дело	abstract	plural	thing	делам	dative	inanimate
Bolshoi	большой	proper	masculine	location	большому	dative	inanimate
Leningrads	Ленинград	proper	plural	location	Ленинграды	accusative	inanimate
notes	примечание	concrete	plural	thing	примечаниях	prepositional	inanimate
answer	ответ	abstract	masculine	thing	ответом	instrumental	inanimate
Yugoslavias	Югославия	proper	plural	location	Югославий	genitive	inanimate
dining halls	столовая	concrete	plural	location	столовые	nominative	inanimate
grandfather	дедушка	concrete	masculine	thing	дедушки	genitive	animate
one	один	abstract	masculine	thing	одим	instrumental	inanimate
dining hall	столовая	concrete	feminine	location	столовую	accusative	inanimate
ones	одно	abstract	plural	thing	одних	genitive	inanimate
Santa Cruzs	Санта-Крус	proper	plural	location	Санта-Крусах	prepositional	inanimate
train station	вокзал	concrete	masculine	location	вокзал	accusative	inanimate
Watsonvilles	Ватсонвиль	proper	plural	location	Ватсонвили	accusative	inanimate
Americans	американка	concrete	plural	thing	американки	nominative	animate
Berlin	Берлин	proper	masculine	location	Берлину	dative	inanimate
example	пример	abstract	masculine	thing	примером	instrumental	inanimate
time	раз	abstract	masculine	thing	раза	genitive	inanimate
cities	города	concrete	plural	location	городы	accusative	inanimate
centers	центр	concrete	plural	location	центрах	prepositional	inanimate
New York	Нью-Йорк	proper	masculine	location	Нью-Йорку	dative	inanimate
number	номер	concrete	masculine	thing	номере	prepositional	inanimate
teacher	учительница	concrete	feminine	thing	учительницы	genitive	animate
sponge	губка	concrete	feminine	thing	губку	accusative	inanimate
Urals	Урал	proper	plural	location	Уралы	nominative	inanimate
Caucuses	Кавказ	proper	plural	location	Кавказы	nominative	inanimate
missus	госпожа	concrete	feminine	thing	госпожи	genitive	animate
chairs	стул	concrete	plural	thing	стулам	dative	inanimate
Magnitogorsks	Магнитогорск	proper	plural	location	Магнитогорскей	genitive	inanimate
Boris	Борис	proper	masculine	thing	Бориса	genitive	animate
libraries	библиотека	concrete	plural	location	библиотек	genitive	inanimate
silks	шёлк	collective	plural	thing	шелках	prepositional	inanimate
Yaltas	Ялта	proper	plural	location	Ялты	accusative	inanimate
teachers	преподавательница	concrete	plural	thing	преподавательницами	instrumental	animate
window	окно	concrete	nueter	thing	окну	dative	inanimate
Kharkhovs	Харьков	proper	plural	location	Харьковах	prepositional	inanimate
Americas	Америка	proper	plural	location	Америкам	dative	inanimate
Volga	Волга	proper	feminine	location	Волга	nominative	inanimate
continuations	продолжение	abstract	plural	thing	продолжениях	prepositional	inanimate
nationality	национальность	abstract	feminine	thing	национальностью	instrumental	inanimate
teachers	преподаватель	concrete	plural	thing	преподавателей	accusative	animate
answers	ответ	abstract	plural	thing	ответами	instrumental	inanimate
descent	съезд	concrete	masculine	location	съезд	accusative	inanimate
meetings	собрание	abstract	plural	thing	собраний	genitive	inanimate
nationalities	национальность	abstract	plural	thing	национальностях	prepositional	inanimate
teachers	преподаватель	concrete	plural	thing	преподавателей	genitive	animate
nonsenses	ерунда	abstract	plural	thing	ерунды	nominative	inanimate
Vladivostok	Владивосток	proper	masculine	location	Владивостоке	prepositional	inanimate
man	мужчина	concrete	feminine	thing	мужчина	nominative	animate
equator	экватор	concrete	masculine	thing	экватор	nominative	inanimate
Sheboygan	Шебойган	proper	masculine	location	Шебойганом	instrumental	inanimate
affairs	дело	abstract	plural	thing	дела	nominative	inanimate
professions	профессия	abstract	plural	thing	профессий	genitive	inanimate
university	университет	concrete	masculine	location	университету	dative	inanimate
teacher	преподаватель	concrete	masculine	thing	преподаватель	nominative	animate
Vladivostok	Владивосток	proper	masculine	location	Владивостоку	dative	inanimate
first name	имя	abstract	nueter	thing	имени	dative	inanimate
libraries	библиотека	concrete	plural	location	библиотеки	nominative	inanimate
Boris	Борис	proper	masculine	thing	Бориса	accusative	animate
question	вопрос	concrete	masculine	thing	вопросе	prepositional	inanimate
one	одна	abstract	feminine	thing	одна	nominative	inanimate
surname	фамилия	concrete	feminine	thing	фамилии	prepositional	inanimate
ones	один	abstract	plural	thing	одних	prepositional	inanimate
Novgorod	Новгород	proper	masculine	location	Новгороде	prepositional	inanimate
Santa Cruzs	Санта-Крус	proper	plural	location	Санта-Крусы	nominative	inanimate
missus	госпожа	concrete	feminine	thing	госпоже	prepositional	animate
New Yorks	Нью-Йорк	proper	plural	location	Нью-Йоркам	dative	inanimate
teacher	учительница	concrete	feminine	thing	учительницу	accusative	animate
mister	господин	concrete	masculine	thing	господин	nominative	animate
Yugoslavia	Югославия	proper	feminine	location	Югославия	nominative	inanimate
Santa Cruzs	Санта-Крус	proper	plural	location	Санта-Крусы	accusative	inanimate
Californias	Калифория	proper	plural	location	Калифорий	genitive	inanimate
libraries	библиотека	concrete	plural	location	библиотеки	accusative	inanimate
assignments	задание	abstract	plural	thing	заданий	genitive	inanimate
Novgorod	Новгород	proper	masculine	location	Новгородом	instrumental	inanimate
nonsenses	ерунда	abstract	plural	thing	ерундами	instrumental	inanimate
ones	одно	abstract	plural	thing	одними	instrumental	inanimate
Urals	Урал	proper	plural	location	Уралам	dative	inanimate
guests	гость	concrete	plural	thing	гостях	prepositional	animate
zero	нуль	abstract	masculine	thing	нуле	prepositional	inanimate
equator	экватор	concrete	masculine	thing	экватор	accusative	inanimate
affairs	дело	abstract	plural	thing	дела	accusative	inanimate
classes	класс	concrete	plural	thing	классами	instrumental	inanimate
mother	мать	concrete	feminine	thing	матери	genitive	animate
nonsenses	ерунда	abstract	plural	thing	ерунды	accusative	inanimate
descent	съезд	concrete	masculine	location	съезд	nominative	inanimate
Philadelphias	Филадельфия	proper	plural	location	Филадельфий	genitive	inanimate
judge	судья	concrete	masculine	thing	судья	nominative	animate
uncle	дядя	concrete	masculine	thing	дяда	nominative	animate
Caucuses	Кавказ	proper	masculine	location	Кавказом	instrumental	inanimate
nonsense	ерунда	abstract	feminine	thing	ерунды	genitive	inanimate
mothers	мать	concrete	plural	thing	матерям	dative	animate
friend	друг	concrete	masculine	thing	другу	dative	animate
field	поле	concrete	nueter	location	поле	prepositional	inanimate
nine	девять	abstract	plural	thing	девяти	genitive	inanimate
class	класс	concrete	masculine	thing	класса	genitive	inanimate
Yaltas	Ялта	proper	plural	location	Ялты	nominative	inanimate
answers	ответ	abstract	plural	thing	ответам	dative	inanimate
foreigners	иностранка	concrete	plural	location	иностранки	nominative	animate
day	день	concrete	masculine	thing	днём	instrumental	inanimate
Philadelphia	Филадельфия	proper	feminine	location	Филадельфии	prepositional	inanimate
Caucuses	Кавказ	proper	plural	location	Кавказы	accusative	inanimate
assignments	задание	abstract	plural	thing	задания	nominative	inanimate
examples	пример	abstract	plural	thing	примеры	nominative	inanimate
reading	чтение	abstract	nueter	thing	чтениие	nominative	inanimate
Yugoslavia	Югославия	proper	feminine	location	Югославию	accusative	inanimate
visit	свидание	abstract	nueter	thing	свиданием	instrumental	inanimate
judges	судья	concrete	plural	thing	судьи	nominative	animate
blemishes	пятно	concrete	plural	thing	пятнах	prepositional	inanimate
response	отзыв	concrete	masculine	thing	отзыву	dative	inanimate
material	материал	concrete	masculine	thing	материале	prepositional	inanimate
seas	море	concrete	plural	location	морях	prepositional	inanimate
Santa Cruzs	Санта-Крус	proper	plural	location	Санта-Крусам	dative	inanimate
examples	пример	abstract	plural	thing	примерами	instrumental	inanimate
father	отец	concrete	masculine	thing	отце	prepositional	animate
Minneapolis	Миннеаполис	proper	plural	location	Миннеаполисы	nominative	inanimate
Gvardyesk	Гвардейск	proper	masculine	location	Гвардейске	prepositional	inanimate
numbers	номер	concrete	plural	thing	номерам	dative	inanimate
Philadelphias	Филадельфия	proper	plural	location	Филадельфиями	instrumental	inanimate
professors	профессор	concrete	plural	thing	профессоров	accusative	animate
examples	пример	abstract	plural	thing	примерах	prepositional	inanimate
professors	профессор	concrete	plural	thing	профессоров	genitive	animate
Ulyanovsks	Уляновск	proper	plural	location	Уляновски	accusative	inanimate
missus	госпожа	concrete	feminine	thing	госпоже	dative	animate
truth	правда	abstract	feminine	thing	правду	accusative	inanimate
houses	дом	concrete	plural	thing	домами	instrumental	inanimate
surname	фамилия	concrete	feminine	thing	фамилии	dative	inanimate
four	четыре	abstract	plural	thing	четырёх	genitive	inanimate
rag	тряпка	concrete	feminine	thing	тряпкой	instrumental	inanimate
New Yorks	Нью-Йорк	proper	plural	location	Нью-Йорки	accusative	inanimate
affairs	дело	abstract	plural	thing	делах	prepositional	inanimate
Pavlovs	Павлов	proper	plural	thing	Павловы	accusative	inanimate
first name	имя	abstract	nueter	thing	имени	prepositional	inanimate
Boris	Борис	proper	masculine	thing	Борисом	instrumental	animate
Geneva	Женева	proper	feminine	location	Женевой	instrumental	inanimate
Tanya	Таня	proper	feminine	thing	Таню	accusative	animate
museum	музей	concrete	masculine	location	музей	nominative	inanimate
Altais	Алтай	proper	plural	location	Алтаи	nominative	inanimate
Yalta	Ялта	proper	feminine	location	Ялту	accusative	inanimate
efforts	труд	abstract	plural	thing	трудам	dative	inanimate
Los Angeles	Лос-Анжелес	proper	plural	location	Лос-Анжелесами	instrumental	inanimate
table	стол	concrete	masculine	thing	стола	genitive	inanimate
dictionaries	словарь	concrete	plural	thing	словарях	prepositional	inanimate
table	стол	concrete	masculine	thing	столу	dative	inanimate
Altais	Алтай	proper	plural	location	Алтаи	accusative	inanimate
museum	музей	concrete	masculine	location	музей	accusative	inanimate
classes	класс	concrete	plural	thing	классах	prepositional	inanimate
joys	рад	abstract	plural	thing	радов	genitive	inanimate
foreigners	иностранец	concrete	plural	thing	иностранцами	instrumental	animate
student	студент	concrete	masculine	thing	студент	nominative	animate
time	пора	concrete	feminine	thing	пору	accusative	inanimate
cities	города	concrete	plural	location	город	genitive	inanimate
materials	материал	concrete	plural	thing	материалах	prepositional	inanimate
Pavlovs	Павлов	proper	plural	thing	Павловы	nominative	inanimate
New Yorks	Нью-Йорк	proper	plural	location	Нью-Йорки	nominative	inanimate
mistake	ошибка	abstract	feminine	thing	ошибки	genitive	inanimate
Russian	русский	proper	masculine	thing	русского	genitive	animate
patronymics	отчество	concrete	plural	thing	отчеств	genitive	inanimate
truth	правда	abstract	feminine	thing	правды	genitive	inanimate
row	ряд	concrete	masculine	thing	ряда	genitive	inanimate
Ulyanovsks	Уляновск	proper	plural	location	Уляновски	nominative	inanimate
Sheboygan	Шебойган	proper	masculine	location	Шебойгана	genitive	inanimate
Russian	русский	proper	masculine	thing	русского	accusative	animate
Shchorsk	Щорск	proper	masculine	location	Щорска	genitive	inanimate
Philadelphia	Филадельфия	proper	feminine	location	Филадельфии	dative	inanimate
Odessas	Одесса	proper	plural	location	Одессами	instrumental	inanimate
time	пора	concrete	feminine	thing	порой	instrumental	inanimate
Minneapolis	Миннеаполис	proper	plural	location	Миннеаполисы	accusative	inanimate
Irtyshes	Иртыш	proper	plural	location	Иртышах	prepositional	inanimate
assignments	задание	abstract	plural	thing	задания	accusative	inanimate
examples	пример	abstract	plural	thing	примеры	accusative	inanimate
reading	чтение	abstract	nueter	thing	чтениие	accusative	inanimate
aviators	авиатор	concrete	plural	thing	авиаторах	prepositional	animate
Sheboygans	Шебойган	proper	plural	location	Шебойганах	prepositional	inanimate
meats	мясо	collective	plural	thing	мясами	instrumental	inanimate
nonsense	ерунда	abstract	feminine	thing	ерунда	nominative	inanimate
sea	море	concrete	nueter	location	морем	instrumental	inanimate
assignments	задание	abstract	plural	thing	заданиям	dative	inanimate
students	студент	concrete	plural	thing	студентам	dative	animate
Moscows	Москва	proper	plural	location	Москвам	dative	inanimate
one	один	abstract	masculine	thing	одн	nominative	inanimate
nonsense	ерунда	abstract	feminine	thing	ерунде	dative	inanimate
seas	море	concrete	plural	location	моря	accusative	inanimate
one	один	abstract	masculine	thing	одного	genitive	inanimate
Arkhangelsks	Архангелск	proper	plural	location	Архангелскам	dative	inanimate
Odessa	Одесса	proper	feminine	location	Одессой	instrumental	inanimate
zero	нуль	abstract	masculine	thing	нуль	accusative	inanimate
museums	музей	concrete	plural	location	музеи	accusative	inanimate
nationalities	национальность	abstract	plural	thing	национальностей	genitive	inanimate
four	четыре	abstract	plural	thing	четыре	nominative	inanimate
Yenisei	Енисей	proper	masculine	location	Енисее	prepositional	inanimate
example	пример	abstract	masculine	thing	пример	accusative	inanimate
meeting	собрание	abstract	nueter	thing	собрание	nominative	inanimate
train station	вокзал	concrete	masculine	location	вокзалом	instrumental	inanimate
pocket	карман	concrete	masculine	location	карману	dative	inanimate
assignment	задание	abstract	nueter	thing	заданиие	nominative	inanimate
blemishes	пятно	concrete	plural	thing	пятна	accusative	inanimate
articles	статья	concrete	plural	thing	статьей	genitive	inanimate
earth	земля	concrete	feminine	thing	земля	nominative	inanimate
Zagorsk	Загорск	proper	masculine	location	Загорск	nominative	inanimate
Paris	Париж	proper	masculine	location	Парижом	instrumental	inanimate
friends	друг	concrete	plural	thing	друзьях	prepositional	animate
school desk	парта	concrete	plural	thing	партах	prepositional	inanimate
Londons	Лондон	proper	plural	location	Лондонам	dative	inanimate
school	школа	concrete	feminine	thing	школу	accusative	inanimate
notebooks	блокнот	concrete	plural	thing	блокнотах	prepositional	inanimate
Rome	Рим	proper	masculine	location	Римом	instrumental	inanimate
Moscow	Москва	proper	feminine	location	Москве	prepositional	inanimate
Altais	Алтай	proper	plural	location	Алтаев	genitive	inanimate
notebook	блокнот	concrete	masculine	thing	блокноту	dative	inanimate
Volga	Волга	proper	feminine	location	Волгу	accusative	inanimate
Dnepropetrovsk	Днепропетровск	proper	masculine	location	Днепропетровска	genitive	inanimate
chair	стул	concrete	masculine	thing	стул	accusative	inanimate
friend	друг	concrete	masculine	thing	друг	nominative	animate
joys	рад	abstract	plural	thing	радами	instrumental	inanimate
American	американец	concrete	masculine	thing	американцом	instrumental	animate
missus	госпожа	concrete	plural	thing	госпож	accusative	animate
chair	стул	concrete	masculine	thing	стул	nominative	inanimate
universities	университет	concrete	plural	location	университетами	instrumental	inanimate
Minneapolis	Миннеаполис	proper	plural	location	Миннеаполисах	prepositional	inanimate
meat	мясо	collective	nueter	thing	мяса	genitive	inanimate
assignment	задание	abstract	nueter	thing	заданиие	accusative	inanimate
libraries	библиотека	concrete	plural	location	библиотекам	dative	inanimate
blemishes	пятно	concrete	plural	thing	пятна	nominative	inanimate
Zagorsk	Загорск	proper	masculine	location	Загорск	accusative	inanimate
guest	гость	concrete	masculine	thing	госте	prepositional	animate
friend	друг	concrete	masculine	thing	друге	prepositional	animate
teas	чай	collective	plural	thing	чаях	prepositional	inanimate
meeting	собрание	abstract	nueter	thing	собрание	accusative	inanimate
notebooks	блокнот	concrete	plural	thing	блокнотами	instrumental	inanimate
example	пример	abstract	masculine	thing	пример	nominative	inanimate
museums	музей	concrete	plural	location	музеи	nominative	inanimate
Paris	Париж	proper	masculine	location	Париже	prepositional	inanimate
four	четыре	abstract	plural	thing	четыре	accusative	inanimate
zero	нуль	abstract	masculine	thing	нуль	nominative	inanimate
seas	море	concrete	plural	location	моря	nominative	inanimate
atom	атом	concrete	masculine	thing	атома	genitive	inanimate
cities	города	concrete	plural	location	городами	instrumental	inanimate
truth	правда	abstract	feminine	thing	правда	nominative	inanimate
times	раз	abstract	plural	thing	разами	instrumental	inanimate
Santa Cruzs	Санта-Крус	proper	plural	location	Санта-Крусов	genitive	inanimate
number	номер	concrete	masculine	thing	номера	genitive	inanimate
missus	госпожа	concrete	plural	thing	госпож	genitive	animate
flag	знамя	abstract	nueter	thing	знамени	prepositional	inanimate
house	дом	concrete	masculine	thing	дом	accusative	inanimate
school desk	парта	concrete	plural	thing	партами	instrumental	inanimate
teacher	учитель	concrete	masculine	thing	учителя	genitive	animate
article	статья	concrete	feminine	thing	статье	dative	inanimate
chalk	мел	concrete	masculine	thing	меле	prepositional	inanimate
accent	акцент	concrete	masculine	thing	акценту	dative	inanimate
notepads	тетрадь	concrete	plural	thing	тетради	accusative	inanimate
ballpoint pens	авторучка	concrete	plural	thing	авторучкам	dative	inanimate
nine	девять	abstract	plural	thing	девятью	instrumental	inanimate
dictations	диктант	concrete	plural	thing	диктантам	dative	inanimate
school desk	парта	concrete	plural	thing	парты	accusative	inanimate
money	деньги	collective	plural	thing	деньги	accusative	inanimate
day	день	concrete	masculine	thing	дню	dative	inanimate
Russians	русский	proper	plural	thing	русских	accusative	animate
city	города	concrete	feminine	location	городе	dative	inanimate
nights	ночь	abstract	plural	thing	ночей	genitive	inanimate
train stations	вокзал	concrete	plural	location	вокзалами	instrumental	inanimate
California	Калифория	proper	feminine	location	Калифориы	genitive	inanimate
grandfathers	дедушка	concrete	plural	thing	дедушках	prepositional	animate
theater	театр	concrete	masculine	location	театра	genitive	inanimate
Yenisei	Енисей	proper	masculine	location	Енисей	accusative	inanimate
briefcases	портфель	concrete	plural	thing	портфелей	genitive	inanimate
Russians	русский	proper	plural	thing	русских	genitive	animate
laboratory	лаборатория	concrete	feminine	location	лаборатория	nominative	inanimate
Novgorod	Новгород	proper	masculine	location	Новгорода	genitive	inanimate
teacher	учитель	concrete	masculine	thing	учителя	accusative	animate
one	одна	abstract	feminine	thing	одной	dative	inanimate
foreigner	иностранка	concrete	feminine	location	иностранка	nominative	animate
chair	стул	concrete	masculine	thing	стула	genitive	inanimate
missus	госпожа	concrete	feminine	thing	госпожой	instrumental	animate
answer	ответ	abstract	masculine	thing	ответа	genitive	inanimate
Paris	Париж	proper	plural	location	Парижами	instrumental	inanimate
teacher	преподавательница	concrete	feminine	thing	преподавательнице	prepositional	animate
letters	письмо	concrete	plural	thing	письма	nominative	inanimate
Urals	Урал	proper	plural	location	Уралами	instrumental	inanimate
old man	серый	proper	plural	thing	серых	prepositional	animate
Yugoslavia	Югославия	proper	feminine	location	Югославии	dative	inanimate
vodkas	водка	collective	plural	thing	водки	nominative	inanimate
blackboard	доска	concrete	feminine	thing	доски	genitive	inanimate
fathers	отец	concrete	plural	thing	отцах	prepositional	animate
Arkhangelsk	Архангелск	proper	masculine	location	Архангелске	prepositional	inanimate
vodkas	водка	collective	plural	thing	водки	accusative	inanimate
pencil	карандаш	concrete	masculine	thing	карандаша	genitive	inanimate
chalk	мел	concrete	masculine	thing	мела	genitive	inanimate
Americans	американка	concrete	plural	thing	американкам	dative	animate
Caucuses	Кавказ	proper	plural	location	Кавказам	dative	inanimate
letters	письмо	concrete	plural	thing	письма	accusative	inanimate
Paris	Париж	proper	plural	location	Парижах	prepositional	inanimate
letters	письмо	concrete	plural	thing	писем	genitive	inanimate
fields	поле	concrete	plural	location	полей	genitive	inanimate
friend	друг	concrete	masculine	thing	другом	instrumental	animate
Yenisei	Енисей	proper	masculine	location	Енисей	nominative	inanimate
man	мужчина	concrete	feminine	thing	мужчину	accusative	animate
pen	ручка	concrete	feminine	thing	ручке	dative	inanimate
pens	перо	concrete	plural	thing	перами	instrumental	inanimate
school desk	парта	concrete	plural	thing	парты	nominative	inanimate
money	деньги	collective	plural	thing	деньги	nominative	inanimate
notepads	тетрадь	concrete	plural	thing	тетради	nominative	inanimate
pupil	ученица	concrete	feminine	thing	ученицой	instrumental	animate
Watsonvilles	Ватсонвиль	proper	plural	location	Ватсонвилях	prepositional	inanimate
Geneva	Женева	proper	feminine	location	Женевы	genitive	inanimate
class	класс	concrete	masculine	thing	классу	dative	inanimate
Berlins	Берлин	proper	plural	location	Берлинов	genitive	inanimate
dictionaries	словарь	concrete	plural	thing	словарям	dative	inanimate
chalks	мел	concrete	plural	thing	мелами	instrumental	inanimate
Caucuses	Кавказ	proper	plural	location	Кавказов	genitive	inanimate
tea	чай	collective	masculine	thing	чае	prepositional	inanimate
house	дом	concrete	masculine	thing	дом	nominative	inanimate
effort	труд	abstract	masculine	thing	трудом	instrumental	inanimate
Kharkhov	Харьков	proper	masculine	location	Харькову	dative	inanimate
Romes	Рим	proper	plural	location	Римам	dative	inanimate
professor	профессор	concrete	masculine	thing	профессору	dative	animate
Vladivostok	Владивосток	proper	masculine	location	Владивосток	nominative	inanimate
readings	чтение	abstract	plural	thing	чтениия	nominative	inanimate
professions	профессия	abstract	plural	thing	профессиями	instrumental	inanimate
pencil	карандаш	concrete	masculine	thing	карандашом	instrumental	inanimate
schools	школа	concrete	plural	thing	школы	accusative	inanimate
descent	съезд	concrete	masculine	location	съезду	dative	inanimate
students	студент	concrete	plural	thing	студентов	accusative	animate
evening	вечер	abstract	masculine	thing	вечеру	dative	inanimate
New York	Нью-Йорк	proper	masculine	location	Нью-Йорке	prepositional	inanimate
engineer	инженер	concrete	masculine	thing	инженером	instrumental	animate
notepad	тетрадь	concrete	masculine	thing	тетраде	prepositional	inanimate
five	пять	abstract	plural	thing	пять	accusative	inanimate
pen	перо	concrete	nueter	thing	пере	prepositional	inanimate
Chitas	Чита	proper	plural	location	Читам	dative	inanimate
paper	бумага	concrete	feminine	thing	бумага	nominative	inanimate
room	комната	concrete	feminine	thing	комнате	dative	inanimate
accents	акцент	concrete	plural	thing	акцентам	dative	inanimate
text	текст	concrete	masculine	thing	текст	accusative	inanimate
Boris	Борис	proper	plural	thing	Борисы	nominative	animate
doors	дверь	concrete	plural	thing	дверями	instrumental	inanimate
four	четыре	abstract	plural	thing	четырьмя	instrumental	inanimate
students	студент	concrete	plural	thing	студентов	genitive	animate
example	пример	abstract	masculine	thing	примеру	dative	inanimate
glasses	очки	concrete	plural	thing	очки	nominative	inanimate
briefcase	портфель	concrete	masculine	thing	портфеле	prepositional	inanimate
pencil	карандаш	concrete	masculine	thing	карандашу	dative	inanimate
surname	фамилия	concrete	feminine	thing	фамилия	nominative	inanimate
affair	дело	abstract	nueter	thing	делу	dative	inanimate
glasses	очки	concrete	plural	thing	очки	accusative	inanimate
pen	ручка	concrete	feminine	thing	ручки	genitive	inanimate
note	примечание	concrete	nueter	thing	примечанием	instrumental	inanimate
rag	тряпка	concrete	feminine	thing	тряпке	prepositional	inanimate
languages	язык	concrete	plural	thing	языках	prepositional	inanimate
profession	профессия	abstract	feminine	thing	профессии	prepositional	inanimate
exercises	упражнение	concrete	plural	thing	упражнениям	dative	inanimate
truth	правда	abstract	feminine	thing	правде	dative	inanimate
judge	судья	concrete	masculine	thing	судьой	instrumental	animate
text	текст	concrete	masculine	thing	текст	nominative	inanimate
Yalta	Ялта	proper	feminine	location	Ялтой	instrumental	inanimate
ballpoint pen	авторучка	concrete	feminine	thing	авторучки	genitive	inanimate
Vladivostoks	Владивосток	proper	plural	location	Владивостоках	prepositional	inanimate
meat	мясо	collective	nueter	thing	мясом	instrumental	inanimate
mistake	ошибка	abstract	feminine	thing	ошибке	prepositional	inanimate
dictations	диктант	concrete	plural	thing	диктантов	genitive	inanimate
Americans	американец	concrete	plural	thing	американцам	dative	animate
aviators	авиатор	concrete	plural	thing	авиаторы	nominative	animate
Chita	Чита	proper	feminine	location	Читой	instrumental	inanimate
five	пять	abstract	plural	thing	пять	nominative	inanimate
accents	акцент	concrete	plural	thing	акцентах	prepositional	inanimate
surnames	фамилия	concrete	plural	thing	фамилиями	instrumental	inanimate
nationality	национальность	abstract	feminine	thing	национальности	prepositional	inanimate
blackboards	доска	concrete	plural	thing	доскам	dative	inanimate
Vladivostok	Владивосток	proper	masculine	location	Владивосток	accusative	inanimate
readings	чтение	abstract	plural	thing	чтениия	accusative	inanimate
schools	школа	concrete	plural	thing	школы	nominative	inanimate
house	дом	concrete	masculine	thing	доме	prepositional	inanimate
times	пора	concrete	plural	thing	порах	prepositional	inanimate
response	отзыв	concrete	masculine	thing	отзыве	prepositional	inanimate
foreigner	иностранец	concrete	masculine	thing	иностранце	prepositional	animate
zeros	нуль	abstract	plural	thing	нулей	genitive	inanimate
Chita	Чита	proper	feminine	location	Читы	genitive	inanimate
article	статья	concrete	feminine	thing	статью	accusative	inanimate
briefcases	портфель	concrete	plural	thing	портфелям	dative	inanimate
countryside	деревня	concrete	feminine	location	деревня	nominative	inanimate
engineers	инженер	concrete	plural	thing	инженерами	instrumental	animate
dictation	диктант	concrete	masculine	thing	диктанту	dative	inanimate
Tanyas	Таня	proper	plural	thing	Таням	dative	animate
dictionary	словарь	concrete	masculine	thing	словаря	genitive	inanimate
bread	хлеб	collective	masculine	thing	хлебу	dative	inanimate
equator	экватор	concrete	masculine	thing	экватору	dative	inanimate
books	книга	concrete	plural	thing	книг	genitive	inanimate
time	пора	concrete	feminine	thing	поры	genitive	inanimate
classes	класс	concrete	plural	thing	классам	dative	inanimate
sponge	губка	concrete	feminine	thing	губкой	instrumental	inanimate
work	занятие	concrete	nueter	thing	занятия	genitive	inanimate
Madrid	Мадрид	proper	masculine	location	Мадриду	dative	inanimate
flags	знамя	abstract	plural	thing	знамён	genitive	inanimate
briefcase	портфель	concrete	masculine	thing	портфелю	dative	inanimate
nonsense	ерунда	abstract	feminine	thing	ерунду	accusative	inanimate
letter	письмо	concrete	nueter	thing	письме	prepositional	inanimate
uncles	дядя	concrete	plural	thing	дядья	nominative	animate
Arkhangelsk	Архангелск	proper	masculine	location	Архангелск	nominative	inanimate
exercise	упражнение	concrete	nueter	thing	упражнением	instrumental	inanimate
trips	поездка	abstract	plural	thing	поездках	prepositional	inanimate
mercies	пощада	concrete	plural	thing	пощадами	instrumental	inanimate
Kharkhovs	Харьков	proper	plural	location	Харьковы	nominative	inanimate
continuation	продолжение	abstract	nueter	thing	продолжением	instrumental	inanimate
center	центр	concrete	masculine	location	центра	genitive	inanimate
Dneprs	Днепр	proper	plural	location	Днепрам	dative	inanimate
room	комната	concrete	feminine	thing	комнате	prepositional	inanimate
patronymic	отчество	concrete	nueter	thing	отчество	accusative	inanimate
one	одна	abstract	feminine	thing	одной	genitive	animate
Yeniseis	Енисей	proper	plural	location	Енисеях	prepositional	inanimate
uncle	дядя	concrete	masculine	thing	дяди	genitive	animate
truth	правда	abstract	feminine	thing	правде	prepositional	inanimate
books	книга	concrete	plural	thing	книгам	dative	inanimate
patronymic	отчество	concrete	nueter	thing	отчество	nominative	inanimate
ten	десять	abstract	plural	thing	десяти	genitive	inanimate
pencil eraser	резинка	concrete	feminine	thing	резинкой	instrumental	inanimate
profession	профессия	abstract	feminine	thing	профессии	dative	inanimate
Kharkhovs	Харьков	proper	plural	location	Харьковы	accusative	inanimate
Stockholm	Стокгольм	proper	masculine	location	Стокгольму	dative	inanimate
train station	вокзал	concrete	masculine	location	вокзала	genitive	inanimate
Yaltas	Ялта	proper	plural	location	Ялт	genitive	inanimate
Irtysh	Иртыш	proper	masculine	location	Иртыша	genitive	inanimate
Vladivostoks	Владивосток	proper	plural	location	Владивостоками	instrumental	inanimate
misters	господин	concrete	plural	thing	господах	prepositional	animate
Arkhangelsk	Архангелск	proper	masculine	location	Архангелск	accusative	inanimate
dictations	диктант	concrete	plural	thing	диктантами	instrumental	inanimate
exam	экзамен	concrete	masculine	thing	экзамене	prepositional	inanimate
Pavlov	Павлов	proper	masculine	thing	Павлове	prepositional	inanimate
rag	тряпка	concrete	feminine	thing	тряпке	dative	inanimate
ballpoint pen	авторучка	concrete	feminine	thing	авторучку	accusative	inanimate
nationality	национальность	abstract	feminine	thing	национальности	dative	inanimate
trip	поездка	abstract	feminine	thing	поездки	genitive	inanimate
efforts	труд	abstract	plural	thing	трудов	genitive	inanimate
meeting	собрание	abstract	nueter	thing	собрания	genitive	inanimate
equators	экватор	concrete	plural	thing	экваторах	prepositional	inanimate
earths	земля	concrete	plural	thing	землями	instrumental	inanimate
Philadelphia	Филадельфия	proper	feminine	location	Филадельфию	accusative	inanimate
Elbrus	Эльбрус	proper	masculine	location	Эльбрусу	dative	inanimate
school desk	парта	concrete	plural	thing	партам	dative	inanimate
Madrid	Мадрид	proper	masculine	location	Мадрида	genitive	inanimate
mistake	ошибка	abstract	feminine	thing	ошибке	dative	inanimate
Yugoslavia	Югославия	proper	feminine	location	Югославией	instrumental	inanimate
Minneapolis	Миннеаполис	proper	masculine	location	Миннеаполисе	prepositional	inanimate
city	города	concrete	feminine	location	городе	prepositional	inanimate
ones	один	abstract	plural	thing	одни	accusative	inanimate
night	ночь	abstract	feminine	thing	ночь	accusative	inanimate
texts	текст	concrete	plural	thing	тексты	nominative	inanimate
surnames	фамилия	concrete	plural	thing	фамилиях	prepositional	inanimate
exercise	упражнение	concrete	nueter	thing	упражнение	nominative	inanimate
pencil	карандаш	concrete	plural	thing	карандашам	dative	inanimate
Leningrads	Ленинград	proper	plural	location	Ленинградах	prepositional	inanimate
article	статья	concrete	feminine	thing	статье	prepositional	inanimate
chairs	стул	concrete	plural	thing	стулы	nominative	inanimate
buildings	здание	concrete	plural	thing	здания	accusative	inanimate
Bolshois	большой	proper	plural	location	больших	prepositional	inanimate
affair	дело	abstract	nueter	thing	дело	accusative	inanimate
center	центр	concrete	masculine	location	центр	accusative	inanimate
meeting	собрание	abstract	nueter	thing	собрании	prepositional	inanimate
flags	знамя	abstract	plural	thing	знаменам	dative	inanimate
Magnitogorsks	Магнитогорск	proper	plural	location	Магнитогорскам	dative	inanimate
books	книга	concrete	plural	thing	книги	accusative	inanimate
pencil	карандаш	concrete	plural	thing	карандашей	genitive	inanimate
Baikal	Байкал	proper	masculine	location	Байкале	prepositional	inanimate
six	шесть	abstract	plural	thing	шесть	accusative	inanimate
flag	знамя	abstract	nueter	thing	знамени	dative	inanimate
assignments	задание	abstract	plural	thing	заданиями	instrumental	inanimate
fathers	отец	concrete	plural	thing	отцами	instrumental	animate
Yugoslavia	Югославия	proper	feminine	location	Югославии	prepositional	inanimate
professors	профессор	concrete	plural	thing	профессорами	instrumental	animate
Londons	Лондон	proper	plural	location	Лондоны	accusative	inanimate
teacher	преподавательница	concrete	feminine	thing	преподавательнице	dative	animate
reading	чтение	abstract	nueter	thing	чтениия	genitive	inanimate
key	ключ	concrete	masculine	thing	ключ	accusative	inanimate
one	одна	abstract	feminine	thing	одной	prepositional	inanimate
readings	чтение	abstract	plural	thing	чтенииям	dative	inanimate
tea	чай	collective	masculine	thing	чай	nominative	inanimate
zeros	нуль	abstract	plural	thing	нулями	instrumental	inanimate
Odessa	Одесса	proper	feminine	location	Одессы	genitive	inanimate
person	человек	concrete	masculine	thing	человеку	dative	animate
Riga	Рига	proper	feminine	location	Ригой	instrumental	inanimate
Rome	Рим	proper	masculine	location	Риму	dative	inanimate
Los Angeles	Лос-Анжелес	proper	plural	location	Лос-Анжелесах	prepositional	inanimate
pen	ручка	concrete	feminine	thing	ручке	prepositional	inanimate
sponges	губка	concrete	plural	thing	губках	prepositional	inanimate
school	школа	concrete	feminine	thing	школой	instrumental	inanimate
misters	господин	concrete	plural	thing	господ	genitive	animate
Altai	Алтай	proper	masculine	location	Алтае	prepositional	inanimate
key	ключ	concrete	masculine	thing	ключ	nominative	inanimate
tea	чай	collective	masculine	thing	чай	accusative	inanimate
Londons	Лондон	proper	plural	location	Лондоны	nominative	inanimate
engineers	инженер	concrete	plural	thing	инженерах	prepositional	animate
pupils	ученица	concrete	plural	thing	учениц	accusative	animate
Sheboygans	Шебойган	proper	plural	location	Шебойганам	dative	inanimate
tables	стол	concrete	plural	thing	столов	genitive	inanimate
six	шесть	abstract	plural	thing	шесть	nominative	inanimate
truths	правда	abstract	plural	thing	правдами	instrumental	inanimate
old man	серый	proper	masculine	thing	серому	dative	animate
Vladivostok	Владивосток	proper	masculine	location	Владивостоком	instrumental	inanimate
Santa Cruz	Санта-Крус	proper	masculine	location	Санта-Крусу	dative	inanimate
pupils	ученица	concrete	plural	thing	учениц	genitive	animate
pencil eraser	резинка	concrete	plural	thing	резинках	prepositional	inanimate
books	книга	concrete	plural	thing	книги	nominative	inanimate
center	центр	concrete	masculine	location	центр	nominative	inanimate
affair	дело	abstract	nueter	thing	дело	nominative	inanimate
buildings	здание	concrete	plural	thing	здания	nominative	inanimate
chairs	стул	concrete	plural	thing	стулы	accusative	inanimate
profession	профессия	abstract	feminine	thing	профессией	instrumental	inanimate
notebook	блокнот	concrete	masculine	thing	блокнотом	instrumental	inanimate
train stations	вокзал	concrete	plural	location	вокзалам	dative	inanimate
material	материал	concrete	masculine	thing	материала	genitive	inanimate
exercise	упражнение	concrete	nueter	thing	упражнение	accusative	inanimate
misters	господин	concrete	plural	thing	господ	accusative	animate
Shchorsks	Щорск	proper	plural	location	Щорскей	genitive	inanimate
foreigners	иностранец	concrete	plural	thing	иностранцам	dative	animate
night	ночь	abstract	feminine	thing	ночь	nominative	inanimate
pencil	карандаш	concrete	masculine	thing	карандаше	prepositional	inanimate
texts	текст	concrete	plural	thing	тексты	accusative	inanimate
ones	один	abstract	plural	thing	одни	nominative	inanimate
ballpoint pens	авторучка	concrete	plural	thing	авторучки	nominative	inanimate
teachers	учительница	concrete	plural	thing	учительниц	accusative	animate
Baikals	Байкал	proper	plural	location	Байкалы	nominative	inanimate
Leningrad	Ленинград	proper	masculine	location	Ленинград	accusative	inanimate
Shchorsks	Щорск	proper	plural	location	Щорски	nominative	inanimate
shores	берег	concrete	plural	location	берегами	instrumental	inanimate
affair	дело	abstract	nueter	thing	деле	prepositional	inanimate
breads	хлеб	collective	plural	thing	хлебами	instrumental	inanimate
aviators	авиатор	concrete	plural	thing	авиаторами	instrumental	animate
teachers	учитель	concrete	plural	thing	учителями	instrumental	animate
Bolshois	большой	proper	plural	location	больших	genitive	inanimate
Elbrus	Эльбрус	proper	masculine	location	Эльбрус	accusative	inanimate
mister	господин	concrete	masculine	thing	господина	genitive	animate
row	ряд	concrete	masculine	thing	ряд	accusative	inanimate
material	материал	concrete	masculine	thing	материалом	instrumental	inanimate
silks	шёлк	collective	plural	thing	шелка	accusative	inanimate
Ulyanovsk	Уляновск	proper	masculine	location	Уляновску	dative	inanimate
Odessa	Одесса	proper	feminine	location	Одессе	prepositional	inanimate
people	человек	concrete	plural	thing	человекам	dative	animate
New York	Нью-Йорк	proper	masculine	location	Нью-Йорка	genitive	inanimate
field	поле	concrete	nueter	location	поля	genitive	inanimate
Yugoslavia	Югославия	proper	feminine	location	Югославии	genitive	inanimate
Novgorod	Новгород	proper	masculine	location	Новгород	accusative	inanimate
teacher	преподавательница	concrete	feminine	thing	преподавательницы	genitive	animate
sponges	губка	concrete	plural	thing	губкам	dative	inanimate
mister	господин	concrete	masculine	thing	господина	accusative	animate
tables	стол	concrete	plural	thing	столах	prepositional	inanimate
blemishes	пятно	concrete	plural	thing	пятн	genitive	inanimate
surnames	фамилия	concrete	plural	thing	фамилии	accusative	inanimate
one	одна	abstract	feminine	thing	одной	genitive	inanimate
American	американец	concrete	masculine	thing	американцу	dative	animate
buildings	здание	concrete	plural	thing	зданиям	dative	inanimate
house	дом	concrete	masculine	thing	домом	instrumental	inanimate
California	Калифория	proper	feminine	location	Калифориой	instrumental	inanimate
continuations	продолжение	abstract	plural	thing	продолжения	accusative	inanimate
Baikals	Байкал	proper	plural	location	Байкалам	dative	inanimate
door	дверь	concrete	masculine	thing	дверю	dative	inanimate
pupil	ученик	concrete	masculine	thing	учеником	instrumental	animate
mercy	пощада	concrete	feminine	thing	пощаде	dative	inanimate
Arkhangelsk	Архангелск	proper	masculine	location	Архангелском	instrumental	inanimate
teachers	учительница	concrete	plural	thing	учительниц	genitive	animate
London	Лондон	proper	masculine	location	Лондоне	prepositional	inanimate
Chita	Чита	proper	feminine	location	Читу	accusative	inanimate
dictionary	словарь	concrete	masculine	thing	словарю	dative	inanimate
grandfathers	дедушка	concrete	plural	thing	дедушек	genitive	animate
New York	Нью-Йорк	proper	masculine	location	Нью-Йорком	instrumental	inanimate
nights	ночь	abstract	plural	thing	ночами	instrumental	inanimate
continuations	продолжение	abstract	plural	thing	продолжения	nominative	inanimate
keys	ключ	concrete	plural	thing	ключах	prepositional	inanimate
one	один	abstract	masculine	thing	одном	prepositional	inanimate
surnames	фамилия	concrete	plural	thing	фамилии	nominative	inanimate
patronymics	отчество	concrete	plural	thing	отчествам	dative	inanimate
uncle	дядя	concrete	masculine	thing	дяде	dative	animate
Novgorod	Новгород	proper	masculine	location	Новгород	nominative	inanimate
old man	серый	proper	plural	thing	серые	nominative	animate
Novgorods	Новгород	proper	plural	location	Новгородам	dative	inanimate
Odessas	Одесса	proper	plural	location	Одессам	dative	inanimate
pen	перо	concrete	nueter	thing	пером	instrumental	inanimate
Elbrus	Эльбрус	proper	masculine	location	Эльбрус	nominative	inanimate
row	ряд	concrete	masculine	thing	ряд	nominative	inanimate
silks	шёлк	collective	plural	thing	шелка	nominative	inanimate
Americans	американка	concrete	plural	thing	американках	prepositional	animate
articles	статья	concrete	plural	thing	статьям	dative	inanimate
Gvardyesks	Гвардейск	proper	plural	location	Гвардейскей	genitive	inanimate
earth	земля	concrete	feminine	thing	землей	instrumental	inanimate
Shchorsks	Щорск	proper	plural	location	Щорски	accusative	inanimate
students	студентка	concrete	plural	thing	студентках	prepositional	animate
grandfathers	дедушка	concrete	plural	thing	дедушек	accusative	animate
Leningrad	Ленинград	proper	masculine	location	Ленинград	nominative	inanimate
ballpoint pens	авторучка	concrete	plural	thing	авторучки	accusative	inanimate
Baikals	Байкал	proper	plural	location	Байкалы	accusative	inanimate
article	статья	concrete	feminine	thing	статьей	instrumental	inanimate
key	ключ	concrete	masculine	thing	ключу	dative	inanimate
Madrids	Мадрид	proper	plural	location	Мадриды	accusative	inanimate
grandfathers	дедушка	concrete	plural	thing	дедушки	nominative	animate
Stockholms	Стокгольм	proper	plural	location	Стокгольмах	prepositional	inanimate
tardinesses	опоздание	abstract	plural	thing	опозданий	genitive	inanimate
teachers	учитель	concrete	plural	thing	учители	nominative	animate
grandfather	дедушка	concrete	masculine	thing	дедушке	dative	animate
New York	Нью-Йорк	proper	masculine	location	Нью-Йорк	nominative	inanimate
notepad	тетрадь	concrete	masculine	thing	тетрадю	dative	inanimate
Boris	Борис	proper	plural	thing	Борисам	dative	animate
exams	экзамен	concrete	plural	thing	экзаменами	instrumental	inanimate
rows	ряд	concrete	plural	thing	ряды	accusative	inanimate
conversations	разговор	concrete	plural	thing	разговорам	dative	inanimate
Kharkhovs	Харьков	proper	plural	location	Харьковами	instrumental	inanimate
number	номер	concrete	masculine	thing	номер	nominative	inanimate
bread	хлеб	collective	masculine	thing	хлеб	accusative	inanimate
meetings	собрание	abstract	plural	thing	собраниях	prepositional	inanimate
school desk	парта	concrete	feminine	thing	парту	accusative	inanimate
ones	одно	abstract	plural	thing	одни	nominative	inanimate
Madrid	Мадрид	proper	masculine	location	Мадриде	prepositional	inanimate
grandfather	дедушка	concrete	masculine	thing	дедушку	accusative	animate
friends	друг	concrete	plural	thing	друзья	nominative	animate
man	мужчина	concrete	feminine	thing	мужчиной	instrumental	animate
Russians	русский	proper	plural	thing	русским	dative	animate
Yakutsk	Якутск	proper	masculine	location	Якутску	dative	inanimate
men	мужчина	concrete	plural	thing	мужчинами	instrumental	animate
California	Калифория	proper	feminine	location	Калифорие	prepositional	inanimate
two	два	abstract	plural	thing	двум	dative	inanimate
languages	язык	concrete	plural	thing	языки	accusative	inanimate
requests	просьба	concrete	plural	thing	просьбы	nominative	inanimate
exams	экзамен	concrete	plural	thing	экзаменов	genitive	inanimate
engineers	инженер	concrete	plural	thing	инженеры	nominative	animate
flags	знамя	abstract	plural	thing	знаменами	instrumental	inanimate
pupil	ученик	concrete	masculine	thing	ученику	dative	animate
teachers	преподаватель	concrete	plural	thing	преподавателям	dative	animate
first names	имя	abstract	plural	thing	именами	instrumental	inanimate
Kharkhov	Харьков	proper	masculine	location	Харькове	prepositional	inanimate
one	одна	abstract	feminine	thing	одной	prepositional	animate
window	окно	concrete	nueter	thing	окна	genitive	inanimate
work	занятие	concrete	nueter	thing	занятии	prepositional	inanimate
truths	правда	abstract	plural	thing	правды	accusative	inanimate
materials	материал	concrete	plural	thing	материалам	dative	inanimate
pupils	ученица	concrete	plural	thing	ученицах	prepositional	animate
lectures	лекция	abstract	plural	thing	лекций	genitive	inanimate
atom	атом	concrete	masculine	thing	атоме	prepositional	inanimate
Kharkhov	Харьков	proper	masculine	location	Харькова	genitive	inanimate
laboratories	лаборатория	concrete	plural	location	лабораторий	genitive	inanimate
truths	правда	abstract	plural	thing	правды	nominative	inanimate
accents	акцент	concrete	plural	thing	акцентами	instrumental	inanimate
ten	десять	abstract	plural	thing	десяти	prepositional	inanimate
reading	чтение	abstract	nueter	thing	чтениии	prepositional	inanimate
Rome	Рим	proper	masculine	location	Рима	genitive	inanimate
Irtysh	Иртыш	proper	masculine	location	Иртышом	instrumental	inanimate
universities	университет	concrete	plural	location	университетов	genitive	inanimate
requests	просьба	concrete	plural	thing	просьбы	accusative	inanimate
Americas	Америка	proper	plural	location	Америками	instrumental	inanimate
city	города	concrete	feminine	location	городу	accusative	inanimate
letters	письмо	concrete	plural	thing	письмам	dative	inanimate
map	карта	concrete	feminine	thing	картой	instrumental	inanimate
aviator	авиатор	concrete	masculine	thing	авиатором	instrumental	animate
languages	язык	concrete	plural	thing	языки	nominative	inanimate
blackboards	доска	concrete	plural	thing	доск	genitive	inanimate
atoms	атом	concrete	plural	thing	атомам	dative	inanimate
blackboard	доска	concrete	feminine	thing	доска	nominative	inanimate
building	здание	concrete	nueter	thing	зданием	instrumental	inanimate
ones	одно	abstract	plural	thing	одни	accusative	inanimate
pen	перо	concrete	nueter	thing	перу	dative	inanimate
number	номер	concrete	masculine	thing	номер	accusative	inanimate
Ulyanovsk	Уляновск	proper	masculine	location	Уляновске	prepositional	inanimate
bread	хлеб	collective	masculine	thing	хлеб	nominative	inanimate
city	города	concrete	feminine	location	города	nominative	inanimate
shore	берег	concrete	masculine	location	берега	genitive	inanimate
rows	ряд	concrete	plural	thing	ряды	nominative	inanimate
atoms	атом	concrete	plural	thing	атомах	prepositional	inanimate
nonsenses	ерунда	abstract	plural	thing	ерундам	dative	inanimate
New York	Нью-Йорк	proper	masculine	location	Нью-Йорк	accusative	inanimate
Romes	Рим	proper	plural	location	Римами	instrumental	inanimate
schools	школа	concrete	plural	thing	школами	instrumental	inanimate
assignment	задание	abstract	nueter	thing	заданиия	genitive	inanimate
Sheboygans	Шебойган	proper	plural	location	Шебойганами	instrumental	inanimate
Madrids	Мадрид	proper	plural	location	Мадриды	nominative	inanimate
universities	университет	concrete	plural	location	университетам	dative	inanimate
flags	знамя	abstract	plural	thing	знаменах	prepositional	inanimate
pockets	карман	concrete	plural	location	карманы	nominative	inanimate
Odessas	Одесса	proper	plural	location	Одессы	accusative	inanimate
foreigner	иностранец	concrete	masculine	thing	иностранцом	instrumental	animate
dictionaries	словарь	concrete	plural	thing	словарей	genitive	inanimate
houses	дом	concrete	plural	thing	домы	nominative	inanimate
pens	ручка	concrete	plural	thing	ручки	nominative	inanimate
efforts	труд	abstract	plural	thing	труды	accusative	inanimate
Genevas	Женева	proper	plural	location	Женевы	nominative	inanimate
grandfather	дедушка	concrete	masculine	thing	дедушке	prepositional	animate
Boris	Борис	proper	plural	thing	Борисах	prepositional	animate
Philadelphia	Филадельфия	proper	feminine	location	Филадельфией	instrumental	inanimate
Yaltas	Ялта	proper	plural	location	Ялтами	instrumental	inanimate
museums	музей	concrete	plural	location	музеям	dative	inanimate
judges	судья	concrete	plural	thing	судьей	genitive	animate
pencil eraser	резинка	concrete	plural	thing	резинки	nominative	inanimate
Yakutsk	Якутск	proper	masculine	location	Якутска	genitive	inanimate
center	центр	concrete	masculine	location	центром	instrumental	inanimate
mister	господин	concrete	masculine	thing	господине	prepositional	animate
American	американка	concrete	feminine	thing	американкой	instrumental	animate
example	пример	abstract	masculine	thing	примере	prepositional	inanimate
Madrid	Мадрид	proper	masculine	location	Мадридом	instrumental	inanimate
briefcases	портфель	concrete	plural	thing	портфелях	prepositional	inanimate
first name	имя	abstract	nueter	thing	имя	nominative	inanimate
mistakes	ошибка	abstract	plural	thing	ошибках	prepositional	inanimate
Stockholms	Стокгольм	proper	plural	location	Стокгольмы	nominative	inanimate
ballpoint pen	авторучка	concrete	feminine	thing	авторучка	nominative	inanimate
one	одна	abstract	feminine	thing	одной	dative	animate
Tanyas	Таня	proper	plural	thing	Танями	instrumental	animate
engineer	инженер	concrete	masculine	thing	инженеру	dative	animate
judges	судья	concrete	plural	thing	судьей	accusative	animate
mercies	пощада	concrete	plural	thing	пощадах	prepositional	inanimate
train stations	вокзал	concrete	plural	location	вокзалы	nominative	inanimate
Paris	Париж	proper	masculine	location	Парижа	genitive	inanimate
descents	съезд	concrete	plural	location	съездами	instrumental	inanimate
pencil	карандаш	concrete	plural	thing	карандашами	instrumental	inanimate
men	мужчина	concrete	plural	thing	мужчины	nominative	animate
times	пора	concrete	plural	thing	поры	accusative	inanimate
blackboards	доска	concrete	plural	thing	досках	prepositional	inanimate
California	Калифория	proper	feminine	location	Калифорие	dative	inanimate
seven	семь	abstract	plural	thing	семь	nominative	inanimate
notebooks	блокнот	concrete	plural	thing	блокнотов	genitive	inanimate
mercies	пощада	concrete	plural	thing	пощад	genitive	inanimate
Russians	русская	proper	plural	thing	русскими	instrumental	animate
fields	поле	concrete	plural	location	полях	prepositional	inanimate
seven	семь	abstract	plural	thing	семь	accusative	inanimate
shores	берег	concrete	plural	location	берегам	dative	inanimate
works	занятие	concrete	plural	thing	занятиям	dative	inanimate
sponges	губка	concrete	plural	thing	губками	instrumental	inanimate
silks	шёлк	collective	plural	thing	шелками	instrumental	inanimate
language	язык	concrete	masculine	thing	языка	genitive	inanimate
Chita	Чита	proper	feminine	location	Чита	nominative	inanimate
question	вопрос	concrete	masculine	thing	вопросом	instrumental	inanimate
profession	профессия	abstract	feminine	thing	профессии	genitive	inanimate
flag	знамя	abstract	nueter	thing	знаменем	instrumental	inanimate
train stations	вокзал	concrete	plural	location	вокзалы	accusative	inanimate
times	пора	concrete	plural	thing	поры	nominative	inanimate
ten	десять	abstract	plural	thing	десяти	dative	inanimate
Magnitogorsk	Магнитогорск	proper	masculine	location	Магнитогорска	genitive	inanimate
uncle	дядя	concrete	masculine	thing	дядей	instrumental	animate
Riga	Рига	proper	feminine	location	Риги	genitive	inanimate
first name	имя	abstract	nueter	thing	имя	accusative	inanimate
aviator	авиатор	concrete	masculine	thing	авиатора	genitive	animate
Stockholms	Стокгольм	proper	plural	location	Стокгольмы	accusative	inanimate
teachers	учитель	concrete	plural	thing	учителей	genitive	animate
Watsonville	Ватсонвиль	proper	masculine	location	Ватсонвилю	dative	inanimate
Shchorsks	Щорск	proper	plural	location	Щорскам	dative	inanimate
aviator	авиатор	concrete	masculine	thing	авиатора	accusative	animate
theaters	театр	concrete	plural	location	театров	genitive	inanimate
teacher	преподавательница	concrete	feminine	thing	преподавательница	nominative	animate
teachers	учитель	concrete	plural	thing	учителей	accusative	animate
Zagorsks	Загорск	proper	plural	location	Загорскей	genitive	inanimate
rags	тряпка	concrete	plural	thing	тряпк	genitive	inanimate
pencil eraser	резинка	concrete	plural	thing	резинки	accusative	inanimate
tea	чай	collective	masculine	thing	чая	genitive	inanimate
pupils	ученик	concrete	plural	thing	учениках	prepositional	animate
Genevas	Женева	proper	plural	location	Женевы	accusative	inanimate
Riga	Рига	proper	feminine	location	Ригу	accusative	inanimate
dictionary	словарь	concrete	masculine	thing	словаре	prepositional	inanimate
nationality	национальность	abstract	feminine	thing	национальности	genitive	inanimate
pens	ручка	concrete	plural	thing	ручки	accusative	inanimate
efforts	труд	abstract	plural	thing	труды	nominative	inanimate
houses	дом	concrete	plural	thing	домы	accusative	inanimate
materials	материал	concrete	plural	thing	материалами	instrumental	inanimate
pockets	карман	concrete	plural	location	карманы	accusative	inanimate
Odessas	Одесса	proper	plural	location	Одессы	nominative	inanimate
exercise	упражнение	concrete	nueter	thing	упражнении	prepositional	inanimate
flag	знамя	abstract	nueter	thing	знамени	genitive	inanimate
responses	отзыв	concrete	plural	thing	отзывами	instrumental	inanimate
centers	центр	concrete	plural	location	центрам	dative	inanimate
Odessa	Одесса	proper	feminine	location	Одессе	dative	inanimate
language	язык	concrete	masculine	thing	язык	nominative	inanimate
old man	серый	proper	plural	thing	серых	accusative	animate
papers	бумага	concrete	plural	thing	бумагах	prepositional	inanimate
cups	чашка	concrete	plural	thing	чашки	nominative	inanimate
eight	восемь	abstract	plural	thing	восемь	accusative	inanimate
Zagorsk	Загорск	proper	masculine	location	Загорска	genitive	inanimate
silks	шёлк	collective	plural	thing	шелков	genitive	inanimate
Los Angeles	Лос-Анжелес	proper	masculine	location	Лос-Анжелес	nominative	inanimate
equator	экватор	concrete	masculine	thing	экваторе	prepositional	inanimate
shores	берег	concrete	plural	location	берегах	prepositional	inanimate
exercises	упражнение	concrete	plural	thing	упражнениями	instrumental	inanimate
mercies	пощада	concrete	plural	thing	пощады	nominative	inanimate
cups	чашка	concrete	plural	thing	чашкам	dative	inanimate
mistakes	ошибка	abstract	plural	thing	ошибкам	dative	inanimate
sponge	губка	concrete	feminine	thing	губки	genitive	inanimate
Los Angeles	Лос-Анжелес	proper	plural	location	Лос-Анжелесы	accusative	inanimate
days	день	concrete	plural	thing	дней	genitive	inanimate
Russians	русский	proper	plural	thing	русских	prepositional	animate
mercy	пощада	concrete	feminine	thing	пощаде	prepositional	inanimate
students	студент	concrete	plural	thing	студентами	instrumental	animate
Stockholm	Стокгольм	proper	masculine	location	Стокгольмом	instrumental	inanimate
theaters	театр	concrete	plural	location	театры	nominative	inanimate
library	библиотека	concrete	feminine	location	библиотеку	accusative	inanimate
works	работа	abstract	plural	thing	работы	accusative	inanimate
professors	профессор	concrete	plural	thing	профессорам	dative	animate
Pavlov	Павлов	proper	masculine	thing	Павлов	accusative	inanimate
pens	ручка	concrete	plural	thing	ручк	genitive	inanimate
day	день	concrete	masculine	thing	день	accusative	inanimate
first names	имя	abstract	plural	thing	именах	prepositional	inanimate
answer	ответ	abstract	masculine	thing	ответ	nominative	inanimate
letter	письмо	concrete	nueter	thing	письмом	instrumental	inanimate
readings	чтение	abstract	plural	thing	чтенииями	instrumental	inanimate
old man	серый	proper	plural	thing	серых	genitive	animate
table	стол	concrete	masculine	thing	столе	prepositional	inanimate
rows	ряд	concrete	plural	thing	рядах	prepositional	inanimate
notepad	тетрадь	concrete	masculine	thing	тетрадём	instrumental	inanimate
answer	ответ	abstract	masculine	thing	ответ	accusative	inanimate
three	три	abstract	plural	thing	трём	dative	inanimate
uncle	дядя	concrete	masculine	thing	дяде	prepositional	animate
meats	мясо	collective	plural	thing	мяс	genitive	inanimate
Pavlov	Павлов	proper	masculine	thing	Павлов	nominative	inanimate
day	день	concrete	masculine	thing	день	nominative	inanimate
works	работа	abstract	plural	thing	работы	nominative	inanimate
theaters	театр	concrete	plural	location	театры	accusative	inanimate
engineer	инженер	concrete	masculine	thing	инженера	accusative	animate
meats	мясо	collective	plural	thing	мясах	prepositional	inanimate
Pavlov	Павлов	proper	masculine	thing	Павлова	genitive	inanimate
Boris	Борис	proper	masculine	thing	Борису	dative	animate
students	студентка	concrete	plural	thing	студенток	genitive	animate
universities	университет	concrete	plural	location	университетах	prepositional	inanimate
Los Angeles	Лос-Анжелес	proper	plural	location	Лос-Анжелесы	nominative	inanimate
notepads	тетрадь	concrete	plural	thing	тетрадей	genitive	inanimate
students	студентка	concrete	plural	thing	студенток	accusative	animate
aviator	авиатор	concrete	masculine	thing	авиаторе	prepositional	animate
mercies	пощада	concrete	plural	thing	пощады	accusative	inanimate
Los Angeles	Лос-Анжелес	proper	masculine	location	Лос-Анжелес	accusative	inanimate
pen	ручка	concrete	feminine	thing	ручкой	instrumental	inanimate
engineer	инженер	concrete	masculine	thing	инженера	genitive	animate
example	пример	abstract	masculine	thing	примера	genitive	inanimate
missus	госпожа	concrete	plural	thing	госпожам	dative	animate
eight	восемь	abstract	plural	thing	восемь	nominative	inanimate
Novgorods	Новгород	proper	plural	location	Новгородами	instrumental	inanimate
cups	чашка	concrete	plural	thing	чашки	accusative	inanimate
Watsonville	Ватсонвиль	proper	masculine	location	Ватсонвилём	instrumental	inanimate
library	библиотека	concrete	feminine	location	библиотекой	instrumental	inanimate
language	язык	concrete	masculine	thing	язык	accusative	inanimate
briefcases	портфель	concrete	plural	thing	портфелями	instrumental	inanimate
surnames	фамилия	concrete	plural	thing	фамилиям	dative	inanimate
tardinesses	опоздание	abstract	plural	thing	опозданиям	dative	inanimate
Baikal	Байкал	proper	masculine	location	Байкала	genitive	inanimate
exam	экзамен	concrete	masculine	thing	экзаменом	instrumental	inanimate
sponge	губка	concrete	feminine	thing	губка	nominative	inanimate
shores	берег	concrete	plural	location	береги	accusative	inanimate
continuations	продолжение	abstract	plural	thing	продолжениям	dative	inanimate
windows	окно	concrete	plural	thing	окнах	prepositional	inanimate
judges	судья	concrete	plural	thing	судьям	dative	animate
teacher	учительница	concrete	feminine	thing	учительнице	prepositional	animate
cup	чашка	concrete	feminine	thing	чашка	nominative	inanimate
man	мужчина	concrete	feminine	thing	мужчины	genitive	animate
Zagorsks	Загорск	proper	plural	location	Загорскам	dative	inanimate
windows	окно	concrete	plural	thing	окон	genitive	inanimate
Yalta	Ялта	proper	feminine	location	Ялте	dative	inanimate
aviators	авиатор	concrete	plural	thing	авиаторам	dative	animate
one	одна	abstract	feminine	thing	одну	accusative	inanimate
Moscow	Москва	proper	feminine	location	Москвой	instrumental	inanimate
train stations	вокзал	concrete	plural	location	вокзалов	genitive	inanimate
Yugoslavias	Югославия	proper	plural	location	Югославии	nominative	inanimate
Californias	Калифория	proper	plural	location	Калифории	accusative	inanimate
table	стол	concrete	masculine	thing	стол	nominative	inanimate
Russian	русская	proper	feminine	thing	русскую	accusative	animate
earth	земля	concrete	feminine	thing	землю	accusative	inanimate
exams	экзамен	concrete	plural	thing	экзаменах	prepositional	inanimate
three	три	abstract	plural	thing	тремя	instrumental	inanimate
sea	море	concrete	nueter	location	море	accusative	inanimate
exercises	упражнение	concrete	plural	thing	упражнениях	prepositional	inanimate
sea	море	concrete	nueter	location	море	nominative	inanimate
surnames	фамилия	concrete	plural	thing	фамилий	genitive	inanimate
Californias	Калифория	proper	plural	location	Калифории	nominative	inanimate
Yugoslavias	Югославия	proper	plural	location	Югославии	accusative	inanimate
table	стол	concrete	masculine	thing	стол	accusative	inanimate
Rigas	Рига	proper	plural	location	Ригах	prepositional	inanimate
Altai	Алтай	proper	masculine	location	Алтая	genitive	inanimate
Altais	Алтай	proper	plural	location	Алтаям	dative	inanimate
ballpoint pen	авторучка	concrete	feminine	thing	авторучке	dative	inanimate
trip	поездка	abstract	feminine	thing	поездке	prepositional	inanimate
Dneprs	Днепр	proper	plural	location	Днепрах	prepositional	inanimate
letters	письмо	concrete	plural	thing	письмах	prepositional	inanimate
Californias	Калифория	proper	plural	location	Калифориями	instrumental	inanimate
visits	свидание	abstract	plural	thing	свиданиях	prepositional	inanimate
laboratory	лаборатория	concrete	feminine	location	лабораторию	accusative	inanimate
American	американка	concrete	feminine	thing	американка	nominative	animate
Dnepr	Днепр	proper	masculine	location	Днепру	dative	inanimate
silks	шёлк	collective	plural	thing	шелкам	dative	inanimate
blackboard	доска	concrete	feminine	thing	доской	instrumental	inanimate
shores	берег	concrete	plural	location	береги	nominative	inanimate
maps	карта	concrete	plural	thing	картами	instrumental	inanimate
centers	центр	concrete	plural	location	центров	genitive	inanimate
keys	ключ	concrete	plural	thing	ключам	dative	inanimate
theater	театр	concrete	masculine	location	театре	prepositional	inanimate
dictation	диктант	concrete	masculine	thing	диктанта	genitive	inanimate
school desk	парта	concrete	feminine	thing	партой	instrumental	inanimate
joys	рад	abstract	plural	thing	рады	accusative	inanimate
student	студентка	concrete	feminine	thing	студентки	genitive	animate
Gvardyesks	Гвардейск	proper	plural	location	Гвардейсках	prepositional	inanimate
night	ночь	abstract	feminine	thing	ночью	instrumental	inanimate
two	два	abstract	plural	thing	два	accusative	inanimate
dining hall	столовая	concrete	feminine	location	столовой	dative	inanimate
Irtysh	Иртыш	proper	masculine	location	Иртыш	nominative	inanimate
misters	господин	concrete	plural	thing	господа	nominative	animate
numbers	номер	concrete	plural	thing	номерами	instrumental	inanimate
blackboard	доска	concrete	feminine	thing	доске	dative	inanimate
time	раз	abstract	masculine	thing	разом	instrumental	inanimate
window	окно	concrete	nueter	thing	окном	instrumental	inanimate
row	ряд	concrete	masculine	thing	ряде	prepositional	inanimate
request	просьба	concrete	feminine	thing	просьбу	accusative	inanimate
Watsonville	Ватсонвиль	proper	masculine	location	Ватсонвиль	nominative	inanimate
earth	земля	concrete	feminine	thing	земле	dative	inanimate
student	студентка	concrete	feminine	thing	студентке	dative	animate
papers	бумага	concrete	plural	thing	бумаги	accusative	inanimate
glasses	очки	concrete	plural	thing	очкам	dative	inanimate
doors	дверь	concrete	plural	thing	дверям	dative	inanimate
vodka	водка	collective	feminine	thing	водке	dative	inanimate
mother	мать	concrete	feminine	thing	матерью	instrumental	animate
Sheboygan	Шебойган	proper	masculine	location	Шебойгане	prepositional	inanimate
laboratory	лаборатория	concrete	feminine	location	лаборатории	genitive	inanimate
Arkhangelsks	Архангелск	proper	plural	location	Архангелскей	genitive	inanimate
Santa Cruzs	Санта-Крус	proper	plural	location	Санта-Крусами	instrumental	inanimate
eight	восемь	abstract	plural	thing	восьми	prepositional	inanimate
exam	экзамен	concrete	masculine	thing	экзамену	dative	inanimate
countrysides	деревня	concrete	plural	location	деревням	dative	inanimate
train station	вокзал	concrete	masculine	location	вокзале	prepositional	inanimate
silk	шёлк	collective	masculine	thing	шёлк	accusative	inanimate
requests	просьба	concrete	plural	thing	просьбах	prepositional	inanimate
judge	судья	concrete	masculine	thing	судью	accusative	animate
aviator	авиатор	concrete	masculine	thing	авиатору	dative	animate
silk	шёлк	collective	masculine	thing	шёлк	nominative	inanimate
theaters	театр	concrete	plural	location	театрам	dative	inanimate
Watsonvilles	Ватсонвиль	proper	plural	location	Ватсонвилям	dative	inanimate
Dnepropetrovsk	Днепропетровск	proper	masculine	location	Днепропетровске	prepositional	inanimate
five	пять	abstract	plural	thing	пяти	genitive	inanimate
Riga	Рига	proper	feminine	location	Риге	dative	inanimate
blemish	пятно	concrete	nueter	thing	пятне	prepositional	inanimate
Zagorsks	Загорск	proper	plural	location	Загорсками	instrumental	inanimate
visits	свидание	abstract	plural	thing	свиданиями	instrumental	inanimate
America	Америка	proper	feminine	location	Америка	nominative	inanimate
papers	бумага	concrete	plural	thing	бумаги	nominative	inanimate
time	пора	concrete	feminine	thing	поре	dative	inanimate
school desk	парта	concrete	feminine	thing	парты	genitive	inanimate
pockets	карман	concrete	plural	location	карманов	genitive	inanimate
Watsonville	Ватсонвиль	proper	masculine	location	Ватсонвиль	accusative	inanimate
table	стол	concrete	masculine	thing	столом	instrumental	inanimate
pupil	ученица	concrete	feminine	thing	ученице	prepositional	animate
Shchorsks	Щорск	proper	plural	location	Щорсках	prepositional	inanimate
material	материал	concrete	masculine	thing	материалу	dative	inanimate
pencil eraser	резинка	concrete	feminine	thing	резинке	dative	inanimate
Watsonvilles	Ватсонвиль	proper	plural	location	Ватсонвилей	genitive	inanimate
Dnepr	Днепр	proper	masculine	location	Днепра	genitive	inanimate
effort	труд	abstract	masculine	thing	труду	dative	inanimate
Ural	Урал	proper	masculine	location	Урала	genitive	inanimate
two	два	abstract	plural	thing	два	nominative	inanimate
joy	рад	abstract	masculine	thing	раде	prepositional	inanimate
house	дом	concrete	masculine	thing	дома	genitive	inanimate
teacher	учительница	concrete	feminine	thing	учительница	nominative	animate
field	поле	concrete	nueter	location	полю	dative	inanimate
Irtysh	Иртыш	proper	masculine	location	Иртыш	accusative	inanimate
one	один	abstract	masculine	thing	одому	dative	inanimate
books	книга	concrete	plural	thing	книгами	instrumental	inanimate
response	отзыв	concrete	masculine	thing	отзывом	instrumental	inanimate
joys	рад	abstract	plural	thing	рады	nominative	inanimate
one	одно	abstract	nueter	thing	одно	accusative	inanimate
Dnepr	Днепр	proper	masculine	location	Днепр	nominative	inanimate
Philadelphias	Филадельфия	proper	plural	location	Филадельфии	nominative	inanimate
blackboard	доска	concrete	feminine	thing	доске	prepositional	inanimate
tardinesses	опоздание	abstract	plural	thing	опоздания	nominative	inanimate
affairs	дело	abstract	plural	thing	делами	instrumental	inanimate
Madrids	Мадрид	proper	plural	location	Мадридами	instrumental	inanimate
chairs	стул	concrete	plural	thing	стулами	instrumental	inanimate
men	мужчина	concrete	plural	thing	мужчинах	prepositional	animate
father	отец	concrete	masculine	thing	отцом	instrumental	animate
Rigas	Рига	proper	plural	location	Ригами	instrumental	inanimate
Yakutsks	Якутск	proper	plural	location	Якутски	accusative	inanimate
dining hall	столовая	concrete	feminine	location	столовой	prepositional	inanimate
briefcase	портфель	concrete	masculine	thing	портфель	nominative	inanimate
pens	ручка	concrete	plural	thing	ручкам	dative	inanimate
Kharkhovs	Харьков	proper	plural	location	Харьковов	genitive	inanimate
Novgorod	Новгород	proper	masculine	location	Новгороду	dative	inanimate
vodka	водка	collective	feminine	thing	водку	accusative	inanimate
efforts	труд	abstract	plural	thing	трудах	prepositional	inanimate
pupils	ученик	concrete	plural	thing	ученики	nominative	animate
six	шесть	abstract	plural	thing	шести	genitive	inanimate
Dnepr	Днепр	proper	masculine	location	Днепре	prepositional	inanimate
exam	экзамен	concrete	masculine	thing	экзамен	nominative	inanimate
Genevas	Женева	proper	plural	location	Женевах	prepositional	inanimate
university	университет	concrete	masculine	location	университетом	instrumental	inanimate
eight	восемь	abstract	plural	thing	восьми	dative	inanimate
fields	поле	concrete	plural	location	поля	nominative	inanimate
dictionaries	словарь	concrete	plural	thing	словари	nominative	inanimate
Chitas	Чита	proper	plural	location	Читы	nominative	inanimate
Elbrus	Эльбрус	proper	plural	location	Эльбрусов	genitive	inanimate
Stockholm	Стокгольм	proper	masculine	location	Стокгольме	prepositional	inanimate
rooms	комната	concrete	plural	thing	комнаты	nominative	inanimate
vodka	водка	collective	feminine	thing	водке	prepositional	inanimate
theaters	театр	concrete	plural	location	театрах	prepositional	inanimate
Stockholm	Стокгольм	proper	masculine	location	Стокгольм	nominative	inanimate
blemish	пятно	concrete	nueter	thing	пятна	genitive	inanimate
theater	театр	concrete	masculine	location	театр	accusative	inanimate
eight	восемь	abstract	plural	thing	восьмью	instrumental	inanimate
Zagorsks	Загорск	proper	plural	location	Загорсках	prepositional	inanimate
student	студентка	concrete	feminine	thing	студентке	prepositional	animate
earth	земля	concrete	feminine	thing	земле	prepositional	inanimate
glasses	очки	concrete	plural	thing	очками	instrumental	inanimate
Minneapolis	Миннеаполис	proper	plural	location	Миннеаполисам	dative	inanimate
maps	карта	concrete	plural	thing	картах	prepositional	inanimate
languages	язык	concrete	plural	thing	языкей	genitive	inanimate
times	пора	concrete	plural	thing	порам	dative	inanimate
Rigas	Рига	proper	plural	location	Риг	genitive	inanimate
pupil	ученица	concrete	feminine	thing	ученице	dative	animate
Londons	Лондон	proper	plural	location	Лондонах	prepositional	inanimate
Russian	русская	proper	feminine	thing	русская	nominative	animate
Russian	русский	proper	masculine	thing	русском	prepositional	animate
time	пора	concrete	feminine	thing	поре	prepositional	inanimate
theater	театр	concrete	masculine	location	театр	nominative	inanimate
texts	текст	concrete	plural	thing	текстов	genitive	inanimate
rooms	комната	concrete	plural	thing	комнаты	accusative	inanimate
Stockholm	Стокгольм	proper	masculine	location	Стокгольм	accusative	inanimate
Yakutsk	Якутск	proper	masculine	location	Якутске	prepositional	inanimate
books	книга	concrete	plural	thing	книгах	prepositional	inanimate
Californias	Калифория	proper	plural	location	Калифориям	dative	inanimate
bread	хлеб	collective	masculine	thing	хлебом	instrumental	inanimate
houses	дом	concrete	plural	thing	домам	dative	inanimate
fields	поле	concrete	plural	location	поля	accusative	inanimate
Riga	Рига	proper	feminine	location	Риге	prepositional	inanimate
dictionaries	словарь	concrete	plural	thing	словари	accusative	inanimate
Chitas	Чита	proper	plural	location	Читы	accusative	inanimate
student	студент	concrete	masculine	thing	студентом	instrumental	animate
evenings	вечер	abstract	plural	thing	вечерам	dative	inanimate
exam	экзамен	concrete	masculine	thing	экзамен	accusative	inanimate
silk	шёлк	collective	masculine	thing	шёлку	dative	inanimate
old man	серый	proper	plural	thing	серым	dative	animate
conversations	разговор	concrete	plural	thing	разговорами	instrumental	inanimate
affair	дело	abstract	nueter	thing	делом	instrumental	inanimate
Elbrus	Эльбрус	proper	plural	location	Эльбрусах	prepositional	inanimate
Yakutsks	Якутск	proper	plural	location	Якутски	nominative	inanimate
briefcase	портфель	concrete	masculine	thing	портфель	accusative	inanimate
teachers	учительница	concrete	plural	thing	учительницами	instrumental	animate
Yeniseis	Енисей	proper	plural	location	Енисеями	instrumental	inanimate
pencil eraser	резинка	concrete	feminine	thing	резинке	prepositional	inanimate
Elbrus	Эльбрус	proper	masculine	location	Эльбрусом	instrumental	inanimate
response	отзыв	concrete	masculine	thing	отзыва	genitive	inanimate
cup	чашка	concrete	feminine	thing	чашки	genitive	inanimate
Pavlovs	Павлов	proper	plural	thing	Павловов	genitive	inanimate
days	день	concrete	plural	thing	днями	instrumental	inanimate
tardinesses	опоздание	abstract	plural	thing	опоздания	accusative	inanimate
one	одно	abstract	nueter	thing	одно	nominative	inanimate
Philadelphias	Филадельфия	proper	plural	location	Филадельфии	accusative	inanimate
Dnepr	Днепр	proper	masculine	location	Днепр	accusative	inanimate
Volgas	Волга	proper	plural	location	Волг	genitive	inanimate
Chitas	Чита	proper	plural	location	Чит	genitive	inanimate
questions	вопрос	concrete	plural	thing	вопросов	genitive	inanimate
guest	гость	concrete	masculine	thing	гостю	dative	animate
Russians	русская	proper	plural	thing	русских	genitive	animate
questions	вопрос	concrete	plural	thing	вопросы	nominative	inanimate
teacher	учительница	concrete	feminine	thing	учительнице	dative	animate
day	день	concrete	masculine	thing	дне	prepositional	inanimate
briefcases	портфель	concrete	plural	thing	портфели	accusative	inanimate
mistakes	ошибка	abstract	plural	thing	ошибки	accusative	inanimate
Berlin	Берлин	proper	masculine	location	Берлин	accusative	inanimate
friends	друг	concrete	plural	thing	друзьям	dative	animate
works	занятие	concrete	plural	thing	занятий	genitive	inanimate
American	американка	concrete	feminine	thing	американку	accusative	animate
joy	рад	abstract	masculine	thing	радом	instrumental	inanimate
letters	письмо	concrete	plural	thing	письмами	instrumental	inanimate
school desk	парта	concrete	feminine	thing	парта	nominative	inanimate
Russian	русский	proper	masculine	thing	русским	instrumental	animate
dictations	диктант	concrete	plural	thing	диктанты	nominative	inanimate
notes	примечание	concrete	plural	thing	примечаниям	dative	inanimate
Shchorsk	Щорск	proper	masculine	location	Щорск	accusative	inanimate
tea	чай	collective	masculine	thing	чаю	dative	inanimate
rags	тряпка	concrete	plural	thing	тряпки	nominative	inanimate
Dnepr	Днепр	proper	masculine	location	Днепром	instrumental	inanimate
earths	земля	concrete	plural	thing	земли	accusative	inanimate
room	комната	concrete	feminine	thing	комнаты	genitive	inanimate
daughters	дочь	concrete	plural	thing	дочерями	instrumental	animate
Yalta	Ялта	proper	feminine	location	Ялте	prepositional	inanimate
Watsonville	Ватсонвиль	proper	masculine	location	Ватсонвиля	genitive	inanimate
pupils	ученица	concrete	plural	thing	ученицы	nominative	animate
Russians	русская	proper	plural	thing	русских	accusative	animate
pocket	карман	concrete	masculine	location	карманом	instrumental	inanimate
Sheboygans	Шебойган	proper	plural	location	Шебойганы	nominative	inanimate
one	один	abstract	masculine	thing	один	nominative	inanimate
efforts	труд	abstract	plural	thing	трудами	instrumental	inanimate
daughters	дочь	concrete	plural	thing	дочерях	prepositional	animate
Sheboygans	Шебойган	proper	plural	location	Шебойганы	accusative	inanimate
rooms	комната	concrete	plural	thing	комнат	genitive	inanimate
one	один	abstract	masculine	thing	один	accusative	inanimate
notes	примечание	concrete	plural	thing	примечаниями	instrumental	inanimate
assignment	задание	abstract	nueter	thing	заданиием	instrumental	inanimate
Americas	Америка	proper	plural	location	Америках	prepositional	inanimate
window	окно	concrete	nueter	thing	окне	prepositional	inanimate
paper	бумага	concrete	feminine	thing	бумаги	genitive	inanimate
language	язык	concrete	masculine	thing	языку	dative	inanimate
trip	поездка	abstract	feminine	thing	поездке	dative	inanimate
ballpoint pen	авторучка	concrete	feminine	thing	авторучке	prepositional	inanimate
nationalities	национальность	abstract	plural	thing	национальностям	dative	inanimate
equators	экватор	concrete	plural	thing	экваторам	dative	inanimate
Moscow	Москва	proper	feminine	location	Москвы	genitive	inanimate
earths	земля	concrete	plural	thing	земли	nominative	inanimate
Americans	американка	concrete	plural	thing	американок	genitive	animate
rags	тряпка	concrete	plural	thing	тряпки	accusative	inanimate
Americans	американка	concrete	plural	thing	американок	accusative	animate
room	комната	concrete	feminine	thing	комнатой	instrumental	inanimate
dictations	диктант	concrete	plural	thing	диктанты	accusative	inanimate
Shchorsk	Щорск	proper	masculine	location	Щорск	nominative	inanimate
seas	море	concrete	plural	location	морям	dative	inanimate
notepads	тетрадь	concrete	plural	thing	тетрадями	instrumental	inanimate
teachers	преподаватель	concrete	plural	thing	преподаватели	nominative	animate
ones	одна	abstract	plural	thing	одни	nominative	animate
America	Америка	proper	feminine	location	Америку	accusative	inanimate
Genevas	Женева	proper	plural	location	Женевам	dative	inanimate
briefcases	портфель	concrete	plural	thing	портфели	nominative	inanimate
mistakes	ошибка	abstract	plural	thing	ошибки	nominative	inanimate
Berlin	Берлин	proper	masculine	location	Берлин	nominative	inanimate
questions	вопрос	concrete	plural	thing	вопросы	accusative	inanimate
judge	судья	concrete	masculine	thing	судьы	genitive	animate
dictation	диктант	concrete	masculine	thing	диктантом	instrumental	inanimate
building	здание	concrete	nueter	thing	зданию	dative	inanimate
mothers	мать	concrete	plural	thing	матерей	accusative	animate
Russians	русская	proper	plural	thing	русских	prepositional	animate
libraries	библиотека	concrete	plural	location	библиотеках	prepositional	inanimate
Americans	американец	concrete	plural	thing	американцах	prepositional	animate
students	студентка	concrete	plural	thing	студентками	instrumental	animate
exams	экзамен	concrete	plural	thing	экзамены	nominative	inanimate
teachers	преподавательница	concrete	plural	thing	преподавательниц	genitive	animate
language	язык	concrete	masculine	thing	языком	instrumental	inanimate
ballpoint pens	авторучка	concrete	plural	thing	авторучках	prepositional	inanimate
Chita	Чита	proper	feminine	location	Чите	dative	inanimate
exercises	упражнение	concrete	plural	thing	упражнения	accusative	inanimate
tardinesses	опоздание	abstract	plural	thing	опозданиях	prepositional	inanimate
request	просьба	concrete	feminine	thing	просьбе	prepositional	inanimate
chalks	мел	concrete	plural	thing	мелов	genitive	inanimate
notebooks	блокнот	concrete	plural	thing	блокноты	accusative	inanimate
map	карта	concrete	feminine	thing	карта	nominative	inanimate
nationality	национальность	abstract	feminine	thing	национальность	nominative	inanimate
mercy	пощада	concrete	feminine	thing	пощаду	accusative	inanimate
nights	ночь	abstract	plural	thing	ночи	accusative	inanimate
pen	ручка	concrete	feminine	thing	ручку	accusative	inanimate
theater	театр	concrete	masculine	location	театру	dative	inanimate
foreigner	иностранка	concrete	feminine	location	иностранкой	instrumental	animate
countryside	деревня	concrete	feminine	location	деревной	instrumental	inanimate
affairs	дело	abstract	plural	thing	дел	genitive	inanimate
equators	экватор	concrete	plural	thing	экваторами	instrumental	inanimate
teachers	преподавательница	concrete	plural	thing	преподавательниц	accusative	animate
bread	хлеб	collective	masculine	thing	хлебе	prepositional	inanimate
countryside	деревня	concrete	feminine	location	деревны	genitive	inanimate
surname	фамилия	concrete	feminine	thing	фамилию	accusative	inanimate
Volgas	Волга	proper	plural	location	Волгам	dative	inanimate
mothers	мать	concrete	plural	thing	матерей	genitive	animate
truths	правда	abstract	plural	thing	правдах	prepositional	inanimate
notepad	тетрадь	concrete	masculine	thing	тетрадь	nominative	inanimate
maps	карта	concrete	plural	thing	карт	genitive	inanimate
notepad	тетрадь	concrete	masculine	thing	тетрадь	accusative	inanimate
library	библиотека	concrete	feminine	location	библиотека	nominative	inanimate
Odessa	Одесса	proper	feminine	location	Одессу	accusative	inanimate
house	дом	concrete	masculine	thing	дому	dative	inanimate
ballpoint pen	авторучка	concrete	feminine	thing	авторучкой	instrumental	inanimate
museums	музей	concrete	plural	location	музеев	genitive	inanimate
Philadelphia	Филадельфия	proper	feminine	location	Филадельфия	nominative	inanimate
missus	госпожа	concrete	plural	thing	госпожами	instrumental	animate
nights	ночь	abstract	plural	thing	ночи	nominative	inanimate
request	просьба	concrete	feminine	thing	просьба	nominative	inanimate
effort	труд	abstract	masculine	thing	труда	genitive	inanimate
teacher	преподавательница	concrete	feminine	thing	преподавательницой	instrumental	animate
daughter	дочь	concrete	feminine	thing	дочерью	instrumental	animate
notebooks	блокнот	concrete	plural	thing	блокноты	nominative	inanimate
continuation	продолжение	abstract	nueter	thing	продолжению	dative	inanimate
nationality	национальность	abstract	feminine	thing	национальность	accusative	inanimate
exercise	упражнение	concrete	nueter	thing	упражнения	genitive	inanimate
mistake	ошибка	abstract	feminine	thing	ошибку	accusative	inanimate
exercises	упражнение	concrete	plural	thing	упражнения	nominative	inanimate
shore	берег	concrete	masculine	location	берегом	instrumental	inanimate
exams	экзамен	concrete	plural	thing	экзамены	accusative	inanimate
pens	перо	concrete	plural	thing	перам	dative	inanimate
seas	море	concrete	plural	location	морями	instrumental	inanimate
Yeniseis	Енисей	proper	plural	location	Енисеям	dative	inanimate
descents	съезд	concrete	plural	location	съездов	genitive	inanimate
Genevas	Женева	proper	plural	location	Женевами	instrumental	inanimate
guest	гость	concrete	masculine	thing	гостя	genitive	animate
daughter	дочь	concrete	feminine	thing	дочерь	nominative	animate
atoms	атом	concrete	plural	thing	атомов	genitive	inanimate
ones	одна	abstract	plural	thing	одни	accusative	inanimate
pencil eraser	резинка	concrete	plural	thing	резинк	genitive	inanimate
days	день	concrete	plural	thing	дни	nominative	inanimate
Leningrads	Ленинград	proper	plural	location	Ленинградами	instrumental	inanimate
chalk	мел	concrete	masculine	thing	мел	accusative	inanimate
Bolshoi	большой	proper	masculine	location	большом	prepositional	inanimate
men	мужчина	concrete	plural	thing	мужчин	accusative	animate
works	занятие	concrete	plural	thing	занятиями	instrumental	inanimate
pocket	карман	concrete	masculine	location	карман	nominative	inanimate
artists	артист	concrete	plural	thing	артистов	accusative	animate
cup	чашка	concrete	feminine	thing	чашку	accusative	inanimate
dining hall	столовая	concrete	feminine	location	столовой	genitive	inanimate
Russian	русская	proper	feminine	thing	русской	instrumental	animate
days	день	concrete	plural	thing	дням	dative	inanimate
briefcase	портфель	concrete	masculine	thing	портфеля	genitive	inanimate
cup	чашка	concrete	feminine	thing	чашке	dative	inanimate
friend	друг	concrete	masculine	thing	друга	genitive	animate
evening	вечер	abstract	masculine	thing	вечере	prepositional	inanimate
visit	свидание	abstract	nueter	thing	свидании	prepositional	inanimate
six	шесть	abstract	plural	thing	шести	prepositional	inanimate
aviators	авиатор	concrete	plural	thing	авиаторов	genitive	animate
teacher	учитель	concrete	masculine	thing	учителе	prepositional	animate
aviators	авиатор	concrete	plural	thing	авиаторов	accusative	animate
artists	артист	concrete	plural	thing	артисты	nominative	animate
Pavlov	Павлов	proper	masculine	thing	Павловом	instrumental	inanimate
Pavlov	Павлов	proper	masculine	thing	Павлову	dative	inanimate
friend	друг	concrete	masculine	thing	друга	accusative	animate
one	одно	abstract	nueter	thing	одном	prepositional	inanimate
row	ряд	concrete	masculine	thing	рядом	instrumental	inanimate
school	школа	concrete	feminine	thing	школа	nominative	inanimate
Stockholms	Стокгольм	proper	plural	location	Стокгольмов	genitive	inanimate
Kharkhov	Харьков	proper	masculine	location	Харьков	accusative	inanimate
people	человек	concrete	plural	thing	человеками	instrumental	animate
laboratory	лаборатория	concrete	feminine	location	лаборатории	dative	inanimate
blemish	пятно	concrete	nueter	thing	пятну	dative	inanimate
artists	артист	concrete	plural	thing	артистов	genitive	animate
men	мужчина	concrete	plural	thing	мужчин	genitive	animate
foreigners	иностранка	concrete	plural	location	иностранкам	dative	animate
Sheboygan	Шебойган	proper	masculine	location	Шебойган	accusative	inanimate
Berlins	Берлин	proper	plural	location	Берлины	nominative	inanimate
guest	гость	concrete	masculine	thing	гостя	accusative	animate
Berlins	Берлин	proper	plural	location	Берлины	accusative	inanimate
Sheboygan	Шебойган	proper	masculine	location	Шебойган	nominative	inanimate
Ulyanovsks	Уляновск	proper	plural	location	Уляновсками	instrumental	inanimate
Yalta	Ялта	proper	feminine	location	Ялты	genitive	inanimate
Odessas	Одесса	proper	plural	location	Одесс	genitive	inanimate
lesson	урок	concrete	masculine	thing	урока	genitive	inanimate
five	пять	abstract	plural	thing	пяти	dative	inanimate
Kharkhov	Харьков	proper	masculine	location	Харьков	nominative	inanimate
glasses	очки	concrete	plural	thing	очках	prepositional	inanimate
old man	серый	proper	masculine	thing	сером	prepositional	animate
meetings	собрание	abstract	plural	thing	собраниями	instrumental	inanimate
Russians	русский	proper	plural	thing	русскими	instrumental	animate
man	мужчина	concrete	feminine	thing	мужчине	prepositional	animate
vodkas	водка	collective	plural	thing	водками	instrumental	inanimate
numbers	номер	concrete	plural	thing	номерах	prepositional	inanimate
conversation	разговор	concrete	masculine	thing	разговора	genitive	inanimate
Russians	русские	concrete	plural	thing	русские	nominative	animate
pocket	карман	concrete	masculine	location	карман	accusative	inanimate
Rome	Рим	proper	masculine	location	Риме	prepositional	inanimate
Irtysh	Иртыш	proper	masculine	location	Иртыше	prepositional	inanimate
days	день	concrete	plural	thing	дни	accusative	inanimate
Dnepropetrovsks	Днепропетровск	proper	plural	location	Днепропетровсками	instrumental	inanimate
chalk	мел	concrete	masculine	thing	мел	nominative	inanimate
class	класс	concrete	masculine	thing	классе	prepositional	inanimate
Irtysh	Иртыш	proper	masculine	location	Иртышу	dative	inanimate
ones	одна	abstract	plural	thing	одни	nominative	inanimate
professors	профессор	concrete	plural	thing	профессорах	prepositional	animate
students	студентка	concrete	plural	thing	студенткам	dative	animate
daughter	дочь	concrete	feminine	thing	дочерь	accusative	animate
evening	вечер	abstract	masculine	thing	вечера	genitive	inanimate
teachers	преподавательница	concrete	plural	thing	преподавательницы	nominative	animate
six	шесть	abstract	plural	thing	шести	dative	inanimate
Russians	русская	proper	plural	thing	русским	dative	animate
Yugoslavias	Югославия	proper	plural	location	Югославиями	instrumental	inanimate
pen	перо	concrete	nueter	thing	перо	accusative	inanimate
cup	чашка	concrete	feminine	thing	чашке	prepositional	inanimate
flag	знамя	abstract	nueter	thing	знамя	accusative	inanimate
old man	серый	proper	plural	thing	серыми	instrumental	animate
uncles	дядя	concrete	plural	thing	дядьев	genitive	animate
breads	хлеб	collective	plural	thing	хлебы	nominative	inanimate
silk	шёлк	collective	masculine	thing	шёлке	prepositional	inanimate
Volga	Волга	proper	feminine	location	Волги	genitive	inanimate
first names	имя	abstract	plural	thing	имён	genitive	inanimate
building	здание	concrete	nueter	thing	здания	genitive	inanimate
nonsense	ерунда	abstract	feminine	thing	ерундой	instrumental	inanimate
professions	профессия	abstract	plural	thing	профессиям	dative	inanimate
one	одна	abstract	feminine	thing	одну	accusative	animate
notepads	тетрадь	concrete	plural	thing	тетрадях	prepositional	inanimate
center	центр	concrete	masculine	location	центру	dative	inanimate
Volga	Волга	proper	feminine	location	Волгой	instrumental	inanimate
uncles	дядя	concrete	plural	thing	дядьев	accusative	animate
mistake	ошибка	abstract	feminine	thing	ошибка	nominative	inanimate
ten	десять	abstract	plural	thing	десять	accusative	inanimate
continuation	продолжение	abstract	nueter	thing	продолжения	genitive	inanimate
Arkhangelsks	Архангелск	proper	plural	location	Архангелски	nominative	inanimate
Watsonville	Ватсонвиль	proper	masculine	location	Ватсонвиле	prepositional	inanimate
laboratory	лаборатория	concrete	feminine	location	лаборатории	prepositional	inanimate
Arkhangelsks	Архангелск	proper	plural	location	Архангелсками	instrumental	inanimate
teacher	учитель	concrete	masculine	thing	учителю	dative	animate
Berlin	Берлин	proper	masculine	location	Берлина	genitive	inanimate
eight	восемь	abstract	plural	thing	восьми	genitive	inanimate
Bolshoi	большой	proper	masculine	location	большой	nominative	inanimate
Berlin	Берлин	proper	masculine	location	Берлином	instrumental	inanimate
Yakutsk	Якутск	proper	masculine	location	Якутском	instrumental	inanimate
pens	перо	concrete	plural	thing	пер	genitive	inanimate
Gvardyesk	Гвардейск	proper	masculine	location	Гвардейска	genitive	inanimate
language	язык	concrete	masculine	thing	языке	prepositional	inanimate
Bolshoi	большой	proper	masculine	location	большой	accusative	inanimate
visits	свидание	abstract	plural	thing	свиданий	genitive	inanimate
five	пять	abstract	plural	thing	пяти	prepositional	inanimate
key	ключ	concrete	masculine	thing	ключе	prepositional	inanimate
works	занятие	concrete	plural	thing	занятиях	prepositional	inanimate
ten	десять	abstract	plural	thing	десять	nominative	inanimate
Arkhangelsks	Архангелск	proper	plural	location	Архангелски	accusative	inanimate
buildings	здание	concrete	plural	thing	зданиями	instrumental	inanimate
book	книга	concrete	feminine	thing	книги	genitive	inanimate
pupils	ученик	concrete	plural	thing	учениками	instrumental	animate
Ural	Урал	proper	masculine	location	Уралом	instrumental	inanimate
Vladivostoks	Владивосток	proper	plural	location	Владивостокей	genitive	inanimate
breads	хлеб	collective	plural	thing	хлебы	accusative	inanimate
fields	поле	concrete	plural	location	полям	dative	inanimate
New Yorks	Нью-Йорк	proper	plural	location	Нью-Йорками	instrumental	inanimate
chairs	стул	concrete	plural	thing	стулов	genitive	inanimate
man	мужчина	concrete	feminine	thing	мужчине	dative	animate
Dnepropetrovsks	Днепропетровск	proper	plural	location	Днепропетровсках	prepositional	inanimate
responses	отзыв	concrete	plural	thing	отзывам	dative	inanimate
flag	знамя	abstract	nueter	thing	знамя	nominative	inanimate
numbers	номер	concrete	plural	thing	номеров	genitive	inanimate
pen	перо	concrete	nueter	thing	перо	nominative	inanimate
Bolshoi	большой	proper	masculine	location	большого	genitive	inanimate
Leningrads	Ленинград	proper	plural	location	Ленинградов	genitive	inanimate
request	просьба	concrete	feminine	thing	просьбой	instrumental	inanimate
sea	море	concrete	nueter	location	море	prepositional	inanimate
libraries	библиотека	concrete	plural	location	библиотеками	instrumental	inanimate
Leningrad	Ленинград	proper	masculine	location	Ленинграде	prepositional	inanimate
zero	нуль	abstract	masculine	thing	нулю	dative	inanimate
request	просьба	concrete	feminine	thing	просьбе	dative	inanimate
student	студентка	concrete	feminine	thing	студенткой	instrumental	animate
Chita	Чита	proper	feminine	location	Чите	prepositional	inanimate
meats	мясо	collective	plural	thing	мяса	nominative	inanimate
times	пора	concrete	plural	thing	пор	genitive	inanimate
question	вопрос	concrete	masculine	thing	вопрос	nominative	inanimate
note	примечание	concrete	nueter	thing	примечание	nominative	inanimate
Londons	Лондон	proper	plural	location	Лондонами	instrumental	inanimate
Americas	Америка	proper	plural	location	Америк	genitive	inanimate
universities	университет	concrete	plural	location	университеты	nominative	inanimate
descents	съезд	concrete	plural	location	съездам	dative	inanimate
pencil eraser	резинка	concrete	feminine	thing	резинки	genitive	inanimate
money	деньги	collective	plural	thing	денег	genitive	inanimate
Yugoslavias	Югославия	proper	plural	location	Югославиях	prepositional	inanimate
lectures	лекция	abstract	plural	thing	лекции	accusative	inanimate
material	материал	concrete	masculine	thing	материал	accusative	inanimate
Bolshois	большой	proper	plural	location	большими	instrumental	inanimate
silk	шёлк	collective	masculine	thing	шёлком	instrumental	inanimate
judges	судья	concrete	plural	thing	судьями	instrumental	animate
time	раз	abstract	masculine	thing	раз	nominative	inanimate
foreigner	иностранец	concrete	masculine	thing	иностранцу	dative	animate
Yeniseis	Енисей	proper	plural	location	Енисеи	accusative	inanimate
earths	земля	concrete	plural	thing	землей	genitive	inanimate
questions	вопрос	concrete	plural	thing	вопросам	dative	inanimate
Riga	Рига	proper	feminine	location	Рига	nominative	inanimate
Genevas	Женева	proper	plural	location	Женев	genitive	inanimate
library	библиотека	concrete	feminine	location	библиотеки	genitive	inanimate
students	студент	concrete	plural	thing	студенты	nominative	animate
text	текст	concrete	masculine	thing	текста	genitive	inanimate
Boris	Борис	proper	masculine	thing	Борисе	prepositional	animate
notes	примечание	concrete	plural	thing	примечаний	genitive	inanimate
rooms	комната	concrete	plural	thing	комнатами	instrumental	inanimate
Yeniseis	Енисей	proper	plural	location	Енисеи	nominative	inanimate
time	раз	abstract	masculine	thing	раз	accusative	inanimate
articles	статья	concrete	plural	thing	статьях	prepositional	inanimate
lectures	лекция	abstract	plural	thing	лекции	nominative	inanimate
material	материал	concrete	masculine	thing	материал	nominative	inanimate
lessons	урок	concrete	plural	thing	урокей	genitive	inanimate
lecture	лекция	abstract	feminine	thing	лекцию	accusative	inanimate
text	текст	concrete	masculine	thing	тексте	prepositional	inanimate
universities	университет	concrete	plural	location	университеты	accusative	inanimate
time	раз	abstract	masculine	thing	разе	prepositional	inanimate
book	книга	concrete	feminine	thing	книгой	instrumental	inanimate
London	Лондон	proper	masculine	location	Лондона	genitive	inanimate
question	вопрос	concrete	masculine	thing	вопрос	accusative	inanimate
note	примечание	concrete	nueter	thing	примечание	accusative	inanimate
meats	мясо	collective	plural	thing	мяса	accusative	inanimate
pencil eraser	резинка	concrete	plural	thing	резинками	instrumental	inanimate
keys	ключ	concrete	plural	thing	ключов	genitive	inanimate
texts	текст	concrete	plural	thing	текстам	dative	inanimate
university	университет	concrete	masculine	location	университета	genitive	inanimate
Novgorods	Новгород	proper	plural	location	Новгородов	genitive	inanimate
uncles	дядя	concrete	plural	thing	дядьями	instrumental	animate
missus	госпожа	concrete	feminine	thing	госпожа	nominative	animate
questions	вопрос	concrete	plural	thing	вопросах	prepositional	inanimate
exams	экзамен	concrete	plural	thing	экзаменам	dative	inanimate
texts	текст	concrete	plural	thing	текстах	prepositional	inanimate
maps	карта	concrete	plural	thing	карты	accusative	inanimate
dictations	диктант	concrete	plural	thing	диктантах	prepositional	inanimate
Magnitogorsks	Магнитогорск	proper	plural	location	Магнитогорски	accusative	inanimate
daughter	дочь	concrete	feminine	thing	дочери	genitive	animate
dining halls	столовая	concrete	plural	location	столовым	dative	inanimate
blemish	пятно	concrete	nueter	thing	пятном	instrumental	inanimate
notepad	тетрадь	concrete	masculine	thing	тетрадя	genitive	inanimate
works	работа	abstract	plural	thing	работам	dative	inanimate
continuation	продолжение	abstract	nueter	thing	продолжении	prepositional	inanimate
Zagorsks	Загорск	proper	plural	location	Загорски	accusative	inanimate
Leningrad	Ленинград	proper	masculine	location	Ленинградом	instrumental	inanimate
Bolshois	большой	proper	plural	location	большие	nominative	inanimate
first names	имя	abstract	plural	thing	имена	accusative	inanimate
zeros	нуль	abstract	plural	thing	нулям	dative	inanimate
Yenisei	Енисей	proper	masculine	location	Енисея	genitive	inanimate
grandfather	дедушка	concrete	masculine	thing	дедушкой	instrumental	animate
nine	девять	abstract	plural	thing	девять	nominative	inanimate
mothers	мать	concrete	plural	thing	матерями	instrumental	animate
Baikals	Байкал	proper	plural	location	Байкалах	prepositional	inanimate
Arkhangelsk	Архангелск	proper	masculine	location	Архангелска	genitive	inanimate
London	Лондон	proper	masculine	location	Лондон	accusative	inanimate
notes	примечание	concrete	plural	thing	примечания	accusative	inanimate
daughters	дочь	concrete	plural	thing	дочерям	dative	animate
school	школа	concrete	feminine	thing	школе	dative	inanimate
foreigners	иностранец	concrete	plural	thing	иностранцах	prepositional	animate
foreigner	иностранка	concrete	feminine	location	иностранке	prepositional	animate
Americas	Америка	proper	plural	location	Америки	accusative	inanimate
keys	ключ	concrete	plural	thing	ключы	nominative	inanimate
requests	просьба	concrete	plural	thing	просьб	genitive	inanimate
visit	свидание	abstract	nueter	thing	свидание	nominative	inanimate
Magnitogorsks	Магнитогорск	proper	plural	location	Магнитогорсками	instrumental	inanimate
Gvardyesk	Гвардейск	proper	masculine	location	Гвардейск	accusative	inanimate
Geneva	Женева	proper	feminine	location	Женева	nominative	inanimate
Paris	Париж	proper	plural	location	Парижам	dative	inanimate
work	занятие	concrete	nueter	thing	занятию	dative	inanimate
Gvardyesk	Гвардейск	proper	masculine	location	Гвардейском	instrumental	inanimate
patronymic	отчество	concrete	nueter	thing	отчеством	instrumental	inanimate
rags	тряпка	concrete	plural	thing	тряпках	prepositional	inanimate
tables	стол	concrete	plural	thing	столами	instrumental	inanimate
library	библиотека	concrete	feminine	location	библиотеке	prepositional	inanimate
Gvardyesk	Гвардейск	proper	masculine	location	Гвардейск	nominative	inanimate
keys	ключ	concrete	plural	thing	ключы	accusative	inanimate
visit	свидание	abstract	nueter	thing	свидание	accusative	inanimate
ballpoint pens	авторучка	concrete	plural	thing	авторучками	instrumental	inanimate
nonsenses	ерунда	abstract	plural	thing	ерунд	genitive	inanimate
Americas	Америка	proper	plural	location	Америки	nominative	inanimate
pupil	ученица	concrete	feminine	thing	ученицы	genitive	animate
notes	примечание	concrete	plural	thing	примечания	nominative	inanimate
pupils	ученица	concrete	plural	thing	ученицам	dative	animate
Bolshois	большой	proper	plural	location	большим	dative	inanimate
Americans	американец	concrete	plural	thing	американцы	nominative	animate
Yenisei	Енисей	proper	masculine	location	Енисеем	instrumental	inanimate
London	Лондон	proper	masculine	location	Лондон	nominative	inanimate
nine	девять	abstract	plural	thing	девять	accusative	inanimate
engineer	инженер	concrete	masculine	thing	инженере	prepositional	animate
Bolshois	большой	proper	plural	location	большие	accusative	inanimate
pens	ручка	concrete	plural	thing	ручками	instrumental	inanimate
readings	чтение	abstract	plural	thing	чтениий	genitive	inanimate
first names	имя	abstract	plural	thing	имена	nominative	inanimate
Zagorsks	Загорск	proper	plural	location	Загорски	nominative	inanimate
two	два	abstract	plural	thing	двух	prepositional	inanimate
maps	карта	concrete	plural	thing	карты	nominative	inanimate
museum	музей	concrete	masculine	location	музеем	instrumental	inanimate
Magnitogorsks	Магнитогорск	proper	plural	location	Магнитогорски	nominative	inanimate
ten	десять	abstract	plural	thing	десятью	instrumental	inanimate
one	одно	abstract	nueter	thing	одному	dative	inanimate
chalk	мел	concrete	masculine	thing	мелу	dative	inanimate
tardiness	опоздание	abstract	nueter	thing	опоздания	genitive	inanimate
patronymic	отчество	concrete	nueter	thing	отчества	genitive	inanimate
articles	статья	concrete	plural	thing	статьи	nominative	inanimate
door	дверь	concrete	masculine	thing	дверя	genitive	inanimate
museums	музей	concrete	plural	location	музеях	prepositional	inanimate
notepads	тетрадь	concrete	plural	thing	тетрадям	dative	inanimate
text	текст	concrete	masculine	thing	тексту	dative	inanimate
guests	гость	concrete	plural	thing	гостей	accusative	animate
examples	пример	abstract	plural	thing	примеров	genitive	inanimate
languages	язык	concrete	plural	thing	языкам	dative	inanimate
conversation	разговор	concrete	masculine	thing	разговор	nominative	inanimate
class	класс	concrete	masculine	thing	класс	nominative	inanimate
visit	свидание	abstract	nueter	thing	свиданию	dative	inanimate
tardinesses	опоздание	abstract	plural	thing	опозданиями	instrumental	inanimate
zeros	нуль	abstract	plural	thing	нули	accusative	inanimate
Irtyshes	Иртыш	proper	plural	location	Иртыши	accusative	inanimate
pens	перо	concrete	plural	thing	перах	prepositional	inanimate
centers	центр	concrete	plural	location	центры	accusative	inanimate
judge	судья	concrete	masculine	thing	судье	prepositional	animate
tables	стол	concrete	plural	thing	столы	nominative	inanimate
accent	акцент	concrete	masculine	thing	акцентом	instrumental	inanimate
shore	берег	concrete	masculine	location	береге	prepositional	inanimate
book	книга	concrete	feminine	thing	книгу	accusative	inanimate
rows	ряд	concrete	plural	thing	рядами	instrumental	inanimate
seven	семь	abstract	plural	thing	семи	dative	inanimate
pocket	карман	concrete	masculine	location	кармане	prepositional	inanimate
doors	дверь	concrete	plural	thing	двери	accusative	inanimate
Urals	Урал	proper	plural	location	Уралов	genitive	inanimate
Moscows	Москва	proper	plural	location	Москвами	instrumental	inanimate
row	ряд	concrete	masculine	thing	ряду	dative	inanimate
response	отзыв	concrete	masculine	thing	отзыв	nominative	inanimate
student	студент	concrete	masculine	thing	студенту	dative	animate
meat	мясо	collective	nueter	thing	мясу	dative	inanimate
Tanya	Таня	proper	feminine	thing	Таня	nominative	animate
paper	бумага	concrete	feminine	thing	бумагу	accusative	inanimate
lessons	урок	concrete	plural	thing	уроками	instrumental	inanimate
guests	гость	concrete	plural	thing	гостей	genitive	animate
truths	правда	abstract	plural	thing	правдам	dative	inanimate
trips	поездка	abstract	plural	thing	поездок	genitive	inanimate
pencil	карандаш	concrete	masculine	thing	карандаш	accusative	inanimate
fields	поле	concrete	plural	location	полями	instrumental	inanimate
Baikal	Байкал	proper	masculine	location	Байкал	nominative	inanimate
pencil	карандаш	concrete	masculine	thing	карандаш	nominative	inanimate
Russians	русские	concrete	plural	thing	русских	accusative	animate
Tanyas	Таня	proper	plural	thing	Танях	prepositional	animate
Baikal	Байкал	proper	masculine	location	Байкал	accusative	inanimate
accents	акцент	concrete	plural	thing	акцентов	genitive	inanimate
vodkas	водка	collective	plural	thing	водк	genitive	inanimate
trip	поездка	abstract	feminine	thing	поездка	nominative	inanimate
pen	перо	concrete	nueter	thing	пера	genitive	inanimate
artist	артист	concrete	masculine	thing	артиста	accusative	animate
earth	земля	concrete	feminine	thing	земли	genitive	inanimate
teachers	преподаватель	concrete	plural	thing	преподавателях	prepositional	animate
Geneva	Женева	proper	feminine	location	Женеве	prepositional	inanimate
missus	госпожа	concrete	plural	thing	госпожах	prepositional	animate
person	человек	concrete	masculine	thing	человеке	prepositional	animate
response	отзыв	concrete	masculine	thing	отзыв	accusative	inanimate
meeting	собрание	abstract	nueter	thing	собранием	instrumental	inanimate
doors	дверь	concrete	plural	thing	двери	nominative	inanimate
Moscows	Москва	proper	plural	location	Москвах	prepositional	inanimate
tables	стол	concrete	plural	thing	столы	accusative	inanimate
centers	центр	concrete	plural	location	центры	nominative	inanimate
London	Лондон	proper	masculine	location	Лондоном	instrumental	inanimate
train stations	вокзал	concrete	plural	location	вокзалах	prepositional	inanimate
works	работа	abstract	plural	thing	работах	prepositional	inanimate
Sheboygans	Шебойган	proper	plural	location	Шебойганов	genitive	inanimate
Irtyshes	Иртыш	proper	plural	location	Иртыши	nominative	inanimate
zeros	нуль	abstract	plural	thing	нули	nominative	inanimate
artist	артист	concrete	masculine	thing	артиста	genitive	animate
conversation	разговор	concrete	masculine	thing	разговор	accusative	inanimate
class	класс	concrete	masculine	thing	класс	accusative	inanimate
articles	статья	concrete	plural	thing	статьи	accusative	inanimate
sea	море	concrete	nueter	location	морю	dative	inanimate
Russians	русские	concrete	plural	thing	русских	genitive	animate
student	студент	concrete	masculine	thing	студенте	prepositional	animate
missus	госпожа	concrete	feminine	thing	госпожу	accusative	animate
cities	города	concrete	plural	location	городах	prepositional	inanimate
flags	знамя	abstract	plural	thing	знамена	nominative	inanimate
pupil	ученица	concrete	feminine	thing	ученица	nominative	animate
judge	судья	concrete	masculine	thing	судье	dative	animate
three	три	abstract	plural	thing	три	accusative	inanimate
Geneva	Женева	proper	feminine	location	Женеву	accusative	inanimate
ones	одна	abstract	plural	thing	одних	accusative	animate
breads	хлеб	collective	plural	thing	хлебов	genitive	inanimate
grandfathers	дедушка	concrete	plural	thing	дедушками	instrumental	animate
chalks	мел	concrete	plural	thing	мелах	prepositional	inanimate
professor	профессор	concrete	masculine	thing	профессоре	prepositional	animate
Yakutsk	Якутск	proper	masculine	location	Якутск	nominative	inanimate
houses	дом	concrete	plural	thing	домов	genitive	inanimate
materials	материал	concrete	plural	thing	материалы	nominative	inanimate
answer	ответ	abstract	masculine	thing	ответе	prepositional	inanimate
chalks	мел	concrete	plural	thing	мелам	dative	inanimate
mercies	пощада	concrete	plural	thing	пощадам	dative	inanimate
Berlins	Берлин	proper	plural	location	Берлинам	dative	inanimate
Santa Cruz	Санта-Крус	proper	masculine	location	Санта-Крус	accusative	inanimate
vodkas	водка	collective	plural	thing	водкам	dative	inanimate
engineers	инженер	concrete	plural	thing	инженерам	dative	animate
misters	господин	concrete	plural	thing	господам	dative	animate
rags	тряпка	concrete	plural	thing	тряпкам	dative	inanimate
ones	одна	abstract	plural	thing	одних	genitive	animate
foreigners	иностранка	concrete	plural	location	иностранках	prepositional	animate
New Yorks	Нью-Йорк	proper	plural	location	Нью-Йорках	prepositional	inanimate
Odessas	Одесса	proper	plural	location	Одессах	prepositional	inanimate
houses	дом	concrete	plural	thing	домах	prepositional	inanimate
classes	класс	concrete	plural	thing	классы	nominative	inanimate
accent	акцент	concrete	masculine	thing	акцент	accusative	inanimate
shores	берег	concrete	plural	location	берегей	genitive	inanimate
Elbrus	Эльбрус	proper	plural	location	Эльбрусы	nominative	inanimate
article	статья	concrete	feminine	thing	статья	nominative	inanimate
seven	семь	abstract	plural	thing	семи	prepositional	inanimate
trips	поездка	abstract	plural	thing	поездками	instrumental	inanimate
room	комната	concrete	feminine	thing	комната	nominative	inanimate
Altai	Алтай	proper	masculine	location	Алтаю	dative	inanimate
readings	чтение	abstract	plural	thing	чтенииях	prepositional	inanimate
buildings	здание	concrete	plural	thing	зданиях	prepositional	inanimate
ones	один	abstract	plural	thing	одним	dative	inanimate
accent	акцент	concrete	masculine	thing	акцент	nominative	inanimate
classes	класс	concrete	plural	thing	классы	accusative	inanimate
three	три	abstract	plural	thing	трёх	prepositional	inanimate
Elbrus	Эльбрус	proper	plural	location	Эльбрусы	accusative	inanimate
Americans	американец	concrete	plural	thing	американцов	accusative	animate
men	мужчина	concrete	plural	thing	мужчинам	dative	animate
Philadelphias	Филадельфия	proper	plural	location	Филадельфиях	prepositional	inanimate
rows	ряд	concrete	plural	thing	рядам	dative	inanimate
keys	ключ	concrete	plural	thing	ключами	instrumental	inanimate
map	карта	concrete	feminine	thing	карту	accusative	inanimate
conversation	разговор	concrete	masculine	thing	разговором	instrumental	inanimate
Geneva	Женева	proper	feminine	location	Женеве	dative	inanimate
materials	материал	concrete	plural	thing	материалы	accusative	inanimate
conversation	разговор	concrete	masculine	thing	разговоре	prepositional	inanimate
Santa Cruz	Санта-Крус	proper	masculine	location	Санта-Крус	nominative	inanimate
teacher	учитель	concrete	masculine	thing	учителём	instrumental	animate
Yakutsk	Якутск	proper	masculine	location	Якутск	accusative	inanimate
Chitas	Чита	proper	plural	location	Читах	prepositional	inanimate
Americans	американец	concrete	plural	thing	американцов	genitive	animate
teas	чай	collective	plural	thing	чаев	genitive	inanimate
schools	школа	concrete	plural	thing	школах	prepositional	inanimate
three	три	abstract	plural	thing	три	nominative	inanimate
Boris	Борис	proper	plural	thing	Борисами	instrumental	animate
Madrids	Мадрид	proper	plural	location	Мадридах	prepositional	inanimate
text	текст	concrete	masculine	thing	текстом	instrumental	inanimate
silk	шёлк	collective	masculine	thing	шёлка	genitive	inanimate
truths	правда	abstract	plural	thing	правд	genitive	inanimate
Zagorsk	Загорск	proper	masculine	location	Загорске	prepositional	inanimate
flags	знамя	abstract	plural	thing	знамена	accusative	inanimate
daughters	дочь	concrete	plural	thing	дочери	nominative	animate
blackboards	доска	concrete	plural	thing	доски	accusative	inanimate
teacher	учительница	concrete	feminine	thing	учительницой	instrumental	animate
patronymics	отчество	concrete	plural	thing	отчества	nominative	inanimate
lectures	лекция	abstract	plural	thing	лекциях	prepositional	inanimate
Magnitogorsk	Магнитогорск	proper	masculine	location	Магнитогорск	accusative	inanimate
mistakes	ошибка	abstract	plural	thing	ошибк	genitive	inanimate
works	занятие	concrete	plural	thing	занятия	accusative	inanimate
teachers	учительница	concrete	plural	thing	учительницам	dative	animate
Madrid	Мадрид	proper	masculine	location	Мадрид	nominative	inanimate
reading	чтение	abstract	nueter	thing	чтениию	dative	inanimate
professions	профессия	abstract	plural	thing	профессии	nominative	inanimate
night	ночь	abstract	feminine	thing	ночи	genitive	inanimate
grandfather	дедушка	concrete	masculine	thing	дедушка	nominative	animate
ballpoint pens	авторучка	concrete	plural	thing	авторучк	genitive	inanimate
continuation	продолжение	abstract	nueter	thing	продолжение	accusative	inanimate
texts	текст	concrete	plural	thing	текстами	instrumental	inanimate
tables	стол	concrete	plural	thing	столам	dative	inanimate
Boris	Борис	proper	plural	thing	Борисов	accusative	animate
lecture	лекция	abstract	feminine	thing	лекции	genitive	inanimate
Boris	Борис	proper	plural	thing	Борисов	genitive	animate
school desk	парта	concrete	plural	thing	парт	genitive	inanimate
one	одна	abstract	feminine	thing	одной	instrumental	animate
Santa Cruz	Санта-Крус	proper	masculine	location	Санта-Крусе	prepositional	inanimate
Gvardyesks	Гвардейск	proper	plural	location	Гвардейсками	instrumental	inanimate
Ulyanovsk	Уляновск	proper	masculine	location	Уляновском	instrumental	inanimate
mothers	мать	concrete	plural	thing	матерях	prepositional	animate
Dneprs	Днепр	proper	plural	location	Днепры	accusative	inanimate
profession	профессия	abstract	feminine	thing	профессия	nominative	inanimate
student	студентка	concrete	feminine	thing	студентку	accusative	animate
theater	театр	concrete	masculine	location	театром	instrumental	inanimate
foreigner	иностранка	concrete	feminine	location	иностранке	dative	animate
school	школа	concrete	feminine	thing	школе	prepositional	inanimate
ones	одна	abstract	plural	thing	одних	prepositional	inanimate
dictionaries	словарь	concrete	plural	thing	словарями	instrumental	inanimate
ones	одна	abstract	plural	thing	одними	instrumental	animate
artist	артист	concrete	masculine	thing	артисте	prepositional	animate
Vladivostok	Владивосток	proper	masculine	location	Владивостока	genitive	inanimate
theaters	театр	concrete	plural	location	театрами	instrumental	inanimate
Shchorsks	Щорск	proper	plural	location	Щорсками	instrumental	inanimate
Baikal	Байкал	proper	masculine	location	Байкалу	dative	inanimate
Caucuses	Кавказ	proper	masculine	location	Кавказа	genitive	inanimate
Berlins	Берлин	proper	plural	location	Берлинах	prepositional	inanimate
Minneapolis	Миннеаполис	proper	masculine	location	Миннеаполисом	instrumental	inanimate
evening	вечер	abstract	masculine	thing	вечером	instrumental	inanimate
Dneprs	Днепр	proper	plural	location	Днепры	nominative	inanimate
joy	рад	abstract	masculine	thing	раду	dative	inanimate
nonsenses	ерунда	abstract	plural	thing	ерундах	prepositional	inanimate
library	библиотека	concrete	feminine	location	библиотеке	dative	inanimate
letter	письмо	concrete	nueter	thing	письму	dative	inanimate
fathers	отец	concrete	plural	thing	отцы	nominative	animate
continuation	продолжение	abstract	nueter	thing	продолжение	nominative	inanimate
mercy	пощада	concrete	feminine	thing	пощадой	instrumental	inanimate
Los Angeles	Лос-Анжелес	proper	masculine	location	Лос-Анжелесом	instrumental	inanimate
professors	профессор	concrete	plural	thing	профессоры	nominative	animate
Elbrus	Эльбрус	proper	masculine	location	Эльбрусе	prepositional	inanimate
professions	профессия	abstract	plural	thing	профессии	accusative	inanimate
dining halls	столовая	concrete	plural	location	столовых	prepositional	inanimate
works	занятие	concrete	plural	thing	занятия	nominative	inanimate
misters	господин	concrete	plural	thing	господами	instrumental	animate
Madrid	Мадрид	proper	masculine	location	Мадрид	accusative	inanimate
people	человек	concrete	plural	thing	человекы	nominative	animate
Berlins	Берлин	proper	plural	location	Берлинами	instrumental	inanimate
joy	рад	abstract	masculine	thing	рада	genitive	inanimate
chalk	мел	concrete	masculine	thing	мелом	instrumental	inanimate
patronymics	отчество	concrete	plural	thing	отчества	accusative	inanimate
Magnitogorsk	Магнитогорск	proper	masculine	location	Магнитогорск	nominative	inanimate
Rigas	Рига	proper	plural	location	Ригам	dative	inanimate
equator	экватор	concrete	masculine	thing	экватором	instrumental	inanimate
cups	чашка	concrete	plural	thing	чашками	instrumental	inanimate
Moscow	Москва	proper	feminine	location	Москва	nominative	inanimate
blackboards	доска	concrete	plural	thing	доски	nominative	inanimate
questions	вопрос	concrete	plural	thing	вопросами	instrumental	inanimate
Magnitogorsk	Магнитогорск	proper	masculine	location	Магнитогорске	prepositional	inanimate
Leningrad	Ленинград	proper	masculine	location	Ленинграду	dative	inanimate
affair	дело	abstract	nueter	thing	дела	genitive	inanimate
cup	чашка	concrete	feminine	thing	чашкой	instrumental	inanimate
teachers	учитель	concrete	plural	thing	учителях	prepositional	animate
cups	чашка	concrete	plural	thing	чашках	prepositional	inanimate
door	дверь	concrete	masculine	thing	двере	prepositional	inanimate
papers	бумага	concrete	plural	thing	бумагам	dative	inanimate
countrysides	деревня	concrete	plural	location	деревни	nominative	inanimate
descent	съезд	concrete	masculine	location	съезда	genitive	inanimate
request	просьба	concrete	feminine	thing	просьбы	genitive	inanimate
night	ночь	abstract	feminine	thing	ночи	prepositional	inanimate
meats	мясо	collective	plural	thing	мясам	dative	inanimate
Romes	Рим	proper	plural	location	Римов	genitive	inanimate
daughter	дочь	concrete	feminine	thing	дочери	dative	animate
Kharkhov	Харьков	proper	masculine	location	Харьковом	instrumental	inanimate
numbers	номер	concrete	plural	thing	номеры	nominative	inanimate
classes	класс	concrete	plural	thing	классов	genitive	inanimate
key	ключ	concrete	masculine	thing	ключом	instrumental	inanimate
sponges	губка	concrete	plural	thing	губк	genitive	inanimate
lecture	лекция	abstract	feminine	thing	лекции	prepositional	inanimate
countryside	деревня	concrete	feminine	location	деревне	prepositional	inanimate
pupils	ученик	concrete	plural	thing	ученикам	dative	animate
ones	одно	abstract	plural	thing	одним	dative	inanimate
schools	школа	concrete	plural	thing	школам	dative	inanimate
meetings	собрание	abstract	plural	thing	собрания	nominative	inanimate
Santa Cruz	Санта-Крус	proper	masculine	location	Санта-Крусом	instrumental	inanimate
Baikals	Байкал	proper	plural	location	Байкалов	genitive	inanimate
uncles	дядя	concrete	plural	thing	дядьям	dative	animate
first names	имя	abstract	plural	thing	именам	dative	inanimate
patronymics	отчество	concrete	plural	thing	отчествах	prepositional	inanimate
two	два	abstract	plural	thing	двумя	instrumental	inanimate
missus	госпожа	concrete	plural	thing	госпожи	nominative	animate
lectures	лекция	abstract	plural	thing	лекциям	dative	inanimate
university	университет	concrete	masculine	location	университет	accusative	inanimate
father	отец	concrete	masculine	thing	отцу	dative	animate
ones	одна	abstract	plural	thing	одних	genitive	inanimate
California	Калифория	proper	feminine	location	Калифорию	accusative	inanimate
Odessa	Одесса	proper	feminine	location	Одесса	nominative	inanimate
key	ключ	concrete	masculine	thing	ключа	genitive	inanimate
paper	бумага	concrete	feminine	thing	бумагой	instrumental	inanimate
university	университет	concrete	masculine	location	университет	nominative	inanimate
blemishes	пятно	concrete	plural	thing	пятнам	dative	inanimate
Dnepropetrovsk	Днепропетровск	proper	masculine	location	Днепропетровску	dative	inanimate
vodka	водка	collective	feminine	thing	водка	nominative	inanimate
exercises	упражнение	concrete	plural	thing	упражненией	genitive	inanimate
meat	мясо	collective	nueter	thing	мясе	prepositional	inanimate
Stockholm	Стокгольм	proper	masculine	location	Стокгольма	genitive	inanimate
foreigner	иностранка	concrete	feminine	location	иностранку	accusative	animate
meetings	собрание	abstract	plural	thing	собрания	accusative	inanimate
Leningrads	Ленинград	proper	plural	location	Ленинградам	dative	inanimate
daughters	дочь	concrete	plural	thing	дочерей	accusative	animate
bread	хлеб	collective	masculine	thing	хлеба	genitive	inanimate
museum	музей	concrete	masculine	location	музея	genitive	inanimate
work	работа	abstract	feminine	thing	работе	dative	inanimate
continuations	продолжение	abstract	plural	thing	продолжениями	instrumental	inanimate
Novgorods	Новгород	proper	plural	location	Новгородах	prepositional	inanimate
Berlin	Берлин	proper	masculine	location	Берлине	prepositional	inanimate
Los Angeles	Лос-Анжелес	proper	masculine	location	Лос-Анжелеса	genitive	inanimate
numbers	номер	concrete	plural	thing	номеры	accusative	inanimate
Santa Cruz	Санта-Крус	proper	masculine	location	Санта-Круса	genitive	inanimate
Minneapolis	Миннеаполис	proper	masculine	location	Миннеаполису	dative	inanimate
map	карта	concrete	feminine	thing	карте	prepositional	inanimate
daughters	дочь	concrete	plural	thing	дочерей	genitive	animate
pen	ручка	concrete	feminine	thing	ручка	nominative	inanimate
dining halls	столовая	concrete	plural	location	столовых	genitive	inanimate
countrysides	деревня	concrete	plural	location	деревни	accusative	inanimate
centers	центр	concrete	plural	location	центрами	instrumental	inanimate
responses	отзыв	concrete	plural	thing	отзывов	genitive	inanimate
pencil	карандаш	concrete	plural	thing	карандашах	prepositional	inanimate
Baikal	Байкал	proper	masculine	location	Байкалом	instrumental	inanimate
conversation	разговор	concrete	masculine	thing	разговору	dative	inanimate
money	деньги	collective	plural	thing	деньгами	instrumental	inanimate
maps	карта	concrete	plural	thing	картам	dative	inanimate
Russians	русские	concrete	plural	thing	русским	dative	animate
breads	хлеб	collective	plural	thing	хлебах	prepositional	inanimate
rag	тряпка	concrete	feminine	thing	тряпку	accusative	inanimate
guest	гость	concrete	masculine	thing	гостём	instrumental	animate
window	окно	concrete	nueter	thing	окно	nominative	inanimate
sponge	губка	concrete	feminine	thing	губке	prepositional	inanimate
meetings	собрание	abstract	plural	thing	собраниям	dative	inanimate
American	американка	concrete	feminine	thing	американке	dative	animate
dictionary	словарь	concrete	masculine	thing	словарь	nominative	inanimate
Boris	Борис	proper	masculine	thing	Борис	nominative	animate
tea	чай	collective	masculine	thing	чаем	instrumental	inanimate
Altai	Алтай	proper	masculine	location	Алтай	nominative	inanimate
people	человек	concrete	plural	thing	человеков	genitive	animate
Ural	Урал	proper	masculine	location	Уралу	dative	inanimate
laboratory	лаборатория	concrete	feminine	location	лабораторией	instrumental	inanimate
judges	судья	concrete	plural	thing	судьях	prepositional	animate
doors	дверь	concrete	plural	thing	дверей	genitive	inanimate
surname	фамилия	concrete	feminine	thing	фамилией	instrumental	inanimate
Moscow	Москва	proper	feminine	location	Москву	accusative	inanimate
building	здание	concrete	nueter	thing	здании	prepositional	inanimate
Ulyanovsk	Уляновск	proper	masculine	location	Уляновска	genitive	inanimate
ones	одна	abstract	plural	thing	одними	instrumental	inanimate
people	человек	concrete	plural	thing	человеков	accusative	animate
Americans	американец	concrete	plural	thing	американцами	instrumental	animate
ones	одна	abstract	plural	thing	одних	prepositional	animate
Bolshoi	большой	proper	masculine	location	большым	instrumental	inanimate
windows	окно	concrete	plural	thing	окна	accusative	inanimate
atom	атом	concrete	masculine	thing	атом	accusative	inanimate
chair	стул	concrete	masculine	thing	стулом	instrumental	inanimate
Irtyshes	Иртыш	proper	plural	location	Иртышам	dative	inanimate
one	одна	abstract	feminine	thing	одной	instrumental	inanimate
door	дверь	concrete	masculine	thing	дверь	nominative	inanimate
pencil eraser	резинка	concrete	feminine	thing	резинку	accusative	inanimate
seven	семь	abstract	plural	thing	семи	genitive	inanimate
America	Америка	proper	feminine	location	Америкой	instrumental	inanimate
grandfathers	дедушка	concrete	plural	thing	дедушкам	dative	animate
foreigners	иностранка	concrete	plural	location	иностранками	instrumental	animate
lesson	урок	concrete	masculine	thing	уроку	dative	inanimate
trips	поездка	abstract	plural	thing	поездкам	dative	inanimate
California	Калифория	proper	feminine	location	Калифория	nominative	inanimate
Volgas	Волга	proper	plural	location	Волгами	instrumental	inanimate
atom	атом	concrete	masculine	thing	атомом	instrumental	inanimate
three	три	abstract	plural	thing	трёх	genitive	inanimate
four	четыре	abstract	plural	thing	четырём	dative	inanimate
door	дверь	concrete	masculine	thing	дверь	accusative	inanimate
atom	атом	concrete	masculine	thing	атом	nominative	inanimate
windows	окно	concrete	plural	thing	окна	nominative	inanimate
friends	друг	concrete	plural	thing	друзьями	instrumental	animate
joys	рад	abstract	plural	thing	радам	dative	inanimate
one	одно	abstract	nueter	thing	одним	instrumental	inanimate
five	пять	abstract	plural	thing	пятью	instrumental	inanimate
doors	дверь	concrete	plural	thing	дверях	prepositional	inanimate
tardiness	опоздание	abstract	nueter	thing	опозданию	dative	inanimate
teachers	учительница	concrete	plural	thing	учительницах	prepositional	animate
times	раз	abstract	plural	thing	разов	genitive	inanimate
Dnepropetrovsks	Днепропетровск	proper	plural	location	Днепропетровскей	genitive	inanimate
museum	музей	concrete	masculine	location	музее	prepositional	inanimate
old man	серый	proper	masculine	thing	серый	nominative	animate
Tanya	Таня	proper	feminine	thing	Тане	dative	animate
old man	серый	proper	masculine	thing	серым	instrumental	animate
evenings	вечер	abstract	plural	thing	вечеров	genitive	inanimate
Altai	Алтай	proper	masculine	location	Алтай	accusative	inanimate
dictionary	словарь	concrete	masculine	thing	словарь	accusative	inanimate
Elbrus	Эльбрус	proper	masculine	location	Эльбруса	genitive	inanimate
vodka	водка	collective	feminine	thing	водки	genitive	inanimate
visit	свидание	abstract	nueter	thing	свидания	genitive	inanimate
window	окно	concrete	nueter	thing	окно	accusative	inanimate
Shchorsk	Щорск	proper	masculine	location	Щорску	dative	inanimate
blemish	пятно	concrete	nueter	thing	пятно	nominative	inanimate
fathers	отец	concrete	plural	thing	отцов	genitive	animate
days	день	concrete	plural	thing	днях	prepositional	inanimate
artist	артист	concrete	masculine	thing	артисту	dative	animate
teachers	учитель	concrete	plural	thing	учителям	dative	animate
blackboards	доска	concrete	plural	thing	досками	instrumental	inanimate
guest	гость	concrete	masculine	thing	гость	nominative	animate
American	американка	concrete	feminine	thing	американке	prepositional	animate
lesson	урок	concrete	masculine	thing	уроком	instrumental	inanimate
sponge	губка	concrete	feminine	thing	губке	dative	inanimate
works	работа	abstract	plural	thing	работ	genitive	inanimate
pencil	карандаш	concrete	plural	thing	карандаши	nominative	inanimate
lecture	лекция	abstract	feminine	thing	лекция	nominative	inanimate
money	деньги	collective	plural	thing	деньгам	dative	inanimate
work	занятие	concrete	nueter	thing	занятие	accusative	inanimate
atoms	атом	concrete	plural	thing	атомы	accusative	inanimate
person	человек	concrete	masculine	thing	человеком	instrumental	animate
mother	мать	concrete	feminine	thing	мать	nominative	animate
accent	акцент	concrete	masculine	thing	акцента	genitive	inanimate
Madrids	Мадрид	proper	plural	location	Мадридов	genitive	inanimate
times	раз	abstract	plural	thing	разы	accusative	inanimate
shore	берег	concrete	masculine	location	берег	nominative	inanimate
chairs	стул	concrete	plural	thing	стулах	prepositional	inanimate
Novgorods	Новгород	proper	plural	location	Новгороды	nominative	inanimate
responses	отзыв	concrete	plural	thing	отзывы	nominative	inanimate
uncle	дядя	concrete	masculine	thing	дяду	accusative	animate
fathers	отец	concrete	plural	thing	отцов	accusative	animate
responses	отзыв	concrete	plural	thing	отзывах	prepositional	inanimate
buildings	здание	concrete	plural	thing	зданий	genitive	inanimate
Novgorods	Новгород	proper	plural	location	Новгороды	accusative	inanimate
responses	отзыв	concrete	plural	thing	отзывы	accusative	inanimate
Watsonvilles	Ватсонвиль	proper	plural	location	Ватсонвилями	instrumental	inanimate
times	раз	abstract	plural	thing	разах	prepositional	inanimate
times	раз	abstract	plural	thing	разы	nominative	inanimate
foreigner	иностранец	concrete	masculine	thing	иностранца	accusative	animate
shore	берег	concrete	masculine	location	берег	accusative	inanimate
museums	музей	concrete	plural	location	музеями	instrumental	inanimate
schools	школа	concrete	plural	thing	школ	genitive	inanimate
teacher	учитель	concrete	masculine	thing	учитель	nominative	animate
evenings	вечер	abstract	plural	thing	вечерах	prepositional	inanimate
mother	мать	concrete	feminine	thing	мать	accusative	animate
teachers	учительница	concrete	plural	thing	учительницы	nominative	animate
person	человек	concrete	masculine	thing	человек	nominative	animate
nights	ночь	abstract	plural	thing	ночам	dative	inanimate
atoms	атом	concrete	plural	thing	атомы	nominative	inanimate
person	человек	concrete	masculine	thing	человека	genitive	animate
pencil	карандаш	concrete	plural	thing	карандаши	accusative	inanimate
person	человек	concrete	masculine	thing	человека	accusative	animate
work	занятие	concrete	nueter	thing	занятие	nominative	inanimate
one	одно	abstract	nueter	thing	одного	genitive	inanimate
mothers	мать	concrete	plural	thing	матери	nominative	animate
guests	гость	concrete	plural	thing	гостями	instrumental	animate
pockets	карман	concrete	plural	location	карманами	instrumental	inanimate
descents	съезд	concrete	plural	location	съездах	prepositional	inanimate
examples	пример	abstract	plural	thing	примерам	dative	inanimate
foreigner	иностранец	concrete	masculine	thing	иностранца	genitive	animate
profession	профессия	abstract	feminine	thing	профессию	accusative	inanimate
laboratories	лаборатория	concrete	plural	location	лабораториях	prepositional	inanimate
students	студентка	concrete	plural	thing	студентки	nominative	animate
Tanya	Таня	proper	feminine	thing	Тане	prepositional	animate
descent	съезд	concrete	masculine	location	съезде	prepositional	inanimate
Americans	американка	concrete	plural	thing	американками	instrumental	animate
blemish	пятно	concrete	nueter	thing	пятно	accusative	inanimate
Russians	русские	concrete	plural	thing	русских	prepositional	animate
Minneapolis	Миннеаполис	proper	masculine	location	Миннеаполис	nominative	inanimate
blemishes	пятно	concrete	plural	thing	пятнами	instrumental	inanimate
seas	море	concrete	plural	location	морей	genitive	inanimate
Yenisei	Енисей	proper	masculine	location	Енисею	dative	inanimate
daughter	дочь	concrete	feminine	thing	дочери	prepositional	animate
book	книга	concrete	feminine	thing	книга	nominative	inanimate
Russians	русская	proper	plural	thing	русские	nominative	animate
joy	рад	abstract	masculine	thing	рад	nominative	inanimate
teachers	преподаватель	concrete	plural	thing	преподавателями	instrumental	animate
night	ночь	abstract	feminine	thing	ночи	dative	inanimate
father	отец	concrete	masculine	thing	отец	nominative	animate
seven	семь	abstract	plural	thing	семью	instrumental	inanimate
Stockholms	Стокгольм	proper	plural	location	Стокгольмам	dative	inanimate
Pavlovs	Павлов	proper	plural	thing	Павловыми	instrumental	inanimate
assignments	задание	abstract	plural	thing	заданиях	prepositional	inanimate
Londons	Лондон	proper	plural	location	Лондонов	genitive	inanimate
foreigners	иностранка	concrete	plural	location	иностранок	accusative	animate
rag	тряпка	concrete	feminine	thing	тряпка	nominative	inanimate
languages	язык	concrete	plural	thing	языками	instrumental	inanimate
Ulyanovsks	Уляновск	proper	plural	location	Уляновскей	genitive	inanimate
articles	статья	concrete	plural	thing	статьями	instrumental	inanimate
patronymic	отчество	concrete	nueter	thing	отчеству	dative	inanimate
sea	море	concrete	nueter	location	моря	genitive	inanimate
Arkhangelsk	Архангелск	proper	masculine	location	Архангелску	dative	inanimate
vodkas	водка	collective	plural	thing	водках	prepositional	inanimate
descents	съезд	concrete	plural	location	съезды	accusative	inanimate
foreigner	иностранец	concrete	masculine	thing	иностранец	nominative	animate
note	примечание	concrete	nueter	thing	примечании	prepositional	inanimate
atoms	атом	concrete	plural	thing	атомами	instrumental	inanimate
mercy	пощада	concrete	feminine	thing	пощады	genitive	inanimate
foreigners	иностранка	concrete	plural	location	иностранок	genitive	animate
laboratories	лаборатория	concrete	plural	location	лабораториями	instrumental	inanimate
first name	имя	abstract	nueter	thing	именем	instrumental	inanimate
conversations	разговор	concrete	plural	thing	разговоры	nominative	inanimate
countryside	деревня	concrete	feminine	location	деревне	dative	inanimate
Shchorsk	Щорск	proper	masculine	location	Щорском	instrumental	inanimate
question	ворпос	concrete	masculine	thing	ворпосом	instrumental	inanimate
lecture	лекция	abstract	feminine	thing	лекции	dative	inanimate
conversations	разговор	concrete	plural	thing	разговорах	prepositional	inanimate
American	американец	concrete	masculine	thing	американце	prepositional	animate
Dneprs	Днепр	proper	plural	location	Днепрами	instrumental	inanimate
pupil	ученик	concrete	masculine	thing	ученика	genitive	animate
work	работа	abstract	feminine	thing	работе	prepositional	inanimate
guests	гость	concrete	plural	thing	гости	nominative	animate
pupil	ученик	concrete	masculine	thing	ученик	nominative	animate
breads	хлеб	collective	plural	thing	хлебам	dative	inanimate
Russian	русский	proper	masculine	thing	русский	nominative	animate
patronymic	отчество	concrete	nueter	thing	отчестве	prepositional	inanimate
Madrids	Мадрид	proper	plural	location	Мадридам	dative	inanimate
conversations	разговор	concrete	plural	thing	разговоры	accusative	inanimate
Paris	Париж	proper	plural	location	Парижей	genitive	inanimate
Tanya	Таня	proper	feminine	thing	Таны	genitive	animate
countrysides	деревня	concrete	plural	location	деревнями	instrumental	inanimate
Caucuses	Кавказ	proper	plural	location	Кавказами	instrumental	inanimate
vodka	водка	collective	feminine	thing	водкой	instrumental	inanimate
descents	съезд	concrete	plural	location	съезды	nominative	inanimate
rows	ряд	concrete	plural	thing	рядов	genitive	inanimate
notebook	блокнот	concrete	masculine	thing	блокнота	genitive	inanimate
mister	господин	concrete	masculine	thing	господином	instrumental	animate
six	шесть	abstract	plural	thing	шестью	instrumental	inanimate
uncles	дядя	concrete	plural	thing	дядьях	prepositional	animate
visits	свидание	abstract	plural	thing	свиданиям	dative	inanimate
class	класс	concrete	masculine	thing	классом	instrumental	inanimate
teachers	преподавательница	concrete	plural	thing	преподавательницам	dative	animate
Leningrad	Ленинград	proper	masculine	location	Ленинграда	genitive	inanimate
London	Лондон	proper	masculine	location	Лондону	dative	inanimate
two	два	abstract	plural	thing	двух	genitive	inanimate
joy	рад	abstract	masculine	thing	рад	accusative	inanimate
windows	окно	concrete	plural	thing	окнами	instrumental	inanimate
requests	просьба	concrete	plural	thing	просьбам	dative	inanimate
map	карта	concrete	feminine	thing	карте	dative	inanimate
Magnitogorsk	Магнитогорск	proper	masculine	location	Магнитогорском	instrumental	inanimate
pupil	ученик	concrete	masculine	thing	ученика	accusative	animate
Minneapolis	Миннеаполис	proper	masculine	location	Миннеаполис	accusative	inanimate
chair	стул	concrete	masculine	thing	стулу	dative	inanimate
Minneapolis	Миннеаполис	proper	plural	location	Миннеаполисами	instrumental	inanimate
countrysides	деревня	concrete	plural	location	деревней	genitive	inanimate
Yakutsks	Якутск	proper	plural	location	Якутсками	instrumental	inanimate
Russian	русская	proper	feminine	thing	русской	dative	animate
Pavlovs	Павлов	proper	plural	thing	Павловах	prepositional	inanimate
earths	земля	concrete	plural	thing	землям	dative	inanimate
Caucuses	Кавказ	proper	masculine	location	Кавказ	nominative	inanimate
conversations	разговор	concrete	plural	thing	разговоров	genitive	inanimate
teacher	преподаватель	concrete	masculine	thing	преподавателём	instrumental	animate
Ural	Урал	proper	masculine	location	Урале	prepositional	inanimate
Yugoslavias	Югославия	proper	plural	location	Югославиям	dative	inanimate
Yakutsks	Якутск	proper	plural	location	Якутскам	dative	inanimate
engineers	инженер	concrete	plural	thing	инженеров	accusative	animate
Paris	Париж	proper	plural	location	Парижи	nominative	inanimate
zeros	нуль	abstract	plural	thing	нулях	prepositional	inanimate
Shchorsk	Щорск	proper	masculine	location	Щорске	prepositional	inanimate
university	университет	concrete	masculine	location	университете	prepositional	inanimate
note	примечание	concrete	nueter	thing	примечания	genitive	inanimate
effort	труд	abstract	masculine	thing	труде	prepositional	inanimate
times	раз	abstract	plural	thing	разам	dative	inanimate
Paris	Париж	proper	plural	location	Парижи	accusative	inanimate
nights	ночь	abstract	plural	thing	ночах	prepositional	inanimate
student	студент	concrete	masculine	thing	студента	accusative	animate
Altais	Алтай	proper	plural	location	Алтаями	instrumental	inanimate
Caucuses	Кавказ	proper	masculine	location	Кавказ	accusative	inanimate
aviator	авиатор	concrete	masculine	thing	авиатор	nominative	animate
Volgas	Волга	proper	plural	location	Волгах	prepositional	inanimate
field	поле	concrete	nueter	location	полем	instrumental	inanimate
Altais	Алтай	proper	plural	location	Алтаях	prepositional	inanimate
Zagorsk	Загорск	proper	masculine	location	Загорску	dative	inanimate
Rome	Рим	proper	masculine	location	Рим	accusative	inanimate
center	центр	concrete	masculine	location	центре	prepositional	inanimate
work	работа	abstract	feminine	thing	работа	nominative	inanimate
Dnepropetrovsk	Днепропетровск	proper	masculine	location	Днепропетровском	instrumental	inanimate
one	один	abstract	masculine	thing	одному	dative	inanimate
student	студентка	concrete	feminine	thing	студентка	nominative	animate
Tanyas	Таня	proper	plural	thing	Тани	nominative	animate
dictation	диктант	concrete	masculine	thing	диктант	accusative	inanimate
pocket	карман	concrete	masculine	location	кармана	genitive	inanimate
trips	поездка	abstract	plural	thing	поездки	nominative	inanimate
four	четыре	abstract	plural	thing	четырёх	prepositional	inanimate
effort	труд	abstract	masculine	thing	труд	accusative	inanimate
map	карта	concrete	feminine	thing	карты	genitive	inanimate
first name	имя	abstract	nueter	thing	имени	genitive	inanimate
laboratories	лаборатория	concrete	plural	location	лаборатории	nominative	inanimate
pupils	ученик	concrete	plural	thing	ученикей	genitive	animate
rooms	комната	concrete	plural	thing	комнатах	prepositional	inanimate
assignment	задание	abstract	nueter	thing	заданиию	dative	inanimate
old man	серый	proper	masculine	thing	серого	genitive	animate
foreigners	иностранец	concrete	plural	thing	иностранцы	nominative	animate
one	один	abstract	masculine	thing	одного	accusative	animate
answers	ответ	abstract	plural	thing	ответы	accusative	inanimate
Paris	Париж	proper	masculine	location	Парижу	dative	inanimate
mercy	пощада	concrete	feminine	thing	пощада	nominative	inanimate
answers	ответ	abstract	plural	thing	ответы	nominative	inanimate
Gvardyesks	Гвардейск	proper	plural	location	Гвардейскам	dative	inanimate
laboratories	лаборатория	concrete	plural	location	лаборатории	accusative	inanimate
teacher	преподаватель	concrete	masculine	thing	преподавателя	accusative	animate
Volga	Волга	proper	feminine	location	Волге	prepositional	inanimate
Sheboygan	Шебойган	proper	masculine	location	Шебойгану	dative	inanimate
effort	труд	abstract	masculine	thing	труд	nominative	inanimate
trips	поездка	abstract	plural	thing	поездки	accusative	inanimate
times	пора	concrete	plural	thing	порами	instrumental	inanimate
artist	артист	concrete	masculine	thing	артист	nominative	animate
Yaltas	Ялта	proper	plural	location	Ялтах	prepositional	inanimate
countrysides	деревня	concrete	plural	location	деревнях	prepositional	inanimate
book	книга	concrete	feminine	thing	книге	dative	inanimate
dictation	диктант	concrete	masculine	thing	диктант	nominative	inanimate
Rome	Рим	proper	masculine	location	Рим	nominative	inanimate
shore	берег	concrete	masculine	location	берегу	dative	inanimate
room	комната	concrete	feminine	thing	комнату	accusative	inanimate
school desk	парта	concrete	feminine	thing	парте	dative	inanimate
trip	поездка	abstract	feminine	thing	поездкой	instrumental	inanimate
city	города	concrete	feminine	location	городой	instrumental	inanimate
note	примечание	concrete	nueter	thing	примечанию	dative	inanimate
American	американка	concrete	feminine	thing	американки	genitive	animate
time	пора	concrete	feminine	thing	пора	nominative	inanimate
tardiness	опоздание	abstract	nueter	thing	опоздание	nominative	inanimate
pockets	карман	concrete	plural	location	карманах	prepositional	inanimate
lesson	урок	concrete	masculine	thing	урок	accusative	inanimate
American	американец	concrete	masculine	thing	американец	nominative	animate
Yeniseis	Енисей	proper	plural	location	Енисеев	genitive	inanimate
Ulyanovsk	Уляновск	proper	masculine	location	Уляновск	nominative	inanimate
Romes	Рим	proper	plural	location	Римы	nominative	inanimate
Los Angeles	Лос-Анжелес	proper	plural	location	Лос-Анжелесов	genitive	inanimate
patronymics	отчество	concrete	plural	thing	отчествами	instrumental	inanimate
exercise	упражнение	concrete	nueter	thing	упражнению	dative	inanimate
tardiness	опоздание	abstract	nueter	thing	опозданием	instrumental	inanimate
artists	артист	concrete	plural	thing	артистам	dative	animate
professor	профессор	concrete	masculine	thing	профессора	genitive	animate
evening	вечер	abstract	masculine	thing	вечер	nominative	inanimate
rag	тряпка	concrete	feminine	thing	тряпки	genitive	inanimate
American	американец	concrete	masculine	thing	американца	accusative	animate
surname	фамилия	concrete	feminine	thing	фамилии	genitive	inanimate
requests	просьба	concrete	plural	thing	просьбами	instrumental	inanimate
Minneapolis	Миннеаполис	proper	plural	location	Миннеаполисов	genitive	inanimate
pupils	ученица	concrete	plural	thing	ученицами	instrumental	animate
ones	один	abstract	plural	thing	одних	genitive	inanimate
paper	бумага	concrete	feminine	thing	бумаге	dative	inanimate
dining halls	столовая	concrete	plural	location	столовыми	instrumental	inanimate
fathers	отец	concrete	plural	thing	отцам	dative	animate
foreigners	иностранец	concrete	plural	thing	иностранцов	accusative	animate
pupil	ученица	concrete	feminine	thing	ученицу	accusative	animate
evening	вечер	abstract	masculine	thing	вечер	accusative	inanimate
ones	одна	abstract	plural	thing	одним	dative	animate
mother	мать	concrete	feminine	thing	матери	prepositional	animate
Californias	Калифория	proper	plural	location	Калифориях	prepositional	inanimate
Romes	Рим	proper	plural	location	Римы	accusative	inanimate
Ulyanovsk	Уляновск	proper	masculine	location	Уляновск	accusative	inanimate
tardiness	опоздание	abstract	nueter	thing	опоздание	accusative	inanimate
question	вопрос	concrete	masculine	thing	вопроса	genitive	inanimate
lesson	урок	concrete	masculine	thing	урок	nominative	inanimate
nine	девять	abstract	plural	thing	девяти	prepositional	inanimate
cups	чашка	concrete	plural	thing	чашк	genitive	inanimate
pencil eraser	резинка	concrete	feminine	thing	резинка	nominative	inanimate
article	статья	concrete	feminine	thing	статьи	genitive	inanimate
Arkhangelsks	Архангелск	proper	plural	location	Архангелсках	prepositional	inanimate
Philadelphia	Филадельфия	proper	feminine	location	Филадельфии	genitive	inanimate
chair	стул	concrete	masculine	thing	стуле	prepositional	inanimate
teas	чай	collective	plural	thing	чаям	dative	inanimate
truth	правда	abstract	feminine	thing	правдой	instrumental	inanimate
pencil eraser	резинка	concrete	plural	thing	резинкам	dative	inanimate
pens	ручка	concrete	plural	thing	ручках	prepositional	inanimate
evenings	вечер	abstract	plural	thing	вечеры	accusative	inanimate
meat	мясо	collective	nueter	thing	мясо	nominative	inanimate
Paris	Париж	proper	masculine	location	Париж	nominative	inanimate
Gvardyesks	Гвардейск	proper	plural	location	Гвардейски	accusative	inanimate
Dnepropetrovsks	Днепропетровск	proper	plural	location	Днепропетровски	accusative	inanimate
Yalta	Ялта	proper	feminine	location	Ялта	nominative	inanimate
accents	акцент	concrete	plural	thing	акценты	nominative	inanimate
reading	чтение	abstract	nueter	thing	чтениием	instrumental	inanimate
mistakes	ошибка	abstract	plural	thing	ошибками	instrumental	inanimate
\.


--
-- Data for Name: participles; Type: TABLE DATA; Schema: public; Owner: machinetrans
--

COPY participles (name, runame, variety, gender, objcase, animate, declension, enval, wordcase) FROM stdin;
to read	читать	present active	nueter	accusative	inanimate	читающее	reading	nominative
to read	читать	past passive	masculine	accusative	inanimate	читанным	read	instrumental
to read	читать	present active	masculine	accusative	inanimate	читающий	reading	accusative
to write	писать	past passive	plural	accusative	inanimate	писанными	written	instrumental
to write	писать	past passive	plural	accusative	inanimate	писанные	written	nominative
to write	писать	past passive	plural	accusative	inanimate	писанные	written	accusative
to read	читать	past active	nueter	accusative	inanimate	читавшим	was reading	instrumental
to read	читать	past passive	masculine	accusative	animate	читанный	read	nominative
to read	читать	past passive	plural	accusative	inanimate	читанных	read	prepositional
to read	читать	past passive	feminine	accusative	inanimate	читанной	read	prepositional
to read	читать	present active	masculine	accusative	animate	читающего	reading	accusative
to read	читать	present verbal adverb	masculine	accusative	animate	читая	is reading	nominative
to read	читать	present passive	nueter	accusative	inanimate	читаемого	being read	genitive
to write	писать	past passive	feminine	accusative	inanimate	писанную	written	accusative
to write	писать	past active	plural	accusative	animate	писавших	were writing	accusative
to read	читать	present active	nueter	accusative	inanimate	читающим	reading	instrumental
to write	писать	past active	feminine	accusative	inanimate	писавшей	was writing	prepositional
to write	писать	past active	plural	accusative	animate	писавших	were writing	genitive
to read	читать	present active	masculine	accusative	animate	читающего	reading	genitive
to read	читать	present passive	masculine	accusative	animate	читаемым	being read	instrumental
to read	читать	present passive	feminine	accusative	inanimate	читаемой	being read	genitive
to read	читать	past passive	masculine	accusative	inanimate	читанном	read	prepositional
to read	читать	present active	masculine	accusative	inanimate	читающий	reading	nominative
to read	читать	past passive	plural	accusative	animate	читанными	read	instrumental
to write	писать	present active	nueter	accusative	inanimate	пишущем	writing	prepositional
to read	читать	past active	masculine	accusative	animate	читавшему	was reading	dative
to read	читать	short past passive	masculine	accusative	animate	читан	read	nominative
to read	читать	present passive	masculine	accusative	inanimate	читаемом	being read	prepositional
to write	писать	past passive	plural	accusative	animate	писанных	written	prepositional
to read	читать	present active	nueter	accusative	inanimate	читающее	reading	accusative
to read	читать	past active	masculine	accusative	inanimate	читавший	was reading	nominative
to write	писать	present active	nueter	accusative	inanimate	пишущего	writing	genitive
to write	писать	past passive	nueter	accusative	inanimate	писанного	written	genitive
to read	читать	present passive	masculine	accusative	inanimate	читаемый	being read	nominative
to write	писать	past verbal adverb 2	masculine	accusative	animate	писавши	was writing	nominative
to read	читать	past active	plural	accusative	animate	читавших	were reading	genitive
to write	писать	past active	nueter	accusative	inanimate	писавшем	was writing	prepositional
to read	читать	present active	plural	accusative	animate	читающими	reading	instrumental
to write	писать	past active	masculine	accusative	animate	писавшим	was writing	instrumental
to read	читать	present active	masculine	accusative	animate	читающем	reading	prepositional
to read	читать	informal imperative	masculine	accusative	animate	читай	read	nominative
to write	писать	present active	masculine	accusative	animate	пишущим	writing	instrumental
to write	писать	past passive	nueter	accusative	inanimate	писанном	written	prepositional
to read	читать	past active	plural	accusative	animate	читавших	were reading	accusative
to read	читать	present active	plural	accusative	inanimate	читающим	reading	dative
to read	читать	present passive	nueter	accusative	inanimate	читаемое	being read	accusative
to read	читать	present passive	nueter	accusative	inanimate	читаемое	being read	nominative
to write	писать	past active	masculine	accusative	animate	писавшего	was writing	accusative
to read	читать	present passive	feminine	accusative	inanimate	читаемая	being read	nominative
to read	читать	short past passive	feminine	accusative	animate	читана	read	nominative
to read	читать	present active	plural	accusative	animate	читающих	reading	accusative
to read	читать	present passive	plural	accusative	inanimate	читаемых	being read	genitive
to write	писать	past passive	feminine	accusative	inanimate	писанной	written	dative
to read	читать	present active	masculine	accusative	inanimate	читающему	reading	dative
to read	читать	present active	plural	accusative	animate	читающих	reading	genitive
to write	писать	past active	nueter	accusative	inanimate	писавшему	was writing	dative
to read	читать	present passive	feminine	accusative	inanimate	читаемой	being read	instrumental
to read	читать	past active	masculine	accusative	inanimate	читавшего	was reading	genitive
to read	читать	present passive	masculine	accusative	inanimate	читаемый	being read	accusative
to write	писать	past passive	masculine	accusative	inanimate	писанным	written	instrumental
to write	писать	past active	masculine	accusative	animate	писавшего	was writing	genitive
to read	читать	past passive	plural	accusative	animate	читанных	read	prepositional
to read	читать	formal imperative	plural	accusative	animate	читайте	read	nominative
to read	читать	past passive	masculine	accusative	inanimate	читанный	read	nominative
to read	читать	past active	masculine	accusative	animate	читавший	was reading	nominative
to read	читать	present passive	masculine	accusative	animate	читаемом	being read	prepositional
to write	писать	past active	nueter	accusative	inanimate	писавшее	was writing	accusative
to write	писать	past passive	plural	accusative	inanimate	писанных	written	prepositional
to read	читать	past active	masculine	accusative	inanimate	читавшему	was reading	dative
to read	читать	past passive	masculine	accusative	animate	читанном	read	prepositional
to read	читать	present active	masculine	accusative	animate	читающий	reading	nominative
to read	читать	past passive	plural	accusative	inanimate	читанными	read	instrumental
to read	читать	past active	feminine	accusative	inanimate	читавшей	was reading	instrumental
to read	читать	present active	masculine	accusative	inanimate	читающего	reading	genitive
to read	читать	present passive	masculine	accusative	inanimate	читаемым	being read	instrumental
to write	писать	past active	plural	accusative	inanimate	писавших	were writing	genitive
to write	писать	past passive	feminine	accusative	inanimate	писанной	written	prepositional
to read	читать	present passive	nueter	accusative	inanimate	читаемому	being read	dative
to read	читать	past passive	masculine	accusative	animate	читанным	read	instrumental
to write	писать	present active	plural	accusative	animate	пишущих	writing	prepositional
to read	читать	present active	feminine	accusative	inanimate	читающей	reading	genitive
to write	писать	past active	nueter	accusative	inanimate	писавшее	was writing	nominative
to read	читать	past active	plural	accusative	inanimate	читавшим	were reading	dative
to write	писать	past passive	plural	accusative	animate	писанные	written	nominative
to write	писать	past passive	plural	accusative	animate	писанными	written	instrumental
to write	писать	present active	feminine	accusative	inanimate	пишущей	writing	genitive
to read	читать	past passive	masculine	accusative	inanimate	читанный	read	accusative
to read	читать	past active	plural	accusative	animate	читавшими	were reading	instrumental
to read	читать	present passive	plural	accusative	animate	читаемых	being read	genitive
to write	писать	present active	nueter	accusative	inanimate	пишущему	writing	dative
to read	читать	past active	masculine	accusative	animate	читавшего	was reading	accusative
to read	читать	past passive	nueter	accusative	inanimate	читанное	read	accusative
to write	писать	past active	masculine	accusative	inanimate	писавшего	was writing	genitive
to write	писать	past passive	masculine	accusative	animate	писанным	written	instrumental
to write	писать	short past passive	feminine	accusative	animate	писана	written	nominative
to read	читать	past active	feminine	accusative	inanimate	читавшей	was reading	genitive
to read	читать	past active	masculine	accusative	animate	читавшего	was reading	genitive
to read	читать	past passive	nueter	accusative	inanimate	читанному	read	dative
to write	писать	past passive	nueter	accusative	inanimate	писанное	written	accusative
to read	читать	present active	masculine	accusative	animate	читающему	reading	dative
to read	читать	present active	plural	accusative	inanimate	читающих	reading	genitive
to write	писать	past passive	nueter	accusative	inanimate	писанному	written	dative
to read	читать	present passive	plural	accusative	animate	читаемых	being read	accusative
to write	писать	past active	feminine	accusative	inanimate	писавшей	was writing	dative
to write	писать	short past passive	masculine	accusative	animate	писан	written	nominative
to read	читать	past active	feminine	accusative	inanimate	читавшюю	was reading	accusative
to read	читать	present passive	feminine	accusative	inanimate	читаемую	being read	accusative
to read	читать	past passive	feminine	accusative	inanimate	читанной	read	dative
to read	читать	present active	feminine	accusative	inanimate	читающей	reading	instrumental
to read	читать	present active	masculine	accusative	inanimate	читающем	reading	prepositional
to read	читать	present active	plural	accusative	inanimate	читающими	reading	instrumental
to write	писать	past active	masculine	accusative	inanimate	писавшим	was writing	instrumental
to write	писать	past passive	nueter	accusative	inanimate	писанное	written	nominative
to read	читать	past active	plural	accusative	inanimate	читавших	were reading	genitive
to read	читать	present passive	masculine	accusative	animate	читаемый	being read	nominative
to read	читать	past passive	nueter	accusative	inanimate	читанное	read	nominative
to read	читать	present active	plural	accusative	animate	читающим	reading	dative
to read	читать	past passive	nueter	accusative	inanimate	читанного	read	genitive
to write	писать	present active	feminine	accusative	inanimate	пишущей	writing	instrumental
to write	писать	present active	masculine	accusative	inanimate	пишущим	writing	instrumental
to read	читать	past active	masculine	accusative	inanimate	читавшим	was reading	instrumental
to read	читать	present passive	plural	accusative	animate	читаемых	being read	prepositional
to write	писать	past active	masculine	accusative	animate	писавший	was writing	nominative
to write	писать	formal imperative	plural	accusative	animate	пишите	write	nominative
to write	писать	present active	plural	accusative	animate	пишущим	writing	dative
to read	читать	past active	nueter	accusative	inanimate	читавшее	was reading	accusative
to write	писать	past active	plural	accusative	inanimate	писавшими	were writing	instrumental
to read	читать	present passive	plural	accusative	inanimate	читаемые	being read	nominative
to read	читать	present active	masculine	accusative	inanimate	читающим	reading	instrumental
to read	читать	present passive	masculine	accusative	inanimate	читаемого	being read	genitive
to read	читать	past active	feminine	accusative	inanimate	читавшей	was reading	prepositional
to read	читать	present active	feminine	accusative	inanimate	читающюю	reading	accusative
to read	читать	past passive	nueter	accusative	inanimate	читанном	read	prepositional
to read	читать	past active	plural	accusative	inanimate	читавшие	were reading	nominative
to write	писать	present active	masculine	accusative	inanimate	пишущем	writing	prepositional
to read	читать	present passive	plural	accusative	animate	читаемыми	being read	instrumental
to read	читать	present passive	nueter	accusative	inanimate	читаемом	being read	prepositional
to read	читать	present active	plural	accusative	inanimate	читающих	reading	prepositional
to read	читать	present active	plural	accusative	inanimate	читающие	reading	accusative
to write	писать	present active	masculine	accusative	inanimate	пишущего	writing	genitive
to write	писать	present verbal adverb	masculine	accusative	animate	пиша	is writing	nominative
to read	читать	present active	plural	accusative	inanimate	читающие	reading	nominative
to read	читать	past active	plural	accusative	inanimate	читавших	were reading	prepositional
to read	читать	past passive	nueter	accusative	inanimate	читанным	read	instrumental
to read	читать	past active	plural	accusative	inanimate	читавшие	were reading	accusative
to write	писать	past passive	plural	accusative	inanimate	писанным	written	dative
to read	читать	present passive	masculine	accusative	animate	читаемому	being read	dative
to write	писать	past passive	feminine	accusative	inanimate	писанной	written	instrumental
to write	писать	short past passive	plural	accusative	animate	писани	written	nominative
to write	писать	past active	feminine	accusative	inanimate	писавшюю	was writing	accusative
to read	читать	present passive	plural	accusative	inanimate	читаемые	being read	accusative
to read	читать	past active	nueter	accusative	inanimate	читавшее	was reading	nominative
to write	писать	past active	feminine	accusative	inanimate	писавшяя	was writing	nominative
to read	читать	present passive	feminine	accusative	inanimate	читаемой	being read	dative
to read	читать	past active	masculine	accusative	inanimate	читавшем	was reading	prepositional
to read	читать	past active	feminine	accusative	inanimate	читавшяя	was reading	nominative
to read	читать	past passive	plural	accusative	inanimate	читанные	read	nominative
to write	писать	present active	masculine	accusative	animate	пишущему	writing	dative
to read	читать	past passive	plural	accusative	animate	читанных	read	genitive
to write	писать	past active	plural	accusative	animate	писавшие	were writing	nominative
to read	читать	short past passive	nueter	accusative	animate	читано	read	nominative
to write	писать	short past passive	nueter	accusative	animate	писано	written	nominative
to write	писать	past active	plural	accusative	inanimate	писавшим	were writing	dative
to read	читать	past passive	masculine	accusative	animate	читанному	read	dative
to write	писать	past passive	masculine	accusative	inanimate	писанный	written	nominative
to write	писать	past passive	plural	accusative	inanimate	писанных	written	genitive
to read	читать	present active	nueter	accusative	inanimate	читающему	reading	dative
to write	писать	past active	masculine	accusative	inanimate	писавшему	was writing	dative
to write	писать	past passive	masculine	accusative	animate	писанному	written	dative
to read	читать	past active	nueter	accusative	inanimate	читавшего	was reading	genitive
to read	читать	past passive	plural	accusative	animate	читанных	read	accusative
to write	писать	past active	plural	accusative	inanimate	писавших	were writing	prepositional
to read	читать	past passive	plural	accusative	inanimate	читанным	read	dative
to write	писать	past passive	nueter	accusative	inanimate	писанным	written	instrumental
to write	писать	past passive	feminine	accusative	inanimate	писанной	written	genitive
to write	писать	past passive	masculine	accusative	inanimate	писанного	written	genitive
to read	читать	present passive	plural	accusative	animate	читаемым	being read	dative
to write	писать	past active	masculine	accusative	inanimate	писавшем	was writing	prepositional
to write	писать	present active	plural	accusative	animate	пишущих	writing	genitive
to read	читать	present active	feminine	accusative	inanimate	читающей	reading	prepositional
to read	читать	past passive	masculine	accusative	animate	читанного	read	accusative
to write	писать	past passive	masculine	accusative	inanimate	писанный	written	accusative
to write	писать	present active	plural	accusative	animate	пишущие	writing	nominative
to read	читать	past verbal adverb 1	masculine	accusative	animate	читав	was reading	nominative
to write	писать	informal imperative	masculine	accusative	animate	пиши	write	nominative
to write	писать	present active	masculine	accusative	animate	пишущий	writing	nominative
to read	читать	past passive	masculine	accusative	animate	читанного	read	genitive
to write	писать	present active	feminine	accusative	inanimate	пишущей	writing	prepositional
to write	писать	past passive	masculine	accusative	inanimate	писанном	written	prepositional
to write	писать	present active	plural	accusative	animate	пишущих	writing	accusative
to write	писать	present active	plural	accusative	animate	пишущими	writing	instrumental
to read	читать	past passive	plural	accusative	inanimate	читанные	read	accusative
to read	читать	present passive	masculine	accusative	inanimate	читаемому	being read	dative
to write	писать	past passive	plural	accusative	animate	писанным	written	dative
to read	читать	past active	plural	accusative	animate	читавших	were reading	prepositional
to read	читать	present active	plural	accusative	animate	читающие	reading	nominative
to write	писать	past active	masculine	accusative	inanimate	писавший	was writing	accusative
to read	читать	past passive	feminine	accusative	inanimate	читанную	read	accusative
to read	читать	past active	masculine	accusative	animate	читавшем	was reading	prepositional
to write	писать	present active	nueter	accusative	inanimate	пишущее	writing	accusative
to write	писать	past verbal adverb 1	masculine	accusative	animate	писав	was writing	nominative
to read	читать	present passive	masculine	accusative	animate	читаемого	being read	genitive
to write	писать	past active	feminine	accusative	inanimate	писавшей	was writing	instrumental
to read	читать	present active	masculine	accusative	animate	читающим	reading	instrumental
to read	читать	past passive	feminine	accusative	inanimate	читанной	read	instrumental
to read	читать	present active	feminine	accusative	inanimate	читающей	reading	dative
to read	читать	present passive	plural	accusative	animate	читаемые	being read	nominative
to write	писать	past active	plural	accusative	animate	писавшими	were writing	instrumental
to write	писать	present active	nueter	accusative	inanimate	пишущее	writing	nominative
to write	писать	present active	plural	accusative	inanimate	пишущим	writing	dative
to read	читать	present passive	plural	accusative	inanimate	читаемых	being read	prepositional
to write	писать	past active	masculine	accusative	inanimate	писавший	was writing	nominative
to write	писать	present active	masculine	accusative	animate	пишущего	writing	accusative
to read	читать	past active	masculine	accusative	animate	читавшим	was reading	instrumental
to write	писать	present active	feminine	accusative	inanimate	пишущюю	writing	accusative
to write	писать	present active	masculine	accusative	animate	пишущего	writing	genitive
to read	читать	past active	nueter	accusative	inanimate	читавшему	was reading	dative
to read	читать	present active	plural	accusative	animate	читающих	reading	prepositional
to read	читать	present active	nueter	accusative	inanimate	читающего	reading	genitive
to read	читать	present passive	nueter	accusative	inanimate	читаемым	being read	instrumental
to read	читать	present passive	plural	accusative	inanimate	читаемыми	being read	instrumental
to read	читать	past active	plural	accusative	animate	читавшие	were reading	nominative
to write	писать	present active	feminine	accusative	inanimate	пишущей	writing	dative
to write	писать	present active	masculine	accusative	animate	пишущем	writing	prepositional
to read	читать	present passive	masculine	accusative	animate	читаемого	being read	accusative
to write	писать	past active	nueter	accusative	inanimate	писавшим	was writing	instrumental
to write	писать	present active	plural	accusative	inanimate	пишущие	writing	nominative
to read	читать	present active	nueter	accusative	inanimate	читающем	reading	prepositional
to write	писать	present active	plural	accusative	inanimate	пишущих	writing	genitive
to write	писать	past passive	feminine	accusative	inanimate	писанная	written	nominative
to write	писать	past active	masculine	accusative	animate	писавшем	was writing	prepositional
to read	читать	present passive	plural	accusative	inanimate	читаемым	being read	dative
to write	писать	past passive	masculine	accusative	animate	писанного	written	genitive
to write	писать	past passive	masculine	accusative	animate	писанного	written	accusative
to write	писать	past active	plural	accusative	inanimate	писавшие	were writing	accusative
to write	писать	present active	plural	accusative	inanimate	пишущими	writing	instrumental
to read	читать	past active	feminine	accusative	inanimate	читавшей	was reading	dative
to read	читать	past passive	masculine	accusative	inanimate	читанного	read	genitive
to write	писать	past passive	masculine	accusative	animate	писанном	written	prepositional
to write	писать	present active	masculine	accusative	inanimate	пишущий	writing	nominative
to write	писать	present active	nueter	accusative	inanimate	пишущим	writing	instrumental
to read	читать	past verbal adverb 2	masculine	accusative	animate	читавши	was reading	nominative
to write	писать	present active	masculine	accusative	inanimate	пишущий	writing	accusative
to write	писать	present active	feminine	accusative	inanimate	пишущяя	writing	nominative
to write	писать	past passive	plural	accusative	animate	писанных	written	accusative
to read	читать	past passive	plural	accusative	inanimate	читанных	read	genitive
to write	писать	past active	plural	accusative	inanimate	писавшие	were writing	nominative
to read	читать	past passive	feminine	accusative	inanimate	читанной	read	genitive
to read	читать	present active	feminine	accusative	inanimate	читающяя	reading	nominative
to write	писать	present active	masculine	accusative	inanimate	пишущему	writing	dative
to read	читать	past passive	plural	accusative	animate	читанные	read	nominative
to write	писать	past active	feminine	accusative	inanimate	писавшей	was writing	genitive
to read	читать	past passive	plural	accusative	animate	читанным	read	dative
to write	писать	past active	nueter	accusative	inanimate	писавшего	was writing	genitive
to write	писать	past active	plural	accusative	animate	писавших	were writing	prepositional
to read	читать	present passive	feminine	accusative	inanimate	читаемой	being read	prepositional
to read	читать	past passive	feminine	accusative	inanimate	читанная	read	nominative
to write	писать	past active	masculine	accusative	animate	писавшему	was writing	dative
to write	писать	past passive	masculine	accusative	inanimate	писанному	written	dative
to read	читать	past passive	masculine	accusative	inanimate	читанному	read	dative
to write	писать	past passive	masculine	accusative	animate	писанный	written	nominative
to write	писать	past passive	plural	accusative	animate	писанных	written	genitive
to write	писать	present active	plural	accusative	inanimate	пишущие	writing	accusative
to write	писать	past active	plural	accusative	animate	писавшим	were writing	dative
to read	читать	past active	masculine	accusative	inanimate	читавший	was reading	accusative
to read	читать	past active	plural	accusative	animate	читавшим	were reading	dative
to read	читать	short past passive	plural	accusative	animate	читани	read	nominative
to write	писать	present active	plural	accusative	inanimate	пишущих	writing	prepositional
to read	читать	past active	plural	accusative	inanimate	читавшими	were reading	instrumental
to read	читать	past active	nueter	accusative	inanimate	читавшем	was reading	prepositional
\.


--
-- Data for Name: pastverbs; Type: TABLE DATA; Schema: public; Owner: machinetrans
--

COPY pastverbs (name, runame, tense, gender, conjugation, conjugationru, objcase, imperfective) FROM stdin;
to read	читать	simple past	feminine	was reading	читала	accusative	imperfective
to write	писать	simple past	plural	were writing	писали	accusative	imperfective
to write	писать	simple past	nueter	was writing	писало	accusative	imperfective
to read	читать	simple past	plural	were reading	читали	accusative	imperfective
to read	читать	simple past	masculine	was reading	читал	accusative	imperfective
to write	писать	simple past	masculine	was writing	писал	accusative	imperfective
to read	читать	simple past	nueter	was reading	читало	accusative	imperfective
to write	писать	simple past	feminine	was writing	писала	accusative	imperfective
\.


--
-- Data for Name: prepositions; Type: TABLE DATA; Schema: public; Owner: machinetrans
--

COPY prepositions (name, runame, variety, objcase) FROM stdin;
have	у	other	genitive
by	по	other	dative
until	до	time	genitive
for	для	other	genitive
for	за	other	accusative
into	в	place	accusative
onto	на	place	accusative
between	между	place	instrumental
\.


--
-- Data for Name: pronouns; Type: TABLE DATA; Schema: public; Owner: machinetrans
--

COPY pronouns (name, runame, variety, gender, declension, wordcase, animate) FROM stdin;
all	всё	inclusive	nueter	всё	nominative	inanimate
she	она	personal	masculine	ней	prepositional	animate
our	наши	possessive	plural	наши	nominative	animate
they	они	personal	masculine	ими	instrumental	animate
this	эти	demonstrative	plural	этих	prepositional	inanimate
mine	мой	possessive	masculine	моём	prepositional	animate
one's own	своя	possessive	feminine	своей	genitive	inanimate
your	ваши	possessive	plural	вашими	instrumental	inanimate
which	какоё	variety	nueter	какого	genitive	inanimate
your	ваше	possessive	nueter	ваше	accusative	inanimate
mine	мои	possessive	plural	моими	instrumental	animate
one's own	свой	possessive	masculine	своим	instrumental	inanimate
this	этот	demonstrative	masculine	этом	prepositional	animate
oneself	самый	reflexive	masculine	самый	nominative	inanimate
which	какой	variety	masculine	какой	nominative	inanimate
your	твои	possessive	plural	твои	nominative	animate
mine	мои	possessive	plural	мои	accusative	inanimate
whose	чей	interrogative	masculine	чей	nominative	animate
all	вся	inclusive	feminine	всей	dative	inanimate
our	наше	possessive	nueter	наше	nominative	inanimate
one's own	свои	possessive	plural	своим	dative	inanimate
our	наш	possessive	masculine	нашим	instrumental	animate
oneself	самое	reflexive	nueter	самом	prepositional	inanimate
our	наша	possessive	feminine	нашей	genitive	inanimate
one's own	своё	possessive	nueter	своё	nominative	inanimate
which	какой	variety	masculine	какому	dative	animate
this	тот	demonstrative	masculine	того	accusative	animate
oneself	самые	reflexive	plural	самих	prepositional	inanimate
one's own	своё	possessive	nueter	своё	accusative	inanimate
he	он	personal	masculine	ему	dative	animate
your	твой	possessive	masculine	твоим	instrumental	animate
your	ваш	possessive	masculine	вашим	instrumental	animate
one's own	свои	possessive	plural	своих	genitive	animate
your	твой	possessive	masculine	твой	nominative	animate
your	ваш	possessive	masculine	вашего	genitive	inanimate
our	наше	possessive	nueter	наше	accusative	inanimate
oneself	самая	reflexive	feminine	самой	dative	inanimate
mine	мои	possessive	plural	мои	nominative	inanimate
which	какие	variety	plural	какие	nominative	animate
this	те	demonstrative	plural	тех	prepositional	animate
this	та	demonstrative	feminine	той	dative	inanimate
whose	чьи	interrogative	plural	чьих	prepositional	inanimate
your	твой	possessive	masculine	твоего	genitive	animate
which	какой	variety	masculine	какой	accusative	inanimate
your	твой	possessive	masculine	твоего	accusative	animate
oneself	самый	reflexive	masculine	самый	accusative	inanimate
your	твои	possessive	plural	твоих	genitive	inanimate
oneself	самый	reflexive	masculine	самим	instrumental	animate
no one	никто	interrogative	masculine	никем	instrumental	animate
which	какой	variety	masculine	какого	genitive	inanimate
oneself	самые	reflexive	plural	самим	dative	animate
whose	чьи	interrogative	plural	чьи	nominative	animate
your	твоя	possessive	feminine	твоей	genitive	inanimate
your	ваше	possessive	nueter	ваше	nominative	inanimate
this	тот	demonstrative	masculine	тот	nominative	animate
all	весь	inclusive	masculine	всём	prepositional	animate
our	наши	possessive	plural	нашими	instrumental	inanimate
which	какие	variety	plural	каких	genitive	inanimate
what	что	interrogative	masculine	чего	genitive	animate
one's own	свои	possessive	plural	своих	accusative	animate
this	эта	demonstrative	feminine	этой	instrumental	inanimate
all	всё	inclusive	nueter	всё	accusative	inanimate
this	тот	demonstrative	masculine	того	genitive	animate
oneself	самый	reflexive	masculine	самому	dative	inanimate
oneself	самые	reflexive	plural	самые	nominative	animate
we	мы	personal	masculine	нам	dative	animate
this	то	demonstrative	nueter	того	genitive	inanimate
which	какоё	variety	nueter	каком	prepositional	inanimate
oneself	себя	reflexive	masculine	себе	dative	animate
one's own	свой	possessive	masculine	свой	nominative	inanimate
one's own	своя	possessive	feminine	своей	instrumental	inanimate
no one	никто	interrogative	masculine	никому	dative	animate
this	этот	demonstrative	masculine	этому	dative	animate
this	эти	demonstrative	plural	этих	genitive	animate
this	эти	demonstrative	plural	этих	accusative	animate
our	наша	possessive	feminine	нашей	instrumental	inanimate
this	эта	demonstrative	feminine	эта	nominative	inanimate
one's own	своя	possessive	feminine	своя	nominative	inanimate
which	какая	variety	feminine	какой	prepositional	inanimate
your	твоё	possessive	nueter	твоё	nominative	inanimate
this	эти	demonstrative	plural	эти	nominative	animate
whose	чья	interrogative	feminine	чьей	dative	inanimate
I	я	personal	masculine	я	nominative	animate
oneself	самый	reflexive	masculine	самом	prepositional	animate
which	какоё	variety	nueter	каким	instrumental	inanimate
whose	чья	interrogative	feminine	чья	nominative	inanimate
all	весь	inclusive	masculine	весь	nominative	inanimate
one's own	свои	possessive	plural	свои	nominative	inanimate
whose	чьи	interrogative	plural	чьим	dative	inanimate
oneself	самый	reflexive	masculine	самого	genitive	inanimate
all	весь	inclusive	masculine	весь	accusative	inanimate
all	весь	inclusive	masculine	всем	instrumental	inanimate
this	эта	demonstrative	feminine	эту	accusative	inanimate
whose	чьи	interrogative	plural	чьих	genitive	animate
this	те	demonstrative	plural	тех	genitive	inanimate
one's own	свои	possessive	plural	свои	accusative	inanimate
this	этот	demonstrative	masculine	этого	genitive	animate
one's own	свой	possessive	masculine	своём	prepositional	animate
whose	чей	interrogative	masculine	чьего	genitive	animate
your	твоё	possessive	nueter	твоё	accusative	inanimate
one's own	свои	possessive	plural	своих	prepositional	inanimate
all	весь	inclusive	masculine	всего	accusative	animate
our	наше	possessive	nueter	нашего	genitive	inanimate
mine	мои	possessive	plural	моим	dative	animate
your	ваш	possessive	masculine	вашему	dative	inanimate
you	вы	personal	masculine	вы	nominative	animate
oneself	самые	reflexive	plural	самих	genitive	animate
which	какие	variety	plural	какими	instrumental	animate
which	какой	variety	masculine	каким	instrumental	inanimate
all	весь	inclusive	masculine	всему	dative	animate
one's own	своё	possessive	nueter	своему	dative	inanimate
oneself	самое	reflexive	nueter	самим	instrumental	inanimate
which	какие	variety	plural	каких	prepositional	animate
this	эта	demonstrative	feminine	этой	genitive	inanimate
they	они	personal	masculine	они	nominative	animate
oneself	самые	reflexive	plural	самих	accusative	animate
this	эти	demonstrative	plural	этими	instrumental	inanimate
all	весь	inclusive	masculine	всего	genitive	animate
your	твоя	possessive	feminine	твоей	instrumental	inanimate
one's own	свой	possessive	masculine	свой	accusative	inanimate
our	наш	possessive	masculine	нашего	genitive	inanimate
which	какой	variety	masculine	каком	prepositional	inanimate
your	твои	possessive	plural	твоих	prepositional	animate
your	ваша	possessive	feminine	вашей	prepositional	inanimate
whose	чей	interrogative	masculine	чьего	accusative	animate
this	эти	demonstrative	plural	этим	dative	animate
your	твой	possessive	masculine	твоем	prepositional	inanimate
this	этот	demonstrative	masculine	этого	accusative	animate
whose	чьи	interrogative	plural	чьих	accusative	animate
oneself	самые	reflexive	plural	самими	instrumental	inanimate
this	те	demonstrative	plural	те	nominative	inanimate
your	твои	possessive	plural	твоим	dative	animate
what	что	interrogative	masculine	чём	prepositional	animate
your	ваши	possessive	plural	ваших	accusative	animate
one's own	свой	possessive	masculine	своему	dative	inanimate
mine	мои	possessive	plural	моих	genitive	animate
whose	чей	interrogative	masculine	чьём	prepositional	animate
oneself	себя	reflexive	masculine	себе	prepositional	animate
nothing	ничто	interrogative	masculine	ничто	nominative	animate
this	тот	demonstrative	masculine	тому	dative	inanimate
mine	мой	possessive	masculine	моего	genitive	animate
mine	мой	possessive	masculine	моего	accusative	animate
this	это	demonstrative	nueter	этим	instrumental	inanimate
your	ваш	possessive	masculine	вашем	prepositional	animate
whose	чья	interrogative	feminine	чьей	prepositional	inanimate
your	ваши	possessive	plural	вашим	dative	animate
mine	моя	possessive	feminine	моей	genitive	inanimate
your	ваши	possessive	plural	ваших	genitive	animate
which	какая	variety	feminine	какой	dative	inanimate
mine	мои	possessive	plural	моих	accusative	animate
which	какоё	variety	nueter	какоё	nominative	inanimate
what	что	interrogative	masculine	что	accusative	animate
oneself	себя	reflexive	masculine	собой	instrumental	animate
we	мы	personal	masculine	нами	instrumental	animate
whose	чей	interrogative	masculine	чьим	instrumental	animate
what	что	interrogative	masculine	что	nominative	animate
which	какоё	variety	nueter	какоё	accusative	inanimate
your	твоё	possessive	nueter	твоем	prepositional	inanimate
your	твои	possessive	plural	твоими	instrumental	animate
our	наш	possessive	masculine	нашем	prepositional	inanimate
your	ваше	possessive	nueter	вашего	genitive	inanimate
all	все	inclusive	plural	всех	genitive	inanimate
our	наши	possessive	plural	наших	accusative	animate
this	те	demonstrative	plural	тем	dative	animate
our	наши	possessive	plural	наших	genitive	animate
our	наше	possessive	nueter	нашем	prepositional	inanimate
this	то	demonstrative	nueter	тем	instrumental	inanimate
your	ваша	possessive	feminine	вашей	dative	inanimate
nothing	ничто	interrogative	masculine	ничто	accusative	animate
whose	чьё	interrogative	nueter	чьему	dative	inanimate
our	наша	possessive	feminine	наша	nominative	inanimate
this	то	demonstrative	nueter	том	prepositional	inanimate
this	те	demonstrative	plural	те	accusative	inanimate
no one	никто	interrogative	masculine	никого	accusative	animate
one's own	свои	possessive	plural	своими	instrumental	animate
all	все	inclusive	plural	всем	dative	animate
mine	мой	possessive	masculine	мой	accusative	inanimate
this	тот	demonstrative	masculine	том	prepositional	animate
you	ты	personal	masculine	тебя	genitive	animate
this	этот	demonstrative	masculine	этим	instrumental	inanimate
our	наш	possessive	masculine	наш	accusative	inanimate
we	мы	personal	masculine	нас	prepositional	animate
this	этот	demonstrative	masculine	этот	nominative	animate
which	какая	variety	feminine	какую	accusative	inanimate
one's own	свой	possessive	masculine	своего	accusative	animate
our	наши	possessive	plural	нашим	dative	inanimate
your	ваши	possessive	plural	ваши	accusative	inanimate
our	наш	possessive	masculine	нашему	dative	animate
this	тот	demonstrative	masculine	тем	instrumental	animate
mine	мои	possessive	plural	моих	prepositional	inanimate
mine	моё	possessive	nueter	моё	nominative	inanimate
your	ваши	possessive	plural	ваших	prepositional	inanimate
all	все	inclusive	plural	все	nominative	inanimate
they	они	personal	masculine	них	prepositional	animate
whose	чей	interrogative	masculine	чьему	dative	inanimate
this	это	demonstrative	nueter	этом	prepositional	inanimate
all	весь	inclusive	masculine	весь	nominative	animate
all	вся	inclusive	feminine	всей	prepositional	inanimate
one's own	свой	possessive	masculine	своего	genitive	animate
all	всё	inclusive	nueter	всем	instrumental	inanimate
mine	моя	possessive	feminine	моей	instrumental	inanimate
one's own	свои	possessive	plural	свои	nominative	animate
oneself	самый	reflexive	masculine	самом	prepositional	inanimate
your	ваш	possessive	masculine	ваш	nominative	animate
who	кто	interrogative	masculine	кого	genitive	animate
I	я	personal	masculine	мне	dative	animate
your	ваша	possessive	feminine	ваша	nominative	inanimate
this	те	demonstrative	plural	теми	instrumental	animate
which	какая	variety	feminine	какой	instrumental	inanimate
you	ты	personal	masculine	тебя	accusative	animate
oneself	себя	reflexive	masculine	себя	nominative	animate
this	эти	demonstrative	plural	эти	nominative	inanimate
no one	никто	interrogative	masculine	никого	genitive	animate
our	наша	possessive	feminine	нашей	prepositional	inanimate
your	ваш	possessive	masculine	вашему	dative	animate
oneself	самые	reflexive	plural	самих	genitive	inanimate
one's own	своя	possessive	feminine	свою	accusative	inanimate
who	кто	interrogative	masculine	ком	prepositional	animate
oneself	себя	reflexive	masculine	себя	accusative	animate
one's own	свои	possessive	plural	своих	prepositional	animate
this	эти	demonstrative	plural	эти	accusative	inanimate
your	ваше	possessive	nueter	вашему	dative	inanimate
our	наш	possessive	masculine	нашего	accusative	animate
mine	мои	possessive	plural	моим	dative	inanimate
all	весь	inclusive	masculine	всему	dative	inanimate
this	та	demonstrative	feminine	той	prepositional	inanimate
which	какие	variety	plural	какими	instrumental	inanimate
which	какой	variety	masculine	каким	instrumental	animate
you	вы	personal	masculine	вами	instrumental	animate
all	все	inclusive	plural	всех	prepositional	animate
oneself	самая	reflexive	feminine	самой	prepositional	inanimate
oneself	самый	reflexive	masculine	самого	genitive	animate
he	он	personal	masculine	он	nominative	animate
whose	чьи	interrogative	plural	чьим	dative	animate
all	весь	inclusive	masculine	всем	instrumental	animate
whose	чьи	interrogative	plural	чьими	instrumental	animate
this	те	demonstrative	plural	тех	genitive	animate
I	я	personal	masculine	мной	instrumental	animate
whose	чьи	interrogative	plural	чьих	genitive	inanimate
she	она	personal	masculine	она	nominative	animate
one's own	свой	possessive	masculine	своём	prepositional	inanimate
you	ты	personal	masculine	тебе	prepositional	animate
whose	чей	interrogative	masculine	чьего	genitive	inanimate
mine	моё	possessive	nueter	моему	dative	inanimate
mine	моё	possessive	nueter	моё	accusative	inanimate
all	все	inclusive	plural	все	accusative	inanimate
mine	мой	possessive	masculine	моим	instrumental	animate
this	этот	demonstrative	masculine	этого	genitive	inanimate
this	та	demonstrative	feminine	ту	accusative	inanimate
who	кто	interrogative	masculine	кем	instrumental	animate
your	твои	possessive	plural	твоих	prepositional	inanimate
your	ваши	possessive	plural	ваши	nominative	inanimate
your	ваша	possessive	feminine	вашу	accusative	inanimate
your	твой	possessive	masculine	твоем	prepositional	animate
this	эти	demonstrative	plural	этим	dative	inanimate
oneself	самые	reflexive	plural	самые	accusative	inanimate
oneself	самый	reflexive	masculine	самого	accusative	animate
whose	чьи	interrogative	plural	чьих	accusative	inanimate
you	вы	personal	masculine	вас	prepositional	animate
this	те	demonstrative	plural	тех	accusative	animate
whose	чьё	interrogative	nueter	чьё	accusative	inanimate
your	твой	possessive	masculine	твоему	dative	animate
she	она	personal	masculine	ей	dative	animate
your	ваша	possessive	feminine	вашей	instrumental	inanimate
which	какие	variety	plural	каким	dative	animate
your	твоя	possessive	feminine	твоей	prepositional	inanimate
our	наш	possessive	masculine	наш	nominative	inanimate
which	какие	variety	plural	каких	prepositional	inanimate
all	все	inclusive	plural	всеми	instrumental	inanimate
our	наши	possessive	plural	наших	prepositional	inanimate
oneself	себя	reflexive	masculine	себя	genitive	animate
one's own	своё	possessive	nueter	своим	instrumental	inanimate
all	весь	inclusive	masculine	всего	genitive	inanimate
our	наш	possessive	masculine	нашего	genitive	animate
which	какой	variety	masculine	каком	prepositional	animate
nothing	ничто	interrogative	masculine	ничему	dative	animate
this	эти	demonstrative	plural	этими	instrumental	animate
mine	мой	possessive	masculine	моему	dative	inanimate
mine	мой	possessive	masculine	мой	nominative	inanimate
this	тот	demonstrative	masculine	тому	dative	animate
this	то	demonstrative	nueter	то	nominative	inanimate
oneself	самое	reflexive	nueter	самое	nominative	inanimate
all	всё	inclusive	nueter	всём	prepositional	inanimate
we	мы	personal	masculine	нас	genitive	animate
mine	мой	possessive	masculine	моего	genitive	inanimate
your	твои	possessive	plural	твоим	dative	inanimate
oneself	самые	reflexive	plural	самими	instrumental	animate
all	вся	inclusive	feminine	всей	accusative	inanimate
this	те	demonstrative	plural	те	nominative	animate
one's own	своя	possessive	feminine	своей	dative	inanimate
whose	чей	interrogative	masculine	чьём	prepositional	inanimate
one's own	свой	possessive	masculine	своему	dative	animate
mine	мои	possessive	plural	моих	genitive	inanimate
your	ваши	possessive	plural	ваших	genitive	inanimate
whose	чья	interrogative	feminine	чью	accusative	inanimate
what	что	interrogative	masculine	чем	instrumental	animate
our	наша	possessive	feminine	нашей	dative	inanimate
your	ваши	possessive	plural	вашим	dative	inanimate
oneself	самая	reflexive	feminine	самая	nominative	inanimate
this	это	demonstrative	nueter	это	accusative	inanimate
I	я	personal	masculine	мне	prepositional	animate
mine	моё	possessive	nueter	моего	genitive	inanimate
whose	чья	interrogative	feminine	чьей	instrumental	inanimate
one's own	своё	possessive	nueter	своём	prepositional	inanimate
what	что	interrogative	masculine	чему	dative	animate
we	мы	personal	masculine	нас	accusative	animate
your	ваш	possessive	masculine	вашем	prepositional	inanimate
our	наш	possessive	masculine	нашем	prepositional	animate
your	твои	possessive	plural	твоими	instrumental	inanimate
you	ты	personal	masculine	тебе	dative	animate
your	ваше	possessive	nueter	вашим	instrumental	inanimate
this	та	demonstrative	feminine	той	genitive	inanimate
all	все	inclusive	plural	всех	genitive	animate
oneself	самая	reflexive	feminine	самой	genitive	inanimate
whose	чей	interrogative	masculine	чьим	instrumental	inanimate
mine	моя	possessive	feminine	моя	nominative	inanimate
they	они	personal	masculine	их	genitive	animate
this	это	demonstrative	nueter	это	nominative	inanimate
you	вы	personal	masculine	вас	accusative	animate
your	твоя	possessive	feminine	твою	accusative	inanimate
he	он	personal	masculine	нём	prepositional	animate
you	ты	personal	masculine	ты	nominative	animate
you	вы	personal	masculine	вас	genitive	animate
they	они	personal	masculine	их	accusative	animate
your	твоя	possessive	feminine	твоей	dative	inanimate
all	все	inclusive	plural	всех	accusative	animate
this	те	demonstrative	plural	тем	dative	inanimate
our	наши	possessive	plural	наших	genitive	inanimate
oneself	самое	reflexive	nueter	самое	accusative	inanimate
your	твоя	possessive	feminine	твоя	nominative	inanimate
this	та	demonstrative	feminine	та	nominative	inanimate
this	то	demonstrative	nueter	то	accusative	inanimate
mine	моя	possessive	feminine	мою	accusative	inanimate
whose	чьё	interrogative	nueter	чьим	instrumental	inanimate
we	мы	personal	masculine	мы	nominative	animate
mine	мои	possessive	plural	моих	prepositional	animate
this	тот	demonstrative	masculine	тем	instrumental	inanimate
our	наши	possessive	plural	нашим	dative	animate
our	наш	possessive	masculine	нашему	dative	inanimate
all	всё	inclusive	nueter	всего	genitive	inanimate
this	тот	demonstrative	masculine	том	prepositional	inanimate
one's own	свои	possessive	plural	своими	instrumental	inanimate
I	я	personal	masculine	меня	accusative	animate
all	все	inclusive	plural	всем	dative	inanimate
this	этот	demonstrative	masculine	этот	nominative	inanimate
which	какая	variety	feminine	какая	nominative	inanimate
this	этот	demonstrative	masculine	этим	instrumental	animate
all	всё	inclusive	nueter	всему	dative	inanimate
he	он	personal	masculine	им	instrumental	animate
this	те	demonstrative	plural	теми	instrumental	inanimate
I	я	personal	masculine	меня	genitive	animate
whose	чья	interrogative	feminine	чьей	genitive	inanimate
whose	чей	interrogative	masculine	чьему	dative	animate
our	наше	possessive	nueter	нашему	dative	inanimate
mine	моя	possessive	feminine	моей	prepositional	inanimate
your	ваши	possessive	plural	ваших	prepositional	animate
all	все	inclusive	plural	все	nominative	animate
all	вся	inclusive	feminine	всей	instrumental	inanimate
nothing	ничто	interrogative	masculine	ничем	instrumental	animate
your	ваш	possessive	masculine	ваш	nominative	inanimate
one's own	свой	possessive	masculine	своего	genitive	inanimate
whose	чьи	interrogative	plural	чьими	instrumental	inanimate
she	она	personal	masculine	её	genitive	animate
your	ваш	possessive	masculine	ваш	accusative	inanimate
mine	мой	possessive	masculine	моим	instrumental	inanimate
whose	чьё	interrogative	nueter	чьём	prepositional	inanimate
oneself	самая	reflexive	feminine	самой	instrumental	inanimate
this	та	demonstrative	feminine	той	instrumental	inanimate
all	все	inclusive	plural	всех	prepositional	inanimate
who	кто	interrogative	masculine	кто	nominative	animate
our	наш	possessive	masculine	наш	nominative	animate
all	все	inclusive	plural	всеми	instrumental	animate
our	наши	possessive	plural	наших	prepositional	animate
this	этот	demonstrative	masculine	этот	accusative	inanimate
nothing	ничто	interrogative	masculine	ничего	genitive	animate
mine	моё	possessive	nueter	моим	instrumental	inanimate
your	твоё	possessive	nueter	твоим	instrumental	inanimate
mine	мой	possessive	masculine	моему	dative	animate
mine	мой	possessive	masculine	мой	nominative	animate
your	ваши	possessive	plural	ваши	nominative	animate
this	то	demonstrative	nueter	тому	dative	inanimate
she	она	personal	masculine	ею	instrumental	animate
your	твоё	possessive	nueter	твоего	genitive	inanimate
she	она	personal	masculine	её	accusative	animate
your	твой	possessive	masculine	твоему	dative	inanimate
which	какие	variety	plural	каким	dative	inanimate
this	эта	demonstrative	feminine	этой	dative	inanimate
one's own	свой	possessive	masculine	своим	instrumental	animate
all	вся	inclusive	feminine	всю	genitive	inanimate
this	этот	demonstrative	masculine	этом	prepositional	inanimate
oneself	самый	reflexive	masculine	самый	nominative	animate
whose	чьё	interrogative	nueter	чьего	genitive	inanimate
our	наши	possessive	plural	наши	nominative	inanimate
oneself	самое	reflexive	nueter	самому	dative	inanimate
our	наше	possessive	nueter	нашим	instrumental	inanimate
mine	мои	possessive	plural	моими	instrumental	inanimate
this	тот	demonstrative	masculine	тот	accusative	inanimate
this	эти	demonstrative	plural	этих	prepositional	animate
your	ваши	possessive	plural	вашими	instrumental	animate
mine	мой	possessive	masculine	моём	prepositional	inanimate
oneself	самая	reflexive	feminine	самую	accusative	inanimate
your	твой	possessive	masculine	твой	accusative	inanimate
you	вы	personal	masculine	вам	dative	animate
whose	чей	interrogative	masculine	чей	nominative	inanimate
mine	моя	possessive	feminine	моей	dative	inanimate
our	наш	possessive	masculine	нашим	instrumental	inanimate
this	это	demonstrative	nueter	этому	dative	inanimate
your	ваше	possessive	nueter	вашем	prepositional	inanimate
which	какая	variety	feminine	какой	genitive	inanimate
one's own	свои	possessive	plural	своим	dative	animate
your	твои	possessive	plural	твои	nominative	inanimate
which	какой	variety	masculine	какой	nominative	animate
all	вся	inclusive	feminine	вся	nominative	inanimate
nothing	ничто	interrogative	masculine	ни о чём	prepositional	animate
which	какоё	variety	nueter	какому	dative	inanimate
no one	никто	interrogative	masculine	никто	nominative	animate
which	какие	variety	plural	какие	accusative	inanimate
mine	моё	possessive	nueter	моём	prepositional	inanimate
this	те	demonstrative	plural	тех	prepositional	inanimate
whose	чьи	interrogative	plural	чьих	prepositional	animate
mine	мои	possessive	plural	мои	nominative	animate
which	какой	variety	masculine	какого	accusative	animate
which	какие	variety	plural	какие	nominative	inanimate
your	твоё	possessive	nueter	твоему	dative	inanimate
your	твой	possessive	masculine	твоего	genitive	inanimate
your	твои	possessive	plural	твоих	accusative	animate
your	твои	possessive	plural	твои	accusative	inanimate
oneself	самое	reflexive	nueter	самого	genitive	inanimate
one's own	свои	possessive	plural	своих	genitive	inanimate
which	какой	variety	masculine	какому	dative	inanimate
one's own	своё	possessive	nueter	своего	genitive	inanimate
your	твой	possessive	masculine	твоим	instrumental	inanimate
your	ваш	possessive	masculine	вашим	instrumental	inanimate
oneself	самые	reflexive	plural	самих	prepositional	animate
he	он	personal	masculine	его	accusative	animate
whose	чей	interrogative	masculine	чей	accusative	inanimate
who	кто	interrogative	masculine	кому	dative	animate
your	ваш	possessive	masculine	вашего	genitive	animate
your	твой	possessive	masculine	твой	nominative	inanimate
which	какие	variety	plural	каких	accusative	animate
this	тот	demonstrative	masculine	тот	nominative	inanimate
all	весь	inclusive	masculine	всём	prepositional	inanimate
your	ваш	possessive	masculine	вашего	accusative	animate
our	наши	possessive	plural	нашими	instrumental	animate
which	какие	variety	plural	каких	genitive	animate
this	эта	demonstrative	feminine	этой	prepositional	inanimate
whose	чьи	interrogative	plural	чьи	nominative	inanimate
you	ты	personal	masculine	тобой	instrumental	animate
he	он	personal	masculine	его	genitive	animate
this	тот	demonstrative	masculine	того	genitive	inanimate
our	наши	possessive	plural	наши	accusative	inanimate
your	твои	possessive	plural	твоих	genitive	animate
oneself	самый	reflexive	masculine	самим	instrumental	inanimate
your	ваша	possessive	feminine	вашей	genitive	inanimate
which	какой	variety	masculine	какого	genitive	animate
oneself	самые	reflexive	plural	самим	dative	inanimate
no one	никто	interrogative	masculine	ни о ком	prepositional	animate
this	это	demonstrative	nueter	этого	genitive	inanimate
they	они	personal	masculine	им	dative	animate
one's own	свой	possessive	masculine	свой	nominative	animate
our	наша	possessive	feminine	нашу	accusative	inanimate
this	этот	demonstrative	masculine	этому	dative	inanimate
this	эти	demonstrative	plural	этих	genitive	inanimate
one's own	своя	possessive	feminine	своей	prepositional	inanimate
who	кто	interrogative	masculine	кого	accusative	animate
whose	чьё	interrogative	nueter	чьё	nominative	inanimate
oneself	самые	reflexive	plural	самые	nominative	inanimate
oneself	самый	reflexive	masculine	самому	dative	animate
\.


--
-- Data for Name: symbols; Type: TABLE DATA; Schema: public; Owner: machinetrans
--

COPY symbols (name, runame, variety) FROM stdin;
1	1	number
\.


--
-- Data for Name: verbs; Type: TABLE DATA; Schema: public; Owner: machinetrans
--

COPY verbs (name, runame, variety, tense, person, objcase, conjugationru, conjugation, imperfective) FROM stdin;
to write	писать	other	simple present	third	accusative	пишет	writes	imperfective
to read	читать	other	simple present	third	accusative	читает	reads	imperfective
to write	писать	other	simple present	first	accusative	пишу	write	imperfective
to read	читать	other	simple present	first	accusative	читаю	read	imperfective
to read	читать	other	simple present	plural second	accusative	читаете	read	imperfective
to write	писать	other	simple present	plural second	accusative	пишете	write	imperfective
to write	писать	other	simple present	plural third	accusative	пишут	write	imperfective
to read	читать	other	simple present	plural first	accusative	читаем	read	imperfective
to write	писать	other	simple present	second	accusative	пишешь	write	imperfective
to read	читать	other	simple present	plural third	accusative	читают	read	imperfective
to read	читать	other	simple present	second	accusative	читаешь	read	imperfective
to write	писать	other	simple present	plural first	accusative	пишем	write	imperfective
\.


--
-- PostgreSQL database dump complete
--

