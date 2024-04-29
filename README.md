<details>

<summary>Русский язык</summary>

# Детектор лиц, глаз, улыбок	

### Описание: здесь представлена моя программа, написанная на языке Python с использованием библиотеки компьютерного зрения OpenCV, которая использует алгоритм Каскада Хаара для обнаружения лиц, глаз и улыбок на видео в реальном времени. Программа получает видео с камеры, анализирует его и определяет наличие различных (указанных выше) объектов. В целом, алгоритм, используемый в программе, позволяет распознавать почти любой объект, но первоначально был разработан как раз для распознавания лиц.

Особенности программы:

1. `Обнаружение лиц`: Программа обнаруживает лица на видео и рисует зелёный прямоугольник вокруг каждого найденного лица. Это достигается благодаря использованию предварительно обученного каскада Хаара для лиц, что позволяет обеспечить высокую точность и скорость обнаружения.
2. `Обнаружение глаз`: После обнаружения лица программа анализирует область внутри зелёного прямоугольника и ищет глаза с помощью предварительно обученного каскада Хаара для глаз. Вокруг каждого обнаруженного глаза рисуется синий прямоугольник.
3. `Обнаружение улыбок`: В дополнение к обнаружению лиц и глаз, программа также ищет улыбки в той же зоне, где было найдено лицо. Для этого используется предварительно обученный каскад Хаара для улыбок. Вокруг каждой обнаруженной улыбки рисуется красный прямоугольник.
4. `Вывод видео`: Программа выводит обработанное видео на экран в реальном времени, показывая зелёные прямоугольники вокруг лиц, синие прямоугольники вокруг глаз и красные прямоугольники вокруг улыбок. Это позволяет пользователям видеть результаты обнаружения объектов непосредственно на видео.
5. `Применение`: Детектор лиц, глаз, улыбок может использоваться в различных областях, таких как видеонаблюдение, системы безопасности, развлекательные приложения, а также для исследовательских целей.
5. `Простота использования`: Программа написана на языке Python, что делает её легкой для разработки и интеграции в другие проекты. Она также использует библиотеку OpenCV, которая является широко распространённой и хорошо документированной, что упрощает разработку и дальнейшее совершенствование программы.

В целом, это эффективная и простая в использовании программа для обнаружения лиц, глаз и улыбок на видео с использованием алгоритма Каскада Хаара. Благододаря высокой точности и скорости работы, она может быть полезной во множестве сценариев и областей применения. Программа не только позволяет пользователям обнаруживать и отслеживать объекты на видео в реальном времени, но и предоставляет возможность разработчикам легко адаптировать и модифицировать код для своих нужд и требований.

Для тех, кто хочет углубиться в изучение алгоритма Каскада Хаара или реализовать свою собственную программу обнаружения объектов, эта программа может служить отличной отправной точкой и образцом для дальнейшего изучения. В дополнение к этому, программа также может стимулировать интерес студентов к изучению нейросетей: если обычный алгоритм, не занимающий много кода, способен делать подобное, то что вообще могут нейросети?


Алгоритм Каскада Хаара: Алгоритм основан на использовании каскадов Хаара, которые являются машинно обучаемыми классификаторами и обеспечивают высокую скорость и точность обнаружения объектов. Он работает путем сканирования изображения на различных масштабах и поиска характерных признаков объектов.

Каскады Хаара - это метод обнаружения объектов, предложенный Полом Виолой и Майклом Джонсом в 2001 году. Основная идея алгоритма заключается в использовании каскадов признаков Хаара для быстрого и эффективного обнаружения объектов на изображении. Каскады Хаара широко используются в компьютерном зрении, особенно для обнаружения лиц.

Признаки Хаара представляют собой простые структуры, состоящие из смежных прямоугольников с разными знаками интенсивности. Они используются для определения наличия определенных характеристик объекта на изображении. Примером такого признака может быть разница между суммой интенсивностей пикселей в двух соседних прямоугольных областях.

Алгоритм Каскада Хаара состоит из нескольких этапов:
1. Интегральное изображение: Для ускорения вычисления признаков Хаара используется интегральное изображение, которое позволяет быстро вычислять сумму интенсивностей пикселей в прямоугольной области. Интегральное изображение представляет собой матрицу, в каждой ячейке которой хранится сумма интенсивностей пикселей, находящихся слева и сверху от текущей позиции.
2. Обучение классификатора: Каскады Хаара используют машинное обучение для обучения классификатора на основе большого количества положительных (содержащих объект) и отрицательных (не содержащих объект) образцов. Для этого применяется алгоритм Adaboost, который выбирает наиболее информативные признаки Хаара и комбинирует их в сильный классификатор.
3. Каскадирование классификаторов: Чтобы повысить скорость обнаружения объектов, классификаторы организуются в каскады. Каскад представляет собой последовательность слабых классификаторов, каждый из которых обучен на определенном подмножестве признаков Хаара. На каждом этапе каскада решается задача обнаружения объекта с разной степенью точности. Если объект не проходит через один из слабых классификаторов, он считается отсеянным, и анализ прекращается. Это позволяет сократить время обработки изображения, поскольку на каждом этапе каскада отсеивается большое количество ложных объектов.
4. Сканирование изображения: Алгоритм Каскада Хаара сканирует изображение с использованием скользящего окна, которое перемещается по изображению и применяет каскад классификаторов к каждому окну. Размер окна и шаг сканирования могут быть настроены для определения оптимального сочетания скорости и точности обнаружения объектов. 
5. Масштабирование изображения: Поскольку объекты могут быть разных размеров, алгоритм также масштабирует изображение на различных уровнях и повторяет процесс сканирования для каждого масштаба. Это увеличивает шансы обнаружения объектов разных размеров на одном изображении.

