#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "QString"
#include<iostream>
#include<cstdlib>
#include<ctime>
#include <QDebug>
#include "QThread"
#include <QTimer>
#include <QMessageBox>

int sum = 0;
int ai_sum =0;


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_start_clicked()
{

}


void MainWindow::on_user_1_clicked()
{

    ui->user_1->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_1->text());

    reapeat();

    ui -> user_1 -> setText("#");
    ui -> user_1 -> setEnabled(false);

    asd();
    AI();


}
void MainWindow::on_user_2_clicked()
{

    ui->user_2->setStyleSheet(
           "background-color: Red"
                  );

    ui->score1->clear();
    ui->score1->setText(ui->user_2->text());
    reapeat();
    ui -> user_2 -> setText("#");
    ui -> user_2 -> setEnabled(false);

    asd();
    AI();
}

void MainWindow::on_user_3_clicked()
{

    ui->user_3->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_3->text());
    reapeat();
    ui -> user_3 -> setText("#");
    ui -> user_3 -> setEnabled(false);

    asd();
    AI();
}

void MainWindow::on_user_4_clicked()
{

    ui->user_4->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_4->text());
    reapeat();
    ui -> user_4 -> setText("#");
    ui -> user_4 -> setEnabled(false);

    asd();
    AI();
}

void MainWindow::on_user_5_clicked()
{

    ui->user_5->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_5->text());
    reapeat();
    ui -> user_5 -> setText("#");
    ui -> user_5 -> setEnabled(false);

    asd();
    AI();
}

void MainWindow::on_user_6_clicked()
{

    ui->user_6->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_6->text());
    reapeat();
    ui -> user_6 -> setText("#");
    ui -> user_6 -> setEnabled(false);

    asd();
    AI();
}

void MainWindow::on_user_7_clicked()
{

    ui->user_7->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_7->text());
    reapeat();
    ui -> user_7 -> setText("#");
    ui -> user_7 -> setEnabled(false);

    asd();
    AI();
}

void MainWindow::on_user_8_clicked()
{

    ui->user_8->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_8->text());
    reapeat();
    ui -> user_8 -> setText("#");
    ui -> user_8 -> setEnabled(false);

    asd();
    AI();
}

void MainWindow::on_user_9_clicked()
{

    ui->user_9->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_9->text());
    reapeat();
    ui -> user_9 -> setText("#");
    ui -> user_9 -> setEnabled(false);

    asd();
    AI();
}

void MainWindow::on_user_10_clicked()
{

    ui->user_10->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_10->text());
    reapeat();
    ui -> user_10 -> setText("#");
    ui -> user_10 -> setEnabled(false);
    asd();
    AI();
}

void MainWindow::on_user_11_clicked()
{

    ui->user_11->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_11->text());
    reapeat();
    ui -> user_11 -> setText("#");
    ui -> user_11 -> setEnabled(false);
    asd();
    AI();
}

void MainWindow::on_user_12_clicked()
{

    ui->user_12->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_12->text());
    reapeat();
    ui -> user_12 -> setText("#");
    ui -> user_12 -> setEnabled(false);
    asd();
    AI();
}


void MainWindow::on_user_13_clicked()
{

    ui->user_13->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_13->text());
    reapeat();
    ui -> user_13 -> setText("#");
    ui -> user_13 -> setEnabled(false);
    asd();
    AI();
}

void MainWindow::on_user_14_clicked()
{

    ui->user_14->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_14->text());
    reapeat();
    ui -> user_14 -> setText("#");
    ui -> user_14 -> setEnabled(false);
    asd();
    AI();
}

void MainWindow::on_user_15_clicked()
{

    ui->user_15->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_15->text());
    reapeat();
    ui -> user_15 -> setText("#");
    ui -> user_15 -> setEnabled(false);
    asd();
    AI();
}

void MainWindow::on_user_16_clicked()
{

    ui->user_16->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_16->text());
    reapeat();
    ui -> user_16 -> setText("#");
    ui -> user_16 -> setEnabled(false);
    asd();
    AI();
}

void MainWindow::on_user_17_clicked()
{

    ui->user_17->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_17->text());
    reapeat();
    ui -> user_17 -> setText("#");
    ui -> user_17 -> setEnabled(false);
    asd();
    AI();
}

void MainWindow::on_user_18_clicked()
{

    ui->user_18->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_18->text());
    reapeat();
    ui -> user_18 -> setText("#");
    ui -> user_18 -> setEnabled(false);
    asd();
    AI();
}

void MainWindow::on_user_19_clicked()
{

    ui->user_19->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_19->text());
    reapeat();
     ui -> user_19 -> setText("#");
     ui -> user_19 -> setEnabled(false);
    asd();
    AI();
}

void MainWindow::on_user_20_clicked()
{

    ui->user_20->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_20->text());
    reapeat();
    ui -> user_20 -> setText("#");
    ui -> user_20 -> setEnabled(false);
    asd();
    AI();
}

void MainWindow::on_user_21_clicked()
{

    ui->user_21->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_21->text());
    reapeat();
     ui -> user_21 -> setText("#");
     ui -> user_21 -> setEnabled(false);
    asd();
    AI();
}

void MainWindow::on_user_22_clicked()
{

    ui->user_22->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_22->text());
    reapeat();
    ui -> user_22 -> setText("#");
    ui -> user_22-> setEnabled(false);
    asd();
    AI();
}

void MainWindow::on_user_23_clicked()
{

    ui->user_23->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_23->text());
    reapeat();
    ui -> user_23 -> setText("#");
    ui -> user_23-> setEnabled(false);
    asd();
    AI();
}

void MainWindow::on_user_24_clicked()
{

    ui->user_24->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_24->text());
    reapeat();
    ui -> user_24 -> setText("#");
    ui -> user_24 -> setEnabled(false);
    asd();
    AI();
}

void MainWindow::on_user_25_clicked()
{

    ui->user_25->setStyleSheet(
           "background-color: Red"
                  );
    ui->score1->clear();
    ui->score1->setText(ui->user_25->text());
    reapeat();
    ui -> user_25 -> setText("#");
    ui -> user_25 -> setEnabled(false);
    asd();
    AI();
}

