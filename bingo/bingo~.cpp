#include <iostream>
#include <time.h>

using namespace std;

void shuffle(int arr[][5])
{
    int destCol, destRow, sourCol, sourRow, temp;
    for (int i = 0; i < 77; i++)
    {
        destCol = rand() % 5;
        destRow = rand() % 5;
        sourCol = rand() % 5;
        sourRow = rand() % 5;

        temp = arr[destRow][destCol];
        arr[destRow][destCol] = arr[sourRow][sourCol];
        arr[sourRow][sourCol] = temp;
    }
}

void enterNum(int arr[][5], const int& num)
{
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (arr[i][j] == num)
                arr[i][j] = -1;
        }
    }
}

void checkNum(int arr[][5], int* ldig, int* rdig, int* bingo)
{
    for (int i = 0; i < 5; i++)
    {
        int rowBingo = 0;
        int colBingo = 0;

        for (int j = 0; j < 5; j++)
        {
            if (arr[i][j] == -1)
            {
                if (i == 2 && j == 2)
                {
                    (*ldig)++;
                    (*rdig)++;
                }
                else if (i + j == 4)
                    (*rdig)++;
                else if (i == j)
                    (*ldig)++;
                rowBingo++;
            }
            if (arr[j][i] == -1)
            {
                colBingo++;
            }

            if (colBingo == 5) (*bingo)++;
            if (rowBingo == 5) (*bingo)++;
        }
    }
}

void printBingo(int arr[][5], int arr2[][5])
{
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (arr[i][j] == -1)
                cout << "#";
            else
                cout << arr[i][j];
            cout << "\t";
        }
        cout << "\t\t";
        for (int j = 0; j < 5; j++)
        {
            if (arr2[i][j] == -1)
                cout << "#";
            else
                cout << arr2[i][j];

            cout << "\t";
        }
        cout << endl << endl;
    }
    cout << endl;
}

int main()
{
    int numPlayer[5][5], numCom[5][5];
    int inputNum = 0, bingoPlayer = 0, bingoCom = 0;
    bool playerWin = false;

    srand(time(NULL));

    // 기본 숫자로 초기화한다. (0 ~ 25)
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            numPlayer[i][j] = 5 * i + j + 1;
            numCom[i][j] = 5 * i + j + 1;
        }
    }

    // 숫자를 랜덤하게 섞는다.
    shuffle(numPlayer);
    shuffle(numCom);

    cout << "\n\t\t\t\t\t~ 빙고 게임 ~\n" << endl;
    while (true)
    {
        int colBingo = 0, leftDigBingo = 0, rightDigBingo = 0;
        int colBingoCom = 0, leftDigBingoCom = 0, rightDigBingoCom = 0;

        printBingo(numPlayer, numCom);

        cout << "숫자 입력: ";
        cin >> inputNum;
        // 잘못된 값이 들어왔을 경우, continue를 통해 맨 처음으로 돌아간다.
        if (inputNum < 1 || inputNum > 25) {
            cout << "잘못된 입력입니다. 다시 입력해 주세요." << endl << endl;
            continue;
        }

        // 사용자로부터 입력받은 숫자를 처리한다.
        enterNum(numPlayer, inputNum);
        enterNum(numCom, inputNum);


        // 컴퓨터의 입력을 처리할 변수를 선언한다.
        int inputNumCom;

        // check: 0 ~ 4는 가로, 5 ~ 9는 세로, 10은 좌측 상단의 대각선\, 11은 우측 상단의 대각선/
        // 각 가로/세로/대각선에 -1이 얼마나 선언되어 있는지를 저장한다.
        // numbers: 빙고가 된 줄을 제외하고, 가장 많이 -1을 가진 줄의 숫자를 저장한다.
        int check[12]{ 0 };
        int numbers[5]{ 0 };

        for (int i = 0; i < 5; i++)
        {
            for (int j = 0; j < 5; j++)
            {
                if (numCom[i][j] == -1)
                {
                    if (i == 2 && j == 2)
                    {
                        check[10]++;
                        check[11]++;
                    }
                    else if (i == j) check[10]++;
                    else if (i + j == 4) check[11]++;
                    check[i]++;
                }
                if (numCom[j][i] == -1)
                {
                    check[5 + i]++;
                }
            }
        }

        // 가장 큰 수를 찾는다. 같은 수가 있다면 우선 순위는 가로 > 세로 > 대각선이다.
        // 5는 이미 빙고가 된 줄이기 때문에 제외한다.
        int a = 0, idx = 0;
        for (int i = 0; i < 12; i++)
        {
            if (check[i] != 5 && a < check[i])
            {
                a = check[i];
                idx = i;
            }
        }

        //idx에 따라서 처리해야 하는데
        if (idx / 5 == 0) // 몫이 0인 경우, 0~4
        {
            for (int i = 0; i < 5; i++)
                numbers[i] = numCom[idx][i];
        }
        else if (idx / 5 == 1) // 5~9
        {
            for (int i = 0; i < 5; i++)
                numbers[i] = numCom[i][idx % 5];
        }
        else // 10,11
        {
            if (idx == 10)
            {
                for (int i = 0; i < 5; i++)
                    numbers[i] = numCom[i][i];
            }
            else
            {
                for (int i = 0; i < 5; i++)
                    numbers[i] = numCom[i][4 - i];
            }
        }

        while (true)
        {
            int t_idx = rand() % 5;
            if (numbers[t_idx] != -1)
            {
                inputNumCom = numbers[t_idx];
                break;
            }
        }

        enterNum(numPlayer, inputNumCom);
        enterNum(numCom, inputNumCom);

        checkNum(numPlayer, &leftDigBingo, &rightDigBingo, &bingoPlayer);
        checkNum(numCom, &leftDigBingoCom, &rightDigBingoCom, &bingoCom);

        if (rightDigBingo == 5)
            bingoPlayer++;
        if (leftDigBingo == 5)
            bingoPlayer++;
        if (rightDigBingoCom == 5)
            bingoCom++;
        if (leftDigBingoCom == 5)
            bingoCom++;

        cout << endl;
        cout << "\t>> 당신의 숫자: " << inputNum << " << \t\t\t\t >> 컴퓨터의 숫자: " << inputNumCom << " <<" << endl;
        cout << "\t>> 빙고 카운트: " << bingoPlayer << " << \t\t\t\t >> 빙고 카운트: " << bingoCom << " <<" << endl;
        cout << endl;

        if (bingoPlayer == 5 || bingoCom == 5)
        {
            break;
        }
        bingoPlayer = 0;
        bingoCom = 0;
    }

    printBingo(numPlayer, numCom);

    if (bingoPlayer >= bingoCom)
    {
        cout << "승리하셨습니다!" << endl;
    }
    else
    {
        cout << "컴퓨터의 승리입니다." << endl;
    }

    return 0;
}