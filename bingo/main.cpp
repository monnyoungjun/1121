
#include <QApplication>
#include <QPushButton>
#include <QDebug>
#include <QTextStream>
#include <mainwindow.h>

int main(int argc, char *argv[])
{
    QTextStream qout(stdout);
    QApplication app(argc, argv);
    qDebug() << "Hello World";
    MainWindow w;
    w.show();
    return app.exec();
}