void MainWindow::asd()
{
    QString a1 = ui ->user_1 -> text();
    QString a2 = ui ->user_2 -> text();
    QString a3 = ui ->user_3 -> text();
    QString a4 = ui ->user_4 -> text();
    QString a5 = ui ->user_5 -> text();
    QString a6 = ui ->user_6 -> text();
    QString a7 = ui ->user_7 -> text();
    QString a8 = ui ->user_8 -> text();
    QString a9 = ui ->user_9 -> text();
    QString a10 = ui ->user_10 -> text();
    QString a11 = ui ->user_11 -> text();
    QString a12 = ui ->user_12 -> text();
    QString a13 = ui ->user_13 -> text();
    QString a14 = ui ->user_14 -> text();
    QString a15 = ui ->user_15 -> text();
    QString a16 = ui ->user_16 -> text();
    QString a17 = ui ->user_17 -> text();
    QString a18 = ui ->user_18 -> text();
    QString a19 = ui ->user_19 -> text();
    QString a20 = ui ->user_20 -> text();
    QString a21 = ui ->user_21 -> text();
    QString a22 = ui ->user_22 -> text();
    QString a23 = ui ->user_23 -> text();
    QString a24 = ui ->user_24 -> text();
    QString a25 = ui ->user_25 -> text();


    sum = 0;
    ai_sum = 0;

    if (a1 == "#" && a2 == "#" && a3 == "#" && a4 == "#" && a5 == "#")
    {
        sum += 1;
        if(sum == 1)
        {
            QString sum2 = "빙고의 갯수는 : 1";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 2)
        {
            QString sum2 = "빙고의 갯수는 : 2";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 3)
        {
            QString sum2 = "빙고의 갯수는 : 3";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 4)
        {
            QString sum2 = "빙고의 갯수는 : 4";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum >= 5)
        {
            QString sum2 = "빙고의 갯수는 : 5";
            ui -> score1_2 -> setPlainText(sum2);
        }
    }
    if (a5 == "#" && a9 == "#" && a13 == "#" && a17 == "#" && a21 == "#")
    {
        sum += 1;
        if(sum == 1)
        {
            QString sum2 = "빙고의 갯수는 : 1";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 2)
        {
            QString sum2 = "빙고의 갯수는 : 2";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 3)
        {
            QString sum2 = "빙고의 갯수는 : 3";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 4)
        {
            QString sum2 = "빙고의 갯수는 : 4";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum >= 5)
        {
            QString sum2 = "빙고의 갯수는 : 5";
            ui -> score1_2 -> setPlainText(sum2);
        }
    }
    if (a1 == "#" && a6 == "#" && a11 == "#" && a16 == "#" && a21 == "#")
    {
        sum += 1;
        if(sum == 1)
        {
            QString sum2 = "빙고의 갯수는 : 1";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 2)
        {
            QString sum2 = "빙고의 갯수는 : 2";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 3)
        {
            QString sum2 = "빙고의 갯수는 : 3";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 4)
        {
            QString sum2 = "빙고의 갯수는 : 4";
            ui -> score1_2 -> setPlainText(sum2);
        }

        if(sum >= 5)
        {
            QString sum2 = "빙고의 갯수는 : 5";
            ui -> score1_2 -> setPlainText(sum2);
        }
    }
    if (a1 == "#" && a7 == "#" && a13 == "#" && a19 == "#" && a25 == "#")
    {
        sum += 1;
        if(sum == 1)
        {
            QString sum2 = "빙고의 갯수는 : 1";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 2)
        {
            QString sum2 = "빙고의 갯수는 : 2";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 3)
        {
            QString sum2 = "빙고의 갯수는 : 3";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 4)
        {
            QString sum2 = "빙고의 갯수는 : 4";
            ui -> score1_2 -> setPlainText(sum2);
        }

        if(sum >= 5)
        {
            QString sum2 = "빙고의 갯수는 : 5";
            ui -> score1_2 -> setPlainText(sum2);
        }
    }
    if (a21 == "#" && a22 == "#" && a23 == "#" && a24 == "#" && a25 == "#")
    {
            sum += 1;

            if(sum == 1)
            {
                QString sum2 = "빙고의 갯수는 : 1";
                ui -> score1_2 -> setPlainText(sum2);
            }
            if(sum == 2)
            {
                QString sum2 = "빙고의 갯수는 : 2";
                ui -> score1_2 -> setPlainText(sum2);
            }
            if(sum == 3)
            {
                QString sum2 = "빙고의 갯수는 : 3";
                ui -> score1_2 -> setPlainText(sum2);
            }
            if(sum == 4)
            {
                QString sum2 = "빙고의 갯수는 : 4";
                ui -> score1_2 -> setPlainText(sum2);
            }

            if(sum >= 5)
            {
                QString sum2 = "빙고의 갯수는 : 5";
                ui -> score1_2 -> setPlainText(sum2);
            }
    }
    if (a5 == "#" && a10 == "#" && a15 == "#" && a20 == "#" && a25 == "#")
        {
            sum += 1;
            if(sum == 1)
            {
                QString sum2 = "빙고의 갯수는 : 1";
                ui -> score1_2 -> setPlainText(sum2);
            }
            if(sum == 2)
            {
                QString sum2 = "빙고의 갯수는 : 2";
                ui -> score1_2 -> setPlainText(sum2);
            }
            if(sum == 3)
            {
                QString sum2 = "빙고의 갯수는 : 3";
                ui -> score1_2 -> setPlainText(sum2);
            }
            if(sum == 4)
            {
                QString sum2 = "빙고의 갯수는 : 4";
                ui -> score1_2 -> setPlainText(sum2);
            }

            if(sum >= 5)
            {
                QString sum2 = "빙고의 갯수는 : 5";
                ui -> score1_2 -> setPlainText(sum2);
            }
    }
    if (a2 == "#" && a7 == "#" && a12 == "#" && a17 == "#" && a22 == "#")
    {
            sum += 1;
            if(sum == 1)
            {
                QString sum2 = "빙고의 갯수는 : 1";
                ui -> score1_2 -> setPlainText(sum2);
            }
            if(sum == 2)
            {
                QString sum2 = "빙고의 갯수는 : 2";
                ui -> score1_2 -> setPlainText(sum2);
            }
            if(sum == 3)
            {
                QString sum2 = "빙고의 갯수는 : 3";
                ui -> score1_2 -> setPlainText(sum2);
            }
            if(sum == 4)
            {
                QString sum2 = "빙고의 갯수는 : 4";
                ui -> score1_2 -> setPlainText(sum2);
            }

            if(sum >= 5)
            {
                QString sum2 = "빙고의 갯수는 : 5";
                ui -> score1_2 -> setPlainText(sum2);
            }
    }
    if (a3 == "#" && a8 == "#" && a13 == "#" && a18 == "#" && a23 == "#")
    {
        sum += 1;
        if(sum == 1)
        {
            QString sum2 = "빙고의 갯수는 : 1";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 2)
        {
            QString sum2 = "빙고의 갯수는 : 2";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 3)
        {
            QString sum2 = "빙고의 갯수는 : 3";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 4)
        {
            QString sum2 = "빙고의 갯수는 : 4";
            ui -> score1_2 -> setPlainText(sum2);
        }

        if(sum >= 5)
        {
            QString sum2 = "빙고의 갯수는 : 5";
            ui -> score1_2 -> setPlainText(sum2);
        }
    }
    if (a4 == "#" && a9 == "#" && a14 == "#" && a19 == "#" && a24 == "#")
    {
        sum += 1;
        if(sum == 1)
        {
            QString sum2 = "빙고의 갯수는 : 1";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 2)
        {
            QString sum2 = "빙고의 갯수는 : 2";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 3)
        {
            QString sum2 = "빙고의 갯수는 : 3";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 4)
        {
            QString sum2 = "빙고의 갯수는 : 4";
            ui -> score1_2 -> setPlainText(sum2);
        }

        if(sum >= 5)
        {
            QString sum2 = "빙고의 갯수는 : 5";
            ui -> score1_2 -> setPlainText(sum2);

        }
    }
    if (a6 == "#" && a7 == "#" && a8 == "#" && a9 == "#" && a10 == "#")
    {
        sum += 1;
        if(sum == 1)
        {
            QString sum2 = "빙고의 갯수는 : 1";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 2)
        {
            QString sum2 = "빙고의 갯수는 : 2";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 3)
        {
            QString sum2 = "빙고의 갯수는 : 3";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 4)
        {
            QString sum2 = "빙고의 갯수는 : 4";
            ui -> score1_2 -> setPlainText(sum2);
        }

        if(sum >= 5)
        {
            QString sum2 = "빙고의 갯수는 : 5";
            ui -> score1_2 -> setPlainText(sum2);

        }
    }
    if (a11 == "#" && a12 == "#" && a13 == "#" && a14 == "#" && a15 == "#")
    {
        sum += 1;
        if(sum == 1)
        {
            QString sum2 = "빙고의 갯수는 : 1";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 2)
        {
            QString sum2 = "빙고의 갯수는 : 2";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 3)
        {
            QString sum2 = "빙고의 갯수는 : 3";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 4)
        {
            QString sum2 = "빙고의 갯수는 : 4";
            ui -> score1_2 -> setPlainText(sum2);
        }

        if(sum >= 5)
        {
            QString sum2 = "빙고의 갯수는 : 5";
            ui -> score1_2 -> setPlainText(sum2);

        }
    }
    if (a16 == "#" && a17 == "#" && a18 == "#" && a19 == "#" && a20 == "#")
    {
        sum += 1;
        if(sum == 1)
        {
            QString sum2 = "빙고의 갯수는 : 1";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 2)
        {
            QString sum2 = "빙고의 갯수는 : 2";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 3)
        {
            QString sum2 = "빙고의 갯수는 : 3";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum == 4)
        {
            QString sum2 = "빙고의 갯수는 : 4";
            ui -> score1_2 -> setPlainText(sum2);
        }
        if(sum >= 5)
        {
            QString sum2 = "빙고의 갯수는 : 5";
            ui -> score1_2 -> setPlainText(sum2);

        }
    }

    QString b1 = ui ->ai_1 -> text();
    QString b2 = ui ->ai_2 -> text();
    QString b3 = ui ->ai_3 -> text();
    QString b4 = ui ->ai_4 -> text();
    QString b5 = ui ->ai_5 -> text();
    QString b6 = ui ->ai_6 -> text();
    QString b7 = ui ->ai_7 -> text();
    QString b8 = ui ->ai_8 -> text();
    QString b9 = ui ->ai_9 -> text();
    QString b10 = ui ->ai_10 -> text();
    QString b11 = ui ->ai_11 -> text();
    QString b12 = ui ->ai_12 -> text();
    QString b13 = ui ->ai_13 -> text();
    QString b14 = ui ->ai_14 -> text();
    QString b15 = ui ->ai_15 -> text();
    QString b16 = ui ->ai_16 -> text();
    QString b17 = ui ->ai_17 -> text();
    QString b18 = ui ->ai_18 -> text();
    QString b19 = ui ->ai_19 -> text();
    QString b20 = ui ->ai_20 -> text();
    QString b21 = ui ->ai_21 -> text();
    QString b22 = ui ->ai_22 -> text();
    QString b23 = ui ->ai_23 -> text();
    QString b24 = ui ->ai_24 -> text();
    QString b25 = ui ->ai_25 -> text();

    if (b1 == "#" && b2 == "#" && b3 == "#" && b4 == "#" && b5 == "#")
    {
        ai_sum += 1;
        if(ai_sum == 1)
        {
            QString ai_sum2 = "빙고의 갯수는 : 1";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 2)
        {
            QString ai_sum2 = "빙고의 갯수는 : 2";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 3)
        {
            QString ai_sum2 = "빙고의 갯수는 : 3";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 4)
        {
            QString ai_sum2 = "빙고의 갯수는 : 4";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum >= 5)
        {
            QString ai_sum2 = "빙고의 갯수는 : 5";
            ui -> score2_2 -> setPlainText(ai_sum2);

        }
    }
    if (b5 == "#" && b9 == "#" && b13 == "#" && b17 == "#" && b21 == "#")
    {
        ai_sum += 1;
        if(ai_sum == 1)
        {
            QString ai_sum2 = "빙고의 갯수는 : 1";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 2)
        {
            QString ai_sum2 = "빙고의 갯수는 : 2";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 3)
        {
            QString ai_sum2 = "빙고의 갯수는 : 3";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 4)
        {
            QString ai_sum2 = "빙고의 갯수는 : 4";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum >= 5)
        {
            QString ai_sum2 = "빙고의 갯수는 : 5";
            ui -> score2_2 -> setPlainText(ai_sum2);

        }
    }
    if (b1 == "#" && b6 == "#" && b11 == "#" && b16 == "#" && b21 == "#")
    {
        ai_sum += 1;
        if(ai_sum == 1)
        {
            QString ai_sum2 = "빙고의 갯수는 : 1";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 2)
        {
            QString ai_sum2 = "빙고의 갯수는 : 2";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 3)
        {
            QString ai_sum2 = "빙고의 갯수는 : 3";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 4)
        {
            QString ai_sum2 = "빙고의 갯수는 : 4";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum >= 5)
        {
            QString ai_sum2 = "빙고의 갯수는 : 5";
            ui -> score2_2 -> setPlainText(ai_sum2);

        }
    }
    if (b1 == "#" && b7 == "#" && b13 == "#" && b19 == "#" && b25 == "#")
    {
        ai_sum += 1;
        if(ai_sum == 1)
        {
            QString ai_sum2 = "빙고의 갯수는 : 1";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 2)
        {
            QString ai_sum2 = "빙고의 갯수는 : 2";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 3)
        {
            QString ai_sum2 = "빙고의 갯수는 : 3";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 4)
        {
            QString ai_sum2 = "빙고의 갯수는 : 4";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum >= 5)
        {
            QString ai_sum2 = "빙고의 갯수는 : 5";
            ui -> score2_2 -> setPlainText(ai_sum2);

        }
    }
    if (b21 == "#" && b22 == "#" && b23 == "#" && b24 == "#" && b25 == "#")
    {
        ai_sum += 1;
        if(ai_sum == 1)
        {
            QString ai_sum2 = "빙고의 갯수는 : 1";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 2)
        {
            QString ai_sum2 = "빙고의 갯수는 : 2";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 3)
        {
            QString ai_sum2 = "빙고의 갯수는 : 3";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 4)
        {
            QString ai_sum2 = "빙고의 갯수는 : 4";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum >= 5)
        {
            QString ai_sum2 = "빙고의 갯수는 : 5";
            ui -> score2_2 -> setPlainText(ai_sum2);

        }
    }
    if (b5 == "#" && b10 == "#" && b15 == "#" && b20 == "#" && b25 == "#")
        {
        ai_sum += 1;
        if(ai_sum == 1)
        {
            QString ai_sum2 = "빙고의 갯수는 : 1";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 2)
        {
            QString ai_sum2 = "빙고의 갯수는 : 2";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 3)
        {
            QString ai_sum2 = "빙고의 갯수는 : 3";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 4)
        {
            QString ai_sum2 = "빙고의 갯수는 : 4";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum >= 5)
        {
            QString ai_sum2 = "빙고의 갯수는 : 5";
            ui -> score2_2 -> setPlainText(ai_sum2);

        }
    }
    if (b2 == "#" && b7 == "#" && b12 == "#" && b17 == "#" && b22 == "#")
    {
        ai_sum += 1;
        if(ai_sum == 1)
        {
            QString ai_sum2 = "빙고의 갯수는 : 1";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 2)
        {
            QString ai_sum2 = "빙고의 갯수는 : 2";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 3)
        {
            QString ai_sum2 = "빙고의 갯수는 : 3";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 4)
        {
            QString ai_sum2 = "빙고의 갯수는 : 4";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum >= 5)
        {
            QString ai_sum2 = "빙고의 갯수는 : 5";
            ui -> score2_2 -> setPlainText(ai_sum2);

        }
    }
    if (b3 == "#" && b8 == "#" && b13 == "#" && b18 == "#" && b23 == "#")
    {
        ai_sum += 1;
        if(ai_sum == 1)
        {
            QString ai_sum2 = "빙고의 갯수는 : 1";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 2)
        {
            QString ai_sum2 = "빙고의 갯수는 : 2";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 3)
        {
            QString ai_sum2 = "빙고의 갯수는 : 3";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 4)
        {
            QString ai_sum2 = "빙고의 갯수는 : 4";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum >= 5)
        {
            QString ai_sum2 = "빙고의 갯수는 : 5";
            ui -> score2_2 -> setPlainText(ai_sum2);

        }
    }
    if (b4 == "#" && b9 == "#" && b14 == "#" && b19 == "#" && b24 == "#")
    {
        ai_sum += 1;
        if(ai_sum == 1)
        {
            QString ai_sum2 = "빙고의 갯수는 : 1";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 2)
        {
            QString ai_sum2 = "빙고의 갯수는 : 2";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 3)
        {
            QString ai_sum2 = "빙고의 갯수는 : 3";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 4)
        {
            QString ai_sum2 = "빙고의 갯수는 : 4";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum >= 5)
        {
            QString ai_sum2 = "빙고의 갯수는 : 5";
            ui -> score2_2 -> setPlainText(ai_sum2);

        }
    }
    if (b6 == "#" && b7 == "#" && b8 == "#" && b9 == "#" && b10 == "#")
    {
        ai_sum += 1;
        if(ai_sum == 1)
        {
            QString ai_sum2 = "빙고의 갯수는 : 1";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 2)
        {
            QString ai_sum2 = "빙고의 갯수는 : 2";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 3)
        {
            QString ai_sum2 = "빙고의 갯수는 : 3";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 4)
        {
            QString ai_sum2 = "빙고의 갯수는 : 4";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum >= 5)
        {
            QString ai_sum2 = "빙고의 갯수는 : 5";
            ui -> score2_2 -> setPlainText(ai_sum2);

        }
    }
    if (b11 == "#" && b12 == "#" && b13 == "#" && b14 == "#" && b15 == "#")
    {
        ai_sum += 1;
        if(ai_sum == 1)
        {
            QString ai_sum2 = "빙고의 갯수는 : 1";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 2)
        {
            QString ai_sum2 = "빙고의 갯수는 : 2";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 3)
        {
            QString ai_sum2 = "빙고의 갯수는 : 3";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 4)
        {
            QString ai_sum2 = "빙고의 갯수는 : 4";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum >= 5)
        {
            QString ai_sum2 = "빙고의 갯수는 : 5";
            ui -> score2_2 -> setPlainText(ai_sum2);

        }
    }
    if (b16 == "#" && b17 == "#" && b18 == "#" && b19 == "#" && b20 == "#")
    {
        ai_sum += 1;
        if(ai_sum == 1)
        {
            QString ai_sum2 = "빙고의 갯수는 : 1";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 2)
        {
            QString ai_sum2 = "빙고의 갯수는 : 2";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 3)
        {
            QString ai_sum2 = "빙고의 갯수는 : 3";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum == 4)
        {
            QString ai_sum2 = "빙고의 갯수는 : 4";
            ui -> score2_2 -> setPlainText(ai_sum2);
        }
        if(ai_sum >= 5)
        {
            QString ai_sum2 = "빙고의 갯수는 : 5";
            ui -> score2_2 -> setPlainText(ai_sum2);

        }
        //한쪽이 빙고 5칸이상일 경우
    }
    QMessageBox msgBox;
    if (sum >4 && ai_sum > 4)
    {
            msgBox.setText("무승부 입니다.");
            msgBox.exec();
        ui->stackedWidget->setCurrentIndex(5);
    }
    else if (sum > 4)
    {
        msgBox.setText("승리하였습니다.");
        msgBox.exec();
        ui->stackedWidget->setCurrentIndex(4);
    }
    else if (ai_sum > 4)
    {
        msgBox.setText("패배하였습니다.");
        msgBox.exec();
        ui->stackedWidget->setCurrentIndex(0);
    }





}

