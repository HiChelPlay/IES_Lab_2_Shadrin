import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox)
from PySide6.QtCore import QRect, QTimer, Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QTransform, QPixmap

from int2 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Инициализация начального и конечного состояний
        self._start = [0, 0, 0, 0, 0, 0]  # человек, коза, капуста, волк 1, волк 2, собака
        self._goal = [1, 1, 1, 1, 1, 1]  # 0 - левый берег, 1 - правый берег
        self.states = []  # Будет хранить последовательность состояний

        # Создание UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Подключение сигналов
        self.ui.pushButton.clicked.connect(self.button_clicked)

        # Таймер для последовательного перемещения
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_position)
        self.current_state_index = 0

        # Инициализация таблиц
        self.init_tables()

        # Подключение обработчиков кликов по таблицам
        self.ui.Start.clicked.connect(self.toggle_item_state)
        self.ui.Goal.clicked.connect(self.toggle_item_state)

    def show_error(self, message):
        """Показывает сообщение об ошибке"""
        QMessageBox.critical(self, "Ошибка", message)

    def init_tables(self):
        """Инициализация таблиц Start и Goal"""
        # Таблица Start
        start_model = QStandardItemModel()
        start_model.setHorizontalHeaderLabels(['Ч', 'Ко', 'Ка', 'В1', 'В2', 'Сб'])
        start_model.setVerticalHeaderLabels(['Б'])

        for col in range(6):
            item = QStandardItem('Л' if self._start[col] == 0 else 'П')
            start_model.setItem(0, col, item)

        self.ui.Start.setModel(start_model)
        self.ui.Start.resizeColumnsToContents()

        # Таблица Goal
        goal_model = QStandardItemModel()
        goal_model.setHorizontalHeaderLabels(['Ч', 'Ко', 'Ка', 'В'])
        goal_model.setVerticalHeaderLabels(['Б'])

        for col in range(6):
            item = QStandardItem('Л' if self._goal[col] == 0 else 'П')
            goal_model.setItem(0, col, item)

        self.ui.Goal.setModel(goal_model)
        self.ui.Goal.resizeColumnsToContents()

    def toggle_item_state(self, index):
        """Изменяет состояние элемента таблицы по клику"""
        if not index.isValid():
            return

        model = self.ui.Start.model() if self.sender() == self.ui.Start else self.ui.Goal.model()
        item = model.itemFromIndex(index)

        if item.text() == 'Л':
            item.setText('П')
        else:
            item.setText('Л')

        # Обновляем соответствующий массив (_start или _goal)
        if self.sender() == self.ui.Start:
            self._start[index.column()] = 0 if item.text() == 'Л' else 1
        else:
            self._goal[index.column()] = 0 if item.text() == 'Л' else 1

    def button_clicked(self):
        """Обработчик нажатия кнопки - запускает поиск решения и анимацию"""
        self.search()  # Находим решение
        if not self.states:
            self.show_error("Не удалось найти решение!")
            return

        self.current_state_index = 0
        self.timer.start(500)  # 500 ms = 0.5 секунды
        self.ui.textEdit.setText('Человек\tКоза\tКапуста\tВолк1\tВолк2\tСобака\n\n')

    def update_position(self):
        """Обновляет позиции объектов на форме"""
        if self.current_state_index < len(self.states):
            state = self.states[self.current_state_index]
            nameState = []
            for i in state:
                if i == 0:
                    nameState.append("Левый")
                else:
                    nameState.append("Правый")

            # Добавляем текущее состояние в текстовое поле
            curTxt = self.ui.textEdit.toPlainText()
            newTxt = curTxt + "\t".join(nameState) + "\n"
            self.ui.textEdit.setText(newTxt)

            # Перемещение лодки и человека
            if state[0] == 1 and self.ui.boat.geometry().x() == 180:
                self.ui.boat.move(270, self.ui.boat.geometry().y())
                self.ui.man.move(430, self.ui.man.geometry().y())
                self.mirror_pixmap(self.ui.boat)
                self.mirror_pixmap(self.ui.man)
            elif state[0] == 0 and self.ui.boat.geometry().x() == 270:
                self.ui.boat.move(180, self.ui.boat.geometry().y())
                self.ui.man.move(100, self.ui.man.geometry().y())
                self.mirror_pixmap(self.ui.boat)
                self.mirror_pixmap(self.ui.man)

            # Перемещение остальных объектов
            objects = [None, self.ui.goat, self.ui.cabbage, self.ui.wolf, self.ui.wolf2, self.ui.dog]

            for i in range(1, 6):  # Обрабатываем все 5 объектов
                obj = objects[i]
                if state[i] == 1 and obj.geometry().x() == 100:
                    obj.move(430, obj.geometry().y())
                    self.mirror_pixmap(obj)
                elif state[i] == 0 and obj.geometry().x() == 430:
                    obj.move(100, obj.geometry().y())
                    self.mirror_pixmap(obj)

            self.current_state_index += 1
        else:
            self.timer.stop()

    def mirror_pixmap(self, widget):
        """Отражает изображение виджета по горизонтали"""
        pixmap = widget.pixmap()
        if pixmap:
            mirrored = pixmap.transformed(QTransform().scale(-1, 1))
            widget.setPixmap(mirrored)

    def is_valid_state(self, state):
        """Проверяет, является ли состояние допустимым"""
        # Коза не должна оставаться с волком без человека
        # Пример для: коза + волк, коза + капуста, волк + собака и т.д.
        # forbidden_pairs = [
        #     (1, 3),  # Коза + волк 1
        #     (1, 4),  # Коза + волк 2
        #     (1, 2),  # Коза + капуста
        #     (3, 5),  # Волк 1 + собака
        #     (4, 5)  # Волк 2 + собака
        # ]
        # for (a, b) in forbidden_pairs:
        #     if state[a] == state[b] and state[0] != state[a]:
        #         return False

        # if (state[1] == state[3] and state[0] != state[1]) or \
        #         (state[1] == state[2] and state[0] != state[1]) or \
        #         (state[1] == state[4] and state[0] != state[1]) or \
        #         (state[1] == state[5] and state[0] != state[1]) or \
        #         (state[3] == state[5] and state[0] != state[5]) or \
        #         (state[4] == state[5] and state[0] != state[5]):
        #     return False

        if (state[1] == state[3] and state[0] != state[1]):
            return False
        if (state[1] == state[2] and state[0] != state[1]):
            return False
        # if (state[1] == state[4] and state[0] != state[1]):
        #     return False
        # if (state[1] == state[5] and state[0] != state[1]):
        #     return False
        # if (state[3] == state[5] and state[0] != state[5]):
        #     return False
        # if (state[4] == state[5] and state[0] != state[5]):
        #     return False


        return True

    def generate_next_states(self, current_state):
        """Генерирует все возможные следующие допустимые состояния"""
        next_states = []
        # Определяем на каком берегу находится человек
        man_pos = current_state[0]

        # Варианты перемещения: ничего, коза, капуста, волк
        for item in [0, 1, 2, 3, 4, 5]:
            new_state = current_state.copy()
            new_state[0] = 1 - man_pos  # Меняем положение человека

            print(new_state)

            # Если перемещаем предмет, меняем и его положение
            if item != 0:
                # Предмет должен быть на том же берегу, что и человек
                if new_state[item] == man_pos:
                    new_state[item] = 1 - man_pos
                else:
                    continue  # Пропускаем недопустимые перемещения

            # Проверяем допустимость нового состояния
            if self.is_valid_state(new_state):
                next_states.append(new_state)
        return next_states

    def search(self):
        """Реализация поиска в глубину (DFS)"""
        visited = set()
        stack = []
        parent = {}

        if not self.is_valid_state(self._start) or not self.is_valid_state(self._goal):
            self.show_error("Начальное или конечное состояние недопустимо!")

        # Преобразуем списки в кортежи для хранения в множестве
        start_tuple = tuple(self._start)
        goal_tuple = tuple(self._goal)

        stack.append(start_tuple)
        visited.add(start_tuple)
        parent[start_tuple] = None

        found = False
        current_tuple = None

        # count = 0

        while stack:

            # count += 1
            # print(f"{count}: {stack}")
            current_tuple = stack.pop()

            if current_tuple == goal_tuple:
                found = True
                break

            # Генерируем следующие состояния
            next_states = self.generate_next_states(list(current_tuple))
            for state in next_states:
                state_tuple = tuple(state)
                if state_tuple not in visited:
                    visited.add(state_tuple)
                    parent[state_tuple] = current_tuple
                    stack.append(state_tuple)


        # Восстанавливаем путь
        self.states = []
        if found:
            path = []
            current_tuple = goal_tuple
            while current_tuple is not None:
                path.append(list(current_tuple))
                current_tuple = parent[current_tuple]
            self.states = path[::-1]  # Разворачиваем путь, чтобы получить от начала до конца


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())