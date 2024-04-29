import cv2
import datetime


def generate_filename():    # Генерируем имя для скриншота. Исопльзуем миллисекунды и текущее время, чтобы избежать одинакового имени файла
    current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
    filename = f'screenshot_{current_time}.png'
    return filename


def save_screenshot(frame): # Сохраняем скриншот в папке photos/
    fileName = generate_filename()
    cv2.imwrite('photos/' + fileName, frame) 
    print('Saved screenshot photos/', fileName, sep='')


# Загружаем настройки для каскада Хаара из файла
cascFacePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascFacePath)
cascEyePath = "haarcascade_eye_tree_eyeglasses.xml"
eyeCascade = cv2.CascadeClassifier(cascEyePath)
cascSmilePath = "haarcascade_smile.xml"
smileCascade = cv2.CascadeClassifier(cascSmilePath)

print('This program will help you to recognize faces, eyes, smiles in real time.')
print('The face recognize system is enabled by default.')
print('The program is starting. Additional window will be opened soon...')

# Включёна или выключена система распознавания глаз и улыбок 
eyes_flag = True
smiles_flag = True

# Первичные настройки захвата видео. Выбираем камеру №1 в системе, выставляем размер.
window_size = [1280, 720]
url = "http://192.168.43.1:4747/video" 
video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#video_capture = cv2.VideoCapture(url)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, window_size[0])
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, window_size[1])