void MainWindow::on_pushButton_start_clicked()
{
    ui->stackedWidget->setCurrentIndex(2);
}

void MainWindow::on_pushButton_ani_clicked()
{
    ui->stackedWidget->setCurrentIndex(3);

    int looo[25] = {};

    QString LoL[30] = {"나미","라이즈","럭스","룰루","바이"
                       ,"사이온","소나","쉔","아리","애쉬"
                       ,"올라프","우디르","자이라","자크","잭스"
                     ,"제드","징크스","피즈","벡스","케일"
                       ,"피오라","코르키","타릭","탈론","뽀삐"};

    QString animal[30] = {"개","소","말","염소","양"
                    ,"쥐","사슴","호랑이","늑대","여우"
                    ,"사자","하이에나","두더지","돼지","나무늘보"
                    ,"곰","팬더","수달","물개","고래"
                    ,"오리","갈매기","매","백조","까마귀"};

    srand((unsigned int)time(NULL));

    qDebug() << "Hello World1231231";
    for (int i = 0; i < 25; i++) {
        looo[i] = rand() % 25;
        qDebug() << "Hello World";

        for (int j = 0; j < i; j++) {
            qDebug() << "Hello World22222";
            if (looo[i] == looo[j])
            {
                --i;
            }

        }
        for(int k = 0; k < 1; k++)
        {
            if(i == 1)
            {
            ui-> user_1 -> setText(animal[looo[i]]);
            }
            else if(i ==2)
            {
            ui-> user_2 -> setText(animal[looo[i]]);
            }
            else if(i ==3)
            {
            ui-> user_3 -> setText(animal[looo[i]]);
            }
            else if(i ==4)
            {
            ui-> user_4 -> setText(animal[looo[i]]);
            }
            else if(i ==5)
            {
            ui-> user_5 -> setText(animal[looo[i]]);
            }
            else if(i ==6)
            {
            ui-> user_6 -> setText(animal[looo[i]]);
            }
            else if(i ==7)
            {
            ui-> user_7 -> setText(animal[looo[i]]);
            }
            else if(i ==8)
            {
            ui-> user_8 -> setText(animal[looo[i]]);
            }
            else if(i ==9)
            {
            ui-> user_9 -> setText(animal[looo[i]]);
            }
            else if(i ==10)
            {
            ui-> user_10 -> setText(animal[looo[i]]);
            }
            else if(i ==11)
            {
            ui-> user_11 -> setText(animal[looo[i]]);
            }
            else if(i ==12)
            {
            ui-> user_12 -> setText(animal[looo[i]]);
            }
            else if(i ==13)
            {
            ui-> user_13 -> setText(animal[looo[i]]);
            }
            else if(i ==14)
            {
            ui-> user_14 -> setText(animal[looo[i]]);
            }
            else if(i ==15)
            {
            ui-> user_15 -> setText(animal[looo[i]]);
            }
            else if(i ==16)
            {
            ui-> user_16 -> setText(animal[looo[i]]);
            }
            else if(i ==17)
            {
            ui-> user_17 -> setText(animal[looo[i]]);
            }
            else if(i ==18)
            {
            ui-> user_18 -> setText(animal[looo[i]]);
            }
            else if(i ==19)
            {
            ui-> user_19 -> setText(animal[looo[i]]);
            }
            else if(i ==20)
            {
            ui-> user_20 -> setText(animal[looo[i]]);
            }
            else if(i ==21)
            {
            ui-> user_21 -> setText(animal[looo[i]]);
            }
            else if(i ==22)
            {
            ui-> user_22 -> setText(animal[looo[i]]);
            }
            else if(i ==23)
            {
            ui-> user_23 -> setText(animal[looo[i]]);
            }
            else if(i ==24)
            {
            ui-> user_24 -> setText(animal[looo[i]]);
            }
            else
            {
            ui-> user_25 -> setText(animal[looo[i]]);
            }
        }
    }

    for (int i = 0; i < 25; i++) {
        looo[i] = rand() % 25;
        qDebug() << "Hello World";

        for (int j = 0; j < i; j++) {
            qDebug() << "Hello World22222";
            if (looo[i] == looo[j])
            {
                --i;
            }

        }
        for(int k = 0; k < 1; k++)
        {
            if(i == 1)
            {
            ui-> ai_1 -> setText(animal[looo[i]]);
            }
            else if(i ==2)
            {
            ui-> ai_2 -> setText(animal[looo[i]]);
            }
            else if(i ==3)
            {
            ui-> ai_3 -> setText(animal[looo[i]]);
            }
            else if(i ==4)
            {
            ui-> ai_4 -> setText(animal[looo[i]]);
            }
            else if(i ==5)
            {
            ui-> ai_5 -> setText(animal[looo[i]]);
            }
            else if(i ==6)
            {
            ui-> ai_6 -> setText(animal[looo[i]]);
            }
            else if(i ==7)
            {
            ui-> ai_7 -> setText(animal[looo[i]]);
            }
            else if(i ==8)
            {
            ui-> ai_8 -> setText(animal[looo[i]]);
            }
            else if(i ==9)
            {
            ui-> ai_9 -> setText(animal[looo[i]]);
            }
            else if(i ==10)
            {
            ui-> ai_10 -> setText(animal[looo[i]]);
            }
            else if(i ==11)
            {
            ui-> ai_11 -> setText(animal[looo[i]]);
            }
            else if(i ==12)
            {
            ui-> ai_12 -> setText(animal[looo[i]]);
            }
            else if(i ==13)
            {
            ui-> ai_13 -> setText(animal[looo[i]]);
            }
            else if(i ==14)
            {
            ui-> ai_14 -> setText(animal[looo[i]]);
            }
            else if(i ==15)
            {
            ui-> ai_15 -> setText(animal[looo[i]]);
            }
            else if(i ==16)
            {
            ui-> ai_16 -> setText(animal[looo[i]]);
            }
            else if(i ==17)
            {
            ui-> ai_17 -> setText(animal[looo[i]]);
            }
            else if(i ==18)
            {
            ui-> ai_18 -> setText(animal[looo[i]]);
            }
            else if(i ==19)
            {
            ui-> ai_19 -> setText(animal[looo[i]]);
            }
            else if(i ==20)
            {
            ui-> ai_20 -> setText(animal[looo[i]]);
            }
            else if(i ==21)
            {
            ui-> ai_21 -> setText(animal[looo[i]]);
            }
            else if(i ==22)
            {
            ui-> ai_22 -> setText(animal[looo[i]]);
            }
            else if(i ==23)
            {
            ui-> ai_23 -> setText(animal[looo[i]]);
            }
            else if(i ==24)
            {
            ui-> ai_24 -> setText(animal[looo[i]]);
            }
            else
            {
            ui-> ai_25 -> setText(animal[looo[i]]);
            }
        }
    }

}

