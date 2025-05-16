import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox)
from PySide6.QtCore import QRect, QTimer, Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QTransform, QPixmap
from collections import deque

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
        self.ui.pushButton.clicked.connect(self.button_clicked_bfs)
        self.ui.pushButton2.clicked.connect(self.button_clicked_dfs)

        # Таймер для последовательного перемещения
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_position)



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
        try:
            # Таблица Start
            start_model = QStandardItemModel()
            start_model.setHorizontalHeaderLabels(['Ч', 'Ко', 'Ка', 'В1', 'В2', 'Сб'])

            for col in range(6):
                item = QStandardItem('Л' if self._start[col] == 0 else 'П')
                start_model.setItem(0, col, item)

            self.ui.Start.setModel(start_model)
            self.ui.Start.resizeColumnsToContents()

            # Таблица Goal
            goal_model = QStandardItemModel()
            goal_model.setHorizontalHeaderLabels(['Ч', 'Ко', 'Ка', 'В1', 'В2', 'Сб'])

            for col in range(6):
                item = QStandardItem('Л' if self._goal[col] == 0 else 'П')
                goal_model.setItem(0, col, item)

            self.ui.Goal.setModel(goal_model)
            self.ui.Goal.resizeColumnsToContents()
        except Exception as e:
            self.show_error(f"Ошибка при инициализации таблиц: {str(e)}")

    def toggle_item_state(self, index):
        """Изменяет состояние элемента таблицы по клику"""
        try:
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
        except Exception as e:
            self.show_error(f"Ошибка при изменении состояния: {str(e)}")

    def button_clicked_bfs(self):
        """Обработчик нажатия кнопки - запускает поиск решения и анимацию"""
        try:
            if not self.is_valid_state(self._start):
                self.show_error("Начальное состояние недопустимо!")
                return
            if not self.is_valid_state(self._goal):
                self.show_error("Конечное состояние недопустимо!")
                return

            self.search_bfs()  # Находим решение
            if not self.states:
                self.show_error("Не удалось найти решение!")
                return

            self.current_state_index = 0
            self.timer.start(500)  # 500 ms = 0.5 секунды
            self.ui.textEdit.setText('Человек\tКоза\tКапуста\tВолк1\tВолк2\tСобака\n\n')
        except Exception as e:
            self.show_error(f"Ошибка при запуске решения: {str(e)}")

    def button_clicked_dfs(self):
        """Обработчик нажатия кнопки - запускает поиск решения и анимацию"""
        try:
            if not self.is_valid_state(self._start):
                self.show_error("Начальное состояние недопустимо!")
                return
            if not self.is_valid_state(self._goal):
                self.show_error("Конечное состояние недопустимо!")
                return

            self.search_dfs()  # Находим решение
            if not self.states:
                self.show_error("Не удалось найти решение!")
                return

            self.current_state_index = 0
            self.timer.start(500)  # 500 ms = 0.5 секунды
            self.ui.textEdit.setText('Человек\tКоза\tКапуста\tВолк1\tВолк2\tСобака\n\n')
        except Exception as e:
            self.show_error(f"Ошибка при запуске решения: {str(e)}")

    def update_position(self):
        """Обновляет позиции объектов на форме"""
        try:
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

                self.current_state_index += 1
            else:
                self.timer.stop()
        except Exception as e:
            self.show_error(f"Ошибка при обновлении позиций: {str(e)}")
            self.timer.stop()

    def is_valid_state(self, state):
        """Проверяет, является ли состояние допустимым"""
        forbidden = [
            (1, 2), (1, 3), (1, 4), (3, 5), (4, 5)  # Добавьте все необходимые
        ]
        for (a, b) in forbidden:
            if state[a] == state[b] and state[0] != state[a]:
                return False
        return True

    def can_transport_together(self, item1, item2):
        """Проверяет, можно ли перевозить два предмета вместе"""
        forbidden_pairs = [
            (1, 2),  # Коза + капуста
            (1, 3),  # Коза + волк1
            (1, 4),  # Коза + волк2
            (3, 5),  # Волк1 + собака
            (4, 5)  # Волк2 + собака
        ]
        pair = tuple(sorted((item1, item2)))
        return pair not in forbidden_pairs

    def generate_next_states(self, current_state):
        """Генерирует все возможные следующие допустимые состояния (можно перевозить до 2 объектов)"""
        try:
            next_states = []
            man_pos = current_state[0]  # Текущее положение человека

            # Все возможные комбинации предметов для перевозки (один или два)
            items_to_move = []

            # Добавляем варианты с одним предметом
            for item in [1, 2, 3, 4, 5]:  # Индексы предметов (коза, капуста, волк1, волк2, собака)
                if current_state[item] == man_pos:  # Предмет на том же берегу, что и человек
                    items_to_move.append([item])

            # Добавляем варианты с двумя предметами
            for i in range(len(items_to_move)):
                for j in range(i + 1, len(items_to_move)):
                    item1 = items_to_move[i][0]
                    item2 = items_to_move[j][0]
                    if self.can_transport_together(item1, item2):  # Добавьте эту проверку
                        items_to_move.append([item1, item2])

            # Добавляем вариант, когда человек переезжает один
            items_to_move.append([])

            # Генерируем новые состояния для каждого варианта перевозки
            for items in items_to_move:
                new_state = current_state.copy()
                new_state[0] = 1 - man_pos  # Человек переезжает

                for item in items:
                    new_state[item] = 1 - man_pos  # Предмет перевозится

                if self.is_valid_state(new_state):
                    next_states.append(new_state)

            return next_states
        except Exception as e:
            self.show_error(f"Ошибка при генерации состояний: {str(e)}")
            return []

    def search_bfs(self):
        """Реализация поиска в ширину (BFS)"""
        try:

            visited = set()
            queue = deque()
            parent = {}

            # Преобразуем списки в кортежи для хранения в множестве
            start_tuple = tuple(self._start)
            goal_tuple = tuple(self._goal)

            queue.append(start_tuple)
            visited.add(start_tuple)
            parent[start_tuple] = None

            found = False
            current_tuple = None

            while queue:
                current_tuple = queue.popleft()

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
                        queue.append(state_tuple)


            # Восстанавливаем путь
            self.states = []
            if found:
                path = []
                current_tuple = goal_tuple
                while current_tuple is not None:
                    path.append(list(current_tuple))
                    current_tuple = parent[current_tuple]
                self.states = path[::-1]  # Разворачиваем путь, чтобы получить от начала до конца
        except Exception as e:
            self.show_error(f"Ошибка при поиске решения: {str(e)}")
            self.states = []


    def search_dfs(self):
        """Реализация поиска в ширину (BFS)"""
        try:
            visited = set()
            queue = deque()
            parent = {}

            # Преобразуем списки в кортежи для хранения в множестве
            start_tuple = tuple(self._start)
            goal_tuple = tuple(self._goal)

            queue.append(start_tuple)
            visited.add(start_tuple)
            parent[start_tuple] = None

            found = False
            current_tuple = None

            while queue:
                current_tuple = queue.pop()

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
                        queue.append(state_tuple)


            # Восстанавливаем путь
            self.states = []
            if found:
                path = []
                current_tuple = goal_tuple
                while current_tuple is not None:
                    path.append(list(current_tuple))
                    current_tuple = parent[current_tuple]
                self.states = path[::-1]  # Разворачиваем путь, чтобы получить от начала до конца
        except Exception as e:
            self.show_error(f"Ошибка при поиске решения: {str(e)}")
            self.states = []

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())