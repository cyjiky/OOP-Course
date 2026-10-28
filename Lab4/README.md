# Lab4: Вдосконалення структури коду графічного редактора об’єктів
 
### Мета 
Отримати вміння та навички проектування класів, виконавши модернізацію коду графічного редактора в об’єктно-орієнтованому стилі для забезпечення зручного додавання нових типів об'єктів


### Завдання

1. Створити у середовищі розробки проект з ім’ям Lab4.
2. Написати вихідний текст програми згідно варіанту завдання.
3. Скомпілювати вихідний текст і отримати виконуваний файл програми.
4. Перевірити роботу програми. Налагодити програму.
5. Проаналізувати та прокоментувати результати та вихідний текст програми.
6. Оформити звіт.


## Варіант завдання — №15 (Ж = 15)

Усі параметри обчислено за формулами для номера за журналом **Ж = 15**:

| Параметр | Умова за варіантом |
| :--- | :--- |
| Об'єкт класу `MyEditor` | Глобальний статичний об'єкт |
| «Гумовий» слід при вводі фігур | Пунктирна лінія чорного кольору |
| Сховище для збереження об'єктів | Динамічний масив об'єктів `Shape` |
| Базові типи фігур | Крапка, Лінія, Прямокутник, Еліпс |
| Нові типи фігур | Лінія з кружечками, Каркас куба |
| Реалізація «Лінії з кружечками» | Множинне успадкування від `Line` та `Ellipse` (або `Point`) |
| Реалізація «Каркасу куба» | Множинне успадкування від `Rectangle` та `Line` |
| Елементи керування (Toolbar) | Кнопки Toolbar з підказками (Tooltips) |
| Меню програми | Меню «Об'єкти» з індикацією обраного інструмента |

### Схема успадкування

```mermaid
flowchart TD
  subgraph app["main"]
    entry["MainClass"]
  end 

  subgraph menu["menu.py"]
    MenuClass["class MenuClass"]
  end 

  subgraph toolbar["toolbar.py"]
    ToolTip["class ToolTip"]
    ToolbarClass["class ToolbarClass"]
  end 

  subgraph info["info.py"]
    InfoWindow["class InfoWindow"]
  end 

  subgraph shapes["shapes.py"]
    Shape["class Shape (ABC)"]
    PointsShape["class PointsShape"]
    Storage["class Storage"]
  end 

  subgraph figures["figures.py"]
    PointClass["class Point"]
    LineClass["class Line"]
    RectClass["class Rectangle"]
    EllipseClass["class Ellipse"]
    LineConnectorClass["class LineConnector"]
    CubeClass["class Cube"]
  end 

  entry --> Storage 
  Storage --> Shape
  entry --> MenuClass 
  entry --> ToolbarClass 
  ToolbarClass <--> ToolTip
  entry --> InfoWindow

  Shape --> PointsShape
  PointsShape --> PointClass
  PointsShape --> LineClass
  PointsShape --> RectClass
  PointsShape --> EllipseClass

  LineClass --> LineConnectorClass
  PointClass --> LineConnectorClass
  
  RectClass --> CubeClass
  LineClass --> CubeClass
```

### Структура проєкту

```text 
./ 
├── icons/
├── widgets/
│   ├── menu.py
│   └── toolbar.py
├── main.py
├── info.py
├── shapes.py
├── figures.py
└── README.md
```