void MainWindow::on_pushButton_lol_clicked()
{
    ui->stackedWidget->setCurrentIndex(3);

    int looo[25] = {};

    QString LoL[30] = {"나미","라이즈","럭스","룰루","바이"
                       ,"사이온","소나","쉔","아리","애쉬"
                       ,"올라프","우디르","자이라","자크","잭스"
                     ,"제드","징크스","피즈","벡스","케일"
                       ,"피오라","코르키","타릭","탈론","뽀삐"};

    QString animal[30] = {"개","소","말","염소","양"
                    ,"쥐","사슴","호랑이","늑대","여우"
                    ,"사자","하이에나","두더지","돼지","나무늘보"
                    ,"곰","팬더","수달","물개","고래"
                    ,"오리","갈매기","매","백조","까마귀"};

    //유저쪽 채우기
    srand((unsigned int)time(NULL));

    qDebug() << "Hello World1231231";
    for (int i = 0; i < 25; i++) {
        looo[i] = rand() % 25;
        qDebug() << "Hello World";

        for (int j = 0; j < i; j++) {
            qDebug() << "Hello World22222";
            if (looo[i] == looo[j])
            {
                --i;
            }

        }
        for(int k = 0; k < 1; k++)
        {
            if(i == 1)
            {
            ui-> user_1 -> setText(LoL[looo[i]]);
            }
            else if(i ==2)
            {
            ui-> user_2 -> setText(LoL[looo[i]]);
            }
            else if(i ==3)
            {
            ui-> user_3 -> setText(LoL[looo[i]]);
            }
            else if(i ==4)
            {
            ui-> user_4 -> setText(LoL[looo[i]]);
            }
            else if(i ==5)
            {
            ui-> user_5 -> setText(LoL[looo[i]]);
            }
            else if(i ==6)
            {
            ui-> user_6 -> setText(LoL[looo[i]]);
            }
            else if(i ==7)
            {
            ui-> user_7 -> setText(LoL[looo[i]]);
            }
            else if(i ==8)
            {
            ui-> user_8 -> setText(LoL[looo[i]]);
            }
            else if(i ==9)
            {
            ui-> user_9 -> setText(LoL[looo[i]]);
            }
            else if(i ==10)
            {
            ui-> user_10 -> setText(LoL[looo[i]]);
            }
            else if(i ==11)
            {
            ui-> user_11 -> setText(LoL[looo[i]]);
            }
            else if(i ==12)
            {
            ui-> user_12 -> setText(LoL[looo[i]]);
            }
            else if(i ==13)
            {
            ui-> user_13 -> setText(LoL[looo[i]]);
            }
            else if(i ==14)
            {
            ui-> user_14 -> setText(LoL[looo[i]]);
            }
            else if(i ==15)
            {
            ui-> user_15 -> setText(LoL[looo[i]]);
            }
            else if(i ==16)
            {
            ui-> user_16 -> setText(LoL[looo[i]]);
            }
            else if(i ==17)
            {
            ui-> user_17 -> setText(LoL[looo[i]]);
            }
            else if(i ==18)
            {
            ui-> user_18 -> setText(LoL[looo[i]]);
            }
            else if(i ==19)
            {
            ui-> user_19 -> setText(LoL[looo[i]]);
            }
            else if(i ==20)
            {
            ui-> user_20 -> setText(LoL[looo[i]]);
            }
            else if(i ==21)
            {
            ui-> user_21 -> setText(LoL[looo[i]]);
            }
            else if(i ==22)
            {
            ui-> user_22 -> setText(LoL[looo[i]]);
            }
            else if(i ==23)
            {
            ui-> user_23 -> setText(LoL[looo[i]]);
            }
            else if(i ==24)
            {
            ui-> user_24 -> setText(LoL[looo[i]]);
            }
            else
            {
            ui-> user_25 -> setText(LoL[looo[i]]);
            }
        }
    }
    //ai쪽 라벨 채우기
    for (int i = 0; i < 25; i++) {
        looo[i] = rand() % 25;
        qDebug() << "Hello World";

        for (int j = 0; j < i; j++) {
            qDebug() << "Hello World22222";
            if (looo[i] == looo[j])
            {
                --i;
            }

        }
        for(int k = 0; k < 1; k++)
        {
            if(i == 1)
            {
            ui-> ai_1 -> setText(LoL[looo[i]]);
            }
            else if(i ==2)
            {
            ui-> ai_2 -> setText(LoL[looo[i]]);
            }
            else if(i ==3)
            {
            ui-> ai_3 -> setText(LoL[looo[i]]);
            }
            else if(i ==4)
            {
            ui-> ai_4 -> setText(LoL[looo[i]]);
            }
            else if(i ==5)
            {
            ui-> ai_5 -> setText(LoL[looo[i]]);
            }
            else if(i ==6)
            {
            ui-> ai_6 -> setText(LoL[looo[i]]);
            }
            else if(i ==7)
            {
            ui-> ai_7 -> setText(LoL[looo[i]]);
            }
            else if(i ==8)
            {
            ui-> ai_8 -> setText(LoL[looo[i]]);
            }
            else if(i ==9)
            {
            ui-> ai_9 -> setText(LoL[looo[i]]);
            }
            else if(i ==10)
            {
            ui-> ai_10 -> setText(LoL[looo[i]]);
            }
            else if(i ==11)
            {
            ui-> ai_11 -> setText(LoL[looo[i]]);
            }
            else if(i ==12)
            {
            ui-> ai_12 -> setText(LoL[looo[i]]);
            }
            else if(i ==13)
            {
            ui-> ai_13 -> setText(LoL[looo[i]]);
            }
            else if(i ==14)
            {
            ui-> ai_14 -> setText(LoL[looo[i]]);
            }
            else if(i ==15)
            {
            ui-> ai_15 -> setText(LoL[looo[i]]);
            }
            else if(i ==16)
            {
            ui-> ai_16 -> setText(LoL[looo[i]]);
            }
            else if(i ==17)
            {
            ui-> ai_17 -> setText(LoL[looo[i]]);
            }
            else if(i ==18)
            {
            ui-> ai_18 -> setText(LoL[looo[i]]);
            }
            else if(i ==19)
            {
            ui-> ai_19 -> setText(LoL[looo[i]]);
            }
            else if(i ==20)
            {
            ui-> ai_20 -> setText(LoL[looo[i]]);
            }
            else if(i ==21)
            {
            ui-> ai_21 -> setText(LoL[looo[i]]);
            }
            else if(i ==22)
            {
            ui-> ai_22 -> setText(LoL[looo[i]]);
            }
            else if(i ==23)
            {
            ui-> ai_23 -> setText(LoL[looo[i]]);
            }
            else if(i ==24)
            {
            ui-> ai_24 -> setText(LoL[looo[i]]);
            }
            else
            {
            ui-> ai_25 -> setText(LoL[looo[i]]);
            }
        }
    }
}

