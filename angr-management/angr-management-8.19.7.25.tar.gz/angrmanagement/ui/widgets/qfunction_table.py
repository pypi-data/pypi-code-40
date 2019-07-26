import os
import string

from angr.analyses.code_tagging import CodeTags

from PySide2.QtWidgets import QWidget, QTableView, QAbstractItemView, QHeaderView, QVBoxLayout, QLineEdit, \
    QStyledItemDelegate
from PySide2.QtGui import QBrush, QColor
from PySide2.QtCore import Qt, QSize, QAbstractTableModel, SIGNAL, QEvent

from ...data.instance import ObjectContainer
from ...config import Conf


class QFunctionTableModel(QAbstractTableModel):

    Headers = ['Name', 'Tags', 'Address', 'Binary', 'Size', 'Blocks']
    NAME_COL = 0
    TAGS_COL = 1
    ADDRESS_COL = 2
    BINARY_COL = 3
    SIZE_COL = 4
    BLOCKS_COL = 5

    def __init__(self, backcolor_callback=None, func_list=None):

        super(QFunctionTableModel, self).__init__()

        self._func_list = None
        self._raw_func_list = func_list
        self._backcolor_callback = backcolor_callback

    def __len__(self):
        if self._func_list is not None:
            return len(self._func_list)
        if self._raw_func_list is not None:
            return len(self._raw_func_list)
        return 0

    @property
    def func_list(self):
        if self._func_list is not None:
            return self._func_list
        return self._raw_func_list

    @func_list.setter
    def func_list(self, v):
        self._func_list = None
        self._raw_func_list = v
        self.emit(SIGNAL("layoutChanged()"))

    def filter(self, keyword):
        if not keyword or self._raw_func_list is None:
            # remove the filtering
            self._func_list = None
        else:
            self._func_list = [ func for func in self._raw_func_list if self._func_match_keyword(func, keyword) ]

        self.emit(SIGNAL("layoutChanged()"))

    def rowCount(self, *args, **kwargs):
        if self.func_list is None:
            return 0
        return len(self.func_list)

    def columnCount(self, *args, **kwargs):
        return len(self.Headers)

    def headerData(self, section, orientation, role):

        if role != Qt.DisplayRole:
            return None

        return self.Headers[section]

    def _get_function_backcolor(self, func) -> (int, int, int):
        return self._backcolor_callback(func)

    def data(self, index, role):

        TAG_STRS = {
            CodeTags.HAS_XOR: "Xor",
            CodeTags.HAS_BITSHIFTS: "Shift",
        }

        def _get_tags_display_string(tags):

            return ", ".join(TAG_STRS.get(t, t) for t in tags)

        if not index.isValid():
            return None

        row = index.row()
        if row >= len(self):
            return None

        col = index.column()
        func = self.func_list[row]

        if role == Qt.DisplayRole:

            mapping = {
                self.NAME_COL:
                    lambda f: f.name,
                self.TAGS_COL:
                    lambda f: _get_tags_display_string(f.tags),
                self.ADDRESS_COL:
                    lambda f: "%x" % f.addr,
                self.BINARY_COL:
                    lambda f: self._get_binary_name(f),
                self.SIZE_COL:
                    lambda f: "%d" % f.size,
                self.BLOCKS_COL:
                    lambda f: "%d" % len(f.block_addrs_set),
            }

            return mapping[col](func)

        elif role == Qt.ForegroundRole:
            # calculate the foreground color

            color = QColor(0, 0, 0)
            if func.is_syscall:
                color = QColor(0, 0, 0x80)
            elif func.is_plt:
                color = QColor(0, 0x80, 0)
            elif func.is_simprocedure:
                color = QColor(0x80, 0, 0)

            #for w in widgets:
            #    w.setFlags(w.flags() & ~Qt.ItemIsEditable)
            #    w.setForeground(color)

            return QBrush(color)

        elif role == Qt.BackgroundColorRole:
            color = QColor(0xff, 0xff, 0xff)
            r, g, b = self._get_function_backcolor(func)
            if r is not None and g is not None and b is not None:
                color = QColor(r, g, b)

            return QBrush(color)

        elif role == Qt.FontRole:
            return Conf.ui_default_font

    def sort(self, column, order):
        mapping = {
            self.NAME_COL:
                lambda: sorted(self.func_list, key=lambda f: f.name, reverse=order==Qt.DescendingOrder),
            self.TAGS_COL:
                lambda: sorted(self.func_list, key=lambda f: f.tags, reverse=order==Qt.DescendingOrder),
            self.ADDRESS_COL:
                lambda: sorted(self.func_list, key=lambda f: f.addr, reverse=order==Qt.DescendingOrder),
            self.BINARY_COL:
                lambda: sorted(self.func_list, key=lambda f: self._get_binary_name(f), reverse=order==Qt.DescendingOrder),
            self.SIZE_COL:
                lambda: sorted(self.func_list, key=lambda f: f.size, reverse=order==Qt.DescendingOrder),
            self.BLOCKS_COL:
                lambda: sorted(self.func_list, key=lambda f: len(f.block_addrs_set), reverse=order==Qt.DescendingOrder),
        }

        self.func_list = mapping[column]()

    #
    # Private methods
    #

    def _get_binary_name(self, func):
        return os.path.basename(func.binary.binary) if func.binary is not None else ""

    def _func_match_keyword(self, func, keyword):
        """
        Check whether the function matches against the given keyword or not.

        :param func:        The function to match on.
        :param str keyword: The keyword to match against.
        :return:            True if the function matches the keyword, False otherwise.
        :rtype:             bool
        """

        if keyword in func.name:
            return True
        if type(func.addr) is int:
            if keyword in "%x" % func.addr:
                return True
            if keyword in "%#x" % func.addr:
                return True
        if keyword.lower() in ",".join(func.tags).lower():
            return True
        if func.binary and keyword in func.binary.binary:
            return True
        return False


