


// First Attempt....
class canPlaceFlowers{
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        if ((flowerbed.length == 1) && (flowerbed[0] == 0) && (n < 2)) return true;

        int tmp = 0;
        for (int i = 0; i < flowerbed.length - 1; i++) {
            if ((i == 0)) {
                if ((flowerbed[i] == 0) && flowerbed[i + 1] == 0) {
                    flowerbed[i] = 1;
                    tmp++;
                }
            } else if (i == flowerbed.length - 2) {
                if ((flowerbed[flowerbed.length - 2] == 0) && (flowerbed[flowerbed.length-1] == 0)) {
                    flowerbed[i] = 1;
                    tmp++;
                }
            } else {
                if ((flowerbed[i-1] == 0) && (flowerbed[i] == 0) && (flowerbed[i+1] == 0)) {
                    flowerbed[i] = 1;
                    tmp++;
                }
            }
        }
    
        if (tmp >= n) return true;

        return false;
    }
}