void MainWindow::reapeat()
{
    for(int i=2;i<30;i++){

        if (ui->ai_1->text()== ui->score1->toPlainText())
        {
            ui->ai_1->setStyleSheet("background-color: Red");
            ui->ai_1->setText("#");
        }
        if (ui->ai_2->text()== ui->score1->toPlainText())
        {
            ui->ai_2->setStyleSheet("background-color: Red");
            ui->ai_2->setText("#");
        }
        if (ui->ai_3->text()== ui->score1->toPlainText())
        {
            ui->ai_3->setStyleSheet("background-color: Red");
            ui->ai_3->setText("#");
        }
        if (ui->ai_4->text()== ui->score1->toPlainText())
        {
            ui->ai_4->setStyleSheet("background-color: Red");
            ui->ai_4->setText("#");
        }
        if (ui->ai_5->text()== ui->score1->toPlainText())
        {
            ui->ai_5->setStyleSheet("background-color: Red");
            ui->ai_5->setText("#");
        }
        if (ui->ai_6->text()== ui->score1->toPlainText())
        {
            ui->ai_6->setStyleSheet("background-color: Red");
            ui->ai_6->setText("#");
        }
        if (ui->ai_7->text()== ui->score1->toPlainText())
        {
            ui->ai_7->setStyleSheet("background-color: Red");
            ui->ai_7->setText("#");
        }
        if (ui->ai_8->text()== ui->score1->toPlainText())
        {
            ui->ai_8->setStyleSheet("background-color: Red");
            ui->ai_8->setText("#");
        }
        if (ui->ai_9->text()== ui->score1->toPlainText())
        {
            ui->ai_9->setStyleSheet("background-color: Red");
            ui->ai_9->setText("#");
        }
        if (ui->ai_10->text()== ui->score1->toPlainText())
        {
            ui->ai_10->setStyleSheet("background-color: Red");
            ui->ai_10->setText("#");
        }
        if (ui->ai_11->text()== ui->score1->toPlainText())
        {
            ui->ai_11->setStyleSheet("background-color: Red");
            ui->ai_11->setText("#");
        }
        if (ui->ai_12->text()== ui->score1->toPlainText())
        {
            ui->ai_12->setStyleSheet("background-color: Red");
            ui->ai_12->setText("#");
        }
        if (ui->ai_13->text()== ui->score1->toPlainText())
        {
            ui->ai_13->setStyleSheet("background-color: Red");
            ui->ai_13->setText("#");
        }
        if (ui->ai_14->text()== ui->score1->toPlainText())
        {
            ui->ai_14->setStyleSheet("background-color: Red");
            ui->ai_14->setText("#");
        }
        if (ui->ai_15->text()== ui->score1->toPlainText())
        {
            ui->ai_15->setStyleSheet("background-color: Red");
            ui->ai_15->setText("#");
        }
        if (ui->ai_16->text()== ui->score1->toPlainText())
        {
            ui->ai_16->setStyleSheet("background-color: Red");
            ui->ai_16->setText("#");
        }
        if (ui->ai_17->text()== ui->score1->toPlainText())
        {
            ui->ai_17->setStyleSheet("background-color: Red");
            ui->ai_17->setText("#");
        }
        if (ui->ai_18->text()== ui->score1->toPlainText())
        {
            ui->ai_18->setStyleSheet("background-color: Red");
            ui->ai_18->setText("#");
        }
        if (ui->ai_19->text()== ui->score1->toPlainText())
        {
            ui->ai_19->setStyleSheet("background-color: Red");
            ui->ai_19->setText("#");
        }
        if (ui->ai_20->text()== ui->score1->toPlainText())
        {
            ui->ai_20->setStyleSheet("background-color: Red");
            ui->ai_20->setText("#");
        }
        if (ui->ai_21->text()== ui->score1->toPlainText())
        {
            ui->ai_21->setStyleSheet("background-color: Red");
            ui->ai_21->setText("#");
        }
        if (ui->ai_22->text()== ui->score1->toPlainText())
        {
            ui->ai_22->setStyleSheet("background-color: Red");
            ui->ai_22->setText("#");
        }
        if (ui->ai_23->text()== ui->score1->toPlainText())
        {
            ui->ai_23->setStyleSheet("background-color: Red");
            ui->ai_23->setText("#");
        }
        if (ui->ai_24->text()== ui->score1->toPlainText())
        {
            ui->ai_24->setStyleSheet("background-color: Red");
            ui->ai_24->setText("#");
        }
        if (ui->ai_25->text()== ui->score1->toPlainText())
        {
            ui->ai_25->setStyleSheet("background-color: Red");
            ui->ai_25->setText("#");
        }

    }
}

