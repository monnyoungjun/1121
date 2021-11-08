#include "mainwindow.h"
#include <QtGui>
//#include "connect.h"
//#include "customsqlmodel.h"
//#include "editablesqlmodel.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();
    return a.exec();
}