class QFunctionTableView(QTableView):
    def __init__(self, parent, selection_callback=None):
        super(QFunctionTableView, self).__init__(parent)

        self._function_table = parent  # type: QFunctionTable
        self._selected_func = ObjectContainer(None, 'Currently selected function')
        self._selected_func.am_subscribe(selection_callback)

        self.horizontalHeader().setVisible(True)
        self.verticalHeader().setVisible(False)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setHorizontalScrollMode(self.ScrollPerPixel)
        self.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)

        # sorting
        # self.horizontalHeader().setSortIndicatorShown(True)

        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.verticalHeader().setDefaultSectionSize(24)

        self._functions = None
        self._model = QFunctionTableModel(self._function_table.get_function_backcolor)
        self.setModel(self._model)

        # slots
        self.horizontalHeader().sortIndicatorChanged.connect(self.sortByColumn)
        self.doubleClicked.connect(self._on_function_selected)

    @property
    def function_manager(self):
        return self._functions

    @function_manager.setter
    def function_manager(self, functions):
        self._functions = functions
        self._model.func_list = list(self._functions.values())

    def subscribe_func_select(self, callback):
        self._selected_func.am_subscribe(callback)

    def filter(self, keyword):
        self._model.filter(keyword)

    def _on_function_selected(self, model_index):
        row = model_index.row()
        self._selected_func.am_obj = self._model.func_list[row]
        self._selected_func.am_event(func=self._selected_func.am_obj)

    def keyPressEvent(self, key_event):

        text = key_event.text()
        if not text or text not in string.printable or text in string.whitespace:
            # modifier keys
            return super(QFunctionTableView, self).keyPressEvent(key_event)

        # show the filtering text box
        self._function_table.show_filter_box(prefix=text)
        return True


class QFunctionTableFilterBox(QLineEdit):
    def __init__(self, parent):
        super(QFunctionTableFilterBox, self).__init__()

        self._table = parent

        self.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Escape:
                if self.text():
                    # clear the text
                    self.setText("")
                else:
                    # close the filterbox and set the function table on focus
                    self._table.hide_filter_box()
                return True

        return False


class QFunctionTable(QWidget):

    def __init__(self, parent, selection_callback=None):
        super(QFunctionTable, self).__init__(parent)

        self._view = parent  # type: 'FunctionsView'
        self._table_view = None  # type: QFunctionTableView
        self._filter_box = None  # type: QFunctionTableFilterBox

        self._init_widgets(selection_callback)

    @property
    def function_manager(self):
        if self._table_view is not None:
            return self._table_view.function_manager
        return None

    @function_manager.setter
    def function_manager(self, v):
        if v is not None:
            self._view.set_function_count(len(v))
        if self._table_view is not None:
            self._table_view.function_manager = v
        else:
            raise ValueError("QFunctionTableView is uninitialized.")

    def get_function_backcolor(self, func):
        return self._view.get_function_backcolor(func)

    #
    # Public methods
    #

    def show_filter_box(self, prefix=""):
        if prefix:
            self._filter_box.setText(prefix)
        self._filter_box.show()
        self._filter_box.setFocus()

    def hide_filter_box(self):
        self._filter_box.hide()
        self._table_view.setFocus()

    def subscribe_func_select(self, callback):
        self._table_view.subscribe_func_select(callback)

    #
    # Private methods
    #

    def _init_widgets(self, selection_callback=None):

        # function table view
        self._table_view = QFunctionTableView(self, selection_callback)

        # filter text box
        self._filter_box = QFunctionTableFilterBox(self)
        self._filter_box.hide()
        self._filter_box.textChanged.connect(self._on_filter_box_text_changed)
        self._filter_box.returnPressed.connect(self._on_filter_box_return_pressed)

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self._filter_box)
        layout.addWidget(self._table_view)

        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

    #
    # Events
    #

    def _on_filter_box_text_changed(self, text):
        self._table_view.filter(text)

    def _on_filter_box_return_pressed(self):
        # Clear the filter
        self._filter_box.setText("")
        # Hide the filter box
        self.hide_filter_box()