void MainWindow::reapeat2()
{
    for(int i=2;i<30;i++){

        if (ui->user_1->text() == ui->score2->toPlainText())
        {

            ui->user_1->setStyleSheet("background-color: Red");
            ui->user_1->setText("#");
            ui->user_1->setEnabled(false);


        }
        if (ui->user_2->text()== ui->score2->toPlainText())
        {

            ui->user_2->setStyleSheet("background-color: Red");
            ui->user_2->setText("#");
            ui->user_2->setEnabled(false);
        }
        if (ui->user_3->text()== ui->score2->toPlainText())
        {

            ui->user_3->setStyleSheet("background-color: Red");
            ui->user_3->setText("#");
            ui->user_3->setEnabled(false);
        }
        if (ui->user_4->text()== ui->score2->toPlainText())
        {

            ui->user_4->setStyleSheet("background-color: Red");
            ui->user_4->setText("#");
            ui->user_4->setEnabled(false);
        }
        if (ui->user_5->text()== ui->score2->toPlainText())
        {

            ui->user_5->setStyleSheet("background-color: Red");
            ui->user_5->setText("#");
            ui->user_5->setEnabled(false);
        }
        if (ui->user_6->text()== ui->score2->toPlainText())
        {

            ui->user_6->setStyleSheet("background-color: Red");
            ui->user_6->setText("#");
            ui->user_6->setEnabled(false);
        }
        if (ui->user_7->text()== ui->score2->toPlainText())
        {

            ui->user_7->setStyleSheet("background-color: Red");
            ui->user_7->setText("#");
            ui->user_7->setEnabled(false);
        }
        if (ui->user_8->text()== ui->score2->toPlainText())
        {

            ui->user_8->setStyleSheet("background-color: Red");
            ui->user_8->setText("#");
            ui->user_8->setEnabled(false);
        }
        if (ui->user_9->text()== ui->score2->toPlainText())
        {

            ui->user_9->setStyleSheet("background-color: Red");
            ui->user_9->setText("#");
            ui->user_9->setEnabled(false);
        }
        if (ui->user_10->text()== ui->score2->toPlainText())
        {

            ui->user_10->setStyleSheet("background-color: Red");
            ui->user_10->setText("#");
            ui->user_10->setEnabled(false);
        }
        if (ui->user_11->text()== ui->score2->toPlainText())
        {

            ui->user_11->setStyleSheet("background-color: Red");
            ui->user_11->setText("#");
            ui->user_11->setEnabled(false);
        }
        if (ui->user_12->text()== ui->score2->toPlainText())
        {

            ui->user_12->setStyleSheet("background-color: Red");
            ui->user_12->setText("#");
            ui->user_12->setEnabled(false);
        }
        if (ui->user_13->text()== ui->score2->toPlainText())
        {

            ui->user_13->setStyleSheet("background-color: Red");
            ui->user_13->setText("#");
            ui->user_13->setEnabled(false);
        }
        if (ui->user_14->text()== ui->score2->toPlainText())
        {

            ui->user_14->setStyleSheet("background-color: Red");
            ui->user_14->setText("#");
            ui->user_14->setEnabled(false);
        }
        if (ui->user_15->text()== ui->score2->toPlainText())
        {

            ui->user_15->setStyleSheet("background-color: Red");
            ui->user_15->setText("#");
            ui->user_15->setEnabled(false);
        }
        if (ui->user_16->text()== ui->score2->toPlainText())
        {

            ui->user_16->setStyleSheet("background-color: Red");
            ui->user_16->setText("#");
            ui->user_16->setEnabled(false);
        }
        if (ui->user_17->text()== ui->score2->toPlainText())
        {

            ui->user_17->setStyleSheet("background-color: Red");
            ui->user_17->setText("#");
            ui->user_17->setEnabled(false);
        }
        if (ui->user_18->text()== ui->score2->toPlainText())
        {

            ui->user_18->setStyleSheet("background-color: Red");
            ui->user_18->setText("#");
            ui->user_18->setEnabled(false);
        }
        if (ui->user_19->text()== ui->score2->toPlainText())
        {

            ui->user_19->setStyleSheet("background-color: Red");
            ui->user_19->setText("#");
            ui->user_19->setEnabled(false);
        }
        if (ui->user_20->text()== ui->score2->toPlainText())
        {

            ui->user_20->setStyleSheet("background-color: Red");
            ui->user_20->setText("#");
            ui->user_20->setEnabled(false);
        }
        if (ui->user_21->text()== ui->score2->toPlainText())
        {

            ui->user_21->setStyleSheet("background-color: Red");
            ui->user_21->setText("#");
            ui->user_21->setEnabled(false);
        }
        if (ui->user_22->text()== ui->score2->toPlainText())
        {

            ui->user_22->setStyleSheet("background-color: Red");
            ui->user_22->setText("#");
            ui->user_22->setEnabled(false);
        }
        if (ui->user_23->text()== ui->score2->toPlainText())
        {

            ui->user_23->setStyleSheet("background-color: Red");
            ui->user_23->setText("#");
            ui->user_23->setEnabled(false);
        }
        if (ui->user_24->text()== ui->score2->toPlainText())
        {

            ui->user_24->setStyleSheet("background-color: Red");
            ui->user_24->setText("#");
            ui->user_24->setEnabled(false);
        }
        if (ui->user_25->text()== ui->score2->toPlainText())
        {

            ui->user_25->setStyleSheet("background-color: Red");
            ui->user_25->setText("#");
            ui->user_25->setEnabled(false);
        }

    }
}