# Основной цикл программы
while True:
    # Разбираем видео кадр за кадром
    ret, frame = video_capture.read()

    #frame = cv2.resize(frame, (window_size[0], window_size[1]))

    # Переводим картинку в чёрно-белое пространство цветов. Алгоритм работает именно с чёрно-белыми изображениями.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Собственно само распознавание лиц средствами OpenCV и загруженными в программу заранее настройками.
    faces = faceCascade.detectMultiScale(
        gray,                           # Чёрно-белая картинка
        scaleFactor=1.1,                # Насколько уменьшается размер изображения при каждом его масштабе?
        minNeighbors=5,                 # Cколько соседей должен иметь каждый прямоугольник-кандидат, чтобы удерживать его?
        minSize=(30, 30),               # Минимальный размер лица для распознания
        flags=cv2.CASCADE_SCALE_IMAGE   # Позволяет найти все объекты (лица в гашем случае) на картинке (по умолчанию ищет лишь самый большой объект, потому что имеет флаг CASCADE_FIND_BIGGEST_OBJECT)
    )

    # Готовимся считать количество глаз и улыбок дополнительно, инициализируем переменные
    eyes_count = 0
    smiles_count = 0
    # Рисуем прямоугольник вокруг лица
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Теперь в найденных лицах находим ещё и глаза (если такая настройка включена)
        if eyes_flag:
            # Берём только первую половину картинки, так как глаза могут быть только сверху (вообще лицо не распознаётся под наклоном, такова особенность алгоритма, так что тут беспроигрышная ситуация)
            roi_gray = gray[y:y+(h//2), x:x+w]
            roi_color = frame[y:y+(h//2), x:x+w]
            eyes = eyeCascade.detectMultiScale(
                roi_gray,                       # Чёрно-белая картинка
                scaleFactor=1.1,                # Насколько уменьшается размер изображения при каждом его масштабе?
                minNeighbors=5,                 # Cколько соседей должен иметь каждый прямоугольник-кандидат, чтобы удерживать его?
                minSize=(30, 30),               # Минимальный размер лица для распознания
                flags=cv2.CASCADE_SCALE_IMAGE   # Позволяет найти все объекты (лица в гашем случае) на картинке (по умолчанию ищет лишь самый большой объект, потому что имеет флаг CASCADE_FIND_BIGGEST_OBJECT)
            )
            # Рисуем прямоугольники вокруг глаз
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)
            # Считаем количество глаз всего
            eyes_count += len(eyes)
        # Теперь в найденных лицах находим ещё и улыбки (если такая настройка включена)
        if smiles_flag:
            # Берём только вторую половину картинки, так как улыбка может быть только снизу (вообще лицо не распознаётся под наклоном, такова особенность алгоритма, так что тут беспроигрышная ситуация)
            roi_gray = gray[y+(h//2):y+h, x:x+w]
            roi_color = frame[y+(h//2):y+h, x:x+w]
            smiles = smileCascade.detectMultiScale(
                roi_gray,                       # Чёрно-белая картинка
                scaleFactor=1.8,                # Насколько уменьшается размер изображения при каждом его масштабе?
                minNeighbors=20,                # Cколько соседей должен иметь каждый прямоугольник-кандидат, чтобы удерживать его?
                minSize=(20, 20),               # Минимальный размер лица для распознания
                flags=cv2.CASCADE_SCALE_IMAGE   # Позволяет найти все объекты (лица в гашем случае) на картинке (по умолчанию ищет лишь самый большой объект, потому что имеет флаг CASCADE_FIND_BIGGEST_OBJECT)
            )
            # Рисуем прямоугольники вокруг улыбок
            for (ex, ey, ew, eh) in smiles:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)
            # Считаем количество улыбок всего
            smiles_count += len(smiles)

    # Смотрим, может быть функция выключена, надо написать об этом вместо вывода числа
    eyes_text_count = str(eyes_count) if eyes_flag else "disabled"
    smiles_text_count = str(smiles_count) if smiles_flag else "disabled"

    # Готовим текст
    text = "Press S to save the current frame.\nPress R to stop the current frame on\nthe screen.\nPress Q to close the program.\nFound faces on this frame: " + str(len(faces)) + "\nFound eyes on this frame:   " + eyes_text_count + "\nFound smiles on this frame: " + smiles_text_count
    coordinates = (window_size[0] - 625, 30)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    colors = [(240, 240, 240), (0, 191, 255), (0, 191, 255), (128, 128, 128), (10, 255, 10), (255, 10, 10), (10, 10, 255)]
    thickness = 2
    bigger_thickness = 5
    
    # Отражаем кадр по горизонтали, так как мы смотрим в монитор, а используем скорее всего вебкамеру
    frame = cv2.flip(frame, 1)
    
    # Делим текст на части (разделитель - символ \n), каждый отрезок рисуем ниже другого, так как OpenCV не поддерживает символ переноса строки. У каждой строки свой цвет.
    y0, dy = coordinates[1], 30
    for i, line in enumerate(text.split('\n')):
        y = y0 + i*dy
        # Рисуем чёрный цвет большой жирности, и внутри него тот же текст, но цветной и с жирностью поменьше. Тем самым имеем чёрную обводку текста, и его видно на любом фоне.
        frame = cv2.putText(frame, line, (coordinates[0], y), font, fontScale, (0, 0, 0), bigger_thickness, cv2.LINE_AA)
        frame = cv2.putText(frame, line, (coordinates[0], y), font, fontScale, colors[i], thickness, cv2.LINE_AA)

    # Пишем текст-подсказку для пользователя по поводу переключения режимом распознавания
    text_eyes_hint = "Press E to switch eyes mode."
    text_smiles_hint = "Press M to switch smiles mode."
    frame = cv2.putText(frame, text_eyes_hint, (10, 30), font, fontScale, (0, 0, 0), bigger_thickness, cv2.LINE_AA)
    frame = cv2.putText(frame, text_eyes_hint, (10, 30), font, fontScale, colors[len(colors) - 2], thickness, cv2.LINE_AA)
    frame = cv2.putText(frame, text_smiles_hint, (10, 60), font, fontScale, (0, 0, 0), bigger_thickness, cv2.LINE_AA)
    frame = cv2.putText(frame, text_smiles_hint, (10, 60), font, fontScale, colors[len(colors) - 1], thickness, cv2.LINE_AA)

    # Отображаем наш кадр на экране после всех необходимых действий с ним
    cv2.imshow('Lyutikov Maxim, OpenCV Face & Eyes & Smile Recognition without any NN, only with Cascade Haar', frame)

    # Получаем нажатую клавишу, если таковая имеется
    key = cv2.waitKey(1) & 0xFF
    # Вызываем функцию, которая соответствует этой нажатой клавише
    if key == ord('s'):
        # Сохраняем скриншот
        save_screenshot(frame)
    elif key == ord('e'):
        # Меняем режим работы, включаем/выключаем систему распознавания глаз
        eyes_flag = not eyes_flag
    elif key == ord('m'):
        # Меняем режим работы, включаем/выключаем систему распознавания улыбок
        smiles_flag = not smiles_flag
    elif key == ord('r'):
        # Поддерживаем выполнение и других нажатых кнопок во время остановки кадра на кнопку R
        while True:
            # Получаем нажатую клавишу, если таковая имеется, но уже внутри ещё одного цикла while (мы находимся в состоянии заморозки кадра, нажата клавиша R)
            key2 = cv2.waitKey(1) & 0xFF
            if key2 == ord('s'):
                # Сохраняем скриншот
                save_screenshot(frame)
            elif key2 == ord('q'):
                # Выходим из программы
                key = ord('q')
                break
            else:
                # Если клавиша не была распознана, то продолжаем режим остановки кадра
                if key2 != ord('r'):
                    continue
                else:
                    # Если клавиша R нажата ещё раз, то возобновляем работу программы
                    break
    # Выходим из программы
    if key == ord('q'):
        break

# Когда закончили, освобождаем захват
video_capture.release()
cv2.destroyAllWindows()