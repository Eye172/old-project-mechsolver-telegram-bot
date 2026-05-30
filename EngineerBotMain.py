from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, CallbackContext
from EngineerBotsToken import botToken
from PIL import Image
import random
import math

bot = Bot(botToken)
updater = Updater(botToken, use_context=True)
dispatcher = updater.dispatcher 

command_list = [
    "/start", "/help", "/c", "/i",
    "/f1", "/f2", "/f3", "/f4", "/f5",
    "/f6", "/f7", "/f8", "/f9",
    "/f10", "/f11", "/f12", "/f13", "/f14", "/f15", "/f16", "/f17", "/f18"
]

prefixes_dictionary = {"а":-18, "ф":-15, "п":-12, "н":-9, "мк":-6, "м":-3, "с":-2, "д":-1,
                       "_":0,
                       "Э":18, "П":15, "Т":12, "Г":9, "М":6, "к":3, "г":2}

info_dictionary = {
    "Нормальное_напряжение": "σ – Отношение продольной силы к площади сечения; характеризует растяжение/сжатие [Па]",
    "Касательное_напряжение": "τ – Напряжение сдвига при кручении, срезе или комбинированной нагрузке [Па]",
    "Эквивалентное_напряжение": "σ_v – эквивалентное напряжение по критерию Мизеса [Па]",
    "Изгибающий_момент": "M – Внутренний момент, вызывающий изгиб элемента [Н·м]",
    "Крутящий_момент": "T – Внутренний момент, вызывающий кручение вокруг продольной оси [Н·м]",
    "Угол_закручивания": "φ – Разность углов поворота концов вала при кручении [рад]",
    "Прогиб_балки": "δ – Перемещение точки балки перпендикулярно оси под нагрузкой [м]",
    "Модуль_упругости": "E – Коэффициент пропорциональности σ/ε при растяжении (модуль Юнга) [Па]",
    "Модуль_сдвига": "G – Коэффициент пропорциональности τ/γ при сдвиге (shear modulus) [Па]",
    "Момент_инерции_сечения": "I – Геометрическая характеристика жёсткости сечения при изгибе [м⁴]",
    "Полярный_момент_инерции": "J – Геометрическая характеристика жёсткости сечения при кручении [м⁴]",
    "Площадь_сечения": "A – Площадь поперечного сечения детали [м²]",
    "Плотность_материала": "ρ – Масса материала в единице объёма [кг/м³]",
    "Длина_элемента": "L – Протяжённость детали вдоль оси [м]",
    "Диаметр_круга": "d – Характерный линейный размер круглого сечения [м]",
    "Ширина_прямоугольника": "b – Горизонтальный размер прямоугольного сечения [м]",
    "Высота_прямоугольника": "h – Вертикальный размер прямоугольного сечения [м]",
    "Число_зубьев": "z – Количество зубьев на шестерне [–]",
    "Передаточное_число": "i – Отношение угловых скоростей или чисел зубьев пары колёс [–]",
    "Угловая_скорость": "ω – Скорость изменения угла во времени [рад/с]",
    "Угловое_ускорение": "α – Скорость изменения угловой скорости [рад/с²]",
    "Линейная_скорость": "v – Путь, проходимый точкой за единицу времени [м/с]",
    "Линейное_ускорение": "a – Скорость изменения линейной скорости [м/с²]",
    "Степени_свободы_механизма": "M – Количество независимых координат, необходимых для задания положения звеньев [–]",
    "Сила_нагрузки": "P – величина внешней силы, приложенной к балке [Н]",
    "Расстояние_до_нейтральной_оси": "y – расстояние от нейтральной оси до точки, где считается напряжение [м]",
    "Радиус_точки": "r – расстояние от центра круглого сечения до рассматриваемой точки [м]",
    "Нормальное_напряжение_по_оси_x": "σ_x – нормальное (растяж./сжат.) напряжение вдоль оси x [Па]",
    "Нормальное_напряжение_по_оси_y": "σ_y – нормальное (растяж./сжат.) напряжение вдоль оси y [Па]",
    "Касательное_напряжение_в_плоскости_xy": "τ_xy – касательное напряжение в плоскости xy [Па]",
    "Частота_вращения": "n – частота вращения звена или колеса, число оборотов в секунду [об/с]",
    "Скорость_точки_B_по_x": "v_Bx – проекция линейной скорости точки B на ось x [м/с]",
    "Скорость_точки_B_по_y": "v_By – проекция линейной скорости точки B на ось y [м/с]",
    "Скорость_точки_A_по_x": "v_Ax – проекция линейной скорости точки A на ось x [м/с]",
    "Скорость_точки_A_по_y": "v_Ay – проекция линейной скорости точки A на ось y [м/с]",
    "Горизонтальное_плечо": "Δx – разность x_B – x_A, горизонтальное расстояние от A до B [м]",
    "Вертикальное_плечо": "Δy – разность y_B – y_A, вертикальное расстояние от A до B [м]",
    "Ускорение_точки_B_по_x": "a_Bx – проекция линейного ускорения точки B на ось x [м/с²]",
    "Ускорение_точки_B_по_y": "a_By – проекция линейного ускорения точки B на ось y [м/с²]",
    "Ускорение_точки_A_по_x": "a_Ax – проекция линейного ускорения точки A на ось x [м/с²]",
    "Ускорение_точки_A_по_y": "a_Ay – проекция линейного ускорения точки A на ось y [м/с²]",
    "Квадрат_угловой_скорости": "ω² – квадрат угловой скорости звена AB, отвечает за центростремительную составляющую [рад²/с²]",
    "Число_звеньев": "N – количество звеньев (элементов) механизма [-]",
    "Простые_кинематические_пары": "J₁ – число простых (поворотных/скользящих) соединений [-]",
    "Сложные_кинематические_пары": "J₂ – число сложных (двойных) соединений [-]",
    "Наружный_диаметр_трубы": "dₒ – наружный (внешний) диаметр полой трубы [м]",
    "Внутренний_диаметр_трубы": "dᵢ – внутренний (внутренний) диаметр полой трубы [м]"
}


