import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QHBoxLayout

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Password Analysis Chart'
        self.setGeometry(100, 100, 1200, 800)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        # Set up the main layout
        main_layout = QVBoxLayout()

        # Create figures and canvases
        self.fig1, self.ax1, self.canvas1 = self.setup_figure()
        self.fig2, self.ax2, self.canvas2 = self.setup_figure()
        self.fig3, self.ax3, self.canvas3 = self.setup_figure()
        self.fig4, self.ax4, self.canvas4 = self.setup_figure()

        # Add canvases to the chart layout
        chart_layout = QHBoxLayout()
        chart_layout.addWidget(self.canvas1)
        chart_layout.addWidget(self.canvas2)
        chart_layout.addWidget(self.canvas3)
        chart_layout.addWidget(self.canvas4)

        # Create buttons and add them to the button layout
        button_layout = QHBoxLayout()
        self.btn_load = QPushButton('Load CSV File')
        self.btn_load.clicked.connect(self.load_csv)
        self.btn_plot = QPushButton('Generate Charts')
        self.btn_plot.clicked.connect(self.plot)
        self.btn_clear = QPushButton('Clear Charts')
        self.btn_clear.clicked.connect(self.clear_plot)
        button_layout.addWidget(self.btn_load)
        button_layout.addWidget(self.btn_plot)
        button_layout.addWidget(self.btn_clear)

        # Combine the layouts
        main_layout.addLayout(chart_layout)
        main_layout.addLayout(button_layout)

        # Set the main widget
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def setup_figure(self):
        fig = Figure()
        ax = fig.add_subplot(111)
        canvas = FigureCanvas(fig)
        return fig, ax, canvas

    def load_csv(self):
        # Open a file dialog to select a CSV file
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Select CSV File", "", "CSV Files (*.csv)", options=options)
        if fileName:
            self.csv_file = fileName
            print("Selected file:", self.csv_file)

    def plot(self):
        # Check if a CSV file has been selected
        if hasattr(self, 'csv_file'):
            try:
                # Read the CSV file
                data = pd.read_csv(self.csv_file, encoding='utf-8')
                # Check for required columns
                required_columns = ['length', 'num_digits', 'num_vowels', 'num_chars']
                if all(column in data.columns for column in required_columns):
                    # Plot the data
                    self.plot_data(data)
                else:
                    print("The CSV file is missing necessary columns.")
            except Exception as e:
                print(f"Error reading CSV file: {e}")
        else:
            print("Please select a CSV file first.")

    def plot_data(self, data):
        # Clear and plot each figure
        self.ax1.clear()
        self.ax1.hist(data['length'], bins=10, color='blue', alpha=0.7, edgecolor='black')
        self.ax1.set_title('Password Length Distribution Chart')
        self.ax1.set_xlabel('Password Length')
        self.ax1.set_ylabel('Count')
        self.canvas1.draw()

        self.ax2.clear()
        self.ax2.hist(data['num_digits'], bins=10, color='blue', alpha=0.7, edgecolor='black')
        self.ax2.set_title('Number of Digits Distribution Chart')
        self.ax2.set_xlabel('Number of Digits')
        self.ax2.set_ylabel('Count')
        self.canvas2.draw()

        self.ax3.clear()
        self.ax3.hist(data['num_vowels'], bins=10, color='blue', alpha=0.7, edgecolor='black')
        self.ax3.set_title('Number of Vowels Distribution Chart')
        self.ax3.set_xlabel('Number of Vowels')
        self.ax3.set_ylabel('Count')
        self.canvas3.draw()

        self.ax4.clear()
        self.ax4.hist(data['num_chars'], bins=10, color='blue', alpha=0.7, edgecolor='black')
        self.ax4.set_title('Number of Characters Distribution Chart')
        self.ax4.set_xlabel('Number of Characters')
        self.ax4.set_ylabel('Count')
        self.canvas4.draw()

    def clear_plot(self):
        # Clear all the plots
        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()
        self.ax4.clear()
        self.ax1.set_title('')
        self.ax2.set_title('')
        self.ax3.set_title('')
        self.ax4.set_title('')
        self.canvas1.draw()
        self.canvas2.draw()
        self.canvas3.draw()
        self.canvas4.draw()


def main():
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()