Картинки:
https://habr.com/ru/companies/recognitor/articles/228195/
https://habr.com/ru/articles/134857/

Каскады Хаара показали хорошую эффективность в обнаружении объектов, особенно лиц, и стали основой многих систем компьютерного зрения. Однако они имеют некоторые ограничения, такие как чувствительность к условиям освещения, поворотам и изменениям масштаба объектов. Несмотря на это, алгоритм Каскада Хаара продолжает использоваться в различных приложениях благодаря своей простоте и высокой скорости работы.

</details>


<details>

<summary>English language</summary>

# Face, eye, smile detector	

### Description: Here is my program written in Python using the OpenCV computer vision library, which uses the Haar Cascade algorithm to detect faces, eyes and smiles in real-time video. The program receives video from the camera, analyzes it and determines the presence of various (mentioned above) objects. In general, the algorithm used in the program allows you to recognize almost any object, but it was originally developed just for face recognition.

Program Features:

1. `Face Detection`: The program detects faces in the video and draws a green rectangle around each face found. This is achieved through the use of a pre-trained Haar cascade for faces, which allows for high accuracy and speed of detection.
2. `Eye Detection`: After detecting a face, the program analyzes the area inside the green rectangle and searches for eyes using a pre-trained Haar cascade for eyes. A blue rectangle is drawn around each detected eye.
3. `Smile Detection`: In addition to detecting faces and eyes, the program also searches for smiles in the same area where the face was found. To do this, a pre-trained Haar cascade for smiles is used. A red rectangle is drawn around each detected smile.
4. `Video Output`: The program displays the processed video on the screen in real time, showing green rectangles around faces, blue rectangles around eyes and red rectangles around smiles. This allows users to see the results of object detection directly on the video.
5. `Application`: The face, eye, smile detector can be used in various fields such as video surveillance, security systems, entertainment applications, as well as for research purposes.
5. `Ease of Use`: The program is written in Python, which makes it easy to develop and integrate into other projects. It also uses the OpenCV library, which is widely distributed and well documented, which simplifies the development and further improvement of the program.

Overall, it is an effective and easy-to-use program for detecting faces, eyes and smiles on video using the Haar Cascade algorithm. Due to its high accuracy and speed of operation, it can be useful in a variety of scenarios and applications. The program not only allows users to detect and track objects on video in real time, but also provides an opportunity for developers to easily adapt and modify the code for their needs and requirements.

For those who want to delve into the Haar Cascade algorithm or implement their own object detection program, this program can serve as an excellent starting point and a model for further study. In addition to this, the program can also stimulate students' interest in studying neural networks: if an ordinary algorithm that does not take up a lot of code is able to do this, then what can neural networks do?


Haar Cascade Algorithm: The algorithm is based on the use of Haar cascades, which are machine-learning classifiers and provide high speed and accuracy of object detection. It works by scanning an image at various scales and searching for characteristic features of objects.

Haar cascades is an object detection method proposed by Paul Viola and Michael Jones in 2001. The main idea of the algorithm is to use cascades of Haar features to quickly and efficiently detect objects in an image. Haar cascades are widely used in computer vision, especially for face detection.

Haar signs are simple structures consisting of adjacent rectangles with different intensity signs. They are used to determine the presence of certain characteristics of an object in an image. An example of such a feature may be the difference between the sum of pixel intensities in two adjacent rectangular areas.

The Haar Cascade algorithm consists of several stages:
1. Integral image: To speed up the calculation of Haar features, an integral image is used, which allows you to quickly calculate the sum of pixel intensities in a rectangular area. The integral image is a matrix, in each cell of which the sum of the pixel intensities located to the left and top of the current position is stored.
2. Classifier Training: Haar Cascades use machine learning to train a classifier based on a large number of positive (containing an object) and negative (not containing an object) samples. To do this, the Adaboost algorithm is used, which selects the most informative Haar features and combines them into a strong classifier.
3. Cascading classifiers: To increase the speed of object detection, classifiers are organized into cascades. The cascade is a sequence of weak classifiers, each of which is trained on a specific subset of Haar features. At each stage of the cascade, the task of detecting an object with varying degrees of accuracy is solved. If an object does not pass through one of the weak classifiers, it is considered eliminated, and the analysis stops. This reduces the image processing time, since a large number of false objects are eliminated at each stage of the cascade.
4. Image Scanning: The Haar Cascade algorithm scans the image using a sliding window that moves across the image and applies a cascade of classifiers to each window. The window size and scanning step can be adjusted to determine the optimal combination of speed and accuracy of object detection. 
5. Image scaling: Since objects can be of different sizes, the algorithm also scales the image at different levels and repeats the scanning process for each scale. This increases the chances of detecting objects of different sizes in the same image.

Pictures:
https://habr.com/ru/companies/recognitor/articles/228195/
https://habr.com/ru/articles/134857/

Haar cascades have shown good effectiveness in detecting objects, especially faces, and have become the basis of many computer vision systems. However, they have some limitations, such as sensitivity to lighting conditions, rotations, and changes in the scale of objects. Despite this, the Haar Cascade algorithm continues to be used in various applications due to its simplicity and high speed of operation.

</details>