def start(update, context):
    context.bot.send_message(update.effective_chat.id,'''Привет! Я — MechSolver 🤖

⚡️Помогу с инженерными расчётами и не только:
🔩 Прочность материалов, механика машин, геометрия сечений и масса деталей
📐 Перевод единиц 
📚Справочные данные

Точные расчеты - быстро и просто. 🚀 ''')
    context.bot.send_message(update.effective_chat.id,"Введите /help чтобы узнать что я могу")
    
def helping(update, context):
    context.bot.send_message(update.effective_chat.id, "Вот что я могу:")
    sending_img1 = open("formula1.jpg", "rb")
    context.bot.send_photo(update.effective_chat.id, sending_img1)
    sending_img2 = open("formula2.jpg", "rb")
    context.bot.send_photo(update.effective_chat.id, sending_img2)
    sending_img3 = open("formula3.jpg", "rb")
    context.bot.send_photo(update.effective_chat.id, sending_img3)
    context.bot.send_message(update.effective_chat.id, '''Также доступны следующие команды:

/c — перевод из одной единицы измерения в другую.
Например: /c 14300 М Па 4 = н Па 4 — бот выполнит преобразование 14300 мегапаскалей в четвёртой степени в нанопаскали в четвёртой степени.

/i — справочная информация по терминам.
Например: /i Нормальное_напряжение — бот выдаст определение и пояснение по заданному термину. ''')
    
    
def conversion(update, context):
    # x1 pref1 unit y = x2 pref2 unit y
    x1, p1, u, y, p2= int(context.args[0]), context.args[1], context.args[2], int(context.args[3]), context.args[5]
    x2 = x1 * (10 ** (y * (prefixes_dictionary[p1] - prefixes_dictionary[p2])))
    x2_str = f"{x2:.6g}"
    context.bot.send_message(update.effective_chat.id, str(x1) + " " + p1 + " " + u + " ^" + str(y) + " = " + x2_str + " " + p2 + " " + u + " ^" + str(y))
    
