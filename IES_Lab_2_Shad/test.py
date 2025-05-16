import sys
from time import sleep
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox)
from PySide6.QtCore import QRect, QTimer, Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QTransform, QPixmap
import random

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

    def init_tables(self):
        """Инициализация таблиц Start и Goal"""
        # Таблица Start
        start_model = QStandardItemModel()
        start_model.setHorizontalHeaderLabels(['Ч', 'Ко', 'Ка', 'В'])
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
            QMessageBox.warning(self, "Ошибка", "Не удалось найти решение!")
            return

        self.current_state_index = 0
        self.timer.start(500)  # 500 ms = 0.5 секунды
        self.ui.textEdit.setText('Человек\tКоза\tКапуста\tВолк\n\n')

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
            objects = [None, self.ui.goat, self.ui.cabbage, self.ui.wolf]

            for i in range(1, 4):
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

    def search(self):
        """Ищет решение задачи и сохраняет последовательность состояний в self.states"""
        current = self._start.copy()
        self.states = [current.copy()]
        max_iterations = 1000  # Ограничение на количество итераций

        def is_valid_state(state):
            # Проверяем, что коза не осталась с волком или капустой без человека
            if (state[1] == state[3] and state[0] != state[1]) or \
                    (state[1] == state[2] and state[0] != state[1]) or \
                    (state[1] == state[4] and state[0] != state[1]) or \
                    (state[1] == state[5] and state[0] != state[1]) or \
                    (state[3] == state[5] and state[0] != state[5]) or \
                    (state[4] == state[5] and state[0] != state[5]):
                return False
            return True

        for _ in range(max_iterations):
            if current == self._goal:
                break

            # Выбираем что перевозим (0-ничего, 1-коза, 2-капуста, 3-волк)
            item_to_move = random.choice([0, 1, 2, 3])

            # Создаем новое состояние
            new_state = current.copy()
            new_state[0] = 1 - new_state[0]  # Меняем положение человека

            # Если перевозим предмет, меняем и его положение
            if item_to_move != 0:
                new_state[item_to_move] = new_state[0]

            # Проверяем новое состояние
            if is_valid_state(new_state) and new_state not in self.states:
                current = new_state.copy()
                self.states.append(current.copy())
            else:
                # Если состояние недопустимо, пробуем снова
                continue

        # Если не нашли решение, очищаем states
        if current != self._goal:
            self.states = []


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())