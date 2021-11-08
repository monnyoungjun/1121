#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

    void asd();
    void reapeat();
    void reapeat2();
    void reset();
    void AI();

    Ui::MainWindow *ui;

private slots:
    void on_start_clicked();


    void on_user_1_clicked();

    void on_user_2_clicked();
    void on_user_3_clicked();
    void on_user_4_clicked();
    void on_user_5_clicked();
    void on_user_6_clicked();
    void on_user_7_clicked();
    void on_user_8_clicked();
    void on_user_9_clicked();
    void on_user_10_clicked();
    void on_user_11_clicked();
    void on_user_12_clicked();
    void on_user_13_clicked();
    void on_user_14_clicked();
    void on_user_15_clicked();
    void on_user_16_clicked();
    void on_user_17_clicked();
    void on_user_18_clicked();
    void on_user_19_clicked();
    void on_user_20_clicked();
    void on_user_21_clicked();
    void on_user_22_clicked();
    void on_user_23_clicked();
    void on_user_24_clicked();
    void on_user_25_clicked();



    void on_pushButton_start_clicked();

    void on_pushButton_ani_clicked();

    void on_pushButton_lol_clicked();

    void on_pushButton_out1_clicked();

    void on_pushButton_out4_clicked();

    void on_pushButton_out2_clicked();

    void on_pushButton_out3_clicked();

    void on_pushButton_return2_clicked();

    void on_pushButton_return3_clicked();

    void on_pushButton_return1_clicked();

    void on_label_8_linkActivated(const QString &link);

private:

};
#endif // MAINWINDOW_H