def info(update, context):
    q=context.args[0]
    context.bot.send_message(update.effective_chat.id, info_dictionary[q]) 
    
def f1(update, context): #1.1 Нормальное напряжение при изгибе
    q1=int(context.args[0]) #M
    q2=int(context.args[1]) #y
    q3=int(context.args[2]) #I
    context.bot.send_message(update.effective_chat.id, "σ (Нормальное напряжение при изгибе) = " + str((q1 * q2) / q3) + " Па")
    
def f2(update, context): #1.2 Касательное напряжение при кручении
    q1=int(context.args[0]) #T
    q2=int(context.args[1]) #r
    q3=int(context.args[2]) #J
    context.bot.send_message(update.effective_chat.id, "τ (Касательное напряжение при кручении) = " + str((q1 * q2) / q3) + " Па")
    
def f3(update, context): #1.3 Угол закручивания вала
    q1=int(context.args[0]) #T
    q2=int(context.args[1]) #L
    q3=int(context.args[2]) #J
    q4=int(context.args[3]) #G
    context.bot.send_message(update.effective_chat.id, "ϕ (Угол закручивания) = " + str((q1 * q2) / (q3 * q4)) + "°")
    
def f4(update, context): #1.5 Максимальный прогиб
    q1=int(context.args[0]) #P
    q2=int(context.args[1]) #L
    q3=int(context.args[2]) #I
    q4=int(context.args[3]) #E
    context.bot.send_message(update.effective_chat.id, "σ max (Максимальный прогиб балки в середине пролета) = " + str((q1 *(q2 ** 3)) / (48 * q3 * q4)) + "м")

def f5(update, context): #1.6 Эквивалентное напряжение фон Мизеса (плоская задача)
    q1=int(context.args[0]) #σx
    q2=int(context.args[1]) #σy
    q3=int(context.args[2]) #τxy
    context.bot.send_message(update.effective_chat.id, "σ v (Эквивалентное напряжение по фон Мизесу) = " + str(math.sqrt(q1**2 - q1 * q2 + q2**2 + 3 * (q3**2))) + "Па")
    
def f6(update, context): #2.1 Передаточное отношение зубчатой передачи 
    q1=int(context.args[0]) #z2 / w1 / n1
    q2=int(context.args[1]) #z1 / w2 / n2
    context.bot.send_message(update.effective_chat.id, "i (Передаточное отношение зубчатой передачи) = " + str(q1 / q2) + "")

def f7(update, context): #2.2 Относительная скорость в плоском механизме 
    q1=int(context.args[0]) #V Ax
    q2=int(context.args[1]) #V Ay
    q3=int(context.args[2]) #Δx
    q4=int(context.args[3]) #Δy
    q5=int(context.args[4]) #w
    context.bot.send_message(update.effective_chat.id, "V Bx (Проекция компонента линейной скорости точки B на ось x) = " + str(q1 - (q5 * q4)) + " м/c")
    сontext.bot.send_message(update.effective_chat.id, "V By (Проекция компонента линейной скорости точки B на ось y) = " + str(q2 + (q5 * q3)) + " м/c")

def f8(update, context): #2.3 Относительное ускорение
    q1=int(context.args[0]) #a Ax
    q2=int(context.args[1]) #a Ay
    q3=int(context.args[2]) #Δx
    q4=int(context.args[3]) #Δy
    q5=int(context.args[4]) #w
    q6=int(context.args[5]) #a (угловое)
    context.bot.send_message(update.effective_chat.id, "a Bx (Проекция компонента линейного ускорения точки B на ось x) = " + str(q1 - (q6 * q4) - (q5**2 * q3)) + " м/c^2")
    сontext.bot.send_message(update.effective_chat.id, "a By (Проекция компонента линейного ускорения точки B на ось y) = " + str(q2 + (q6 * q3) - (q5**2 * q4)) + " м/c^2")

def f9(update, context): #2.4 Критерий подвижности (Грюблер, плоский механизм)
    q1=int(context.args[0]) #τ1
    q2=int(context.args[1]) #τ2
    q3=int(context.args[2]) #N
    context.bot.send_message(update.effective_chat.id, "M (Число степеней свободы / подвижности) = " + str(3 * (q3 - 1) - (2 * q1) - q2) + "")