void MainWindow::on_pushButton_out1_clicked()
{
    this -> close();
}

void MainWindow::on_pushButton_out4_clicked()
{
    this -> close();
}

void MainWindow::on_pushButton_out2_clicked()
{
    this -> close();
}

void MainWindow::on_pushButton_out3_clicked()
{
    this -> close();
}

void MainWindow::on_pushButton_return2_clicked()
{
    reset();
    ui->stackedWidget->setCurrentIndex(2);
}

void MainWindow::on_pushButton_return3_clicked()
{
    reset();
    ui->stackedWidget->setCurrentIndex(2);
}

void MainWindow::on_pushButton_return1_clicked()
{
    reset();
    ui->stackedWidget->setCurrentIndex(2);
}

void MainWindow::reset()
{
    sum =0;
    ai_sum =0;
    ui -> score1 -> clear();
    ui -> score1_2 -> clear();
    ui -> score2 -> clear();
    ui -> score2_2 -> clear();
    ui -> user_1 -> setStyleSheet("background-color: white");
    ui -> user_2 -> setStyleSheet("background-color: white");
    ui -> user_3 -> setStyleSheet("background-color: white");
    ui -> user_4 -> setStyleSheet("background-color: white");
    ui -> user_5 -> setStyleSheet("background-color: white");
    ui -> user_6 -> setStyleSheet("background-color: white");
    ui -> user_7 -> setStyleSheet("background-color: white");
    ui -> user_8 -> setStyleSheet("background-color: white");
    ui -> user_9 -> setStyleSheet("background-color: white");
    ui -> user_10 -> setStyleSheet("background-color: white");
    ui -> user_11 -> setStyleSheet("background-color: white");
    ui -> user_12 -> setStyleSheet("background-color: white");
    ui -> user_13 -> setStyleSheet("background-color: white");
    ui -> user_14 -> setStyleSheet("background-color: white");
    ui -> user_15 -> setStyleSheet("background-color: white");
    ui -> user_16 -> setStyleSheet("background-color: white");
    ui -> user_17 -> setStyleSheet("background-color: white");
    ui -> user_18 -> setStyleSheet("background-color: white");
    ui -> user_19 -> setStyleSheet("background-color: white");
    ui -> user_20 -> setStyleSheet("background-color: white");
    ui -> user_21 -> setStyleSheet("background-color: white");
    ui -> user_22 -> setStyleSheet("background-color: white");
    ui -> user_23 -> setStyleSheet("background-color: white");
    ui -> user_24 -> setStyleSheet("background-color: white");
    ui -> user_25 -> setStyleSheet("background-color: white");
    ui -> ai_1 -> setStyleSheet("background-color: white");
    ui -> ai_2 -> setStyleSheet("background-color: white");
    ui -> ai_3 -> setStyleSheet("background-color: white");
    ui -> ai_4 -> setStyleSheet("background-color: white");
    ui -> ai_5 -> setStyleSheet("background-color: white");
    ui -> ai_6 -> setStyleSheet("background-color: white");
    ui -> ai_7 -> setStyleSheet("background-color: white");
    ui -> ai_8 -> setStyleSheet("background-color: white");
    ui -> ai_9 -> setStyleSheet("background-color: white");
    ui -> ai_10 -> setStyleSheet("background-color: white");
    ui -> ai_11 -> setStyleSheet("background-color: white");
    ui -> ai_12 -> setStyleSheet("background-color: white");
    ui -> ai_13 -> setStyleSheet("background-color: white");
    ui -> ai_14 -> setStyleSheet("background-color: white");
    ui -> ai_15 -> setStyleSheet("background-color: white");
    ui -> ai_16 -> setStyleSheet("background-color: white");
    ui -> ai_17 -> setStyleSheet("background-color: white");
    ui -> ai_18 -> setStyleSheet("background-color: white");
    ui -> ai_19 -> setStyleSheet("background-color: white");
    ui -> ai_20 -> setStyleSheet("background-color: white");
    ui -> ai_21 -> setStyleSheet("background-color: white");
    ui -> ai_22 -> setStyleSheet("background-color: white");
    ui -> ai_23 -> setStyleSheet("background-color: white");
    ui -> ai_24 -> setStyleSheet("background-color: white");
    ui -> ai_25 -> setStyleSheet("background-color: white");

    ui -> user_1 -> setEnabled(true);
    ui -> user_2 -> setEnabled(true);
    ui -> user_3 -> setEnabled(true);
    ui -> user_4 -> setEnabled(true);
    ui -> user_5 -> setEnabled(true);
    ui -> user_6 -> setEnabled(true);
    ui -> user_7 -> setEnabled(true);
    ui -> user_8 -> setEnabled(true);
    ui -> user_9 -> setEnabled(true);
    ui -> user_10 -> setEnabled(true);
    ui -> user_11 -> setEnabled(true);
    ui -> user_12 -> setEnabled(true);
    ui -> user_13 -> setEnabled(true);
    ui -> user_14 -> setEnabled(true);
    ui -> user_15 -> setEnabled(true);
    ui -> user_16 -> setEnabled(true);
    ui -> user_17 -> setEnabled(true);
    ui -> user_18 -> setEnabled(true);
    ui -> user_19 -> setEnabled(true);
    ui -> user_20 -> setEnabled(true);
    ui -> user_21 -> setEnabled(true);
    ui -> user_22 -> setEnabled(true);
    ui -> user_23 -> setEnabled(true);
    ui -> user_24 -> setEnabled(true);
    ui -> user_25 -> setEnabled(true);
}


