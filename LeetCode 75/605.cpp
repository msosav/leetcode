#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    bool canPlaceFlowers(vector<int> &flowerbed, int n)
    {
        int flowers_placed = 0;
        if (n == 0)
            return true;
        if (flowerbed.size() < n)
            return false;
        if (flowerbed.size() == 1 && flowerbed[0] == 1)
            return false;
        else if (flowerbed.size() == 1 && flowerbed[0] == 0)
            return true;
        for (int i = 0; i < flowerbed.size(); i++)
        {
            if (i != 0 && i != flowerbed.size() - 1)
            {
                if (flowerbed[i - 1] == 0 && flowerbed[i] == 0 && flowerbed[i + 1] == 0)
                {
                    flowerbed[i] = 1;
                    flowers_placed++;
                }
            }
            else
            {
                if (i == 0)
                {
                    if (flowerbed[i + 1] == 0 && flowerbed[i] == 0)
                    {
                        flowerbed[i] = 1;
                        flowers_placed++;
                    }
                }
                else
                {
                    if (flowerbed[i - 1] == 0 && flowerbed[i] == 0)
                    {
                        flowerbed[i] = 1;
                        flowers_placed++;
                    }
                }
            }
        }
        if (flowers_placed >= n)
            return true;
        else
            return false;
    }
};