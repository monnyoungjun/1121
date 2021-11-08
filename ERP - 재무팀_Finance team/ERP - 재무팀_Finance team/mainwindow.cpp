#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "QtSql"
#include "QSqlQuery"
#include <QSqlQueryModel>
#include <QtGui>
#include <QString>
#include <QSqlRecord>
#include <QMessageBox>
#include <cctype>

int myplus =0;  //이윤총액
int mysale =0;  //판매총액
int myPurchase =0;  //구매총액

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    qDebug() << "드라이버" << QSqlDatabase::drivers(); //설치된 드라이버들을 확인하기
    qDebug() << QCoreApplication::libraryPaths();
    db = QSqlDatabase::addDatabase("QMYSQL"); //"QMYSQL" 드라이버가 없으면 DB에 접속이 불가능하다.
    db.setHostName("10.10.21.118");      // IP 또는 DNS Host name
    db.setPort(3306);  //포트명
    db.setDatabaseName("starDB"); // DB명
    db.setUserName("root");     // 계정 명
    db.setPassword("starDB1234@");     // 계정 Password

    db.open();
}


MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_myselete_clicked() //검색버튼
{
    myplus = 0; //이윤 총액
    mysale = 0; //판매 총액

    int strat1 = 0+(ui->st_1->text().toInt()); //조회 처음 시작 년도
    int end1 = 0+(ui->ed_1->text().toInt()); //조회 끝의 년도
    int strat2 = 0+(ui->st_2->text().toInt()); //조회 시작 월
    int end2 = 0+(ui->ed_2->text().toInt());//조회 마지막 월
    int strat3 = 0+(ui->st_3->text().toInt()); //조회 시작 일
    int end3 = 0+(ui->ed_3->text().toInt());//조회 마지막 일

    qDebug() << strat1;
    qDebug() << strat2;
    qDebug() << strat3;
    qDebug() << end1;
    qDebug() << end2;
    qDebug() << end3;

    if (strat1 != 0 && end1 != 0){                                                                         //년도가 0이 아닐떄 실행
        if (strat2 != 0 && end2 != 0 && strat2 < 13 && end2 < 13){                    //월이 0이 아니거나 12이상이 아닐때 실행
            if (strat3 != 0 && end3 != 0 && strat3 < 32 && end3 < 32){                //일이 0이 아니거나 31이상이 아닐때 실행


                QString stratt = QString("%1.%2.%3").arg(strat1).arg(strat2).arg(strat3);  //조회 시작 날 예)1994.05.05 형식으로 변수로 저장
                QString endd = QString("%1.%2.%3").arg(end1).arg(end2).arg(end3);      //조회 마지막 날

                qDebug() << stratt;
                qDebug() << endd;

                QSqlQueryModel *model = new QSqlQueryModel;            //모델 변수 선언
                QString a = QString("SELECT * FROM data_sale WHERE 판매날짜 >= ('%1%') AND 판매날짜 <= ('%2%') ORDER BY 판매날짜").arg(stratt).arg(endd);    //쿼리문을 변수로 저장
                qDebug() << a;
                model->setQuery(a);   //모델에 쿼리문 실행
                ui->tableView_1->setModel(model);            //테이블뷰에 내가사용한 모델을 입력
                ui->tableView_1->show();                             //테이블뷰에 실행한 쿼리문 보여주기

//                QString ingredient[21];

                for( int i=0; i<model->rowCount(); ++i ){        //for문을 이용하여 쿼리로 뽑아온 데이터를 리스트 for문 돌리듯이 조회된만큼 반복
                    QSqlRecord record = model->record(i);
                    int title = record.value("이윤").toInt();         //조회하려고 하는 것 = 이윤
                    int year = record.value("판매가").toInt();         //조회하려고 하는 것2 = 판매가

//                    ingredient[i+1]= model-> record(i).value("판매날짜").toString();


                    myplus += title;                                             //이윤 총액에 조회한 이윤액 1개씩 더하기
                    mysale += year;                                             //판매 총액에 조회한 판매액 1개씩 더하기

                    qDebug() << myplus;
                    qDebug() << mysale;
                }

//                qDebug() << ingredient[1];
//                QString bb = {};
//                QString cc = {};
//                for (int i = 0; i < ingredient[i+1]; ++i){
//                    bb = ingredient[1];
//                    cc = ingredient[i+1];
//                }
//                qDebug() << bb;
//                qDebug() << cc;

                ui -> sale_sum -> setNum(mysale);                  //이윤총액 변수를 sale_sum이라는 라벨에 입력 (숫자만 입력할시 setNum을 사용해야 적용되었음)
                ui -> plus_sum -> setNum(myplus);                 //판매총액 변수를 plus_sum이라는 라벨에 입력 (숫자만 입력할시 setNum을 사용해야 적용되었음)


                QString strattt = QString("%1").arg(strat1);                //구매 테이블은 날짜 형식이 달라 따로 년도만 변수로 입력 예) 1994
                QString enddd = QString("%1").arg(end1);

                QSqlQueryModel *model2 = new QSqlQueryModel;              //모델2 변수 선언
                QString b = QString("SELECT * FROM data_order WHERE 날짜 >= '%%1%' ORDER BY 날짜").arg(enddd);        //구매액을 볼수있는 조회 쿼리문
                qDebug() << b;
                model2->setQuery(b);                                            //모델2에 쿼리문 실행
                ui->tableView_2->setModel(model2);                  //테이블뷰2에 모델2를 입력
                ui->tableView_2->show();                                     //테이블뷰2 실행한 쿼리문 보여주기

                for( int i=0; i<model2->rowCount(); ++i ){                           //레코드를 이용하여 for문을 사용해 조회된만큼 반복
                    QSqlRecord record = model2->record(i);
                    int ssss = record.value("가격").toInt();                               //조회할 것 = 가격

                    myPurchase += ssss;                                                           //구매 총액에 조회한 구매액들 1개씩 더하기
                    qDebug() << ssss;
            }
                ui -> Purchase_sum -> setNum(myPurchase);                        //구매총액 변수를 Purchase_sum 에 입력
                ui -> plus_sum_2 -> setNum(myplus - myPurchase);             //조회한 기간내에 구매총액 과 이윤총액을 뺀 금액을 입력

                //그래프생성코드


                int ii = 0;

                QVector<double> x(101), y(101); // initialize with entries 0..100          //그래프에 넣을 데이터 변수 선언
                for (int i=0; i<1; ++i)
                {
                    for( int j=0; j<model->rowCount(); ++j ){                              //for문 으로 조회된만큼 반복
                        QSqlRecord record = model->record(j);
                        int title = record.value("이윤").toInt();                                //첫번째 이윤을 조회
                        qDebug() << title;
                        ii = j+1;

                        x[j+1] = j+1; // x goes from -1 to 1                                             //x[1] = 1 ....
                        y[j+1] = title; // let's plot a quadratic function                           //y[1] = 이윤1 ....

                    }
                }


                ui->customPlot->addGraph();                                                            //ui에 customPlot에 그래프 선언
                ui->customPlot->graph(0)->setData(x, y);                                         //들어갈 데이터 입력
                ui->customPlot->graph(0)->setLineStyle(QCPGraph::lsLine);           //그래프의 스타일 막대, 선  (막대는 이유를알수없으나 안됨)
                ui->customPlot->xAxis->setLabel("조회된 기간내 이윤금액");             //x축 타이틀
                ui->customPlot->yAxis->setLabel("이윤금액");                                   //y축 타이틀

                ui->customPlot->xAxis->setRange(1,ii);                                          //x축에 적히는것 1~31
                ui->customPlot->yAxis->setRange(-20000,50000);                          //y축에 적히는것 -50000~50000

                ui->customPlot->replot();		                                                     // 그래프 그리기

                ii = 0;



                QVector<double> z(101), c(101); // initialize with entries 0..100                  //2번쨰 그래프에 넣을 값
                for (int i=0; i<1; ++i)
                {
                    for( int j=0; j<model2->rowCount(); ++j ){
                        QSqlRecord record = model2->record(j);
                        int title = record.value("가격").toInt();
                        qDebug() << title;
                        ii = j+1;

                        z[j+1] = j+1; // x goes from -1 to 1
                        c[j+1] = title; // let's plot a quadratic function

                    }
                }


                ui->customPlot_2->addGraph();                                                                     //2번쨰 그래프 그리기
                ui->customPlot_2->graph(0)->setData(z, c);
                ui->customPlot_2->graph(0)->setLineStyle(QCPGraph::lsLine);
                ui->customPlot_2->xAxis->setLabel("조회된 기간내 재료 구매금액");
                ui->customPlot_2->yAxis->setLabel("구매금액");

                ui->customPlot_2->xAxis->setRange(1,ii);
                ui->customPlot_2->yAxis->setRange(-20000,50000);

                ui->customPlot_2->replot();		// 그래프 그림

                ii = 0 ;


                QVector<double> v(101), n(101); // initialize with entries 0..100                               //3번쨰 그래프에 넣을 값
                for (int i=0; i<1; ++i)
                {
                    for( int j=0; j<model->rowCount(); ++j ){
                        QSqlRecord record = model->record(j);
                        int title = record.value("판매가").toInt();
                        ii = j+1;
                        qDebug() << title;
                        qDebug() << "조회2";

                        v[j+1] = j+1; // x goes from -1 to 1
                        n[j+1] = title; // let's plot a quadratic function

                    }
                }


                ui->customPlot_3->addGraph();                                                             //3번째 그래프 그리기
                ui->customPlot_3->graph(0)->setData(v, n);
                ui->customPlot_3->graph(0)->setLineStyle(QCPGraph::lsLine);
                ui->customPlot_3->xAxis->setLabel("조회된 기간내 판매 금액");
                ui->customPlot_3->yAxis->setLabel("판매금액");

                ui->customPlot_3->xAxis->setRange(1,ii);
                ui->customPlot_3->yAxis->setRange(-20000,50000);

                ui->customPlot_3->replot();		// 그래프 그림



                myplus =0;                                       //판매 , 이윤 , 구매 총액 0으로 초기화
                mysale =0;
                myPurchase =0;


            }
            else{
            QMessageBox msgBox;
            msgBox.setText("일 을(를) 잘못 입력하셨습니다. 다시 입력해 주세요.");
            msgBox.exec();
            }
        }
        else{
            QMessageBox msgBox;
            msgBox.setText("월 을(를) 잘못 입력하셨습니다. 다시 입력해 주세요.");
            msgBox.exec();
        }
    }
    else {
        QMessageBox msgBox;
        msgBox.setText("년(연)도 을(를) 잘못 입력하셨습니다. 다시 입력해 주세요.");
        msgBox.exec();
    }


}

void MainWindow::on_pushButton_clicked()
{
    QString id = (ui->id_1->text());
    QString pw = (ui->pw_1->text());

    if (id != ""){

        if (pw != ""){

            if (id == "root" && pw == "1234"){
                ui -> stackedWidget -> setCurrentIndex(1);

            }
            else{
                QMessageBox msgBox;
                msgBox.setText("등록되지않은 ID입니다.");
                msgBox.exec();
            }

        }
        else{
            QMessageBox msgBox;
            msgBox.setText("Password 을(를) 입력해 주세요.");
            msgBox.exec();
        }
    }
    else {
        QMessageBox msgBox;
        msgBox.setText("ID 을(를) 입력해 주세요.");
        msgBox.exec();
    }
}