void MainWindow::AI()
{
    if(sum >= 5 || ai_sum >= 5)
    {
        qDebug() << "종료";
    }
    else
    {
        QMessageBox msgBox;
            msgBox.setText("상대방의 턴입니다.");
            msgBox.exec();
        int ai_looo[25] = {};

        srand((unsigned int)time(NULL));

        qDebug() << "Hello World1231231";
        for (int i = 0; i < 25; i++) {
            ai_looo[i] = rand() % 25;

            qDebug() << "Hello World";

            for (int j = 0; j < i; j++) {

                qDebug() << "Hello World22222";
                if (ai_looo[i] == ai_looo[j])
                {
                    --i;
                }
            }
            if(ai_looo[i] == 1)
            {
                if(ui -> ai_1 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_1->text());
            ui-> ai_1 -> setText("#");
            ui-> ai_1 -> setStyleSheet("background-color: red");
            reapeat2();


            break;
            }

            else if(ai_looo[i] ==2)
            {
                if(ui -> ai_2 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_2->text());
            ui-> ai_2 -> setText("#");

            ui-> ai_2 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else if(ai_looo[i] ==3)
            {
                if(ui -> ai_3 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_3->text());
            ui-> ai_3 -> setText("#");

            ui-> ai_3 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else if(ai_looo[i] ==4)
            {
                if(ui -> ai_4 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_4->text());
            ui-> ai_4 -> setText("#");

            ui-> ai_4 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else if(ai_looo[i] ==5)
            {
                if(ui -> ai_5 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_5->text());
            ui-> ai_5 -> setText("#");

            ui-> ai_5 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else if(ai_looo[i] ==6)
            {
                if(ui -> ai_6 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_6->text());
            ui-> ai_6 -> setText("#");

            ui-> ai_6 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else if(ai_looo[i] ==7)
            {
                if(ui -> ai_7 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_7->text());
            ui-> ai_7 -> setText("#");

            ui-> ai_7 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else if(ai_looo[i] ==8)
            {
                if(ui -> ai_8 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_8->text());
            ui-> ai_8 -> setText("#");

            ui-> ai_8 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else if(ai_looo[i] ==9)
            {
                if(ui -> ai_9 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_9->text());
            ui-> ai_9 -> setText("#");

            ui-> ai_9 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else if(ai_looo[i] ==10)
            {
                if(ui -> ai_10 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_10->text());
            ui-> ai_10 -> setText("#");

            ui-> ai_10 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else if(ai_looo[i] ==11)
            {
                if(ui -> ai_11 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_11->text());
            ui-> ai_11 -> setText("#");

            ui-> ai_11 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else if(ai_looo[i] ==12)
            {
                if(ui -> ai_12 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_12->text());
            ui-> ai_12 -> setText("#");

            ui-> ai_12 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else if(ai_looo[i] ==13)
            {
                if(ui -> ai_13 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_13->text());
            ui-> ai_13 -> setText("#");

            ui-> ai_13 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else if(ai_looo[i]==14)
            {
                if(ui -> ai_14 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_14->text());
            ui-> ai_14 -> setText("#");

            ui-> ai_14 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else if(ai_looo[i] ==15)
            {
                if(ui -> ai_15 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_15->text());
            ui-> ai_15 -> setText("#");

            ui-> ai_15 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else if(ai_looo[i] ==16)
            {
                if(ui -> ai_16 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_16->text());
            ui-> ai_16 -> setText("#");

            ui-> ai_16 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else if(ai_looo[i] ==17)
            {
                if(ui -> ai_17 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_17->text());
            ui-> ai_17 -> setText("#");

            ui-> ai_17 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else if(ai_looo[i] ==18)
            {
                if(ui -> ai_18 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_18->text());
            ui-> ai_18 -> setText("#");

            ui-> ai_18 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else if(ai_looo[i] ==19)
            {
                if(ui -> ai_19 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_19->text());
            ui-> ai_19 -> setText("#");

            ui-> ai_19 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else if(ai_looo[i] ==20)
            {
                if(ui -> ai_20 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_20->text());
            ui-> ai_20 -> setText("#");

            ui-> ai_20 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else if(ai_looo[i] ==21)
            {
                if(ui -> ai_21 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_21->text());
            ui-> ai_21 -> setText("#");

            ui-> ai_21 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else if(ai_looo[i] ==22)
            {
                if(ui -> ai_22 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_22->text());
            ui-> ai_22 -> setText("#");

            ui-> ai_22 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else if(ai_looo[i] ==23)
            {
                if(ui -> ai_23 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_23->text());
            ui-> ai_23 -> setText("#");

            ui-> ai_23 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else if(ai_looo[i] ==24)
            {
                if(ui -> ai_24 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_24->text());
            ui-> ai_24 -> setText("#");

            ui-> ai_24 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
            else
            {
                if(ui -> ai_25 -> text() == "#")
                {
                    continue;
                }
                ui->score2->clear();
                ui->score2->setText(ui->ai_25->text());
            ui-> ai_25 -> setText("#");

            ui-> ai_25 -> setStyleSheet("background-color: red");
            reapeat2();
            break;
            }
       }
       asd();
    }

}

