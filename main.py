import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QColor, QPalette
from textblob import TextBlob


class SentimentAnalyzer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sentiment Analyzer')
        self.setGeometry(100, 100, 400, 200)
        self.initUI()

    def initUI(self):
        self.input_label = QLabel('Enter Text:', self)
        self.input_edit = QLineEdit(self)
        self.sentiment_label = QLabel('Sentiment Score:', self)

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.input_label)
        vbox.addWidget(self.input_edit)
        vbox.addWidget(self.sentiment_label)

        pal = QPalette()
        bg_color = QColor(255, 255, 255, 100)
        pal.setColor(QPalette.Window, bg_color)
        self.setPalette(pal)

        self.input_label.setStyleSheet('''
            QLabel {
                color: white;
                font-size: 12px;
            }
        ''')

        self.input_edit.setStyleSheet('''
            QLineEdit {
                background: rgba(255, 255, 255, 0.2);
                font-size: 12px;
                color: white;
                border: 1px solid gray;
                border-radius: 10px;
                padding: 5px;
            }

            QLineEdit:focus {
                background: rgba(255, 255, 255, 0.4);
            }
        ''')

        self.sentiment_label.setStyleSheet('''
            QLabel {
                color: white;
                font-size: 12px;
            }
        ''')

        self.input_edit.textChanged.connect(self.analyze_sentiment)

    def analyze_sentiment(self):
        text = self.input_edit.text()
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        self.sentiment_label.setText(f'Sentiment Score: {sentiment:.2f}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SentimentAnalyzer()
    ex.show()
    sys.exit(app.exec_())