def f10(update, context): #3.1 Площадь сечения прямоугольника
    q1=int(context.args[0]) #b
    q2=int(context.args[1]) #h
    context.bot.send_message(update.effective_chat.id, "A (Площадь сечения прямоугольника) = " + str(q1 * q2) + "м^2")
    
def f11(update, context): #3.2 Площадь сечения круга
    q1=int(context.args[0]) #d
    context.bot.send_message(update.effective_chat.id, "A (Площадь сечения круга) = " + str((3.14 * (q1**2)) / 4) + "м^2")
    
def f12(update, context): #3.3 Площадь сечения полой трубы
    q1=int(context.args[0]) #d0
    q2=int(context.args[1]) #d1
    context.bot.send_message(update.effective_chat.id, "A (Площадь сечения полой трубы) = " + str((3.14 / 4) * ((q1**2) - (q2**2))) + "м^2")
    
def f13(update, context): #3.4 Момент инерции прямоугольника
    q1=int(context.args[0]) #b
    q2=int(context.args[1]) #h
    context.bot.send_message(update.effective_chat.id, "I (Момент инерции прямоугольника) = " + str((q1 * (q2**3)) / 12) + "м^4")
    
def f14(update, context): #3.5  Момент инерции круга
    q1=int(context.args[0]) #d
    context.bot.send_message(update.effective_chat.id, "I (Момент инерции круга) = " + str((3.14 / 64) * (q1**4)) + "м^4")
    
def f15(update, context): #3.6  Момент инерции полой трубы
    q1=int(context.args[0]) #d0
    q2=int(context.args[1]) #d1
    context.bot.send_message(update.effective_chat.id, "I (Момент инерции полой трубы) = " + str((3.14 / 64) * ((q1**4) - (q2**4))) + "м^4")
    
def f16(update, context): #3.7 Полярный момент круга
    q1=int(context.args[0]) #d
    context.bot.send_message(update.effective_chat.id, "τ (Полярный момент круга) = " + str((3.14 / 32) * (q1**4)) + "м^4")
    
def f17(update, context): #3.8 Полярный момент полой трубы
    q1=int(context.args[0]) #d0
    q2=int(context.args[1]) #d1
    context.bot.send_message(update.effective_chat.id, "τ (Полярный момент полой трубы) = " + str((3.14 / 32) * ((q1**4) - (q2**4))) + "м^4")

def f18(update, context): #3.9 Масса призматической детали
    q1=int(context.args[0]) #p
    q2=int(context.args[1]) #A
    q3=int(context.args[2]) #L
    context.bot.send_message(update.effective_chat.id, "m (Масса призматической детали) = " + str(q1 * q2 * q3) + "кг")

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", helping))
dispatcher.add_handler(CommandHandler("c", conversion))
dispatcher.add_handler(CommandHandler("i", info))
dispatcher.add_handler(CommandHandler("f1", f1))
dispatcher.add_handler(CommandHandler("f2", f2))
dispatcher.add_handler(CommandHandler("f3", f3))
dispatcher.add_handler(CommandHandler("f4", f4))
dispatcher.add_handler(CommandHandler("f5", f5))
dispatcher.add_handler(CommandHandler("f6", f6))
dispatcher.add_handler(CommandHandler("f7", f7))
dispatcher.add_handler(CommandHandler("f8", f8))
dispatcher.add_handler(CommandHandler("f9", f9))
dispatcher.add_handler(CommandHandler("f10", f10))
dispatcher.add_handler(CommandHandler("f11", f11))
dispatcher.add_handler(CommandHandler("f12", f12))
dispatcher.add_handler(CommandHandler("f13", f13))
dispatcher.add_handler(CommandHandler("f14", f14))
dispatcher.add_handler(CommandHandler("f15", f15))
dispatcher.add_handler(CommandHandler("f16", f16))
dispatcher.add_handler(CommandHandler("f17", f17))
dispatcher.add_handler(CommandHandler("f18", f18))

updater.start_polling()
updater.idle()